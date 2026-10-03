# -*- coding: utf-8 -*-
"""
Настраивает приложение перед его запуском.

Загружает файл конфигурации, настраивает отдельные компоненты приложения.
"""

import config
from . import _config, _logging, _modules
from utils.file import load_file


def setup() -> None:
    """Настраивает приложение перед его запуском."""

    # # Настройка конфигурации приложения
    _config.setup()

    # # Настройка логирования приложения
    _logging.setup()

    # # Настройка модулей приложения
    _modules.setup()
