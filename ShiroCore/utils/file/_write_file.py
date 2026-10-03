# -*- coding: utf-8 -*-
"""Функция для записи данных в файлы различного типа."""

import json
from io import TextIOWrapper
from pathlib import Path
from typing import Any

import tomli_w
from loguru import logger


def write_file(file_data: Any, file_path: Path, mode: str = "w") -> None:
    """Записывает данные в файл по переданному пути.

    Args:
        file_data (Any): Данные файла.
        file_path (Path): Путь к файлу.
        mode (str, optional): Режим записи Python file.write(). 
            По умолчанию - "w".
    """
    logger.trace(f"Записываю данные в файл: \"{file_path}\".")  # Логирование

    # # Открывает файл для записи
    file: TextIOWrapper = open(encoding="utf-8", file=file_path, mode=mode)

    # # Файл записывается разным способом в зависимости от его типа
    file_ext: str = str(file_path).split(".")[-1]
    match file_ext:

        case "json":
            json.dumps(file_data, ensure_ascii=False, indent=4)

        case "toml":
            file.write(tomli_w.dumps(file_data))

        # * Обработчик по умолчанию. Для txt или иных типов файлов
        case _:
            file.write(file_data)

    file.close()
