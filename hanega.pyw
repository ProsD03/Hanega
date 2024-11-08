import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from pathlib import Path
from libs import ui


class MainWindow(QMainWindow):
    def accept(self):
        print("Done")
        self.close()

    def reject(self):
        self.close()

    def selectMigoto(self):
        migotoPath, selectedFilter = QFileDialog.getOpenFileUrl(self, "Select 3DMigoto Executable", str(Path.home()),
                                                                "All Executables (*.exe)")
        self.migotoPath = migotoPath.toLocalFile()
        self.ui.migotoPathField.setText(self.migotoPath)

    def selectGenshin(self):
        genshinPath, selectedFilter = QFileDialog.getOpenFileUrl(self, "Select Genshin Impact Executable",
                                                                 str(Path.home()),"All Executables (*.exe)")
        self.genshinPath = genshinPath.toLocalFile()
        self.ui.genshinPathField.setText(self.genshinPath)

    def regeditCheckbox(self):
        if self.ui.uacCheckbox.isChecked():
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Hanega will make changes to certain Windows Registry keys and configuration files to remove "
                        "the \"Run as Admin\" pop-up (UAC) requirements from the 3DMigoto and Genshin Impact "
                        "executables. This action will only alter settings related to 3DMigoto and Genshin Impact. "
                        "Nevertheless, this action may impact system functionality, and previous settings cannot be "
                        "restored by Hanega.\n\nWould you like to proceed?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDefaultButton(QMessageBox.Yes)
            value = msg.exec()
            if value != QMessageBox.Yes:
                self.ui.uacCheckbox.setChecked(False)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui.InitialConfig()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.selectMigotoButton.clicked.connect(self.selectMigoto)
        self.ui.selectGenshinButton.clicked.connect(self.selectGenshin)
        self.ui.uacCheckbox.clicked.connect(self.regeditCheckbox)

        self.migotoPath = None
        self.genshinPath = None


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
