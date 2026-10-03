# -*- coding: utf-8 -*-
"""Загружает данные модуля по схеме первой версии."""

from pathlib import Path

from loguru import logger


def load_schema_1(module_data: dict, module_path: Path) -> dict:
    """
    Загружает данные модуля по схеме первой версии.

    Обрабатывает возможное отсутствие некоторых данных.

    Args:
        module_data (dict): Данные модуля из дата-файла "data.toml".
        module_path (Path): Путь к директории модуля.

    Returns:
        dict: Обработанный словарь данных модуля.
    """
    dir_: str = module_path.name

    # Логирование
    logger.trace(f"Загружаю данные модуля \"{dir_}\" по первой версии схемы.")

    # # Получает данные модуля
    # В случае если данные модуля отсутствуют полностью - будут
    # использованы значения по умолчанию
    data_module: dict = module_data.get("module", {})

    # # Обрабатывает данные модуля
    # ? [dir] - Имя директории в которой расположен модуль
    # ? [name] - Название модуля
    # ? [type] - Тип модуля (menu / module / ...)
    # ? [version] - Версия модуля (пока не используется)
    data: dict = {
        "dir": dir_,
        "name": data_module.get(
            "name",
            f"Module_{dir_}"
        ),
        "type": data_module.get("type", "module"),
        "version": data_module.get("version", "1.0.0")
    }

    logger.trace(f"Данные модуля загружены.")  # Логирование

    return data
