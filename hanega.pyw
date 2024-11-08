import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile
from libs import ui


class MainWindow(QMainWindow):
    def accept(self):
        print("Done")
        self.close()

    def reject(self):
        self.close()

    def selectMigoto(self):
        migotoPath, selectedFilter = QFileDialog.getOpenFileUrl(self, "Select 3DMigoto Executable", "C:/",
                                                                "3DMigoto Executable (3DMigoto.exe);;All Executables (*.exe)")
        self.migotoPath = migotoPath.toLocalFile()
        self.ui.migotoPathField.setText(self.migotoPath)

    def selectGenshin(self):
        genshinPath, selectedFilter = QFileDialog.getOpenFileUrl(self, "Select Genshin Impact Executable", "C:/",
                                                                 "Genshin Impact Executable (GenshinImpact.exe);;All Executables (*.exe)")
        self.genshinPath = genshinPath.toLocalFile()
        self.ui.genshinPathField.setText(self.genshinPath)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui.InitialConfig()
        self.ui.setupUi(self)
        self.migotoPath = None
        self.genshinPath = None


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
