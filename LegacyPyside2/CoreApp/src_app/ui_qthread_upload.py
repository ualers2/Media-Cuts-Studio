# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_qthread_upload.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomQPushButton import QCustomQPushButton
from PySide2extn.RoundProgressBar import roundProgressBar
from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 757)
        MainWindow.setMinimumSize(QSize(800, 0))
        MainWindow.setMaximumSize(QSize(1045, 16777215))
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #ffffff;\n"
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(408, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(182, -1, 0, 0)
        self.restore_window_button = QCustomQPushButton(self.centralwidget)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMinimumSize(QSize(50, 0))
        self.restore_window_button.setMaximumSize(QSize(50, 16777215))
        self.restore_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon)

        self.gridLayout_2.addWidget(self.restore_window_button, 0, 6, 1, 1)

        self.minimize_window_button = QCustomQPushButton(self.centralwidget)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_window_button.sizePolicy().hasHeightForWidth())
        self.minimize_window_button.setSizePolicy(sizePolicy)
        self.minimize_window_button.setMinimumSize(QSize(50, 0))
        self.minimize_window_button.setMaximumSize(QSize(50, 16777215))
        self.minimize_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.gridLayout_2.addWidget(self.minimize_window_button, 0, 5, 1, 1)

        self.close_window_button = QCustomQPushButton(self.centralwidget)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(50, 0))
        self.close_window_button.setMaximumSize(QSize(50, 16777215))
        self.close_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon2)

        self.gridLayout_2.addWidget(self.close_window_button, 0, 7, 1, 1)

        self.pushButton_5 = QCustomQPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 28))
        self.pushButton_5.setMaximumSize(QSize(50, 28))
        self.pushButton_5.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_solid/icons/font_awesome/solid/arrow-right-long.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon3)

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/font_awesome_solid/icons/font_awesome/solid/arrow-left-long.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.widget_preview_slide = QCustomSlideMenu(self.centralwidget)
        self.widget_preview_slide.setObjectName(u"widget_preview_slide")
        self.gridLayout_48 = QGridLayout(self.widget_preview_slide)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.AndroidPreviewWithAdb = QCustomQPushButton(self.widget_preview_slide)
        self.AndroidPreviewWithAdb.setObjectName(u"AndroidPreviewWithAdb")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AndroidPreviewWithAdb.sizePolicy().hasHeightForWidth())
        self.AndroidPreviewWithAdb.setSizePolicy(sizePolicy2)
        self.AndroidPreviewWithAdb.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/Mediacuts/icons/mediacuts/icons8-android-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AndroidPreviewWithAdb.setIcon(icon5)

        self.gridLayout_48.addWidget(self.AndroidPreviewWithAdb, 0, 0, 1, 1)

        self.AndroidPreviewWithApp = QCustomQPushButton(self.widget_preview_slide)
        self.AndroidPreviewWithApp.setObjectName(u"AndroidPreviewWithApp")
        self.AndroidPreviewWithApp.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        self.AndroidPreviewWithApp.setIcon(icon5)

        self.gridLayout_48.addWidget(self.AndroidPreviewWithApp, 0, 1, 1, 1)

        self.stackedWidget_preview = QStackedWidget(self.widget_preview_slide)
        self.stackedWidget_preview.setObjectName(u"stackedWidget_preview")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_12 = QGridLayout(self.page_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.openGLWidget_Adb = QOpenGLWidget(self.page_5)
        self.openGLWidget_Adb.setObjectName(u"openGLWidget_Adb")

        self.gridLayout_12.addWidget(self.openGLWidget_Adb, 1, 0, 1, 1)

        self.stackedWidget_preview.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_13 = QGridLayout(self.page_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.openGLWidget_App = QOpenGLWidget(self.page_6)
        self.openGLWidget_App.setObjectName(u"openGLWidget_App")

        self.gridLayout_13.addWidget(self.openGLWidget_App, 0, 0, 1, 1)

        self.stackedWidget_preview.addWidget(self.page_6)

        self.gridLayout_48.addWidget(self.stackedWidget_preview, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.widget_preview_slide, 1, 3, 2, 1)

        self.widget_slidemenu = QCustomSlideMenu(self.centralwidget)
        self.widget_slidemenu.setObjectName(u"widget_slidemenu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_slidemenu.sizePolicy().hasHeightForWidth())
        self.widget_slidemenu.setSizePolicy(sizePolicy3)
        self.widget_slidemenu.setMinimumSize(QSize(37, 669))
        self.widget_slidemenu.setMaximumSize(QSize(37, 669))
        self.widget_slidemenu.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_slidemenu)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(0, 537, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.upload_Home = QCustomQPushButton(self.widget_slidemenu)
        self.upload_Home.setObjectName(u"upload_Home")
        self.upload_Home.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_Home.setIcon(icon6)
        self.upload_Home.setIconSize(QSize(18, 17))

        self.gridLayout_3.addWidget(self.upload_Home, 1, 0, 1, 1)

        self.upload_ACC = QCustomQPushButton(self.widget_slidemenu)
        self.upload_ACC.setObjectName(u"upload_ACC")
        self.upload_ACC.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Mediacuts/icons/mediacuts/do-utilizador (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_ACC.setIcon(icon7)

        self.gridLayout_3.addWidget(self.upload_ACC, 2, 0, 1, 1)

        self.upload_Metrics = QCustomQPushButton(self.widget_slidemenu)
        self.upload_Metrics.setObjectName(u"upload_Metrics")
        self.upload_Metrics.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/Mediacuts/icons/mediacuts/icons8-velocidade-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_Metrics.setIcon(icon8)

        self.gridLayout_3.addWidget(self.upload_Metrics, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_slidemenu, 2, 0, 1, 1)

        self.stackedWidget = QCustomQStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(400, 16777215))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #E0E0E0; /* Borda ao redor */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QStackedWidget QWidget {\n"
"    background-color: transparent; /* Fundo transparente dos widgets internos */\n"
"    color: black; /* Cor do texto dentro do QStackedWidget */\n"
"    font-size: 16px; /* Tamanho da fonte do texto interno */\n"
"}\n"
"\n"
"QStackedWidget:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_8 = QGridLayout(self.page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_previsao = QLabel(self.page)
        self.label_previsao.setObjectName(u"label_previsao")
        self.label_previsao.setStyleSheet(u"QLabel {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 8px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")
        self.label_previsao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_previsao.setMargin(-2)
        self.label_previsao.setIndent(1)

        self.gridLayout_7.addWidget(self.label_previsao, 1, 0, 1, 1)

        self.label_41 = QLabel(self.page)
        self.label_41.setObjectName(u"label_41")
        sizePolicy1.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy1)
        self.label_41.setMinimumSize(QSize(358, 31))
        self.label_41.setMaximumSize(QSize(16777215, 30))
        self.label_41.setStyleSheet(u"QLabel {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 8px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")
        self.label_41.setIndent(0)

        self.gridLayout_7.addWidget(self.label_41, 0, 0, 1, 1)

        self.pushButton_3 = QCustomQPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/play-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon9)

        self.gridLayout_7.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.pushButton_2 = QCustomQPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"				border: 1px solid #F7F7F7; /* Borda */\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon10)

        self.gridLayout_7.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.timeEdit_2 = QTimeEdit(self.page)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setStyleSheet(u"QTimeEdit {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 16px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QTimeEdit::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QTimeEdit::up-button, QTimeEdit::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 1px; /* Espa\u00e7amento ao redor dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada dos bot\u00f5es */\n"
"}\n"
"\n"
"QTimeEdit::up-button:hover, QTimeEdit::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QTimeEdit::up-button:pressed, QTimeEdit"
                        "::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QTimeEdit::up-arrow, QTimeEdit::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"\n"
"QTimeEdit:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.timeEdit_2, 0, 2, 1, 2)


        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 168, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_kwai = roundProgressBar(self.page)
        self.widget_kwai.setObjectName(u"widget_kwai")
        self.widget_kwai.setMinimumSize(QSize(141, 141))
        self.widget_kwai.setMaximumSize(QSize(141, 141))

        self.gridLayout_9.addWidget(self.widget_kwai, 1, 1, 1, 1)

        self.widget_tiktok = roundProgressBar(self.page)
        self.widget_tiktok.setObjectName(u"widget_tiktok")
        self.widget_tiktok.setMinimumSize(QSize(141, 141))
        self.widget_tiktok.setMaximumSize(QSize(141, 141))

        self.gridLayout_9.addWidget(self.widget_tiktok, 1, 0, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 8px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 8px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 7, 0, 1, 1)

        self.textEdit = QTextEdit(self.page)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(0, 207))
        self.textEdit.setMaximumSize(QSize(490, 207))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #E0E0E0; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 16px; /* Tamanho da fonte */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    background-color: #FFFFFF; /* Fundo ao focar */\n"
"    border: 1px solid #A0A0A0; /* Borda ao focar */\n"
"}\n"
"\n"
"QTextEdit:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.textEdit, 3, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_youtube = QLabel(self.page)
        self.label_youtube.setObjectName(u"label_youtube")
        font = QFont()
        self.label_youtube.setFont(font)
        self.label_youtube.setStyleSheet(u"QLabel {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 8px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.label_youtube, 0, 2, 1, 1)

        self.label_tiktok = QLabel(self.page)
        self.label_tiktok.setObjectName(u"label_tiktok")
        self.label_tiktok.setFont(font)
        self.label_tiktok.setStyleSheet(u"QLabel {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 8px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.label_tiktok, 0, 0, 1, 1)

        self.label_kwai = QLabel(self.page)
        self.label_kwai.setObjectName(u"label_kwai")
        self.label_kwai.setFont(font)
        self.label_kwai.setStyleSheet(u"QLabel {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 8px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.label_kwai, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.treeView_perfis = QTreeView(self.page_2)
        self.treeView_perfis.setObjectName(u"treeView_perfis")

        self.gridLayout_6.addWidget(self.treeView_perfis, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_11 = QGridLayout(self.page_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.widgetviews = QWidget(self.page_3)
        self.widgetviews.setObjectName(u"widgetviews")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widgetviews.sizePolicy().hasHeightForWidth())
        self.widgetviews.setSizePolicy(sizePolicy4)
        self.widgetviews.setMinimumSize(QSize(400, 600))
        self.widgetviews.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.widgetviews, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_preview.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.restore_window_button.setText("")
        self.minimize_window_button.setText("")
        self.close_window_button.setText("")
        self.pushButton_5.setText("")
        self.pushButton.setText("")
        self.AndroidPreviewWithAdb.setText(QCoreApplication.translate("MainWindow", u"Preview\n"
"Adb", None))
        self.AndroidPreviewWithApp.setText(QCoreApplication.translate("MainWindow", u"Preview\n"
"App", None))
        self.upload_Home.setText("")
        self.upload_ACC.setText("")
        self.upload_Metrics.setText("")
        self.label_previsao.setText(QCoreApplication.translate("MainWindow", u"Previs\u00e3o De Tempo: 00h 00m 00s", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"N/possiveis Cortes: 00", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Full Tiktok Load Today:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Full Kwai Load Today:", None))
        self.label_youtube.setText(QCoreApplication.translate("MainWindow", u"Youtube: 0", None))
        self.label_tiktok.setText(QCoreApplication.translate("MainWindow", u"Tiktok: 0", None))
        self.label_kwai.setText(QCoreApplication.translate("MainWindow", u"Kwai: 0", None))
    # retranslateUi

