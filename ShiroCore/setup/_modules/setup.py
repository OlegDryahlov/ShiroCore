# -*- coding: utf-8 -*-
"""Настраивает модули приложения."""

# TODO: Реализовать проверку зависимостей

from pathlib import Path

from loguru import logger

from ._create_init_file import create_init_file
from ._load_modules_data import load_modules_data
from ._process_text_data import process_text_data
from config import App


def setup() -> None:
    """Загружает и настраивает установленные модули приложения."""
    logger.trace("Настраиваю модули приложения.")  # Логирование

    # # Пути к директориям модулей приложения
    # Модуль должен быть директорией и содержать файл "module.toml"
    modules_dirs: list[Path] = [
        dir_
        for dir_ in App.modules_path.iterdir()
        if dir_.is_dir() and (dir_ / "module.toml").is_file()
    ]

    # # Чтение и обработка данных модулей приложения
    modules_data: list[dict] = load_modules_data(modules_dirs=modules_dirs)

    # # Создание файла "modules.__init__.py" на основе данных модулей
    create_init_file(modules_data=modules_data)

    # # Обрабатывает текстовые данные модулей и сохраняет их в конфигурацию
    process_text_data(modules_data=modules_data)

    logger.trace("Модули приложения загружены и настроены.")  # Логирование
