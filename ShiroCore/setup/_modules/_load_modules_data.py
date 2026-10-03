# -*- coding: utf-8 -*-
"""Собирает данные установленных модулей."""

from pathlib import Path

from loguru import logger

from ._load_schema import load_schema_1
from utils.file import load_file


def load_modules_data(modules_dirs: list[Path]) -> list[dict]:
    """Загружает данные установленных модулей приложения.

    Загружает и обрабатывает данные модулей согласно их файлов
    данных "module.toml".

    Args:
        modules_dirs (list[Path]): Список путей к директориям модулей.

    Returns:
        list[dict]: Список данных загруженных модулей.
    """
    logger.trace("Загружаю данные установленных модулей.")  # Логирование

    modules_data: list[dict] = []

    for module_path in modules_dirs:

        # Логирование
        logger.trace(f"Загружаю данные модуля: {module_path.name}")

        # # Загружает данные модуля из файла "module.toml"
        module_data_path: Path = module_path / "module.toml"
        module_data: dict = load_file(file_path=module_data_path)

        # # Получает версию схемы
        # Если версия схемы не указана - по умолчанию будет использована 1
        module_schema: dict = module_data.get("schema")
        module_schema_version: int = int(module_schema.get("version", 1))

        # # Обработка данных модуля согласно версии схемы
        data: dict | None = None

        match module_schema_version:

            case 1:
                data = load_schema_1(
                    module_data=module_data, module_path=module_path
                )

        # ! Если указана неподдерживаемая схема - модуль не будет загружен
        if data is None:
            continue    

        # # Загружает текстовые файлы приложения
        text_path: Path = module_path / "text.toml"
        if text_path.is_file():
            logger.trace("Загружаю тектовый файл модуля.")  # Логирование
            text_data: dict = load_file(file_path=text_path)
            data["text"] = text_data

        logger.trace("Данные модуля успешно загружены.")  # Логирование
        modules_data.append(data)

    return modules_data
