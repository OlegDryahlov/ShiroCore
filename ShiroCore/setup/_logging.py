# -*- coding: utf-8 -*-
"""Настройка логирования приложения."""

import sys

from loguru import logger

from config import Logging


def setup() -> None:
    """
    Настраивает логирование приложения.

    Настройки загружаются из файла конфигурации и сохранаются в config.py,
    откуда функция их и берёт.
    """
    # # Удаляет настройки Loguru по умолчанию
    logger.remove()

    # # Добавляет логирование в файл согласно настроек пользователя
    logger.add(
        format=Logging.format_,
        level=Logging.level,
        rotation=Logging.rotation,
        sink=Logging.file_path
    )

    # # Если включено - добавляет логирование в терминал
    if Logging.console:
        logger.add(
            format=Logging.format_,
            level=Logging.level,
            rotation=Logging.rotation,
            sink=sys.stdout
        )

    logger.trace("Логирование настроено.")  # Логирование
