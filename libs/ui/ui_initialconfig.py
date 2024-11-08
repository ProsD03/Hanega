# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InitialConfig.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class InitialConfig(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(390, 196)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 371, 192))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.migotoPathField = QLineEdit(self.widget)
        self.migotoPathField.setObjectName(u"migotoPathField")
        self.migotoPathField.setEnabled(False)

        self.horizontalLayout.addWidget(self.migotoPathField)

        self.selectMigotoButton = QPushButton(self.widget)
        self.selectMigotoButton.setObjectName(u"selectMigotoButton")

        self.horizontalLayout.addWidget(self.selectMigotoButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.genshinPathField = QLineEdit(self.widget)
        self.genshinPathField.setObjectName(u"genshinPathField")
        self.genshinPathField.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.genshinPathField)

        self.selectGenshinButton = QPushButton(self.widget)
        self.selectGenshinButton.setObjectName(u"selectGenshinButton")

        self.horizontalLayout_2.addWidget(self.selectGenshinButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.uacCheckbox = QCheckBox(self.widget)
        self.uacCheckbox.setObjectName(u"uacCheckbox")

        self.verticalLayout_2.addWidget(self.uacCheckbox)

        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Hanega Initial Configuration", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"3DMigoto Executable Path", None))
        self.selectMigotoButton.setText(QCoreApplication.translate("Dialog", u"Select...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Genshin Impact Executable Path", None))
        self.selectGenshinButton.setText(QCoreApplication.translate("Dialog", u"Select...", None))
        self.uacCheckbox.setText(QCoreApplication.translate("Dialog", u"Remove \"Run as Admin\" pop-up?", None))
    # retranslateUi

