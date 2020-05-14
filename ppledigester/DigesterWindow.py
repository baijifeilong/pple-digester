# Created by BaiJiFeiLong@gmail.com at 2020/5/14 18:51

from PySide2 import QtWidgets

from ppledigester import log_utils
from ppledigester.common import translator


class DigesterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.logger = log_utils.get_logger("MainWindow")
        self.resize(600, 400)
        self.logger.info("Window resize to 600x400")
        self.statusBar().showMessage(translator.translate("DRAG_TIP"))
        self.logger.info("The tip in status bar is shown.")
