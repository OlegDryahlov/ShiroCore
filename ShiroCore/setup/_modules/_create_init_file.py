# -*- coding: utf-8 -*-
"""Генерирует файл modules.__init__.py согласно дата-файлов модулей."""

from loguru import logger

from config import App
from utils.file import load_file, write_file


def create_init_file(modules_data: list[dict]) -> None:
    """Генерирует файл modules.__init__.py на основе данных модулей.

    Args:
        modules_data (list[dict]): Список данных модулей.
    """
    # Логирование
    logger.trace(f"Генерирую файл __init__.py: \"{App.modules_init_path}\".")

    import_menu: str = ""
    import_modules: list[str] = []

    # # Шаблоны для файла "__init__.py"
    base: dict = load_file(file_path=App.modules_init_base_path)

    # # Заполнение данных для файла
    for module in modules_data:

        match module["type"]:

            case "menu":
                import_menu = base["import"]["menu"].format(dir_=module["dir"])

            case "module":
                import_modules.append(
                    base["import"]["module"].format(
                        dir_=module["dir"],
                        name=module["name"]
                    )
                )

    # # Список названий модулей
    # Список названий модулей который будет передан в меню приложения
    modules_names: list[str] = [
        i["name"]
        for i in modules_data
        if i["type"] == "module"
    ]

    logger.trace("Содержимое файла сгенерировано.")  # Логирование

    # # Запись в файл "__init__.py"
    file_data: str = base["file"].format(
        import_menu=import_menu,
        import_modules="\n".join(import_modules),
        modules_names=",\n\t\t".join(modules_names)
    )
    write_file(file_data=file_data, file_path=App.modules_init_path)

    logger.trace("Файл успешно создан и записан.")  # Логирование
