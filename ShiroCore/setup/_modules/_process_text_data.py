# -*- coding: utf-8 -*-
"""Обрабатывает данные из текстовых файлов приложений."""

from loguru import logger

from config import App


def process_text_data(modules_data: list[dict]) -> None:
    """Обрабатывает данные из текстовых файлов приложений.

    И сохраняет их в конфигурацию приложения.

    Args:
        modules_data (list[dict]): Список данных модулей.
    """
    logger.trace("Обрабатываю текстовые данные модулей.")  # Логирование

    # # Словарь с текстовыми данными всех модулей
    text_data: dict = {}

    # # Обрабатываем все модули
    for module in modules_data:
        module_name: str = module.get("name")

        module_text: dict = module.get("text")

        # * Если в модуле отсутствуют текстовые данные - пропускаем его
        if module_text is None:
            continue

        text_data[module_name] = module_text

    # # Сохраням текстовые данные модулей в конфигурацию
    App.text = text_data

    logger.trace("Текстовые данные модулей обработаны.")
