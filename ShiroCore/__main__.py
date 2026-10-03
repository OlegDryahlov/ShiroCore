# -*- coding: utf-8 -*-
"""
ShiroCore - приложение-ядро для запуска модулей серии Shiro.

Работа с приложением производится с помощью системы модулей, которые
настраиваются при его запуске. Благодаря этому можно настроить приложение
под различные задачи и нужды конкретного пользователя.

Разработчик: OlegDryahlov
GitHub: https://github.com/OlegDryahlov/ShiroCore
Лицензия: MIT License
"""

from loguru import logger

import setup


def main() -> None:
    """If __name__ == "__main__"."""
    # # Настройка приложения перед запуском
    setup.setup()

    # # Запуск приложения
    # Импорт объекта меню производится после настройки приложения, чтобы
    # файл "modules.__init__.py" был заново сгенерирован
    from modules import menu

    logger.info("Запуск ShiroCore.")

    menu.show()


if __name__ == "__main__":
    main()
