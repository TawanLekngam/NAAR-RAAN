"""
    theme.py for control theme of view of application.
"""

import os
from PySide6.QtGui import QFont


class Theme:
    __ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    __THEME_PATH = os.path.join(__ROOT_DIR, "theme.qss")

    """
    Aplication font.
    """
    DONGLE_REGULAR_50 = QFont("Dongle")
    DONGLE_REGULAR_50.setPixelSize(50)

    DONGLE_REGULAR_65 = QFont("Dongle")
    DONGLE_REGULAR_65.setPixelSize(65)

    DONGLE_BOLD_80 = QFont("Dongle")
    DONGLE_BOLD_80.setPixelSize(80)
    DONGLE_BOLD_80.setBold(True)

    DONGLE_BOLD_70 = QFont("Dongle")
    DONGLE_BOLD_70.setPixelSize(70)
    DONGLE_BOLD_70.setBold(True)

    DONGLE_BOLD_65 = QFont("Dongle")
    DONGLE_BOLD_65.setPixelSize(65)
    DONGLE_BOLD_65.setBold(True)

    """
    Operation for get stylesheet.
    """
    @staticmethod
    def get_stylesheet() -> str:
        """get style from theme.qss file"""
        stylesheet: str
        with open(Theme.__THEME_PATH, "r") as file:
            stylesheet = file.read()
        file.close()
        return stylesheet

    #Colors (Just in case)
    # DARK_BROWN = "4A321C"
    # LIGHT_BROWN = "754926"
    # CREAM = "D8B797"
    # EGG_WHITE = "F9F5F0"
