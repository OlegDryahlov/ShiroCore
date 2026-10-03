# -*- coding: utf-8 -*-
"""Конфигурация приложения."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class App:  # # Настройки приложения

    # * Путь к директории приложения
    path: Path = Path(".").resolve()

    # * Путь к файлу конфигурации приложения
    config_path: Path = path / "config.toml"

    # * Путь к директории модулей приложения
    modules_path: Path = path / "ShiroCore" / "modules"

    # * Путь к файлу "__init__.py" в директории модулей приложения
    modules_init_path: Path = modules_path / "__init__.py"

    # * Путь к файлу с шаблонами для генерации файла "__init__.py" в
    # * директории модулей приложения
    modules_init_base_path: Path = path / "__init__.py_base.toml"

    # * Текст приложения
    # ! Значение переменной устанавливается во время настройки приложения
    # ! так как приложение загружает текст со всех модулей
    text = {}

    # * Путь к файлу с текстом приложения
    text_path: Path = path / "text.toml"


# # Настройки по умолчанию

@dataclass(frozen=True)  # # Настройки по умолчанию для логирования
class DefaultLogging:

    # * Выводить ли логи приложения в терминал
    console: bool = False

    # * Путь к файлам с логами приложения
    file_path: Path = App.path.joinpath(*["logs", "logs_ShiroCore.txt"])

    # * Формат сообщений логов
    format_: str = "{time:HH:mm:ss} | {level: <8} | {module} | {message}"

    # * Минимальный уровень сообщения для записи в файл
    level: str = "INFO"

    # * Периодичность создания нового файла с логами
    rotation: str = "24h"


# # Настройки загружаемые из файла конфигурации
# ! Значения переменным присваиваются при настройке приложения во время запуска

@dataclass  # # Настройки логирования
class Logging:

    console: bool
    file_path: Path
    format_: str
    level: str
    rotation: str
