# -*- coding: utf-8 -*-
"""Функция для получения тектовых данных."""

from config import App


def get_text(text: str) -> dict | str:
    """Возвращает текст по указанным заголовкам.

    Args:
        text (str): Загловок текста. Например: ExampleMenu.button

    Returns:
        dict | str: Вернёт строку в случае, если указан полный путь к заголовку
            текста. Вернёт словарь в противном случае.
    """
    # # Разделение текста на заголовки
    text_headers: dict[str] = text.split(".")

    # # Входим в первый заголовок
    result = App.text.get(text_headers[0], None)

    # # Возвращает "Text Not Found"
    # Чтобы не вызывать ошибку и не мучаться с её обработкой
    if result is None:
        return "Text Not Found."

    # # Переходит по указанным заголовкам
    for header in text_headers[1:]:
        result = result.get(header, None)
        if result is None:
            return "Text Not Found."

    return result
