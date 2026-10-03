# -*- coding: utf-8 -*-
"""Загружает текстовые файлы и файлы конфигурации."""

import json
from io import TextIOWrapper
from pathlib import Path

import tomli
from loguru import logger


def load_file(file_path: Path) -> dict | str:
    """
    Загружает данные из файла по переданному пути.

    Поддерживает следующие типы файлов: json, toml, txt. В случае если будет
    указан иной тип файла - файл будет обработан как txt.

    Args:
        file_path (Path): Путь к файлу.

    Returns:
        dict | str: Возвращает ожидаемый тип данных.
            str - для .txt;
            dict - для json, toml.
    """
    logger.trace(f"Читаю данные файла: \"{file_path}\".")  # Логирование

    # # Открывает файл для чтения
    file: TextIOWrapper = open(encoding="utf-8", file=file_path, mode="r")

    # # Файл читается разным способом в зависимости от его типа
    file_ext: str = str(file_path).split(".")[-1]
    match file_ext:

        case "json":
            file_data: dict = json.load(file)

        case "toml":
            file_data: dict = tomli.loads(file.read())

        # * Обработчик по умолчанию. Для txt или иных типов файлов
        case _:
            file_data: str = file.read()

    file.close()

    return file_data
