# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_media_cuts_thread.ui'
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
        MainWindow.resize(448, 406)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #111111;\n"
"    color: #D8DEE9;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4C566A;\n"
"    border: 1px solid #434C5E;\n"
"    color: #D8DEE9;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.close_window_button = QPushButton(self.centralwidget)
        self.close_window_button.setObjectName(u"close_window_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_window_button.sizePolicy().hasHeightForWidth())
        self.close_window_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon)

        self.gridLayout_6.addWidget(self.close_window_button, 0, 2, 1, 1)

        self.minimize_window_button = QPushButton(self.centralwidget)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        sizePolicy.setHeightForWidth(self.minimize_window_button.sizePolicy().hasHeightForWidth())
        self.minimize_window_button.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.gridLayout_6.addWidget(self.minimize_window_button, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(364, 27, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 296))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 1, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #111111;\n"
"    border: 1px solid #434C5E;\n"
"    color: #D8DEE9;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/icons8-pushpin-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QSize(15, 16))

        self.gridLayout.addWidget(self.pushButton_14, 0, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.frame)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout.addWidget(self.timeEdit, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 185))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setBaseSize(QSize(0, 0))
        self.frame_6.setStyleSheet(u"QWidget {\n"
"    background-color: #1C1C1C;\n"
"    color: #D8DEE9;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_6)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.pushButton_13 = QPushButton(self.frame_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"icons/icons8-label-emoji-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon3)
        self.pushButton_13.setIconSize(QSize(44, 17))

        self.gridLayout_35.addWidget(self.pushButton_13, 1, 0, 1, 1)

        self.progressBar_5 = QProgressBar(self.frame_6)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setValue(0)

        self.gridLayout_35.addWidget(self.progressBar_5, 3, 0, 1, 1)

        self.textEdit_10 = QTextEdit(self.frame_6)
        self.textEdit_10.setObjectName(u"textEdit_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_10.sizePolicy().hasHeightForWidth())
        self.textEdit_10.setSizePolicy(sizePolicy1)
        self.textEdit_10.setMinimumSize(QSize(0, 0))
        self.textEdit_10.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_35.addWidget(self.textEdit_10, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.close_window_button.setText("")
        self.minimize_window_button.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Info:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Created at:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mediabase:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cuts Duration: 60s", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Target: 0/41 ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Thread id:", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Thread:", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Progress Create:", None))
    # retranslateUi

