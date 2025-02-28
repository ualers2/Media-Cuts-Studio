# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_ControlPanelLogin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 935)
        MainWindow.setStyleSheet(u"background:white")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background: #ffffff;\n"
"    border-radius: 16px;\n"
"    padding: 72px 0px 72px 0px;\n"
"    min-height: 773px;\n"
"    overflow: hidden;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 46))
        self.label.setMaximumSize(QSize(16777215, 58))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #1a1e29;\n"
"    text-align: left;\n"
"    font-family: \"ABeeZee-Regular\", sans-serif;\n"
"    font-size: 13px;\n"
"    letter-spacing: 0.016em;\n"
"    font-weight: 400;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 3)

        self.label_hello_3 = QLabel(self.frame)
        self.label_hello_3.setObjectName(u"label_hello_3")
        self.label_hello_3.setMinimumSize(QSize(44, 44))
        self.label_hello_3.setMaximumSize(QSize(44, 44))
        self.label_hello_3.setStyleSheet(u"")
        self.label_hello_3.setPixmap(QPixmap(u":/web_icons/icons/web_icons/rectangle-3370.png"))
        self.label_hello_3.setScaledContents(False)

        self.gridLayout_2.addWidget(self.label_hello_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(52, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 449, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.mensage_input = QTextEdit(self.frame)
        self.mensage_input.setObjectName(u"mensage_input")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mensage_input.sizePolicy().hasHeightForWidth())
        self.mensage_input.setSizePolicy(sizePolicy)
        self.mensage_input.setMinimumSize(QSize(0, 795))
        self.mensage_input.setMaximumSize(QSize(16777215, 48))
        self.mensage_input.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.mensage_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mensage_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.mensage_input, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.mensage_input_2 = QTextEdit(self.frame)
        self.mensage_input_2.setObjectName(u"mensage_input_2")
        sizePolicy.setHeightForWidth(self.mensage_input_2.sizePolicy().hasHeightForWidth())
        self.mensage_input_2.setSizePolicy(sizePolicy)
        self.mensage_input_2.setMinimumSize(QSize(0, 795))
        self.mensage_input_2.setMaximumSize(QSize(16777215, 48))
        self.mensage_input_2.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.mensage_input_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mensage_input_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.mensage_input_2, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/web_icons/icons/web_icons/group0.svg"))

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Media Cuts Studio", None))
        self.label_hello_3.setText("")
        self.mensage_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message...", None))
        self.mensage_input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message...", None))
        self.label_2.setText("")
    # retranslateUi

