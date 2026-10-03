# -*- coding: utf-8 -*-
"""Загружает данные из файла конфигурации."""

import config
from utils.file import load_file


def setup() -> None:
    """
    Загружает данные из файла конфигурации.

    Обрабатывает возможное отсутствие некоторых данных и устанавливает для них
    значение по умолчанию.
    """
    config_data: dict = load_file(file_path=config.App.config_path)

    # # Загрузка конфигурации логирования
    logging_config: dict = config_data.get("logging", {})
    if logging_config is None:
        raise ValueError

    # # Чтение данных конфигурации с обработкой их возможного отсутствия
    log_files: list[str] = logging_config.get(
        "files",
        config.DefaultLogging.file_path
    )
    config.Logging.console = logging_config.get(
        "console",
        config.DefaultLogging.console
    )
    config.Logging.file_path = config.App.path.joinpath(*log_files)
    config.Logging.format_ = logging_config.get(
        "format",
        config.DefaultLogging.format_
    )
    config.Logging.level = logging_config.get(
        "level",
        config.DefaultLogging.level
    )
    config.Logging.rotation = logging_config.get(
        "rotation",
        config.DefaultLogging.rotation
    )
