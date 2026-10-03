# -*- coding: utf-8 -*-
"""
Утилита для работы с файлами.

Определяет функции для чтения / записи фалов разных типов (ini, toml, txt, ...)
"""

# TODO: Добавить поддержку INI-файлов.


from ._load_file import load_file  # noqa: F401
from ._write_file import write_file  # noqa: F401
