# Created by BaiJiFeiLong@gmail.com at 2020/5/14 18:35

from PySide2 import QtWidgets

from ppledigester import log_utils
from ppledigester.DigesterWindow import DigesterWindow
from ppledigester.common import translator


class DigesterApplication(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()
        self.logger = log_utils.get_logger("Application")
        translator.locale = "zh_CN"
        self.logger.info("Application locale changed to zh_CN.")
        self.setApplicationName("PpleDigester")
        self.setApplicationDisplayName(translator.translate("APP_NAME"))
        self.setApplicationVersion("0.0.1")
        self.main_window = DigesterWindow()
        self.logger.info("Main window created.")
        self.main_window.show()

    def run(self):
        self.exec_()
