# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
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
from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomQSlider import QCustomQSlider
from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1188, 747)
        font = QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background:white\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_slidemenu = QCustomSlideMenu(self.centralwidget)
        self.widget_slidemenu.setObjectName(u"widget_slidemenu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_slidemenu.sizePolicy().hasHeightForWidth())
        self.widget_slidemenu.setSizePolicy(sizePolicy)
        self.widget_slidemenu.setMinimumSize(QSize(142, 669))
        self.widget_slidemenu.setMaximumSize(QSize(142, 669))
        self.widget_slidemenu.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_slidemenu)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.subcolor_button = QPushButton(self.widget_slidemenu)
        self.subcolor_button.setObjectName(u"subcolor_button")
        self.subcolor_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon = QIcon()
        icon.addFile(u":/Mediacuts/icons/mediacuts/icons8-c\u00edrculo-rgb-2-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.subcolor_button.setIcon(icon)
        self.subcolor_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.subcolor_button, 18, 0, 1, 1)

        self.subfont_button = QPushButton(self.widget_slidemenu)
        self.subfont_button.setObjectName(u"subfont_button")
        self.subfont_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Mediacuts/icons/mediacuts/icons8-escolha-a-fonte-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.subfont_button.setIcon(icon1)
        self.subfont_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.subfont_button, 17, 0, 1, 1)

        self.subfontsizre_button = QPushButton(self.widget_slidemenu)
        self.subfontsizre_button.setObjectName(u"subfontsizre_button")
        self.subfontsizre_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/Mediacuts/icons/mediacuts/icons8-altura-do-texto-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.subfontsizre_button.setIcon(icon2)
        self.subfontsizre_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.subfontsizre_button, 19, 0, 1, 1)

        self.subannimation_button = QPushButton(self.widget_slidemenu)
        self.subannimation_button.setObjectName(u"subannimation_button")
        self.subannimation_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/Mediacuts/icons/mediacuts/icons8-anima\u00e7\u00e3o-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.subannimation_button.setIcon(icon3)
        self.subannimation_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.subannimation_button, 20, 0, 1, 1)

        self.subeffects_button = QPushButton(self.widget_slidemenu)
        self.subeffects_button.setObjectName(u"subeffects_button")
        self.subeffects_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/Mediacuts/icons/mediacuts/icons8-efeitos-visuais-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.subeffects_button.setIcon(icon4)
        self.subeffects_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.subeffects_button, 21, 0, 1, 1)

        self.CutingTIME_button = QPushButton(self.widget_slidemenu)
        self.CutingTIME_button.setObjectName(u"CutingTIME_button")
        self.CutingTIME_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/Mediacuts/icons/mediacuts/icons8-tesoura-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CutingTIME_button.setIcon(icon5)
        self.CutingTIME_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.CutingTIME_button, 7, 0, 1, 1)

        self.Hardware_button = QPushButton(self.widget_slidemenu)
        self.Hardware_button.setObjectName(u"Hardware_button")
        self.Hardware_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/Mediacuts/icons/mediacuts/icons8-cpu-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Hardware_button.setIcon(icon6)
        self.Hardware_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.Hardware_button, 6, 0, 1, 1)

        self.thread_button = QPushButton(self.widget_slidemenu)
        self.thread_button.setObjectName(u"thread_button")
        self.thread_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Mediacuts/icons/mediacuts/icons8-processador-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.thread_button.setIcon(icon7)
        self.thread_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.thread_button, 9, 0, 1, 1)

        self.subreference_button = QPushButton(self.widget_slidemenu)
        self.subreference_button.setObjectName(u"subreference_button")
        self.subreference_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/Mediacuts/icons/mediacuts/icons8-redimensionar-vertical-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.subreference_button.setIcon(icon8)
        self.subreference_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.subreference_button, 22, 0, 1, 1)

        self.scale_button = QPushButton(self.widget_slidemenu)
        self.scale_button.setObjectName(u"scale_button")
        self.scale_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/Mediacuts/icons/mediacuts/icons8-cortar-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scale_button.setIcon(icon9)
        self.scale_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.scale_button, 11, 0, 1, 1)

        self.RemovingWords = QPushButton(self.widget_slidemenu)
        self.RemovingWords.setObjectName(u"RemovingWords")
        self.RemovingWords.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/font_awesome_solid/icons/font_awesome/solid/florin-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RemovingWords.setIcon(icon10)
        self.RemovingWords.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.RemovingWords, 13, 0, 1, 1)

        self.watermask_button = QPushButton(self.widget_slidemenu)
        self.watermask_button.setObjectName(u"watermask_button")
        self.watermask_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/Mediacuts/icons/mediacuts/icons8-borrar-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.watermask_button.setIcon(icon11)
        self.watermask_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.watermask_button, 12, 0, 1, 1)

        self.AI_button = QPushButton(self.widget_slidemenu)
        self.AI_button.setObjectName(u"AI_button")
        self.AI_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/Mediacuts/icons/mediacuts/icons8-ai-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AI_button.setIcon(icon12)
        self.AI_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.AI_button, 5, 0, 1, 1)

        self.upload_secn_button = QPushButton(self.widget_slidemenu)
        self.upload_secn_button.setObjectName(u"upload_secn_button")
        self.upload_secn_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/Mediacuts/icons/mediacuts/icons8-fazer-upload-100 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_secn_button.setIcon(icon13)
        self.upload_secn_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.upload_secn_button, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 459, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer, 29, 0, 1, 1)

        self.UploadMedia_base_button = QPushButton(self.widget_slidemenu)
        self.UploadMedia_base_button.setObjectName(u"UploadMedia_base_button")
        self.UploadMedia_base_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 11px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/Mediacuts/icons/mediacuts/icons8-folder-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.UploadMedia_base_button.setIcon(icon14)
        self.UploadMedia_base_button.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.UploadMedia_base_button, 3, 0, 1, 1)

        self.Start_media_Cuts = QPushButton(self.widget_slidemenu)
        self.Start_media_Cuts.setObjectName(u"Start_media_Cuts")
        self.Start_media_Cuts.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/Mediacuts/icons/mediacuts/icons8-online-startup-53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_media_Cuts.setIcon(icon15)
        self.Start_media_Cuts.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.Start_media_Cuts, 2, 0, 1, 1)

        self.Caption = QPushButton(self.widget_slidemenu)
        self.Caption.setObjectName(u"Caption")
        self.Caption.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/Mediacuts/icons/mediacuts/icons8-legendas-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Caption.setIcon(icon16)
        self.Caption.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.Caption, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_slidemenu, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(182, -1, 0, 0)
        self.close_window_button = QPushButton(self.centralwidget)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(50, 0))
        self.close_window_button.setMaximumSize(QSize(50, 16777215))
        self.close_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon17)

        self.gridLayout_2.addWidget(self.close_window_button, 0, 5, 1, 1)

        self.restore_window_button = QPushButton(self.centralwidget)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMinimumSize(QSize(50, 0))
        self.restore_window_button.setMaximumSize(QSize(50, 16777215))
        self.restore_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon18 = QIcon()
        icon18.addFile(u":/feather/icons/feather/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon18)

        self.gridLayout_2.addWidget(self.restore_window_button, 0, 4, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 28))
        self.pushButton_5.setMaximumSize(QSize(50, 28))
        self.pushButton_5.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon19 = QIcon()
        icon19.addFile(u":/font_awesome_solid/icons/font_awesome/solid/arrow-right-long.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon19)

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.minimize_window_button = QPushButton(self.centralwidget)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_window_button.sizePolicy().hasHeightForWidth())
        self.minimize_window_button.setSizePolicy(sizePolicy1)
        self.minimize_window_button.setMinimumSize(QSize(50, 0))
        self.minimize_window_button.setMaximumSize(QSize(50, 16777215))
        self.minimize_window_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon20 = QIcon()
        icon20.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon20)

        self.gridLayout_2.addWidget(self.minimize_window_button, 0, 3, 1, 1)

        self.Vertical_Preview = QPushButton(self.centralwidget)
        self.Vertical_Preview.setObjectName(u"Vertical_Preview")
        self.Vertical_Preview.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon21 = QIcon()
        icon21.addFile(u":/font_awesome_solid/icons/font_awesome/solid/ellipsis-vertical.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Vertical_Preview.setIcon(icon21)

        self.gridLayout_2.addWidget(self.Vertical_Preview, 0, 1, 1, 1)

        self.Horizontalpreview = QPushButton(self.centralwidget)
        self.Horizontalpreview.setObjectName(u"Horizontalpreview")
        self.Horizontalpreview.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon22 = QIcon()
        icon22.addFile(u":/font_awesome_solid/icons/font_awesome/solid/ellipsis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Horizontalpreview.setIcon(icon22)
        self.Horizontalpreview.setIconSize(QSize(17, 16))

        self.gridLayout_2.addWidget(self.Horizontalpreview, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(680, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon23 = QIcon()
        icon23.addFile(u":/font_awesome_solid/icons/font_awesome/solid/arrow-left-long.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon23)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.widget_preview_slide = QCustomSlideMenu(self.centralwidget)
        self.widget_preview_slide.setObjectName(u"widget_preview_slide")
        self.gridLayout_81 = QGridLayout(self.widget_preview_slide)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.stackedWidget_7 = QStackedWidget(self.widget_preview_slide)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.stackedWidget_7.setStyleSheet(u"QStackedWidget {\n"
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
"QStackedWidget:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QStackedWidget:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"")
        self.page_33 = QWidget()
        self.page_33.setObjectName(u"page_33")
        self.gridLayout_48 = QGridLayout(self.page_33)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.openGLWidget = QOpenGLWidget(self.page_33)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.gridLayout_48.addWidget(self.openGLWidget, 0, 0, 1, 1)

        self.stackedWidget_7.addWidget(self.page_33)
        self.page_34 = QWidget()
        self.page_34.setObjectName(u"page_34")
        self.stackedWidget_7.addWidget(self.page_34)

        self.gridLayout_81.addWidget(self.stackedWidget_7, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_preview_slide, 1, 3, 2, 1)

        self.stackedWidget = QCustomQStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(426, 669))
        self.stackedWidget.setMaximumSize(QSize(16777215, 669))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #E0E0E0; /* Borda ao redor */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_40 = QFrame(self.page)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_40)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.button_upload_video = QPushButton(self.frame_40)
        self.button_upload_video.setObjectName(u"button_upload_video")
        self.button_upload_video.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 18px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")
        icon24 = QIcon()
        icon24.addFile(u"../../Media Cuts (dev)/uisave/icons/icons8-adicionar-pasta-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_upload_video.setIcon(icon24)
        self.button_upload_video.setIconSize(QSize(45, 31))

        self.gridLayout_41.addWidget(self.button_upload_video, 1, 0, 1, 1)

        self.treeView = QTreeView(self.frame_40)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"")
        self.treeView.setFrameShape(QFrame.NoFrame)
        self.treeView.setFrameShadow(QFrame.Plain)

        self.gridLayout_41.addWidget(self.treeView, 3, 0, 1, 1)

        self.label_170 = QLabel(self.frame_40)
        self.label_170.setObjectName(u"label_170")

        self.gridLayout_41.addWidget(self.label_170, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_40, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_7 = QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_8 = QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_9 = QGridLayout(self.page_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_10 = QGridLayout(self.page_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.scrollArea_19 = QScrollArea(self.page_6)
        self.scrollArea_19.setObjectName(u"scrollArea_19")
        self.scrollArea_19.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m"
                        "\u00f3vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, Q"
                        "ScrollBar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_19.setFrameShape(QFrame.VLine)
        self.scrollArea_19.setFrameShadow(QFrame.Plain)
        self.scrollArea_19.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 483, 629))
        self.gridLayout_35 = QGridLayout(self.scrollAreaWidgetContents_19)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setHorizontalSpacing(34)
        self.gridLayout_34.setVerticalSpacing(72)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_119 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(81, 51))
        self.label_119.setMaximumSize(QSize(81, 51))
        self.label_119.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Century Gothic.gif"))
        self.label_119.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_119, 2, 1, 1, 1)

        self.button_Comic_Sans_MS_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_Comic_Sans_MS_sub.setObjectName(u"button_Comic_Sans_MS_sub")
        self.button_Comic_Sans_MS_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_Comic_Sans_MS_sub, 3, 2, 1, 1)

        self.label_120 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(81, 51))
        self.label_120.setMaximumSize(QSize(81, 51))
        self.label_120.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Comic Sans MS.gif"))
        self.label_120.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_120, 2, 2, 1, 1)

        self.button_CenturyGothic_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_CenturyGothic_sub.setObjectName(u"button_CenturyGothic_sub")
        self.button_CenturyGothic_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_CenturyGothic_sub, 3, 1, 1, 1)

        self.label_121 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(81, 51))
        self.label_121.setMaximumSize(QSize(81, 51))
        self.label_121.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Tahoma.gif"))
        self.label_121.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_121, 0, 0, 1, 1)

        self.button_Calibri_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_Calibri_sub.setObjectName(u"button_Calibri_sub")
        self.button_Calibri_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_Calibri_sub, 1, 2, 1, 1)

        self.button_LucidaConsole_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_LucidaConsole_sub.setObjectName(u"button_LucidaConsole_sub")
        self.button_LucidaConsole_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_LucidaConsole_sub, 1, 3, 1, 1)

        self.button_Tahoma_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_Tahoma_sub.setObjectName(u"button_Tahoma_sub")
        self.button_Tahoma_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_Tahoma_sub, 1, 0, 1, 1)

        self.label_122 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(81, 51))
        self.label_122.setMaximumSize(QSize(81, 51))
        self.label_122.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/fontname_Lucida Console.gif"))
        self.label_122.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_122, 0, 3, 1, 1)

        self.button_Impact_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_Impact_sub.setObjectName(u"button_Impact_sub")
        self.button_Impact_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_Impact_sub, 1, 1, 1, 1)

        self.label_123 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(81, 51))
        self.label_123.setMaximumSize(QSize(81, 51))
        self.label_123.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Calibri.gif"))
        self.label_123.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_123, 0, 2, 1, 1)

        self.label_124 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(81, 51))
        self.label_124.setMaximumSize(QSize(81, 51))
        self.label_124.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Impact.gif"))
        self.label_124.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_124, 0, 1, 1, 1)

        self.label_125 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(81, 51))
        self.label_125.setMaximumSize(QSize(81, 51))
        self.label_125.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Garamond.gif"))
        self.label_125.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_125, 2, 3, 1, 1)

        self.button_Garamond_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_Garamond_sub.setObjectName(u"button_Garamond_sub")
        self.button_Garamond_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_Garamond_sub, 3, 3, 1, 1)

        self.label_126 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(81, 51))
        self.label_126.setMaximumSize(QSize(81, 51))
        self.label_126.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Trebuchet MS.gif"))
        self.label_126.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_126, 4, 0, 1, 1)

        self.label_127 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(81, 51))
        self.label_127.setMaximumSize(QSize(81, 51))
        self.label_127.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/fontname_Franklin Gothic.gif"))
        self.label_127.setScaledContents(True)

        self.gridLayout_34.addWidget(self.label_127, 2, 0, 1, 1)

        self.button_FranklinGothic_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_FranklinGothic_sub.setObjectName(u"button_FranklinGothic_sub")
        self.button_FranklinGothic_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_FranklinGothic_sub, 3, 0, 1, 1)

        self.button_Trebuchet_MS_sub = QPushButton(self.scrollAreaWidgetContents_19)
        self.button_Trebuchet_MS_sub.setObjectName(u"button_Trebuchet_MS_sub")
        self.button_Trebuchet_MS_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_34.addWidget(self.button_Trebuchet_MS_sub, 5, 0, 1, 1)


        self.gridLayout_35.addLayout(self.gridLayout_34, 0, 0, 1, 1)

        self.scrollArea_19.setWidget(self.scrollAreaWidgetContents_19)

        self.gridLayout_10.addWidget(self.scrollArea_19, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_11 = QGridLayout(self.page_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea_5 = QScrollArea(self.page_7)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m"
                        "\u00f3vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, Q"
                        "ScrollBar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_5.setFrameShape(QFrame.VLine)
        self.scrollArea_5.setFrameShadow(QFrame.Plain)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 505, 1103))
        self.gridLayout_31 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_62 = QGridLayout()
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setHorizontalSpacing(17)
        self.gridLayout_62.setVerticalSpacing(16)
        self.gridLayout_62.setContentsMargins(2, 10, 4, 8)
        self.button_gold_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_gold_sub.setObjectName(u"button_gold_sub")
        self.button_gold_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_gold_sub, 6, 8, 1, 1)

        self.button_gray_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_gray_sub.setObjectName(u"button_gray_sub")
        self.button_gray_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_gray_sub, 9, 0, 1, 1)

        self.button_green_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_green_sub.setObjectName(u"button_green_sub")
        self.button_green_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_green_sub, 9, 2, 1, 1)

        self.button_indigo_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_indigo_sub.setObjectName(u"button_indigo_sub")
        self.button_indigo_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_indigo_sub, 9, 4, 1, 1)

        self.button_khaki_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_khaki_sub.setObjectName(u"button_khaki_sub")
        self.button_khaki_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_khaki_sub, 9, 6, 1, 1)

        self.button_lavender_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_lavender_sub.setObjectName(u"button_lavender_sub")
        self.button_lavender_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_lavender_sub, 9, 8, 1, 1)

        self.line_115 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_115.setObjectName(u"line_115")
        self.line_115.setFrameShape(QFrame.HLine)
        self.line_115.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_115, 22, 6, 1, 1)

        self.line_116 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_116.setObjectName(u"line_116")
        self.line_116.setFrameShape(QFrame.HLine)
        self.line_116.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_116, 7, 4, 1, 1)

        self.line_117 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_117.setObjectName(u"line_117")
        self.line_117.setFrameShape(QFrame.HLine)
        self.line_117.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_117, 7, 6, 1, 1)

        self.line_118 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_118.setObjectName(u"line_118")
        self.line_118.setFrameShape(QFrame.HLine)
        self.line_118.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_118, 7, 8, 1, 1)

        self.line_119 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_119.setObjectName(u"line_119")
        self.line_119.setFrameShape(QFrame.HLine)
        self.line_119.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_119, 7, 0, 1, 1)

        self.line_120 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_120.setObjectName(u"line_120")
        self.line_120.setFrameShape(QFrame.HLine)
        self.line_120.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_120, 7, 2, 1, 1)

        self.line_121 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_121.setObjectName(u"line_121")
        self.line_121.setFrameShape(QFrame.VLine)
        self.line_121.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_121, 0, 5, 1, 1)

        self.line_122 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_122.setObjectName(u"line_122")
        self.line_122.setFrameShape(QFrame.VLine)
        self.line_122.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_122, 0, 3, 1, 1)

        self.line_123 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_123.setObjectName(u"line_123")
        self.line_123.setFrameShape(QFrame.VLine)
        self.line_123.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_123, 0, 1, 1, 1)

        self.line_124 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_124.setObjectName(u"line_124")
        self.line_124.setFrameShape(QFrame.HLine)
        self.line_124.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_124, 22, 4, 1, 1)

        self.button_sky_blue_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_sky_blue_sub.setObjectName(u"button_sky_blue_sub")
        self.button_sky_blue_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_sky_blue_sub, 23, 0, 1, 1)

        self.button_pink_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_pink_sub.setObjectName(u"button_pink_sub")
        self.button_pink_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_pink_sub, 16, 8, 1, 1)

        self.button_teal_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_teal_sub.setObjectName(u"button_teal_sub")
        self.button_teal_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_teal_sub, 23, 2, 1, 1)

        self.button_turquoise_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_turquoise_sub.setObjectName(u"button_turquoise_sub")
        self.button_turquoise_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_turquoise_sub, 23, 4, 1, 1)

        self.button_white_subb = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_white_subb.setObjectName(u"button_white_subb")
        self.button_white_subb.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_white_subb, 23, 8, 1, 1)

        self.button_violet_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_violet_sub.setObjectName(u"button_violet_sub")
        self.button_violet_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_violet_sub, 23, 6, 1, 1)

        self.button_yellow_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_yellow_sub.setObjectName(u"button_yellow_sub")
        self.button_yellow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_yellow_sub, 26, 0, 1, 1)

        self.button_orange_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_orange_sub.setObjectName(u"button_orange_sub")
        self.button_orange_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_orange_sub, 16, 4, 1, 1)

        self.button_peach_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_peach_sub.setObjectName(u"button_peach_sub")
        self.button_peach_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_peach_sub, 16, 6, 1, 1)

        self.line_125 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_125.setObjectName(u"line_125")
        self.line_125.setFrameShape(QFrame.HLine)
        self.line_125.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_125, 17, 2, 1, 1)

        self.line_126 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_126.setObjectName(u"line_126")
        self.line_126.setFrameShape(QFrame.HLine)
        self.line_126.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_126, 14, 6, 1, 1)

        self.line_127 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_127.setObjectName(u"line_127")
        self.line_127.setFrameShape(QFrame.HLine)
        self.line_127.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_127, 17, 8, 1, 1)

        self.button_light_blue_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_light_blue_sub.setObjectName(u"button_light_blue_sub")
        self.button_light_blue_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_light_blue_sub, 13, 0, 1, 1)

        self.button_light_gray_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_light_gray_sub.setObjectName(u"button_light_gray_sub")
        self.button_light_gray_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_light_gray_sub, 13, 2, 1, 1)

        self.button_salmon_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_salmon_sub.setObjectName(u"button_salmon_sub")
        self.button_salmon_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_salmon_sub, 19, 6, 1, 1)

        self.button_royal_blue_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_royal_blue_sub.setObjectName(u"button_royal_blue_sub")
        self.button_royal_blue_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_royal_blue_sub, 19, 4, 1, 1)

        self.button_magenta_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_magenta_sub.setObjectName(u"button_magenta_sub")
        self.button_magenta_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_magenta_sub, 13, 8, 1, 1)

        self.button_purple_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_purple_sub.setObjectName(u"button_purple_sub")
        self.button_purple_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_purple_sub, 19, 0, 1, 1)

        self.button_light_pink_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_light_pink_sub.setObjectName(u"button_light_pink_sub")
        self.button_light_pink_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_light_pink_sub, 13, 4, 1, 1)

        self.button_lime_green_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_lime_green_sub.setObjectName(u"button_lime_green_sub")
        self.button_lime_green_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_lime_green_sub, 13, 6, 1, 1)

        self.button_olive_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_olive_sub.setObjectName(u"button_olive_sub")
        self.button_olive_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_olive_sub, 16, 2, 1, 1)

        self.button_red_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_red_sub.setObjectName(u"button_red_sub")
        self.button_red_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_red_sub, 19, 2, 1, 1)

        self.button_navy_blue_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_navy_blue_sub.setObjectName(u"button_navy_blue_sub")
        self.button_navy_blue_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_navy_blue_sub, 16, 0, 1, 1)

        self.button_silver_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_silver_sub.setObjectName(u"button_silver_sub")
        self.button_silver_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_silver_sub, 19, 8, 1, 1)

        self.line_128 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_128.setObjectName(u"line_128")
        self.line_128.setFrameShape(QFrame.HLine)
        self.line_128.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_128, 14, 4, 1, 1)

        self.line_129 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_129.setObjectName(u"line_129")
        self.line_129.setFrameShape(QFrame.HLine)
        self.line_129.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_129, 14, 8, 1, 1)

        self.line_131 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_131.setObjectName(u"line_131")
        self.line_131.setFrameShape(QFrame.HLine)
        self.line_131.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_131, 17, 0, 1, 1)

        self.line_132 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_132.setObjectName(u"line_132")
        self.line_132.setFrameShape(QFrame.VLine)
        self.line_132.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_132, 8, 7, 1, 1)

        self.line_133 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_133.setObjectName(u"line_133")
        self.line_133.setFrameShape(QFrame.VLine)
        self.line_133.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_133, 8, 3, 1, 1)

        self.line_134 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_134.setObjectName(u"line_134")
        self.line_134.setFrameShape(QFrame.VLine)
        self.line_134.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_134, 11, 1, 1, 1)

        self.line_136 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_136.setObjectName(u"line_136")
        self.line_136.setFrameShape(QFrame.VLine)
        self.line_136.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_136, 11, 3, 1, 1)

        self.line_137 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_137.setObjectName(u"line_137")
        self.line_137.setFrameShape(QFrame.VLine)
        self.line_137.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_137, 11, 5, 1, 1)

        self.line_138 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_138.setObjectName(u"line_138")
        self.line_138.setFrameShape(QFrame.VLine)
        self.line_138.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_138, 8, 1, 1, 1)

        self.line_140 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_140.setObjectName(u"line_140")
        self.line_140.setFrameShape(QFrame.VLine)
        self.line_140.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_140, 8, 5, 1, 1)

        self.line_141 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_141.setObjectName(u"line_141")
        self.line_141.setFrameShape(QFrame.VLine)
        self.line_141.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_141, 11, 7, 1, 1)

        self.line_143 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_143.setObjectName(u"line_143")
        self.line_143.setFrameShape(QFrame.HLine)
        self.line_143.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_143, 17, 4, 1, 1)

        self.line_144 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_144.setObjectName(u"line_144")
        self.line_144.setFrameShape(QFrame.HLine)
        self.line_144.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_144, 22, 0, 1, 1)

        self.line_145 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_145.setObjectName(u"line_145")
        self.line_145.setFrameShape(QFrame.HLine)
        self.line_145.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_145, 10, 2, 1, 1)

        self.line_146 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_146.setObjectName(u"line_146")
        self.line_146.setFrameShape(QFrame.HLine)
        self.line_146.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_146, 10, 4, 1, 1)

        self.line_147 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_147.setObjectName(u"line_147")
        self.line_147.setFrameShape(QFrame.HLine)
        self.line_147.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_147, 10, 0, 1, 1)

        self.line_148 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_148.setObjectName(u"line_148")
        self.line_148.setFrameShape(QFrame.HLine)
        self.line_148.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_148, 10, 6, 1, 1)

        self.line_149 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_149.setObjectName(u"line_149")
        self.line_149.setFrameShape(QFrame.HLine)
        self.line_149.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_149, 10, 8, 1, 1)

        self.line_150 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_150.setObjectName(u"line_150")
        self.line_150.setFrameShape(QFrame.HLine)
        self.line_150.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_150, 22, 8, 1, 1)

        self.line_151 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_151.setObjectName(u"line_151")
        self.line_151.setFrameShape(QFrame.HLine)
        self.line_151.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_151, 14, 2, 1, 1)

        self.line_152 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_152.setObjectName(u"line_152")
        self.line_152.setFrameShape(QFrame.HLine)
        self.line_152.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_152, 14, 0, 1, 1)

        self.line_153 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_153.setObjectName(u"line_153")
        self.line_153.setFrameShape(QFrame.HLine)
        self.line_153.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_153, 17, 6, 1, 1)

        self.line_154 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_154.setObjectName(u"line_154")
        self.line_154.setFrameShape(QFrame.HLine)
        self.line_154.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_154, 24, 0, 1, 1)

        self.line_155 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_155.setObjectName(u"line_155")
        self.line_155.setFrameShape(QFrame.HLine)
        self.line_155.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_155, 27, 0, 1, 1)

        self.line_8 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_8, 20, 0, 1, 1)

        self.line_156 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_156.setObjectName(u"line_156")
        self.line_156.setFrameShape(QFrame.HLine)
        self.line_156.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_156, 20, 2, 1, 1)

        self.line_157 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_157.setObjectName(u"line_157")
        self.line_157.setFrameShape(QFrame.HLine)
        self.line_157.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_157, 20, 4, 1, 1)

        self.line_158 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_158.setObjectName(u"line_158")
        self.line_158.setFrameShape(QFrame.HLine)
        self.line_158.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_158, 20, 6, 1, 1)

        self.line_159 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_159.setObjectName(u"line_159")
        self.line_159.setFrameShape(QFrame.HLine)
        self.line_159.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_159, 20, 8, 1, 1)

        self.line_160 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_160.setObjectName(u"line_160")
        self.line_160.setFrameShape(QFrame.HLine)
        self.line_160.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_160, 22, 2, 1, 1)

        self.line_161 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_161.setObjectName(u"line_161")
        self.line_161.setFrameShape(QFrame.HLine)
        self.line_161.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_161, 4, 8, 1, 1)

        self.line_162 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_162.setObjectName(u"line_162")
        self.line_162.setFrameShape(QFrame.HLine)
        self.line_162.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_162, 4, 6, 1, 1)

        self.line_163 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_163.setObjectName(u"line_163")
        self.line_163.setFrameShape(QFrame.HLine)
        self.line_163.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_163, 4, 4, 1, 1)

        self.line_164 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_164.setObjectName(u"line_164")
        self.line_164.setFrameShape(QFrame.HLine)
        self.line_164.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_164, 4, 2, 1, 1)

        self.line_165 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_165.setObjectName(u"line_165")
        self.line_165.setFrameShape(QFrame.VLine)
        self.line_165.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_165, 5, 7, 1, 1)

        self.line_166 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_166.setObjectName(u"line_166")
        self.line_166.setFrameShape(QFrame.VLine)
        self.line_166.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_166, 5, 5, 1, 1)

        self.line_167 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_167.setObjectName(u"line_167")
        self.line_167.setFrameShape(QFrame.VLine)
        self.line_167.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_167, 5, 3, 1, 1)

        self.line_168 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_168.setObjectName(u"line_168")
        self.line_168.setFrameShape(QFrame.VLine)
        self.line_168.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_168, 5, 1, 1, 1)

        self.line_169 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_169.setObjectName(u"line_169")
        self.line_169.setFrameShape(QFrame.HLine)
        self.line_169.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_169, 4, 0, 1, 1)

        self.line_9 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_62.addWidget(self.line_9, 0, 7, 1, 1)

        self.label_106 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(50, 50))
        self.label_106.setMaximumSize(QSize(50, 50))
        self.label_106.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_aquaA.gif"))
        self.label_106.setScaledContents(True)
        self.label_106.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_62.addWidget(self.label_106, 0, 0, 1, 1)

        self.label_292 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setMinimumSize(QSize(50, 50))
        self.label_292.setMaximumSize(QSize(50, 50))
        self.label_292.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_dark blue.gif"))

        self.gridLayout_62.addWidget(self.label_292, 5, 0, 1, 1)

        self.label_293 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setMinimumSize(QSize(50, 50))
        self.label_293.setMaximumSize(QSize(50, 50))
        self.label_293.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_gray.gif"))
        self.label_293.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_293, 8, 0, 1, 1)

        self.label_309 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_309.setObjectName(u"label_309")
        self.label_309.setMinimumSize(QSize(50, 50))
        self.label_309.setMaximumSize(QSize(50, 50))
        self.label_309.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_sky blue.png"))
        self.label_309.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_309, 21, 0, 1, 1)

        self.label_294 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setMinimumSize(QSize(50, 50))
        self.label_294.setMaximumSize(QSize(50, 50))
        self.label_294.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_navy blue.png"))
        self.label_294.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_294, 15, 0, 1, 1)

        self.label_295 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setMinimumSize(QSize(50, 50))
        self.label_295.setMaximumSize(QSize(50, 50))
        self.label_295.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_purple.gif"))
        self.label_295.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_295, 18, 0, 1, 1)

        self.label_296 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setMinimumSize(QSize(50, 50))
        self.label_296.setMaximumSize(QSize(50, 50))
        self.label_296.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_light blue.gif"))
        self.label_296.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_296, 11, 0, 1, 1)

        self.label_310 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_310.setObjectName(u"label_310")
        self.label_310.setMinimumSize(QSize(50, 50))
        self.label_310.setMaximumSize(QSize(50, 50))
        self.label_310.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_yellow.gif"))
        self.label_310.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_310, 25, 0, 1, 1)

        self.label_347 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_347.setObjectName(u"label_347")
        self.label_347.setMinimumSize(QSize(50, 50))
        self.label_347.setMaximumSize(QSize(50, 50))
        self.label_347.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_turquoise.gif"))
        self.label_347.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_347, 21, 4, 1, 1)

        self.label_356 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_356.setObjectName(u"label_356")
        self.label_356.setMinimumSize(QSize(50, 50))
        self.label_356.setMaximumSize(QSize(50, 50))
        self.label_356.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_white.gif"))
        self.label_356.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_356, 21, 8, 1, 1)

        self.label_358 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_358.setObjectName(u"label_358")
        self.label_358.setMinimumSize(QSize(50, 50))
        self.label_358.setMaximumSize(QSize(50, 50))
        self.label_358.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_violet.gif"))
        self.label_358.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_358, 21, 6, 1, 1)

        self.button_aqua_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_aqua_sub.setObjectName(u"button_aqua_sub")
        self.button_aqua_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_aqua_sub, 1, 0, 1, 1)

        self.button_blue_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_blue_sub.setObjectName(u"button_blue_sub")
        self.button_blue_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_blue_sub, 1, 2, 1, 1)

        self.button_brown_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_brown_sub.setObjectName(u"button_brown_sub")
        self.button_brown_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_brown_sub, 1, 4, 1, 1)

        self.button_coral_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_coral_sub.setObjectName(u"button_coral_sub")
        self.button_coral_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_coral_sub, 1, 6, 1, 1)

        self.button_cyan_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_cyan_sub.setObjectName(u"button_cyan_sub")
        self.button_cyan_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_cyan_sub, 1, 8, 1, 1)

        self.button_dark_green_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_dark_green_sub.setObjectName(u"button_dark_green_sub")
        self.button_dark_green_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_dark_green_sub, 6, 2, 1, 1)

        self.button_dark_blue_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_dark_blue_sub.setObjectName(u"button_dark_blue_sub")
        self.button_dark_blue_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_dark_blue_sub, 6, 0, 1, 1)

        self.button_dark_red_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_dark_red_sub.setObjectName(u"button_dark_red_sub")
        self.button_dark_red_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_dark_red_sub, 6, 4, 1, 1)

        self.button_forest_green_sub = QPushButton(self.scrollAreaWidgetContents_5)
        self.button_forest_green_sub.setObjectName(u"button_forest_green_sub")
        self.button_forest_green_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_62.addWidget(self.button_forest_green_sub, 6, 6, 1, 1)

        self.label_311 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_311.setObjectName(u"label_311")
        self.label_311.setMinimumSize(QSize(50, 50))
        self.label_311.setMaximumSize(QSize(50, 50))
        self.label_311.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_brown.gif"))
        self.label_311.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_311, 0, 4, 1, 1)

        self.label_312 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_312.setObjectName(u"label_312")
        self.label_312.setMinimumSize(QSize(50, 50))
        self.label_312.setMaximumSize(QSize(50, 50))
        self.label_312.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_cyan.gif"))
        self.label_312.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_312, 0, 8, 1, 1)

        self.label_313 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_313.setObjectName(u"label_313")
        self.label_313.setMinimumSize(QSize(50, 50))
        self.label_313.setMaximumSize(QSize(50, 50))
        self.label_313.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_dark green.png"))
        self.label_313.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_313, 5, 2, 1, 1)

        self.label_314 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setMinimumSize(QSize(50, 50))
        self.label_314.setMaximumSize(QSize(50, 50))
        self.label_314.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_coral.gif"))
        self.label_314.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_314, 0, 6, 1, 1)

        self.label_321 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_321.setObjectName(u"label_321")
        self.label_321.setMinimumSize(QSize(50, 50))
        self.label_321.setMaximumSize(QSize(50, 50))
        self.label_321.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_forest green.gif"))
        self.label_321.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_321, 5, 6, 1, 1)

        self.label_322 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_322.setObjectName(u"label_322")
        self.label_322.setMinimumSize(QSize(50, 50))
        self.label_322.setMaximumSize(QSize(50, 50))
        self.label_322.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_dark red.gif"))
        self.label_322.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_322, 5, 4, 1, 1)

        self.label_328 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_328.setObjectName(u"label_328")
        self.label_328.setMinimumSize(QSize(50, 50))
        self.label_328.setMaximumSize(QSize(50, 50))
        self.label_328.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_gold.gif"))
        self.label_328.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_328, 5, 8, 1, 1)

        self.label_332 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_332.setObjectName(u"label_332")
        self.label_332.setMinimumSize(QSize(50, 50))
        self.label_332.setMaximumSize(QSize(50, 50))
        self.label_332.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_green.gif"))
        self.label_332.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_332, 8, 2, 1, 1)

        self.label_348 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_348.setObjectName(u"label_348")
        self.label_348.setMinimumSize(QSize(50, 50))
        self.label_348.setMaximumSize(QSize(50, 50))
        self.label_348.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_indigo.gif"))
        self.label_348.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_348, 8, 4, 1, 1)

        self.label_349 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_349.setObjectName(u"label_349")
        self.label_349.setMinimumSize(QSize(50, 50))
        self.label_349.setMaximumSize(QSize(50, 50))
        self.label_349.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_khaki.gif"))
        self.label_349.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_349, 8, 6, 1, 1)

        self.label_350 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_350.setObjectName(u"label_350")
        self.label_350.setMinimumSize(QSize(50, 50))
        self.label_350.setMaximumSize(QSize(50, 50))
        self.label_350.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_light pink.gif"))
        self.label_350.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_350, 11, 4, 1, 1)

        self.label_351 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_351.setObjectName(u"label_351")
        self.label_351.setMinimumSize(QSize(50, 50))
        self.label_351.setMaximumSize(QSize(50, 50))
        self.label_351.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_lavender.gif"))
        self.label_351.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_351, 8, 8, 1, 1)

        self.label_352 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_352.setObjectName(u"label_352")
        self.label_352.setMinimumSize(QSize(50, 50))
        self.label_352.setMaximumSize(QSize(50, 50))
        self.label_352.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_light gray.gif"))
        self.label_352.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_352, 11, 2, 1, 1)

        self.label_353 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_353.setObjectName(u"label_353")
        self.label_353.setMinimumSize(QSize(50, 50))
        self.label_353.setMaximumSize(QSize(50, 50))
        self.label_353.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_magenta.gif"))
        self.label_353.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_353, 11, 8, 1, 1)

        self.label_354 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_354.setObjectName(u"label_354")
        self.label_354.setMinimumSize(QSize(50, 50))
        self.label_354.setMaximumSize(QSize(50, 50))
        self.label_354.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_lime green.gif"))
        self.label_354.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_354, 11, 6, 1, 1)

        self.label_359 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_359.setObjectName(u"label_359")
        self.label_359.setMinimumSize(QSize(50, 50))
        self.label_359.setMaximumSize(QSize(50, 50))
        self.label_359.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_olive.gif"))
        self.label_359.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_359, 15, 2, 1, 1)

        self.label_360 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_360.setObjectName(u"label_360")
        self.label_360.setMinimumSize(QSize(50, 50))
        self.label_360.setMaximumSize(QSize(50, 50))
        self.label_360.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_orange.gif"))
        self.label_360.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_360, 15, 4, 1, 1)

        self.label_361 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_361.setObjectName(u"label_361")
        self.label_361.setMinimumSize(QSize(50, 50))
        self.label_361.setMaximumSize(QSize(50, 50))
        self.label_361.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_silver.gif"))
        self.label_361.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_361, 18, 8, 1, 1)

        self.label_362 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_362.setObjectName(u"label_362")
        self.label_362.setMinimumSize(QSize(50, 50))
        self.label_362.setMaximumSize(QSize(50, 50))
        self.label_362.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_pink.gif"))
        self.label_362.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_362, 15, 8, 1, 1)

        self.label_363 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_363.setObjectName(u"label_363")
        self.label_363.setMinimumSize(QSize(50, 50))
        self.label_363.setMaximumSize(QSize(50, 50))
        self.label_363.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_dark red.gif"))
        self.label_363.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_363, 18, 2, 1, 1)

        self.label_364 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_364.setObjectName(u"label_364")
        self.label_364.setMinimumSize(QSize(50, 50))
        self.label_364.setMaximumSize(QSize(50, 50))
        self.label_364.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_peach.gif"))
        self.label_364.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_364, 15, 6, 1, 1)

        self.label_365 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_365.setObjectName(u"label_365")
        self.label_365.setMinimumSize(QSize(50, 50))
        self.label_365.setMaximumSize(QSize(50, 50))
        self.label_365.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_teal.gif"))
        self.label_365.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_365, 21, 2, 1, 1)

        self.label_366 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_366.setObjectName(u"label_366")
        self.label_366.setMinimumSize(QSize(50, 50))
        self.label_366.setMaximumSize(QSize(50, 50))
        self.label_366.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_salmon.gif"))
        self.label_366.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_366, 18, 6, 1, 1)

        self.label_367 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_367.setObjectName(u"label_367")
        self.label_367.setMinimumSize(QSize(50, 50))
        self.label_367.setMaximumSize(QSize(50, 50))
        self.label_367.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_royal blue.gif"))
        self.label_367.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_367, 18, 4, 1, 1)

        self.label_315 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setMinimumSize(QSize(50, 50))
        self.label_315.setMaximumSize(QSize(50, 50))
        self.label_315.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_blue.gif"))
        self.label_315.setScaledContents(True)

        self.gridLayout_62.addWidget(self.label_315, 0, 2, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_62, 0, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_11.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_12 = QGridLayout(self.page_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.spin_fontsize_sub = QSpinBox(self.page_8)
        self.spin_fontsize_sub.setObjectName(u"spin_fontsize_sub")
        self.spin_fontsize_sub.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.spin_fontsize_sub.setValue(20)

        self.gridLayout_12.addWidget(self.spin_fontsize_sub, 0, 1, 1, 1)

        self.label_103 = QLabel(self.page_8)
        self.label_103.setObjectName(u"label_103")
        font1 = QFont()
        self.label_103.setFont(font1)

        self.gridLayout_12.addWidget(self.label_103, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 651, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_12.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_13 = QGridLayout(self.page_9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.scrollArea_7 = QScrollArea(self.page_9)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m"
                        "\u00f3vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, Q"
                        "ScrollBar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_7.setFrameShape(QFrame.VLine)
        self.scrollArea_7.setFrameShadow(QFrame.Plain)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 500, 607))
        self.gridLayout_30 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setHorizontalSpacing(36)
        self.gridLayout_29.setVerticalSpacing(128)
        self.button_animation_Gradual_Blink_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_Gradual_Blink_sub.setObjectName(u"button_animation_Gradual_Blink_sub")
        self.button_animation_Gradual_Blink_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_Gradual_Blink_sub, 1, 2, 1, 1)

        self.button_animation_AppearDisappear_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_AppearDisappear_sub.setObjectName(u"button_animation_AppearDisappear_sub")
        self.button_animation_AppearDisappear_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_AppearDisappear_sub, 1, 1, 1, 1)

        self.button_animation_StrobeEffect_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_StrobeEffect_sub.setObjectName(u"button_animation_StrobeEffect_sub")
        self.button_animation_StrobeEffect_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_StrobeEffect_sub, 2, 0, 1, 1)

        self.button_animation_Soft_Fade_In_Out_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_Soft_Fade_In_Out_sub.setObjectName(u"button_animation_Soft_Fade_In_Out_sub")
        self.button_animation_Soft_Fade_In_Out_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_Soft_Fade_In_Out_sub, 1, 3, 1, 1)

        self.button_animation_FadeInandHold_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_FadeInandHold_sub.setObjectName(u"button_animation_FadeInandHold_sub")
        self.button_animation_FadeInandHold_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_FadeInandHold_sub, 2, 1, 1, 1)

        self.button_animation_FadeOut_and_Hold_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_FadeOut_and_Hold_sub.setObjectName(u"button_animation_FadeOut_and_Hold_sub")
        self.button_animation_FadeOut_and_Hold_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_FadeOut_and_Hold_sub, 2, 3, 1, 1)

        self.button_animation_PulseOut_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_PulseOut_sub.setObjectName(u"button_animation_PulseOut_sub")
        self.button_animation_PulseOut_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_PulseOut_sub, 2, 2, 1, 1)

        self.button_animation_Pulse_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_Pulse_sub.setObjectName(u"button_animation_Pulse_sub")
        self.button_animation_Pulse_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_Pulse_sub, 0, 1, 1, 1)

        self.button_animation_SlowFadeIn_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_SlowFadeIn_sub.setObjectName(u"button_animation_SlowFadeIn_sub")
        self.button_animation_SlowFadeIn_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_SlowFadeIn_sub, 0, 2, 1, 1)

        self.button_animation_FastBlink_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_FastBlink_sub.setObjectName(u"button_animation_FastBlink_sub")
        self.button_animation_FastBlink_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_FastBlink_sub, 1, 0, 1, 1)

        self.button_animation_FadeIn_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_FadeIn_sub.setObjectName(u"button_animation_FadeIn_sub")
        self.button_animation_FadeIn_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_FadeIn_sub, 0, 0, 1, 1)

        self.button_animation_SlowFadeOut_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_SlowFadeOut_sub.setObjectName(u"button_animation_SlowFadeOut_sub")
        self.button_animation_SlowFadeOut_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_SlowFadeOut_sub, 0, 3, 1, 1)

        self.button_animation_BlinkingText_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_BlinkingText_sub.setObjectName(u"button_animation_BlinkingText_sub")
        self.button_animation_BlinkingText_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_BlinkingText_sub, 3, 0, 1, 1)

        self.button_animation_QuickFadeOut_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_QuickFadeOut_sub.setObjectName(u"button_animation_QuickFadeOut_sub")
        self.button_animation_QuickFadeOut_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_QuickFadeOut_sub, 3, 1, 1, 1)

        self.button_animation_QuickFadeIn_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_QuickFadeIn_sub.setObjectName(u"button_animation_QuickFadeIn_sub")
        self.button_animation_QuickFadeIn_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_QuickFadeIn_sub, 3, 2, 1, 1)

        self.button_animation_None_sub = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_animation_None_sub.setObjectName(u"button_animation_None_sub")
        self.button_animation_None_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_29.addWidget(self.button_animation_None_sub, 3, 3, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_29, 0, 0, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_13.addWidget(self.scrollArea_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_14 = QGridLayout(self.page_10)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.scrollArea_8 = QScrollArea(self.page_10)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m"
                        "\u00f3vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, Q"
                        "ScrollBar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_8.setFrameShape(QFrame.VLine)
        self.scrollArea_8.setFrameShadow(QFrame.Plain)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 505, 592))
        self.gridLayout_28 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setHorizontalSpacing(38)
        self.gridLayout_27.setVerticalSpacing(103)
        self.button_GlowEffect_Shadow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_GlowEffect_Shadow_sub.setObjectName(u"button_GlowEffect_Shadow_sub")
        self.button_GlowEffect_Shadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_GlowEffect_Shadow_sub, 0, 1, 1, 1)

        self.button_effects_BoldShadow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_BoldShadow_sub.setObjectName(u"button_effects_BoldShadow_sub")
        self.button_effects_BoldShadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_BoldShadow_sub, 1, 3, 1, 1)

        self.button_effects_DropShadow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_DropShadow_sub.setObjectName(u"button_effects_DropShadow_sub")
        self.button_effects_DropShadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_DropShadow_sub, 1, 2, 1, 1)

        self.button_effects_DottedOutline_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_DottedOutline_sub.setObjectName(u"button_effects_DottedOutline_sub")
        self.button_effects_DottedOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_DottedOutline_sub, 0, 3, 1, 1)

        self.button_effects_NeonGlow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_NeonGlow_sub.setObjectName(u"button_effects_NeonGlow_sub")
        self.button_effects_NeonGlow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_NeonGlow_sub, 0, 2, 1, 1)

        self.button_effects_InnerGlow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_InnerGlow_sub.setObjectName(u"button_effects_InnerGlow_sub")
        self.button_effects_InnerGlow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_InnerGlow_sub, 1, 0, 1, 1)

        self.button_effects_HardGlow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_HardGlow_sub.setObjectName(u"button_effects_HardGlow_sub")
        self.button_effects_HardGlow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_HardGlow_sub, 2, 1, 1, 1)

        self.button_effects_SoftShadow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_SoftShadow_sub.setObjectName(u"button_effects_SoftShadow_sub")
        self.button_effects_SoftShadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_SoftShadow_sub, 2, 2, 1, 1)

        self.button_effects_WavyOutline_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_WavyOutline_sub.setObjectName(u"button_effects_WavyOutline_sub")
        self.button_effects_WavyOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_WavyOutline_sub, 1, 1, 1, 1)

        self.button_effects_BlurredShadow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_BlurredShadow_sub.setObjectName(u"button_effects_BlurredShadow_sub")
        self.button_effects_BlurredShadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_BlurredShadow_sub, 2, 0, 1, 1)

        self.button_effects_Emboss_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_Emboss_sub.setObjectName(u"button_effects_Emboss_sub")
        self.button_effects_Emboss_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_Emboss_sub, 3, 1, 1, 1)

        self.button_effects_Outline_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_Outline_sub.setObjectName(u"button_effects_Outline_sub")
        self.button_effects_Outline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_Outline_sub, 2, 3, 1, 1)

        self.button_effects_DoubleOutline_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_DoubleOutline_sub.setObjectName(u"button_effects_DoubleOutline_sub")
        self.button_effects_DoubleOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_DoubleOutline_sub, 3, 3, 1, 1)

        self.button_effects_TransparentOutline_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_TransparentOutline_sub.setObjectName(u"button_effects_TransparentOutline_sub")
        self.button_effects_TransparentOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_TransparentOutline_sub, 3, 2, 1, 1)

        self.button_effects_SoftGlow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_SoftGlow_sub.setObjectName(u"button_effects_SoftGlow_sub")
        self.button_effects_SoftGlow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_SoftGlow_sub, 3, 0, 1, 1)

        self.button_effects_Shadow_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_Shadow_sub.setObjectName(u"button_effects_Shadow_sub")
        self.button_effects_Shadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_Shadow_sub, 0, 0, 1, 1)

        self.button_effects_ThickOutline_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_ThickOutline_sub.setObjectName(u"button_effects_ThickOutline_sub")
        self.button_effects_ThickOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_27.addWidget(self.button_effects_ThickOutline_sub, 4, 0, 1, 1)

        self.button_effects_None_sub = QPushButton(self.scrollAreaWidgetContents_8)
        self.button_effects_None_sub.setObjectName(u"button_effects_None_sub")
        self.button_effects_None_sub.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    background-color: #111111;\n"
"    border: 1px solid #434C5E;\n"
"    color: #D8DEE9;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")

        self.gridLayout_27.addWidget(self.button_effects_None_sub, 4, 1, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_27, 0, 0, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.gridLayout_14.addWidget(self.scrollArea_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.gridLayout_15 = QGridLayout(self.page_11)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.button_SubReference = QSpinBox(self.page_11)
        self.button_SubReference.setObjectName(u"button_SubReference")
        self.button_SubReference.setEnabled(True)
        self.button_SubReference.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.button_SubReference.setValue(15)

        self.gridLayout_15.addWidget(self.button_SubReference, 0, 1, 1, 1)

        self.label_282 = QLabel(self.page_11)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setFont(font1)

        self.gridLayout_15.addWidget(self.label_282, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 633, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_15.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.gridLayout_16 = QGridLayout(self.page_12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.scrollArea_11 = QScrollArea(self.page_12)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m"
                        "\u00f3vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, Q"
                        "ScrollBar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_11.setFrameShape(QFrame.VLine)
        self.scrollArea_11.setFrameShadow(QFrame.Plain)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 510, 591))
        self.gridLayout_39 = QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setHorizontalSpacing(45)
        self.gridLayout_38.setVerticalSpacing(65)
        self.gridLayout_38.setContentsMargins(-1, -1, -1, 0)
        self.label_397 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_397.setObjectName(u"label_397")
        self.label_397.setMinimumSize(QSize(50, 50))
        self.label_397.setMaximumSize(QSize(50, 50))
        self.label_397.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/10.gif"))
        self.label_397.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_397, 2, 4, 1, 1)

        self.button_9_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_9_Thread.setObjectName(u"button_9_Thread")
        self.button_9_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_9_Thread, 3, 3, 1, 1)

        self.label_399 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_399.setObjectName(u"label_399")
        self.label_399.setMinimumSize(QSize(50, 50))
        self.label_399.setMaximumSize(QSize(50, 50))
        self.label_399.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/11.gif"))
        self.label_399.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_399, 4, 0, 1, 1)

        self.button_10_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_10_Thread.setObjectName(u"button_10_Thread")
        self.button_10_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_10_Thread, 3, 4, 1, 1)

        self.button_11_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_11_Thread.setObjectName(u"button_11_Thread")
        self.button_11_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_11_Thread, 5, 0, 1, 1)

        self.label_389 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_389.setObjectName(u"label_389")
        self.label_389.setMinimumSize(QSize(50, 50))
        self.label_389.setMaximumSize(QSize(50, 50))
        self.label_389.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/1.gif"))
        self.label_389.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_389, 0, 0, 1, 1)

        self.label_390 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_390.setObjectName(u"label_390")
        self.label_390.setMinimumSize(QSize(50, 50))
        self.label_390.setMaximumSize(QSize(50, 50))
        self.label_390.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/2.gif"))
        self.label_390.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_390, 0, 1, 1, 1)

        self.button_2_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_2_Thread.setObjectName(u"button_2_Thread")
        self.button_2_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_2_Thread, 1, 1, 1, 1)

        self.button_1_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_1_Thread.setObjectName(u"button_1_Thread")
        self.button_1_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_1_Thread, 1, 0, 1, 1)

        self.button_4_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_4_Thread.setObjectName(u"button_4_Thread")
        self.button_4_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_4_Thread, 1, 3, 1, 1)

        self.label_400 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_400.setObjectName(u"label_400")
        self.label_400.setMinimumSize(QSize(50, 50))
        self.label_400.setMaximumSize(QSize(50, 50))
        self.label_400.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/3c.gif"))
        self.label_400.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_400, 0, 2, 1, 1)

        self.label_392 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_392.setObjectName(u"label_392")
        self.label_392.setMinimumSize(QSize(50, 50))
        self.label_392.setMaximumSize(QSize(50, 50))
        self.label_392.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/4.gif"))
        self.label_392.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_392, 0, 3, 1, 1)

        self.button_5_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_5_Thread.setObjectName(u"button_5_Thread")
        self.button_5_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_5_Thread, 1, 4, 1, 1)

        self.button_3_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_3_Thread.setObjectName(u"button_3_Thread")
        self.button_3_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_3_Thread, 1, 2, 1, 1)

        self.label_398 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_398.setObjectName(u"label_398")
        self.label_398.setMinimumSize(QSize(50, 50))
        self.label_398.setMaximumSize(QSize(50, 50))
        self.label_398.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/6.gif"))
        self.label_398.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_398, 2, 0, 1, 1)

        self.label_393 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_393.setObjectName(u"label_393")
        self.label_393.setMinimumSize(QSize(50, 50))
        self.label_393.setMaximumSize(QSize(50, 50))
        self.label_393.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/5.gif"))
        self.label_393.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_393, 0, 4, 1, 1)

        self.button_7_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_7_Thread.setObjectName(u"button_7_Thread")
        self.button_7_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_7_Thread, 3, 1, 1, 1)

        self.label_394 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_394.setObjectName(u"label_394")
        self.label_394.setMinimumSize(QSize(50, 50))
        self.label_394.setMaximumSize(QSize(50, 50))
        self.label_394.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/7.gif"))
        self.label_394.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_394, 2, 1, 1, 1)

        self.label_395 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_395.setObjectName(u"label_395")
        self.label_395.setMinimumSize(QSize(50, 50))
        self.label_395.setMaximumSize(QSize(50, 50))
        self.label_395.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/8.gif"))
        self.label_395.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_395, 2, 2, 1, 1)

        self.button_8_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_8_Thread.setObjectName(u"button_8_Thread")
        self.button_8_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_8_Thread, 3, 2, 1, 1)

        self.button_6_Thread = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_6_Thread.setObjectName(u"button_6_Thread")
        self.button_6_Thread.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_38.addWidget(self.button_6_Thread, 3, 0, 1, 1)

        self.label_396 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_396.setObjectName(u"label_396")
        self.label_396.setMinimumSize(QSize(50, 50))
        self.label_396.setMaximumSize(QSize(50, 50))
        self.label_396.setPixmap(QPixmap(u":/threadsimg/icons/gifs/threadsimg/9.gif"))
        self.label_396.setScaledContents(True)

        self.gridLayout_38.addWidget(self.label_396, 2, 3, 1, 1)


        self.gridLayout_39.addLayout(self.gridLayout_38, 0, 0, 1, 1)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.gridLayout_16.addWidget(self.scrollArea_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.gridLayout_17 = QGridLayout(self.page_13)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.scrollArea_17 = QScrollArea(self.page_13)
        self.scrollArea_17.setObjectName(u"scrollArea_17")
        self.scrollArea_17.setMinimumSize(QSize(0, 121))
        self.scrollArea_17.setMaximumSize(QSize(16777215, 121))
        self.scrollArea_17.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 2px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m\u00f3"
                        "vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, QScroll"
                        "Bar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_17.setFrameShape(QFrame.VLine)
        self.scrollArea_17.setFrameShadow(QFrame.Plain)
        self.scrollArea_17.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 516, 115))
        self.gridLayout_91 = QGridLayout(self.scrollAreaWidgetContents_17)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.gridLayout_93 = QGridLayout()
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.gridLayout_93.setVerticalSpacing(6)
        self.label_391 = QLabel(self.scrollAreaWidgetContents_17)
        self.label_391.setObjectName(u"label_391")
        self.label_391.setMinimumSize(QSize(73, 50))
        self.label_391.setMaximumSize(QSize(73, 50))
        self.label_391.setPixmap(QPixmap(u":/Whisper/icons/gifs/Whisper/tiny.gif"))
        self.label_391.setScaledContents(True)

        self.gridLayout_93.addWidget(self.label_391, 0, 0, 1, 1)

        self.button_whisper_tiny = QPushButton(self.scrollAreaWidgetContents_17)
        self.button_whisper_tiny.setObjectName(u"button_whisper_tiny")
        self.button_whisper_tiny.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_93.addWidget(self.button_whisper_tiny, 1, 0, 1, 1)

        self.button_whisper_medium = QPushButton(self.scrollAreaWidgetContents_17)
        self.button_whisper_medium.setObjectName(u"button_whisper_medium")
        self.button_whisper_medium.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_93.addWidget(self.button_whisper_medium, 1, 3, 1, 1)

        self.label_402 = QLabel(self.scrollAreaWidgetContents_17)
        self.label_402.setObjectName(u"label_402")
        self.label_402.setMinimumSize(QSize(81, 50))
        self.label_402.setMaximumSize(QSize(81, 50))
        self.label_402.setPixmap(QPixmap(u":/Whisper/icons/gifs/Whisper/small.gif"))
        self.label_402.setScaledContents(True)

        self.gridLayout_93.addWidget(self.label_402, 0, 2, 1, 1)

        self.button_whisper_base = QPushButton(self.scrollAreaWidgetContents_17)
        self.button_whisper_base.setObjectName(u"button_whisper_base")
        self.button_whisper_base.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_93.addWidget(self.button_whisper_base, 1, 1, 1, 1)

        self.button_whisper_small = QPushButton(self.scrollAreaWidgetContents_17)
        self.button_whisper_small.setObjectName(u"button_whisper_small")
        self.button_whisper_small.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_93.addWidget(self.button_whisper_small, 1, 2, 1, 1)

        self.label_401 = QLabel(self.scrollAreaWidgetContents_17)
        self.label_401.setObjectName(u"label_401")
        self.label_401.setMinimumSize(QSize(81, 50))
        self.label_401.setMaximumSize(QSize(81, 50))
        self.label_401.setPixmap(QPixmap(u":/Whisper/icons/gifs/Whisper/base.gif"))
        self.label_401.setScaledContents(True)

        self.gridLayout_93.addWidget(self.label_401, 0, 1, 1, 1)

        self.label_403 = QLabel(self.scrollAreaWidgetContents_17)
        self.label_403.setObjectName(u"label_403")
        self.label_403.setMinimumSize(QSize(81, 50))
        self.label_403.setMaximumSize(QSize(81, 50))
        self.label_403.setPixmap(QPixmap(u":/Whisper/icons/gifs/Whisper/medium.gif"))
        self.label_403.setScaledContents(True)

        self.gridLayout_93.addWidget(self.label_403, 0, 3, 1, 1)

        self.label_404 = QLabel(self.scrollAreaWidgetContents_17)
        self.label_404.setObjectName(u"label_404")
        self.label_404.setMinimumSize(QSize(81, 50))
        self.label_404.setMaximumSize(QSize(81, 50))
        self.label_404.setPixmap(QPixmap(u":/Whisper/icons/gifs/Whisper/large.gif"))
        self.label_404.setScaledContents(True)

        self.gridLayout_93.addWidget(self.label_404, 0, 4, 1, 1)

        self.button_whisper_large = QPushButton(self.scrollAreaWidgetContents_17)
        self.button_whisper_large.setObjectName(u"button_whisper_large")
        self.button_whisper_large.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #ADD8E6, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de azul claro para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #87CEEB, stop:1 #000000);  /* Gradiente alterado no hover (azul claro mais escuro) */\n"
"}")

        self.gridLayout_93.addWidget(self.button_whisper_large, 1, 4, 1, 1)


        self.gridLayout_91.addLayout(self.gridLayout_93, 0, 0, 1, 1)

        self.scrollArea_17.setWidget(self.scrollAreaWidgetContents_17)

        self.gridLayout_17.addWidget(self.scrollArea_17, 0, 0, 1, 1)

        self.textEdit_4 = QTextEdit(self.page_13)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy3)
        self.textEdit_4.setMinimumSize(QSize(0, 535))
        self.textEdit_4.setMaximumSize(QSize(16777215, 535))
        self.textEdit_4.setStyleSheet(u"QTextEdit {\n"
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
        self.textEdit_4.setReadOnly(True)

        self.gridLayout_17.addWidget(self.textEdit_4, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.gridLayout_18 = QGridLayout(self.page_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.scrollArea_13 = QScrollArea(self.page_14)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setMinimumSize(QSize(0, 190))
        self.scrollArea_13.setMaximumSize(QSize(16777215, 190))
        self.scrollArea_13.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 2px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m\u00f3"
                        "vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, QScroll"
                        "Bar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_13.setFrameShape(QFrame.VLine)
        self.scrollArea_13.setFrameShadow(QFrame.Plain)
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 639, 177))
        self.gridLayout_94 = QGridLayout(self.scrollAreaWidgetContents_13)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.gridLayout_92 = QGridLayout()
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.label_409 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_409.setObjectName(u"label_409")
        self.label_409.setMinimumSize(QSize(119, 119))
        self.label_409.setMaximumSize(QSize(119, 119))
        self.label_409.setPixmap(QPixmap(u":/cutsimg/icons/gifs/cutsimg/260s.gif"))
        self.label_409.setScaledContents(True)

        self.gridLayout_92.addWidget(self.label_409, 0, 4, 1, 1)

        self.label_408 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_408.setObjectName(u"label_408")
        self.label_408.setMinimumSize(QSize(119, 119))
        self.label_408.setMaximumSize(QSize(119, 119))
        self.label_408.setPixmap(QPixmap(u":/cutsimg/icons/gifs/cutsimg/160s.gif"))
        self.label_408.setScaledContents(True)

        self.gridLayout_92.addWidget(self.label_408, 0, 3, 1, 1)

        self.button_Cutting60seconds = QPushButton(self.scrollAreaWidgetContents_13)
        self.button_Cutting60seconds.setObjectName(u"button_Cutting60seconds")
        self.button_Cutting60seconds.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_92.addWidget(self.button_Cutting60seconds, 1, 0, 1, 1)

        self.button_Cutting90seconds = QPushButton(self.scrollAreaWidgetContents_13)
        self.button_Cutting90seconds.setObjectName(u"button_Cutting90seconds")
        self.button_Cutting90seconds.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_92.addWidget(self.button_Cutting90seconds, 1, 1, 1, 1)

        self.button_Cutting120seconds = QPushButton(self.scrollAreaWidgetContents_13)
        self.button_Cutting120seconds.setObjectName(u"button_Cutting120seconds")
        self.button_Cutting120seconds.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_92.addWidget(self.button_Cutting120seconds, 1, 2, 1, 1)

        self.button_Cutting160seconds = QPushButton(self.scrollAreaWidgetContents_13)
        self.button_Cutting160seconds.setObjectName(u"button_Cutting160seconds")
        self.button_Cutting160seconds.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_92.addWidget(self.button_Cutting160seconds, 1, 3, 1, 1)

        self.button_Cutting260seconds = QPushButton(self.scrollAreaWidgetContents_13)
        self.button_Cutting260seconds.setObjectName(u"button_Cutting260seconds")
        self.button_Cutting260seconds.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_92.addWidget(self.button_Cutting260seconds, 1, 4, 1, 1)

        self.label_405 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_405.setObjectName(u"label_405")
        self.label_405.setMinimumSize(QSize(119, 119))
        self.label_405.setMaximumSize(QSize(119, 119))
        self.label_405.setPixmap(QPixmap(u":/cutsimg/icons/gifs/cutsimg/120s.gif"))
        self.label_405.setScaledContents(True)

        self.gridLayout_92.addWidget(self.label_405, 0, 2, 1, 1)

        self.label_407 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_407.setObjectName(u"label_407")
        self.label_407.setMinimumSize(QSize(119, 119))
        self.label_407.setMaximumSize(QSize(119, 119))
        self.label_407.setPixmap(QPixmap(u":/cutsimg/icons/gifs/cutsimg/60ss.gif"))
        self.label_407.setScaledContents(True)

        self.gridLayout_92.addWidget(self.label_407, 0, 0, 1, 1)

        self.label_406 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_406.setObjectName(u"label_406")
        self.label_406.setMinimumSize(QSize(119, 119))
        self.label_406.setMaximumSize(QSize(119, 119))
        self.label_406.setPixmap(QPixmap(u":/cutsimg/icons/gifs/cutsimg/90s.gif"))
        self.label_406.setScaledContents(True)

        self.gridLayout_92.addWidget(self.label_406, 0, 1, 1, 1)


        self.gridLayout_94.addLayout(self.gridLayout_92, 0, 0, 1, 1)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)

        self.gridLayout_18.addWidget(self.scrollArea_13, 0, 0, 1, 1)

        self.textEdit_5 = QTextEdit(self.page_14)
        self.textEdit_5.setObjectName(u"textEdit_5")
        sizePolicy3.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy3)
        self.textEdit_5.setMinimumSize(QSize(0, 440))
        self.textEdit_5.setMaximumSize(QSize(16777215, 440))
        self.textEdit_5.setStyleSheet(u"QTextEdit {\n"
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
        self.textEdit_5.setReadOnly(True)

        self.gridLayout_18.addWidget(self.textEdit_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.gridLayout_19 = QGridLayout(self.page_15)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.scrollArea_15 = QScrollArea(self.page_15)
        self.scrollArea_15.setObjectName(u"scrollArea_15")
        self.scrollArea_15.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 2px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m\u00f3"
                        "vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, QScroll"
                        "Bar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_15.setFrameShape(QFrame.VLine)
        self.scrollArea_15.setFrameShadow(QFrame.Plain)
        self.scrollArea_15.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setObjectName(u"scrollAreaWidgetContents_15")
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 499, 729))
        self.gridLayout_54 = QGridLayout(self.scrollAreaWidgetContents_15)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.scrollArea_16 = QScrollArea(self.scrollAreaWidgetContents_15)
        self.scrollArea_16.setObjectName(u"scrollArea_16")
        self.scrollArea_16.setMinimumSize(QSize(0, 120))
        self.scrollArea_16.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 2px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m\u00f3"
                        "vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, QScroll"
                        "Bar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.scrollArea_16.setFrameShape(QFrame.VLine)
        self.scrollArea_16.setFrameShadow(QFrame.Plain)
        self.scrollArea_16.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setObjectName(u"scrollAreaWidgetContents_16")
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 463, 118))
        self.gridLayout_98 = QGridLayout(self.scrollAreaWidgetContents_16)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.gridLayout_66 = QGridLayout()
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.label_415 = QLabel(self.scrollAreaWidgetContents_16)
        self.label_415.setObjectName(u"label_415")
        self.label_415.setMinimumSize(QSize(72, 47))
        self.label_415.setMaximumSize(QSize(72, 60))
        self.label_415.setPixmap(QPixmap(u":/Mediacuts/icons/mediacuts/icons8-gpu-64.png"))
        self.label_415.setScaledContents(True)

        self.gridLayout_66.addWidget(self.label_415, 0, 2, 1, 1)

        self.button_HwaccelCUDA = QPushButton(self.scrollAreaWidgetContents_16)
        self.button_HwaccelCUDA.setObjectName(u"button_HwaccelCUDA")
        self.button_HwaccelCUDA.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #00FF00, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de verde para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #32CD32, stop:1 #000000);  /* Gradiente alterado no hover (verde mais escuro) */\n"
"}")

        self.gridLayout_66.addWidget(self.button_HwaccelCUDA, 1, 2, 1, 1)

        self.label_410 = QLabel(self.scrollAreaWidgetContents_16)
        self.label_410.setObjectName(u"label_410")
        self.label_410.setMinimumSize(QSize(81, 60))
        self.label_410.setMaximumSize(QSize(81, 60))
        self.label_410.setPixmap(QPixmap(u":/hardwareimg/icons/gifs/hardwareimg/Hwaccel CPU.gif"))
        self.label_410.setScaledContents(True)

        self.gridLayout_66.addWidget(self.label_410, 0, 0, 1, 1)

        self.button_HwaccelCPU = QPushButton(self.scrollAreaWidgetContents_16)
        self.button_HwaccelCPU.setObjectName(u"button_HwaccelCPU")
        self.button_HwaccelCPU.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #00FF00, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de verde para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #32CD32, stop:1 #000000);  /* Gradiente alterado no hover (verde mais escuro) */\n"
"}")

        self.gridLayout_66.addWidget(self.button_HwaccelCPU, 1, 0, 1, 1)

        self.label_411 = QLabel(self.scrollAreaWidgetContents_16)
        self.label_411.setObjectName(u"label_411")
        self.label_411.setMinimumSize(QSize(88, 60))
        self.label_411.setMaximumSize(QSize(88, 60))
        self.label_411.setPixmap(QPixmap(u":/hardwareimg/icons/gifs/hardwareimg/Vcodec libx264.gif"))
        self.label_411.setScaledContents(True)

        self.gridLayout_66.addWidget(self.label_411, 0, 1, 1, 1)

        self.button_Vcodeclibx264 = QPushButton(self.scrollAreaWidgetContents_16)
        self.button_Vcodeclibx264.setObjectName(u"button_Vcodeclibx264")
        self.button_Vcodeclibx264.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #00FF00, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de verde para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #32CD32, stop:1 #000000);  /* Gradiente alterado no hover (verde mais escuro) */\n"
"}")

        self.gridLayout_66.addWidget(self.button_Vcodeclibx264, 1, 1, 1, 1)

        self.label_416 = QLabel(self.scrollAreaWidgetContents_16)
        self.label_416.setObjectName(u"label_416")
        self.label_416.setMinimumSize(QSize(108, 60))
        self.label_416.setMaximumSize(QSize(108, 60))
        self.label_416.setPixmap(QPixmap(u":/hardwareimg/icons/gifs/hardwareimg/Vcodec h264_nvenc.gif"))
        self.label_416.setScaledContents(True)

        self.gridLayout_66.addWidget(self.label_416, 0, 3, 1, 1)

        self.button_Vcodech264_nvenc = QPushButton(self.scrollAreaWidgetContents_16)
        self.button_Vcodech264_nvenc.setObjectName(u"button_Vcodech264_nvenc")
        self.button_Vcodech264_nvenc.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #00FF00, stop:0.5 #000000, stop:1 #000000);  /* Gradiente de verde para preto */\n"
"    color: white;  /* Cor do texto do bot\u00e3o */\n"
"    border: none;  /* Remove a borda padr\u00e3o */\n"
"    border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"    padding: 10px;  /* Espa\u00e7amento interno */\n"
"    font-size: 10px;  /* Tamanho da fonte */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #32CD32, stop:1 #000000);  /* Gradiente alterado no hover (verde mais escuro) */\n"
"}")

        self.gridLayout_66.addWidget(self.button_Vcodech264_nvenc, 1, 3, 1, 1)


        self.gridLayout_98.addLayout(self.gridLayout_66, 0, 0, 2, 1)

        self.scrollArea_16.setWidget(self.scrollAreaWidgetContents_16)

        self.gridLayout_54.addWidget(self.scrollArea_16, 0, 0, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 52, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.gridLayout_97 = QGridLayout()
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.label_98 = QLabel(self.scrollAreaWidgetContents_15)
        self.label_98.setObjectName(u"label_98")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy4)

        self.gridLayout_97.addWidget(self.label_98, 1, 2, 1, 1)

        self.button_Bitrate = QSpinBox(self.scrollAreaWidgetContents_15)
        self.button_Bitrate.setObjectName(u"button_Bitrate")
        self.button_Bitrate.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.button_Bitrate.setMaximum(999999999)
        self.button_Bitrate.setValue(2000)

        self.gridLayout_97.addWidget(self.button_Bitrate, 1, 3, 1, 1)

        self.label_99 = QLabel(self.scrollAreaWidgetContents_15)
        self.label_99.setObjectName(u"label_99")
        sizePolicy4.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy4)

        self.gridLayout_97.addWidget(self.label_99, 2, 2, 1, 1)

        self.button_Maxrate = QSpinBox(self.scrollAreaWidgetContents_15)
        self.button_Maxrate.setObjectName(u"button_Maxrate")
        self.button_Maxrate.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.button_Maxrate.setMaximum(999999999)
        self.button_Maxrate.setValue(2000)

        self.gridLayout_97.addWidget(self.button_Maxrate, 2, 3, 1, 1)

        self.label_100 = QLabel(self.scrollAreaWidgetContents_15)
        self.label_100.setObjectName(u"label_100")
        sizePolicy4.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy4)

        self.gridLayout_97.addWidget(self.label_100, 3, 2, 1, 1)

        self.button_Bufsize = QSpinBox(self.scrollAreaWidgetContents_15)
        self.button_Bufsize.setObjectName(u"button_Bufsize")
        self.button_Bufsize.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.button_Bufsize.setMaximum(999999999)
        self.button_Bufsize.setValue(4000)

        self.gridLayout_97.addWidget(self.button_Bufsize, 3, 3, 1, 1)

        self.button_Preset = QComboBox(self.scrollAreaWidgetContents_15)
        self.button_Preset.addItem("")
        self.button_Preset.addItem("")
        self.button_Preset.addItem("")
        self.button_Preset.addItem("")
        self.button_Preset.addItem("")
        self.button_Preset.setObjectName(u"button_Preset")
        self.button_Preset.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 5px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 12px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_97.addWidget(self.button_Preset, 3, 1, 1, 1)

        self.button_gpu_or_cpu = QComboBox(self.scrollAreaWidgetContents_15)
        self.button_gpu_or_cpu.addItem("")
        self.button_gpu_or_cpu.addItem("")
        self.button_gpu_or_cpu.setObjectName(u"button_gpu_or_cpu")
        self.button_gpu_or_cpu.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 5px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 12px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"\n"
"")

        self.gridLayout_97.addWidget(self.button_gpu_or_cpu, 1, 1, 1, 1)

        self.label_168 = QLabel(self.scrollAreaWidgetContents_15)
        self.label_168.setObjectName(u"label_168")

        self.gridLayout_97.addWidget(self.label_168, 1, 0, 1, 1)

        self.label_169 = QLabel(self.scrollAreaWidgetContents_15)
        self.label_169.setObjectName(u"label_169")

        self.gridLayout_97.addWidget(self.label_169, 2, 0, 1, 1)

        self.button_Profile = QComboBox(self.scrollAreaWidgetContents_15)
        self.button_Profile.addItem("")
        self.button_Profile.addItem("")
        self.button_Profile.setObjectName(u"button_Profile")
        self.button_Profile.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 5px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 12px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_97.addWidget(self.button_Profile, 2, 1, 1, 1)

        self.label_167 = QLabel(self.scrollAreaWidgetContents_15)
        self.label_167.setObjectName(u"label_167")

        self.gridLayout_97.addWidget(self.label_167, 3, 0, 1, 1)


        self.gridLayout_54.addLayout(self.gridLayout_97, 1, 1, 1, 1)

        self.textEdit_6 = QTextEdit(self.scrollAreaWidgetContents_15)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy3)
        self.textEdit_6.setMinimumSize(QSize(0, 481))
        self.textEdit_6.setMaximumSize(QSize(16777215, 481))
        self.textEdit_6.setStyleSheet(u"QTextEdit {\n"
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
        self.textEdit_6.setReadOnly(True)

        self.gridLayout_54.addWidget(self.textEdit_6, 2, 0, 1, 3)

        self.scrollArea_15.setWidget(self.scrollAreaWidgetContents_15)

        self.gridLayout_19.addWidget(self.scrollArea_15, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.gridLayout_20 = QGridLayout(self.page_16)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.widget = QWidget(self.page_16)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"    background-color: #ffffff;\n"
"    color: #050505;\n"
"}")
        self.gridLayout_22 = QGridLayout(self.widget)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.stackedWidget_2 = QCustomQStackedWidget(self.widget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setStyleSheet(u"")
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.gridLayout_26 = QGridLayout(self.page_17)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_4 = QLabel(self.page_17)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_21.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.page_17)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_21.addWidget(self.label_5, 2, 0, 1, 1)

        self.Scalewidth_spin = QSpinBox(self.page_17)
        self.Scalewidth_spin.setObjectName(u"Scalewidth_spin")
        self.Scalewidth_spin.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.Scalewidth_spin.setMaximum(999999999)
        self.Scalewidth_spin.setValue(1280)

        self.gridLayout_21.addWidget(self.Scalewidth_spin, 0, 1, 1, 1)

        self.Scaleheight_spin = QSpinBox(self.page_17)
        self.Scaleheight_spin.setObjectName(u"Scaleheight_spin")
        self.Scaleheight_spin.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.Scaleheight_spin.setMaximum(999999999)
        self.Scaleheight_spin.setValue(1800)

        self.gridLayout_21.addWidget(self.Scaleheight_spin, 2, 1, 1, 1)


        self.gridLayout_26.addLayout(self.gridLayout_21, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_17)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.gridLayout_24 = QGridLayout(self.page_18)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalSpacer_8 = QSpacerItem(20, 14, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_23.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.horizontalSlider = QCustomQSlider(self.page_18)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_23.addWidget(self.horizontalSlider, 1, 0, 1, 1)

        self.label_2 = QLabel(self.page_18)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_23.addWidget(self.label_2, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.page_18)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy5)
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")

        self.gridLayout_23.addWidget(self.spinBox, 1, 1, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_23, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_18)

        self.gridLayout_22.addWidget(self.stackedWidget_2, 1, 0, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.checkBox = QCustomCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_25.addWidget(self.checkBox, 0, 0, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_25, 2, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font1)
        self.label.setIndent(19)

        self.gridLayout_22.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 457, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_20.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_16)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.gridLayout_50 = QGridLayout(self.page_19)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_49 = QGridLayout()
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_3 = QLabel(self.page_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_49.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_50.addLayout(self.gridLayout_49, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(39)
        self.gridLayout_4.setContentsMargins(28, 17, 63, 32)
        self.checkBox_7 = QCustomCheckBox(self.page_19)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy2.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy2)
        self.checkBox_7.setMinimumSize(QSize(212, 0))
        self.checkBox_7.setMaximumSize(QSize(212, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_7, 10, 0, 1, 1)

        self.checkBox_12 = QCustomCheckBox(self.page_19)
        self.checkBox_12.setObjectName(u"checkBox_12")
        sizePolicy2.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy2)
        self.checkBox_12.setMinimumSize(QSize(115, 0))
        self.checkBox_12.setMaximumSize(QSize(115, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_12, 2, 2, 1, 1)

        self.checkBox_16 = QCustomCheckBox(self.page_19)
        self.checkBox_16.setObjectName(u"checkBox_16")
        sizePolicy2.setHeightForWidth(self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy2)
        self.checkBox_16.setMinimumSize(QSize(115, 0))
        self.checkBox_16.setMaximumSize(QSize(115, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_16, 6, 2, 1, 1)

        self.checkBox_11 = QCustomCheckBox(self.page_19)
        self.checkBox_11.setObjectName(u"checkBox_11")
        sizePolicy2.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy2)
        self.checkBox_11.setMinimumSize(QSize(115, 0))
        self.checkBox_11.setMaximumSize(QSize(115, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_11, 2, 0, 1, 1)

        self.checkBox_8 = QCustomCheckBox(self.page_19)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy2.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy2)
        self.checkBox_8.setMinimumSize(QSize(212, 0))
        self.checkBox_8.setMaximumSize(QSize(212, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_8, 11, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 73, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 9, 0, 1, 7)

        self.verticalSpacer_10 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer_10, 0, 0, 1, 7)

        self.label_8 = QLabel(self.page_19)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 4)

        self.checkBox_4 = QCustomCheckBox(self.page_19)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy2.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy2)
        self.checkBox_4.setMinimumSize(QSize(115, 0))
        self.checkBox_4.setMaximumSize(QSize(115, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_4, 2, 4, 1, 2)

        self.checkBox_13 = QCustomCheckBox(self.page_19)
        self.checkBox_13.setObjectName(u"checkBox_13")
        sizePolicy2.setHeightForWidth(self.checkBox_13.sizePolicy().hasHeightForWidth())
        self.checkBox_13.setSizePolicy(sizePolicy2)
        self.checkBox_13.setMinimumSize(QSize(187, 0))
        self.checkBox_13.setMaximumSize(QSize(187, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_13, 6, 4, 1, 1)

        self.checkBox_10 = QCustomCheckBox(self.page_19)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy2.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy2)
        self.checkBox_10.setMinimumSize(QSize(115, 0))
        self.checkBox_10.setMaximumSize(QSize(115, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_10, 6, 0, 1, 1)

        self.textEdit = QTextEdit(self.page_19)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 50))
        self.textEdit.setMaximumSize(QSize(16777215, 50))
        self.textEdit.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_4.addWidget(self.textEdit, 12, 0, 1, 7)


        self.gridLayout_50.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 262, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_50.addItem(self.verticalSpacer_9, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_19)
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.gridLayout_61 = QGridLayout(self.page_23)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_52 = QGridLayout()
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_9 = QLabel(self.page_23)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_52.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_61.addLayout(self.gridLayout_52, 0, 0, 1, 2)

        self.verticalSpacer_12 = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_61.addItem(self.verticalSpacer_12, 1, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.page_23)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_59 = QGridLayout(self.groupBox_3)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_60 = QGridLayout()
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.spinBox_6 = QSpinBox(self.groupBox_3)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.spinBox_6.setMaximum(999)
        self.spinBox_6.setValue(100)

        self.gridLayout_60.addWidget(self.spinBox_6, 0, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_60.addWidget(self.label_20, 1, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox_3)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.spinBox_7.setMaximum(9999)
        self.spinBox_7.setValue(43)

        self.gridLayout_60.addWidget(self.spinBox_7, 1, 1, 1, 1)

        self.button_UploadWatermark = QPushButton(self.groupBox_3)
        self.button_UploadWatermark.setObjectName(u"button_UploadWatermark")
        self.button_UploadWatermark.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 18px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")
        self.button_UploadWatermark.setIcon(icon24)
        self.button_UploadWatermark.setIconSize(QSize(45, 31))

        self.gridLayout_60.addWidget(self.button_UploadWatermark, 2, 0, 1, 2)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_60.addWidget(self.label_18, 0, 0, 1, 1)


        self.gridLayout_59.addLayout(self.gridLayout_60, 0, 0, 1, 1)


        self.gridLayout_61.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.page_23)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_58 = QGridLayout(self.groupBox_2)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_55 = QGridLayout()
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_55.addWidget(self.label_12, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_55.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_55.addWidget(self.label_16, 4, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_55.addWidget(self.label_13, 2, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_2)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.spinBox_4.setValue(39)

        self.gridLayout_55.addWidget(self.spinBox_4, 2, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_55.addWidget(self.comboBox_3, 3, 1, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox_2)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.spinBox_5.setValue(4)

        self.gridLayout_55.addWidget(self.spinBox_5, 4, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_55.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_55.addWidget(self.label_17, 1, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.groupBox_2)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_55.addWidget(self.comboBox_4, 1, 1, 1, 1)


        self.gridLayout_58.addLayout(self.gridLayout_55, 0, 0, 1, 1)


        self.gridLayout_61.addWidget(self.groupBox_2, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.page_23)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_53 = QGridLayout(self.groupBox)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_51 = QGridLayout()
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_51.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_51.addWidget(self.label_10, 2, 0, 1, 1)

        self.x_axis_spinbox = QSpinBox(self.groupBox)
        self.x_axis_spinbox.setObjectName(u"x_axis_spinbox")
        self.x_axis_spinbox.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.x_axis_spinbox.setMinimum(10)
        self.x_axis_spinbox.setMaximum(999999999)

        self.gridLayout_51.addWidget(self.x_axis_spinbox, 1, 1, 1, 1)

        self.y_axis_spinbox = QSpinBox(self.groupBox)
        self.y_axis_spinbox.setObjectName(u"y_axis_spinbox")
        self.y_axis_spinbox.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.y_axis_spinbox.setMinimum(10)
        self.y_axis_spinbox.setMaximum(999999999)

        self.gridLayout_51.addWidget(self.y_axis_spinbox, 2, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_51.addWidget(self.comboBox_2, 0, 0, 1, 2)


        self.gridLayout_53.addLayout(self.gridLayout_51, 0, 0, 1, 1)


        self.gridLayout_61.addWidget(self.groupBox, 2, 2, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 429, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_61.addItem(self.verticalSpacer_13, 3, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_23)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.gridLayout_47 = QGridLayout(self.page_20)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.stackedWidget_3 = QCustomQStackedWidget(self.page_20)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"QStackedWidget {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda ao redor */\n"
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
"\n"
"")
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.gridLayout_46 = QGridLayout(self.page_21)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.upload_refresh = QPushButton(self.page_21)
        self.upload_refresh.setObjectName(u"upload_refresh")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.upload_refresh.sizePolicy().hasHeightForWidth())
        self.upload_refresh.setSizePolicy(sizePolicy7)
        self.upload_refresh.setMinimumSize(QSize(41, 0))
        self.upload_refresh.setMaximumSize(QSize(41, 16777215))
        self.upload_refresh.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon25 = QIcon()
        icon25.addFile(u":/feather/icons/feather/refresh-ccw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_refresh.setIcon(icon25)
        self.upload_refresh.setIconSize(QSize(18, 30))

        self.gridLayout_42.addWidget(self.upload_refresh, 0, 2, 1, 1)

        self.device_serials_combox = QComboBox(self.page_21)
        self.device_serials_combox.setObjectName(u"device_serials_combox")
        self.device_serials_combox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_42.addWidget(self.device_serials_combox, 0, 1, 1, 1)

        self.SelectallAndroidDevice = QPushButton(self.page_21)
        self.SelectallAndroidDevice.setObjectName(u"SelectallAndroidDevice")
        self.SelectallAndroidDevice.setMinimumSize(QSize(41, 0))
        self.SelectallAndroidDevice.setMaximumSize(QSize(41, 16777215))
        self.SelectallAndroidDevice.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon26 = QIcon()
        icon26.addFile(u":/feather/icons/feather/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SelectallAndroidDevice.setIcon(icon26)
        self.SelectallAndroidDevice.setIconSize(QSize(29, 29))

        self.gridLayout_42.addWidget(self.SelectallAndroidDevice, 0, 3, 1, 1)

        self.RemoeallAndroidDevice = QPushButton(self.page_21)
        self.RemoeallAndroidDevice.setObjectName(u"RemoeallAndroidDevice")
        self.RemoeallAndroidDevice.setMinimumSize(QSize(41, 0))
        self.RemoeallAndroidDevice.setMaximumSize(QSize(41, 16777215))
        self.RemoeallAndroidDevice.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon27 = QIcon()
        icon27.addFile(u":/material_design/icons/material_design/leak_remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RemoeallAndroidDevice.setIcon(icon27)
        self.RemoeallAndroidDevice.setIconSize(QSize(29, 29))

        self.gridLayout_42.addWidget(self.RemoeallAndroidDevice, 0, 4, 1, 1)

        self.pushButton_7 = QPushButton(self.page_21)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 37))
        self.pushButton_7.setMaximumSize(QSize(16777215, 37))
        self.pushButton_7.setStyleSheet(u"            QPushButton {\n"
"                background-color: #transparency;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"")
        icon28 = QIcon()
        icon28.addFile(u":/Mediacuts/icons/mediacuts/icons8-android-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon28)
        self.pushButton_7.setIconSize(QSize(12, 12))

        self.gridLayout_42.addWidget(self.pushButton_7, 0, 0, 1, 1)


        self.gridLayout_46.addLayout(self.gridLayout_42, 1, 0, 1, 1)

        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setHorizontalSpacing(15)
        self.gridLayout_43.setVerticalSpacing(10)
        self.gridLayout_43.setContentsMargins(29, 2, 9, 0)
        self.Scheduleduploadseconds = QSpinBox(self.page_21)
        self.Scheduleduploadseconds.setObjectName(u"Scheduleduploadseconds")
        self.Scheduleduploadseconds.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.Scheduleduploadseconds.setMinimum(1)
        self.Scheduleduploadseconds.setMaximum(999999999)
        self.Scheduleduploadseconds.setValue(180)

        self.gridLayout_43.addWidget(self.Scheduleduploadseconds, 4, 1, 1, 1)

        self.Scheduledupload = QCustomCheckBox(self.page_21)
        self.Scheduledupload.setObjectName(u"Scheduledupload")
        sizePolicy7.setHeightForWidth(self.Scheduledupload.sizePolicy().hasHeightForWidth())
        self.Scheduledupload.setSizePolicy(sizePolicy7)
        self.Scheduledupload.setMinimumSize(QSize(157, 17))
        self.Scheduledupload.setMaximumSize(QSize(171, 17))
        self.Scheduledupload.setStyleSheet(u"")
        icon29 = QIcon()
        icon29.addFile(u":/Mediacuts/icons/mediacuts/icons8-time-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Scheduledupload.setIcon(icon29)
        self.Scheduledupload.setChecked(False)

        self.gridLayout_43.addWidget(self.Scheduledupload, 4, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.page_21)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon30 = QIcon()
        icon30.addFile(u":/font_awesome_regular/icons/font_awesome/regular/hourglass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon30)

        self.gridLayout_43.addWidget(self.pushButton_8, 1, 0, 1, 1)

        self.SelectNumbercutsUploadperhour = QSpinBox(self.page_21)
        self.SelectNumbercutsUploadperhour.setObjectName(u"SelectNumbercutsUploadperhour")
        self.SelectNumbercutsUploadperhour.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")

        self.gridLayout_43.addWidget(self.SelectNumbercutsUploadperhour, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.page_21)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon31 = QIcon()
        icon31.addFile(u":/material_design/icons/material_design/supervisor_account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon31)

        self.gridLayout_43.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.SelectNumbercutsUploadperday = QSpinBox(self.page_21)
        self.SelectNumbercutsUploadperday.setObjectName(u"SelectNumbercutsUploadperday")
        self.SelectNumbercutsUploadperday.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.SelectNumbercutsUploadperday.setValue(10)

        self.gridLayout_43.addWidget(self.SelectNumbercutsUploadperday, 0, 1, 1, 1)


        self.gridLayout_46.addLayout(self.gridLayout_43, 2, 0, 1, 1)

        self.start_upload = QPushButton(self.page_21)
        self.start_upload.setObjectName(u"start_upload")
        self.start_upload.setMinimumSize(QSize(0, 43))
        self.start_upload.setMaximumSize(QSize(16777215, 43))
        self.start_upload.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon32 = QIcon()
        icon32.addFile(u":/Mediacuts/icons/mediacuts/icons8-start-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_upload.setIcon(icon32)
        self.start_upload.setIconSize(QSize(26, 26))

        self.gridLayout_46.addWidget(self.start_upload, 0, 0, 1, 1)

        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.ModesShortify = QCustomQPushButton(self.page_21)
        self.ModesShortify.setObjectName(u"ModesShortify")
        sizePolicy5.setHeightForWidth(self.ModesShortify.sizePolicy().hasHeightForWidth())
        self.ModesShortify.setSizePolicy(sizePolicy5)
        self.ModesShortify.setMinimumSize(QSize(0, 43))
        self.ModesShortify.setMaximumSize(QSize(16777215, 43))
        self.ModesShortify.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon33 = QIcon()
        icon33.addFile(u":/Mediacuts/icons/mediacuts/definicoes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ModesShortify.setIcon(icon33)
        self.ModesShortify.setIconSize(QSize(26, 26))

        self.gridLayout_44.addWidget(self.ModesShortify, 0, 0, 1, 2)


        self.gridLayout_46.addLayout(self.gridLayout_44, 3, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_21)
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.gridLayout_86 = QGridLayout(self.page_22)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.groupBox_6 = QGroupBox(self.page_22)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(498, 0))
        self.groupBox_6.setMaximumSize(QSize(498, 16777215))
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"    background-color: #F7F7F7; /* Fundo do QGroupBox */\n"
"    border: 1px solid #E0E0E0; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    margin-top: 10px; /* Espa\u00e7amento entre o t\u00edtulo e o conte\u00fado */\n"
"    font-size: 16px; /* Tamanho da fonte do t\u00edtulo */\n"
"    color: black; /* Cor do texto do t\u00edtulo */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; /* Define o t\u00edtulo fora do fundo */\n"
"    subcontrol-position: top center; /* Posiciona o t\u00edtulo no topo central */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno do t\u00edtulo */\n"
"    background-color: #F7F7F7; /* Fundo do t\u00edtulo */\n"
"    border-radius: 10px; /* Borda arredondada do t\u00edtulo */\n"
"    font-weight: bold; /* T\u00edtulo em negrito */\n"
"}\n"
"\n"
"QGroupBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QGroupBox:pressed {\n"
""
                        "    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"")
        self.gridLayout_40 = QGridLayout(self.groupBox_6)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.stackedWidget_8 = QCustomQStackedWidget(self.groupBox_6)
        self.stackedWidget_8.setObjectName(u"stackedWidget_8")
        self.stackedWidget_8.setStyleSheet(u"QStackedWidget {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #F7F7F7; /* Borda ao redor */\n"
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
"\n"
"")
        self.page_36 = QWidget()
        self.page_36.setObjectName(u"page_36")
        self.gridLayout_84 = QGridLayout(self.page_36)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.gridLayout_83 = QGridLayout()
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.verticalSpacer_17 = QSpacerItem(20, 97, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_83.addItem(self.verticalSpacer_17, 2, 0, 1, 1)

        self.AlgoV1 = QCheckBox(self.page_36)
        self.AlgoV1.setObjectName(u"AlgoV1")
        self.AlgoV1.setMinimumSize(QSize(0, 24))
        self.AlgoV1.setMaximumSize(QSize(16777215, 24))
        self.AlgoV1.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px; /* Espa\u00e7o entre o texto e a caixa de sele\u00e7\u00e3o */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    color: black; /* Cor do texto */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    padding: 5px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px; /* Largura da caixa de sele\u00e7\u00e3o */\n"
"    height: 16px; /* Altura da caixa de sele\u00e7\u00e3o */\n"
"    background-color: #B0C4DE; /* Fundo padr\u00e3o da caixa */\n"
"    border: 1px solid #B0C4DE; /* Borda da caixa */\n"
"    border-radius: 4px; /* Borda arredondada */\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse na caixa */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #DCDCDC; /* Fundo da caixa quando marcada */\n"
"    border: 1px solid #A0A0A0; /* Borda ao marcar */\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #F0F0F0; /* F"
                        "undo quando desabilitada */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitada */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse no texto */\n"
"}\n"
"\n"
"QCheckBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar no texto */\n"
"}\n"
"")

        self.gridLayout_83.addWidget(self.AlgoV1, 0, 0, 1, 1)

        self.GetThreads = QCheckBox(self.page_36)
        self.GetThreads.setObjectName(u"GetThreads")
        self.GetThreads.setMinimumSize(QSize(0, 24))
        self.GetThreads.setMaximumSize(QSize(16777215, 24))
        self.GetThreads.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px; /* Espa\u00e7o entre o texto e a caixa de sele\u00e7\u00e3o */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    color: black; /* Cor do texto */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    padding: 5px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px; /* Largura da caixa de sele\u00e7\u00e3o */\n"
"    height: 16px; /* Altura da caixa de sele\u00e7\u00e3o */\n"
"    background-color: #B0C4DE; /* Fundo padr\u00e3o da caixa */\n"
"    border: 1px solid #B0C4DE; /* Borda da caixa */\n"
"    border-radius: 4px; /* Borda arredondada */\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse na caixa */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #DCDCDC; /* Fundo da caixa quando marcada */\n"
"    border: 1px solid #A0A0A0; /* Borda ao marcar */\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #F0F0F0; /* F"
                        "undo quando desabilitada */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitada */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse no texto */\n"
"}\n"
"\n"
"QCheckBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar no texto */\n"
"}\n"
"")

        self.gridLayout_83.addWidget(self.GetThreads, 1, 0, 1, 1)


        self.gridLayout_84.addLayout(self.gridLayout_83, 0, 0, 1, 1)

        self.stackedWidget_8.addWidget(self.page_36)
        self.page_37 = QWidget()
        self.page_37.setObjectName(u"page_37")
        self.gridLayout_85 = QGridLayout(self.page_37)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.gridLayout_45 = QGridLayout()
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(-1, -1, 70, -1)
        self.comboBoxacctiktoks = QComboBox(self.page_37)
        self.comboBoxacctiktoks.setObjectName(u"comboBoxacctiktoks")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.comboBoxacctiktoks.sizePolicy().hasHeightForWidth())
        self.comboBoxacctiktoks.setSizePolicy(sizePolicy8)
        self.comboBoxacctiktoks.setMinimumSize(QSize(283, 0))
        self.comboBoxacctiktoks.setMaximumSize(QSize(283, 16777215))
        self.comboBoxacctiktoks.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 4px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 11px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 11px; /* Ajuste de fonte para itens */\n"
"}\n"
"")
        self.comboBoxacctiktoks.setEditable(True)

        self.gridLayout_45.addWidget(self.comboBoxacctiktoks, 1, 1, 1, 1)

        self.Uploadyoutube_app = QCheckBox(self.page_37)
        self.Uploadyoutube_app.setObjectName(u"Uploadyoutube_app")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.Uploadyoutube_app.sizePolicy().hasHeightForWidth())
        self.Uploadyoutube_app.setSizePolicy(sizePolicy9)
        self.Uploadyoutube_app.setMinimumSize(QSize(127, 23))
        self.Uploadyoutube_app.setMaximumSize(QSize(124, 18))
        self.Uploadyoutube_app.setStyleSheet(u"QCheckBox {\n"
"\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"\n"
"}\n"
"\n"
"")
        icon34 = QIcon()
        icon34.addFile(u":/feather/icons/feather/youtube.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Uploadyoutube_app.setIcon(icon34)

        self.gridLayout_45.addWidget(self.Uploadyoutube_app, 3, 0, 1, 1)

        self.comboBox_accYoutube = QComboBox(self.page_37)
        self.comboBox_accYoutube.setObjectName(u"comboBox_accYoutube")
        self.comboBox_accYoutube.setMinimumSize(QSize(283, 0))
        self.comboBox_accYoutube.setMaximumSize(QSize(283, 16777215))
        self.comboBox_accYoutube.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 4px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 11px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 11px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_45.addWidget(self.comboBox_accYoutube, 3, 1, 1, 1)

        self.KwaiApp = QCheckBox(self.page_37)
        self.KwaiApp.setObjectName(u"KwaiApp")
        sizePolicy9.setHeightForWidth(self.KwaiApp.sizePolicy().hasHeightForWidth())
        self.KwaiApp.setSizePolicy(sizePolicy9)
        self.KwaiApp.setMinimumSize(QSize(127, 0))
        self.KwaiApp.setMaximumSize(QSize(127, 24))
        self.KwaiApp.setFont(font1)
        self.KwaiApp.setStyleSheet(u"")
        icon35 = QIcon()
        icon35.addFile(u":/Mediacuts/icons/mediacuts/icone-do-aplicativo-kwai-plataforma-de-video-curto-rede-social-chinesa_277909-632-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.KwaiApp.setIcon(icon35)

        self.gridLayout_45.addWidget(self.KwaiApp, 2, 0, 1, 1)

        self.TiktokApp = QCheckBox(self.page_37)
        self.TiktokApp.setObjectName(u"TiktokApp")
        sizePolicy9.setHeightForWidth(self.TiktokApp.sizePolicy().hasHeightForWidth())
        self.TiktokApp.setSizePolicy(sizePolicy9)
        self.TiktokApp.setMinimumSize(QSize(127, 24))
        self.TiktokApp.setMaximumSize(QSize(127, 24))
        self.TiktokApp.setStyleSheet(u"")
        icon36 = QIcon()
        icon36.addFile(u":/Mediacuts/icons/mediacuts/icons8-tiktok-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.TiktokApp.setIcon(icon36)

        self.gridLayout_45.addWidget(self.TiktokApp, 1, 0, 1, 1)

        self.comboBoxacckwais = QComboBox(self.page_37)
        self.comboBoxacckwais.setObjectName(u"comboBoxacckwais")
        sizePolicy7.setHeightForWidth(self.comboBoxacckwais.sizePolicy().hasHeightForWidth())
        self.comboBoxacckwais.setSizePolicy(sizePolicy7)
        self.comboBoxacckwais.setMinimumSize(QSize(283, 0))
        self.comboBoxacckwais.setMaximumSize(QSize(283, 16777215))
        self.comboBoxacckwais.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 4px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 11px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 11px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_45.addWidget(self.comboBoxacckwais, 2, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.page_37)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(418, 43))
        self.pushButton_10.setMaximumSize(QSize(418, 43))
        self.pushButton_10.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon37 = QIcon()
        icon37.addFile(u":/material_design/icons/material_design/person_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon37)

        self.gridLayout_45.addWidget(self.pushButton_10, 0, 0, 1, 2)


        self.gridLayout_85.addLayout(self.gridLayout_45, 0, 0, 1, 1)

        self.stackedWidget_8.addWidget(self.page_37)
        self.page_38 = QWidget()
        self.page_38.setObjectName(u"page_38")
        self.gridLayout_88 = QGridLayout(self.page_38)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.pushButton_11 = QPushButton(self.page_38)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 44))
        self.pushButton_11.setMaximumSize(QSize(16777215, 44))
        self.pushButton_11.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon38 = QIcon()
        icon38.addFile(u":/material_design/icons/material_design/arrow_back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon38)

        self.gridLayout_88.addWidget(self.pushButton_11, 3, 0, 1, 1)

        self.gridLayout_87 = QGridLayout()
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.gridLayout_87.setContentsMargins(9, 2, 2, 9)
        self.Tiktok_AddAcc = QLineEdit(self.page_38)
        self.Tiktok_AddAcc.setObjectName(u"Tiktok_AddAcc")
        self.Tiktok_AddAcc.setMinimumSize(QSize(126, 0))
        self.Tiktok_AddAcc.setMaximumSize(QSize(126, 16777215))
        self.Tiktok_AddAcc.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #E0E0E0; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 16px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"    selection-background-color: #DCDCDC; /* Fundo da sele\u00e7\u00e3o de texto */\n"
"    selection-color: black; /* Cor do texto selecionado */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #FFFFFF; /* Fundo ao focar */\n"
"    border: 1px solid #A0A0A0; /* Borda ao focar */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_87.addWidget(self.Tiktok_AddAcc, 3, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_87.addItem(self.verticalSpacer_18, 8, 2, 1, 1)

        self.Day_AddAcc = QLineEdit(self.page_38)
        self.Day_AddAcc.setObjectName(u"Day_AddAcc")
        self.Day_AddAcc.setMinimumSize(QSize(108, 0))
        self.Day_AddAcc.setMaximumSize(QSize(108, 16777215))
        self.Day_AddAcc.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #E0E0E0; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 11px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"    selection-background-color: #DCDCDC; /* Fundo da sele\u00e7\u00e3o de texto */\n"
"    selection-color: black; /* Cor do texto selecionado */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #FFFFFF; /* Fundo ao focar */\n"
"    border: 1px solid #A0A0A0; /* Borda ao focar */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_87.addWidget(self.Day_AddAcc, 2, 2, 1, 1)

        self.ChannelYoutube_AddAcc = QLineEdit(self.page_38)
        self.ChannelYoutube_AddAcc.setObjectName(u"ChannelYoutube_AddAcc")
        self.ChannelYoutube_AddAcc.setMinimumSize(QSize(102, 0))
        self.ChannelYoutube_AddAcc.setMaximumSize(QSize(194, 16777215))
        self.ChannelYoutube_AddAcc.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #E0E0E0; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 11px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"    selection-background-color: #DCDCDC; /* Fundo da sele\u00e7\u00e3o de texto */\n"
"    selection-color: black; /* Cor do texto selecionado */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #FFFFFF; /* Fundo ao focar */\n"
"    border: 1px solid #A0A0A0; /* Borda ao focar */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_87.addWidget(self.ChannelYoutube_AddAcc, 2, 1, 1, 1)

        self.label_14 = QLabel(self.page_38)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_87.addWidget(self.label_14, 2, 0, 1, 1)

        self.Time_AddAcc = QLineEdit(self.page_38)
        self.Time_AddAcc.setObjectName(u"Time_AddAcc")
        self.Time_AddAcc.setMinimumSize(QSize(92, 0))
        self.Time_AddAcc.setMaximumSize(QSize(111, 16777215))
        self.Time_AddAcc.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #E0E0E0; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 11px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"    selection-background-color: #DCDCDC; /* Fundo da sele\u00e7\u00e3o de texto */\n"
"    selection-color: black; /* Cor do texto selecionado */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #FFFFFF; /* Fundo ao focar */\n"
"    border: 1px solid #A0A0A0; /* Borda ao focar */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_87.addWidget(self.Time_AddAcc, 2, 5, 1, 1)

        self.label_6 = QLabel(self.page_38)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_87.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_7 = QLabel(self.page_38)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 34))
        self.label_7.setMaximumSize(QSize(16777215, 34))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_87.addWidget(self.label_7, 4, 0, 1, 1)

        self.Kwai_AddAcc = QLineEdit(self.page_38)
        self.Kwai_AddAcc.setObjectName(u"Kwai_AddAcc")
        self.Kwai_AddAcc.setMinimumSize(QSize(126, 0))
        self.Kwai_AddAcc.setMaximumSize(QSize(126, 16777215))
        self.Kwai_AddAcc.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Fundo principal */\n"
"    border: 1px solid #E0E0E0; /* Borda */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 16px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"    selection-background-color: #DCDCDC; /* Fundo da sele\u00e7\u00e3o de texto */\n"
"    selection-color: black; /* Cor do texto selecionado */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #FFFFFF; /* Fundo ao focar */\n"
"    border: 1px solid #A0A0A0; /* Borda ao focar */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Fundo quando desabilitado */\n"
"    border: 1px solid #C0C0C0; /* Borda quando desabilitado */\n"
"    color: #A0A0A0; /* Cor do texto desabilitado */\n"
"}\n"
"")

        self.gridLayout_87.addWidget(self.Kwai_AddAcc, 4, 1, 1, 1)


        self.gridLayout_88.addLayout(self.gridLayout_87, 0, 0, 1, 1)

        self.Addacctoshortify_button = QPushButton(self.page_38)
        self.Addacctoshortify_button.setObjectName(u"Addacctoshortify_button")
        self.Addacctoshortify_button.setMinimumSize(QSize(0, 40))
        self.Addacctoshortify_button.setMaximumSize(QSize(16777215, 44))
        self.Addacctoshortify_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon39 = QIcon()
        icon39.addFile(u":/font_awesome_regular/icons/font_awesome/regular/address-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Addacctoshortify_button.setIcon(icon39)
        self.Addacctoshortify_button.setIconSize(QSize(26, 26))

        self.gridLayout_88.addWidget(self.Addacctoshortify_button, 2, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 75, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_88.addItem(self.verticalSpacer_19, 1, 0, 1, 1)

        self.stackedWidget_8.addWidget(self.page_38)

        self.gridLayout_40.addWidget(self.stackedWidget_8, 0, 0, 1, 1)


        self.gridLayout_86.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.page_22)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon40 = QIcon()
        icon40.addFile(u":/feather/icons/feather/skip-back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon40)

        self.gridLayout_86.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_22)

        self.gridLayout_47.addWidget(self.stackedWidget_3, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 376, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_47.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_20)
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.gridLayout_64 = QGridLayout(self.page_24)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.widget_2 = QCustomSlideMenu(self.page_24)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_63 = QGridLayout(self.widget_2)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))
        self.pushButton_2.setMaximumSize(QSize(16777215, 35))
        self.pushButton_2.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        self.pushButton_2.setIcon(icon16)
        self.pushButton_2.setIconSize(QSize(28, 23))

        self.gridLayout_63.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 35))
        self.pushButton_3.setMaximumSize(QSize(16777215, 35))
        self.pushButton_3.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon41 = QIcon()
        icon41.addFile(u":/Mediacuts/icons/mediacuts/icons8-legendas-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon41)
        self.pushButton_3.setIconSize(QSize(28, 23))

        self.gridLayout_63.addWidget(self.pushButton_3, 0, 1, 1, 1)


        self.gridLayout_64.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stackedWidget_4 = QCustomQStackedWidget(self.page_24)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.gridLayout_67 = QGridLayout(self.page_25)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.widget_3 = QWidget(self.page_25)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_65 = QGridLayout(self.widget_3)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.cc_font_button = QPushButton(self.widget_3)
        self.cc_font_button.setObjectName(u"cc_font_button")
        self.cc_font_button.setMinimumSize(QSize(0, 35))
        self.cc_font_button.setMaximumSize(QSize(16777215, 35))
        self.cc_font_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon42 = QIcon()
        icon42.addFile(u":/Mediacuts/icons/mediacuts/icons8-escolha-a-fonte-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cc_font_button.setIcon(icon42)

        self.gridLayout_65.addWidget(self.cc_font_button, 0, 1, 1, 1)

        self.cc_Color_button = QPushButton(self.widget_3)
        self.cc_Color_button.setObjectName(u"cc_Color_button")
        self.cc_Color_button.setMinimumSize(QSize(0, 35))
        self.cc_Color_button.setMaximumSize(QSize(16777215, 35))
        self.cc_Color_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon43 = QIcon()
        icon43.addFile(u":/Mediacuts/icons/mediacuts/icons8-cor-de-preenchimento-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cc_Color_button.setIcon(icon43)

        self.gridLayout_65.addWidget(self.cc_Color_button, 0, 0, 1, 1)

        self.cc_Fontsize_button = QPushButton(self.widget_3)
        self.cc_Fontsize_button.setObjectName(u"cc_Fontsize_button")
        self.cc_Fontsize_button.setMinimumSize(QSize(0, 35))
        self.cc_Fontsize_button.setMaximumSize(QSize(16777215, 35))
        self.cc_Fontsize_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon44 = QIcon()
        icon44.addFile(u":/Mediacuts/icons/mediacuts/icons8-altura-do-texto-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.cc_Fontsize_button.setIcon(icon44)

        self.gridLayout_65.addWidget(self.cc_Fontsize_button, 0, 2, 1, 1)

        self.CC_slignment_button = QPushButton(self.widget_3)
        self.CC_slignment_button.setObjectName(u"CC_slignment_button")
        self.CC_slignment_button.setMinimumSize(QSize(0, 35))
        self.CC_slignment_button.setMaximumSize(QSize(16777215, 35))
        self.CC_slignment_button.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon45 = QIcon()
        icon45.addFile(u":/Mediacuts/icons/mediacuts/icons8-alinhar-\u00e0-direita-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CC_slignment_button.setIcon(icon45)

        self.gridLayout_65.addWidget(self.CC_slignment_button, 0, 3, 1, 1)


        self.gridLayout_67.addWidget(self.widget_3, 0, 0, 1, 1)

        self.stackedWidget_5 = QCustomQStackedWidget(self.page_25)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.stackedWidget_5.setStyleSheet(u"QScrollArea {\n"
"    background-color: #F7F7F7; /* Fundo da \u00e1rea de rolagem */\n"
"    border: 1px solid #E0E0E0; /* Borda da \u00e1rea */\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem vertical */\n"
"    width: 12px; /* Largura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollArea QScrollBar:horizontal {\n"
"    background: #EDEDED; /* Fundo da barra de rolagem horizontal */\n"
"    height: 12px; /* Altura da barra */\n"
"    border: 1px solid #E0E0E0; /* Borda da barra */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem entre a barra e o conte\u00fado */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #DCDCDC; /* Cor do manipulador (parte m"
                        "\u00f3vel) */\n"
"    border-radius: 6px; /* Borda arredondada */\n"
"    margin: 2px; /* Margem interna */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background: #C0C0C0; /* Cor do manipulador ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #A0A0A0; /* Cor do manipulador ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: #F7F7F7; /* Fundo dos bot\u00f5es de incremento/decremento */\n"
"    border: 1px solid #E0E0E0; /* Borda dos bot\u00f5es */\n"
"    width: 10px; /* Largura dos bot\u00f5es */\n"
"    height: 10px; /* Altura dos bot\u00f5es */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QScrollBar::add-line:hover, QScrollBar::sub-line:hover {\n"
"    background: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed {\n"
"    background: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QScrollBar::add-page, Q"
                        "ScrollBar::sub-page {\n"
"    background: none; /* Fundo das \u00e1reas n\u00e3o utilizadas */\n"
"}\n"
"")
        self.page_27 = QWidget()
        self.page_27.setObjectName(u"page_27")
        self.gridLayout_80 = QGridLayout(self.page_27)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.scrollArea_2 = QScrollArea(self.page_27)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy10)
        self.scrollArea_2.setFrameShape(QFrame.VLine)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 505, 1103))
        self.gridLayout_57 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_56 = QGridLayout()
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setHorizontalSpacing(17)
        self.gridLayout_56.setVerticalSpacing(16)
        self.gridLayout_56.setContentsMargins(2, 10, 4, 8)
        self.button_green_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_green_cc.setObjectName(u"button_green_cc")
        self.button_green_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_green_cc, 9, 2, 1, 1)

        self.button_gray_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_gray_cc.setObjectName(u"button_gray_cc")
        self.button_gray_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_gray_cc, 9, 0, 1, 1)

        self.button_gold_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_gold_cc.setObjectName(u"button_gold_cc")
        self.button_gold_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_gold_cc, 6, 8, 1, 1)

        self.button_khaki_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_khaki_cc.setObjectName(u"button_khaki_cc")
        self.button_khaki_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_khaki_cc, 9, 6, 1, 1)

        self.line_55 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.HLine)
        self.line_55.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_55, 22, 6, 1, 1)

        self.button_lavender_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_lavender_cc.setObjectName(u"button_lavender_cc")
        self.button_lavender_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_lavender_cc, 9, 8, 1, 1)

        self.button_indigo_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_indigo_cc.setObjectName(u"button_indigo_cc")
        self.button_indigo_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_indigo_cc, 9, 4, 1, 1)

        self.line_26 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_26, 7, 8, 1, 1)

        self.line_25 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_25, 7, 6, 1, 1)

        self.line_24 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_24, 7, 4, 1, 1)

        self.line_23 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_23, 7, 2, 1, 1)

        self.line_27 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_27, 7, 0, 1, 1)

        self.line_11 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_11, 0, 1, 1, 1)

        self.line_57 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.HLine)
        self.line_57.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_57, 22, 4, 1, 1)

        self.line_13 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_13, 0, 5, 1, 1)

        self.line_12 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_12, 0, 3, 1, 1)

        self.button_sky_blue_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_sky_blue_cc.setObjectName(u"button_sky_blue_cc")
        self.button_sky_blue_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_sky_blue_cc, 23, 0, 1, 1)

        self.button_turquoise_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_turquoise_cc.setObjectName(u"button_turquoise_cc")
        self.button_turquoise_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_turquoise_cc, 23, 4, 1, 1)

        self.button_pink_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_pink_cc.setObjectName(u"button_pink_cc")
        self.button_pink_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_pink_cc, 16, 8, 1, 1)

        self.button_teal_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_teal_cc.setObjectName(u"button_teal_cc")
        self.button_teal_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_teal_cc, 23, 2, 1, 1)

        self.button_yellow_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_yellow_cc.setObjectName(u"button_yellow_cc")
        self.button_yellow_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_yellow_cc, 26, 0, 1, 1)

        self.button_white_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_white_cc.setObjectName(u"button_white_cc")
        self.button_white_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_white_cc, 23, 8, 1, 1)

        self.button_violet_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_violet_cc.setObjectName(u"button_violet_cc")
        self.button_violet_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_violet_cc, 23, 6, 1, 1)

        self.line_50 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.HLine)
        self.line_50.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_50, 17, 2, 1, 1)

        self.button_orange_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_orange_cc.setObjectName(u"button_orange_cc")
        self.button_orange_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_orange_cc, 16, 4, 1, 1)

        self.button_peach_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_peach_cc.setObjectName(u"button_peach_cc")
        self.button_peach_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_peach_cc, 16, 6, 1, 1)

        self.line_45 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.HLine)
        self.line_45.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_45, 14, 6, 1, 1)

        self.button_light_blue_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_light_blue_cc.setObjectName(u"button_light_blue_cc")
        self.button_light_blue_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_light_blue_cc, 13, 0, 1, 1)

        self.line_48 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.HLine)
        self.line_48.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_48, 17, 8, 1, 1)

        self.button_salmon_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_salmon_cc.setObjectName(u"button_salmon_cc")
        self.button_salmon_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_salmon_cc, 19, 6, 1, 1)

        self.button_light_gray_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_light_gray_cc.setObjectName(u"button_light_gray_cc")
        self.button_light_gray_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_light_gray_cc, 13, 2, 1, 1)

        self.button_purple_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_purple_cc.setObjectName(u"button_purple_cc")
        self.button_purple_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_purple_cc, 19, 0, 1, 1)

        self.button_royal_blue_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_royal_blue_cc.setObjectName(u"button_royal_blue_cc")
        self.button_royal_blue_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_royal_blue_cc, 19, 4, 1, 1)

        self.button_magenta_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_magenta_cc.setObjectName(u"button_magenta_cc")
        self.button_magenta_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_magenta_cc, 13, 8, 1, 1)

        self.button_olive_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_olive_cc.setObjectName(u"button_olive_cc")
        self.button_olive_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_olive_cc, 16, 2, 1, 1)

        self.button_lime_green_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_lime_green_cc.setObjectName(u"button_lime_green_cc")
        self.button_lime_green_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_lime_green_cc, 13, 6, 1, 1)

        self.button_light_pink_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_light_pink_cc.setObjectName(u"button_light_pink_cc")
        self.button_light_pink_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_light_pink_cc, 13, 4, 1, 1)

        self.button_red_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_red_cc.setObjectName(u"button_red_cc")
        self.button_red_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_red_cc, 19, 2, 1, 1)

        self.button_navy_blue_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_navy_blue_cc.setObjectName(u"button_navy_blue_cc")
        self.button_navy_blue_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_navy_blue_cc, 16, 0, 1, 1)

        self.line_44 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.HLine)
        self.line_44.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_44, 14, 8, 1, 1)

        self.button_silver_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_silver_cc.setObjectName(u"button_silver_cc")
        self.button_silver_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_silver_cc, 19, 8, 1, 1)

        self.line_43 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.HLine)
        self.line_43.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_43, 14, 4, 1, 1)

        self.line_37 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.VLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_37, 11, 1, 1, 1)

        self.line_35 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.VLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_35, 8, 3, 1, 1)

        self.line_38 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.VLine)
        self.line_38.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_38, 11, 3, 1, 1)

        self.line_51 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.HLine)
        self.line_51.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_51, 17, 0, 1, 1)

        self.line_34 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.VLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_34, 8, 7, 1, 1)

        self.line_33 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.VLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_33, 8, 5, 1, 1)

        self.line_40 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.VLine)
        self.line_40.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_40, 11, 7, 1, 1)

        self.line_39 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.VLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_39, 11, 5, 1, 1)

        self.line_36 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.VLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_36, 8, 1, 1, 1)

        self.line_59 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.HLine)
        self.line_59.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_59, 22, 0, 1, 1)

        self.line_29 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_29, 10, 2, 1, 1)

        self.line_47 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.HLine)
        self.line_47.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_47, 17, 4, 1, 1)

        self.line_30 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_30, 10, 4, 1, 1)

        self.line_28 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_28, 10, 0, 1, 1)

        self.line_41 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.HLine)
        self.line_41.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_41, 14, 2, 1, 1)

        self.line_32 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_32, 10, 8, 1, 1)

        self.line_56 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.HLine)
        self.line_56.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_56, 22, 8, 1, 1)

        self.line_31 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_31, 10, 6, 1, 1)

        self.line_60 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.HLine)
        self.line_60.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_60, 24, 0, 1, 1)

        self.line_46 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.HLine)
        self.line_46.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_46, 17, 6, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_6, 20, 0, 1, 1)

        self.line_42 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.HLine)
        self.line_42.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_42, 14, 0, 1, 1)

        self.line_61 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_61, 27, 0, 1, 1)

        self.line_49 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.HLine)
        self.line_49.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_49, 20, 2, 1, 1)

        self.line_53 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShape(QFrame.HLine)
        self.line_53.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_53, 20, 6, 1, 1)

        self.line_54 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.HLine)
        self.line_54.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_54, 20, 8, 1, 1)

        self.line_58 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.HLine)
        self.line_58.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_58, 22, 2, 1, 1)

        self.line_52 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShape(QFrame.HLine)
        self.line_52.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_52, 20, 4, 1, 1)

        self.line_18 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_18, 4, 8, 1, 1)

        self.line_15 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_15, 4, 2, 1, 1)

        self.line_16 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_16, 4, 4, 1, 1)

        self.line_17 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_17, 4, 6, 1, 1)

        self.line_22 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.VLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_22, 5, 1, 1, 1)

        self.line_20 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_20, 5, 5, 1, 1)

        self.line_19 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.VLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_19, 5, 7, 1, 1)

        self.line_21 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.VLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_21, 5, 3, 1, 1)

        self.line_14 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_14, 4, 0, 1, 1)

        self.label_105 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(50, 50))
        self.label_105.setMaximumSize(QSize(50, 50))
        self.label_105.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_aquaA.gif"))
        self.label_105.setScaledContents(True)
        self.label_105.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_56.addWidget(self.label_105, 0, 0, 1, 1)

        self.label_287 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setMinimumSize(QSize(50, 50))
        self.label_287.setMaximumSize(QSize(50, 50))
        self.label_287.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_dark blue.gif"))

        self.gridLayout_56.addWidget(self.label_287, 5, 0, 1, 1)

        self.line_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_56.addWidget(self.line_7, 0, 7, 1, 1)

        self.label_302 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_302.setObjectName(u"label_302")
        self.label_302.setMinimumSize(QSize(50, 50))
        self.label_302.setMaximumSize(QSize(50, 50))
        self.label_302.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_sky blue.png"))
        self.label_302.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_302, 21, 0, 1, 1)

        self.label_288 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setMinimumSize(QSize(50, 50))
        self.label_288.setMaximumSize(QSize(50, 50))
        self.label_288.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_gray.gif"))
        self.label_288.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_288, 8, 0, 1, 1)

        self.label_290 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setMinimumSize(QSize(50, 50))
        self.label_290.setMaximumSize(QSize(50, 50))
        self.label_290.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_navy blue.png"))
        self.label_290.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_290, 15, 0, 1, 1)

        self.label_291 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setMinimumSize(QSize(50, 50))
        self.label_291.setMaximumSize(QSize(50, 50))
        self.label_291.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_purple.gif"))
        self.label_291.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_291, 18, 0, 1, 1)

        self.label_303 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_303.setObjectName(u"label_303")
        self.label_303.setMinimumSize(QSize(50, 50))
        self.label_303.setMaximumSize(QSize(50, 50))
        self.label_303.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_yellow.gif"))
        self.label_303.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_303, 25, 0, 1, 1)

        self.label_289 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setMinimumSize(QSize(50, 50))
        self.label_289.setMaximumSize(QSize(50, 50))
        self.label_289.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_light blue.gif"))
        self.label_289.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_289, 11, 0, 1, 1)

        self.label_346 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_346.setObjectName(u"label_346")
        self.label_346.setMinimumSize(QSize(50, 50))
        self.label_346.setMaximumSize(QSize(50, 50))
        self.label_346.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_turquoise.gif"))
        self.label_346.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_346, 21, 4, 1, 1)

        self.button_aqua_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_aqua_cc.setObjectName(u"button_aqua_cc")
        self.button_aqua_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_aqua_cc, 1, 0, 1, 1)

        self.label_355 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_355.setObjectName(u"label_355")
        self.label_355.setMinimumSize(QSize(50, 50))
        self.label_355.setMaximumSize(QSize(50, 50))
        self.label_355.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_white.gif"))
        self.label_355.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_355, 21, 8, 1, 1)

        self.label_357 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_357.setObjectName(u"label_357")
        self.label_357.setMinimumSize(QSize(50, 50))
        self.label_357.setMaximumSize(QSize(50, 50))
        self.label_357.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_violet.gif"))
        self.label_357.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_357, 21, 6, 1, 1)

        self.button_coral_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_coral_cc.setObjectName(u"button_coral_cc")
        self.button_coral_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_coral_cc, 1, 6, 1, 1)

        self.button_blue_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_blue_cc.setObjectName(u"button_blue_cc")
        self.button_blue_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_blue_cc, 1, 2, 1, 1)

        self.button_brown_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_brown_cc.setObjectName(u"button_brown_cc")
        self.button_brown_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_brown_cc, 1, 4, 1, 1)

        self.button_dark_red_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_dark_red_cc.setObjectName(u"button_dark_red_cc")
        self.button_dark_red_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_dark_red_cc, 6, 4, 1, 1)

        self.button_cyan_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_cyan_cc.setObjectName(u"button_cyan_cc")
        self.button_cyan_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_cyan_cc, 1, 8, 1, 1)

        self.button_dark_green_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_dark_green_cc.setObjectName(u"button_dark_green_cc")
        self.button_dark_green_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_dark_green_cc, 6, 2, 1, 1)

        self.button_dark_blue_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_dark_blue_cc.setObjectName(u"button_dark_blue_cc")
        self.button_dark_blue_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_dark_blue_cc, 6, 0, 1, 1)

        self.button_forest_green_cc = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_forest_green_cc.setObjectName(u"button_forest_green_cc")
        self.button_forest_green_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_56.addWidget(self.button_forest_green_cc, 6, 6, 1, 1)

        self.label_307 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_307.setObjectName(u"label_307")
        self.label_307.setMinimumSize(QSize(50, 50))
        self.label_307.setMaximumSize(QSize(50, 50))
        self.label_307.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_cyan.gif"))
        self.label_307.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_307, 0, 8, 1, 1)

        self.label_305 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_305.setObjectName(u"label_305")
        self.label_305.setMinimumSize(QSize(50, 50))
        self.label_305.setMaximumSize(QSize(50, 50))
        self.label_305.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_brown.gif"))
        self.label_305.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_305, 0, 4, 1, 1)

        self.label_308 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_308.setObjectName(u"label_308")
        self.label_308.setMinimumSize(QSize(50, 50))
        self.label_308.setMaximumSize(QSize(50, 50))
        self.label_308.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_dark green.png"))
        self.label_308.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_308, 5, 2, 1, 1)

        self.label_306 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_306.setObjectName(u"label_306")
        self.label_306.setMinimumSize(QSize(50, 50))
        self.label_306.setMaximumSize(QSize(50, 50))
        self.label_306.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_coral.gif"))
        self.label_306.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_306, 0, 6, 1, 1)

        self.label_320 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_320.setObjectName(u"label_320")
        self.label_320.setMinimumSize(QSize(50, 50))
        self.label_320.setMaximumSize(QSize(50, 50))
        self.label_320.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_forest green.gif"))
        self.label_320.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_320, 5, 6, 1, 1)

        self.label_329 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_329.setObjectName(u"label_329")
        self.label_329.setMinimumSize(QSize(50, 50))
        self.label_329.setMaximumSize(QSize(50, 50))
        self.label_329.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_indigo.gif"))
        self.label_329.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_329, 8, 4, 1, 1)

        self.label_326 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_326.setObjectName(u"label_326")
        self.label_326.setMinimumSize(QSize(50, 50))
        self.label_326.setMaximumSize(QSize(50, 50))
        self.label_326.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_gold.gif"))
        self.label_326.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_326, 5, 8, 1, 1)

        self.label_327 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_327.setObjectName(u"label_327")
        self.label_327.setMinimumSize(QSize(50, 50))
        self.label_327.setMaximumSize(QSize(50, 50))
        self.label_327.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_green.gif"))
        self.label_327.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_327, 8, 2, 1, 1)

        self.label_319 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_319.setObjectName(u"label_319")
        self.label_319.setMinimumSize(QSize(50, 50))
        self.label_319.setMaximumSize(QSize(50, 50))
        self.label_319.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_dark red.gif"))
        self.label_319.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_319, 5, 4, 1, 1)

        self.label_334 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_334.setObjectName(u"label_334")
        self.label_334.setMinimumSize(QSize(50, 50))
        self.label_334.setMaximumSize(QSize(50, 50))
        self.label_334.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_light pink.gif"))
        self.label_334.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_334, 11, 4, 1, 1)

        self.label_331 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_331.setObjectName(u"label_331")
        self.label_331.setMinimumSize(QSize(50, 50))
        self.label_331.setMaximumSize(QSize(50, 50))
        self.label_331.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_lavender.gif"))
        self.label_331.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_331, 8, 8, 1, 1)

        self.label_330 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_330.setObjectName(u"label_330")
        self.label_330.setMinimumSize(QSize(50, 50))
        self.label_330.setMaximumSize(QSize(50, 50))
        self.label_330.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_khaki.gif"))
        self.label_330.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_330, 8, 6, 1, 1)

        self.label_333 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_333.setObjectName(u"label_333")
        self.label_333.setMinimumSize(QSize(50, 50))
        self.label_333.setMaximumSize(QSize(50, 50))
        self.label_333.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_light gray.gif"))
        self.label_333.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_333, 11, 2, 1, 1)

        self.label_335 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_335.setObjectName(u"label_335")
        self.label_335.setMinimumSize(QSize(50, 50))
        self.label_335.setMaximumSize(QSize(50, 50))
        self.label_335.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_magenta.gif"))
        self.label_335.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_335, 11, 8, 1, 1)

        self.label_336 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_336.setObjectName(u"label_336")
        self.label_336.setMinimumSize(QSize(50, 50))
        self.label_336.setMaximumSize(QSize(50, 50))
        self.label_336.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_lime green.gif"))
        self.label_336.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_336, 11, 6, 1, 1)

        self.label_338 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_338.setObjectName(u"label_338")
        self.label_338.setMinimumSize(QSize(50, 50))
        self.label_338.setMaximumSize(QSize(50, 50))
        self.label_338.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_orange.gif"))
        self.label_338.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_338, 15, 4, 1, 1)

        self.label_337 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_337.setObjectName(u"label_337")
        self.label_337.setMinimumSize(QSize(50, 50))
        self.label_337.setMaximumSize(QSize(50, 50))
        self.label_337.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_olive.gif"))
        self.label_337.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_337, 15, 2, 1, 1)

        self.label_343 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_343.setObjectName(u"label_343")
        self.label_343.setMinimumSize(QSize(50, 50))
        self.label_343.setMaximumSize(QSize(50, 50))
        self.label_343.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_silver.gif"))
        self.label_343.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_343, 18, 8, 1, 1)

        self.label_340 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_340.setObjectName(u"label_340")
        self.label_340.setMinimumSize(QSize(50, 50))
        self.label_340.setMaximumSize(QSize(50, 50))
        self.label_340.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_pink.gif"))
        self.label_340.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_340, 15, 8, 1, 1)

        self.label_339 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_339.setObjectName(u"label_339")
        self.label_339.setMinimumSize(QSize(50, 50))
        self.label_339.setMaximumSize(QSize(50, 50))
        self.label_339.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_peach.gif"))
        self.label_339.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_339, 15, 6, 1, 1)

        self.label_341 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_341.setObjectName(u"label_341")
        self.label_341.setMinimumSize(QSize(50, 50))
        self.label_341.setMaximumSize(QSize(50, 50))
        self.label_341.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_dark red.gif"))
        self.label_341.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_341, 18, 2, 1, 1)

        self.label_304 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_304.setObjectName(u"label_304")
        self.label_304.setMinimumSize(QSize(50, 50))
        self.label_304.setMaximumSize(QSize(50, 50))
        self.label_304.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_blue.gif"))
        self.label_304.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_304, 0, 2, 1, 1)

        self.label_344 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_344.setObjectName(u"label_344")
        self.label_344.setMinimumSize(QSize(50, 50))
        self.label_344.setMaximumSize(QSize(50, 50))
        self.label_344.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_salmon.gif"))
        self.label_344.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_344, 18, 6, 1, 1)

        self.label_342 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_342.setObjectName(u"label_342")
        self.label_342.setMinimumSize(QSize(50, 50))
        self.label_342.setMaximumSize(QSize(50, 50))
        self.label_342.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_royal blue.gif"))
        self.label_342.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_342, 18, 4, 1, 1)

        self.label_345 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_345.setObjectName(u"label_345")
        self.label_345.setMinimumSize(QSize(50, 50))
        self.label_345.setMaximumSize(QSize(50, 50))
        self.label_345.setPixmap(QPixmap(u":/legendascc/icons/gifs/legendascc/legendas_teal.gif"))
        self.label_345.setScaledContents(True)

        self.gridLayout_56.addWidget(self.label_345, 21, 2, 1, 1)


        self.gridLayout_57.addLayout(self.gridLayout_56, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_80.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget_5.addWidget(self.page_27)
        self.page_28 = QWidget()
        self.page_28.setObjectName(u"page_28")
        self.gridLayout_79 = QGridLayout(self.page_28)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.scrollArea_3 = QScrollArea(self.page_28)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.VLine)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 414, 589))
        self.gridLayout_33 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(13)
        self.gridLayout_32.setVerticalSpacing(64)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_111 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(81, 51))
        self.label_111.setMaximumSize(QSize(81, 51))
        self.label_111.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Century Gothic.gif"))
        self.label_111.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_111, 2, 1, 1, 1)

        self.button_Comic_Sans_MS_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_Comic_Sans_MS_cc.setObjectName(u"button_Comic_Sans_MS_cc")
        self.button_Comic_Sans_MS_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_Comic_Sans_MS_cc, 3, 2, 1, 1)

        self.label_112 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(81, 51))
        self.label_112.setMaximumSize(QSize(81, 51))
        self.label_112.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Comic Sans MS.gif"))
        self.label_112.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_112, 2, 2, 1, 1)

        self.button_CenturyGothic_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_CenturyGothic_cc.setObjectName(u"button_CenturyGothic_cc")
        self.button_CenturyGothic_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_CenturyGothic_cc, 3, 1, 1, 1)

        self.label_114 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(81, 51))
        self.label_114.setMaximumSize(QSize(81, 51))
        self.label_114.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Tahoma.gif"))
        self.label_114.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_114, 0, 0, 1, 1)

        self.button_Calibri_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_Calibri_cc.setObjectName(u"button_Calibri_cc")
        self.button_Calibri_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_Calibri_cc, 1, 2, 1, 1)

        self.button_LucidaConsole_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_LucidaConsole_cc.setObjectName(u"button_LucidaConsole_cc")
        self.button_LucidaConsole_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_LucidaConsole_cc, 1, 3, 1, 1)

        self.button_Tahoma_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_Tahoma_cc.setObjectName(u"button_Tahoma_cc")
        self.button_Tahoma_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_Tahoma_cc, 1, 0, 1, 1)

        self.label_107 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(81, 51))
        self.label_107.setMaximumSize(QSize(81, 51))
        self.label_107.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/fontname_Lucida Console.gif"))
        self.label_107.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_107, 0, 3, 1, 1)

        self.button_Impact_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_Impact_cc.setObjectName(u"button_Impact_cc")
        self.button_Impact_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_Impact_cc, 1, 1, 1, 1)

        self.label_110 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(81, 51))
        self.label_110.setMaximumSize(QSize(81, 51))
        self.label_110.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Calibri.gif"))
        self.label_110.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_110, 0, 2, 1, 1)

        self.label_109 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(81, 51))
        self.label_109.setMaximumSize(QSize(81, 51))
        self.label_109.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Impact.gif"))
        self.label_109.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_109, 0, 1, 1, 1)

        self.label_113 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(81, 51))
        self.label_113.setMaximumSize(QSize(81, 51))
        self.label_113.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Garamond.gif"))
        self.label_113.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_113, 2, 3, 1, 1)

        self.button_Garamond_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_Garamond_cc.setObjectName(u"button_Garamond_cc")
        self.button_Garamond_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_Garamond_cc, 3, 3, 1, 1)

        self.label_115 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(81, 51))
        self.label_115.setMaximumSize(QSize(81, 51))
        self.label_115.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/Trebuchet MS.gif"))
        self.label_115.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_115, 4, 0, 1, 1)

        self.label_108 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(81, 51))
        self.label_108.setMaximumSize(QSize(81, 51))
        self.label_108.setPixmap(QPixmap(u":/fontnamecc/icons/gifs/fontnamecc/fontname_Franklin Gothic.gif"))
        self.label_108.setScaledContents(True)

        self.gridLayout_32.addWidget(self.label_108, 2, 0, 1, 1)

        self.button_FranklinGothic_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_FranklinGothic_cc.setObjectName(u"button_FranklinGothic_cc")
        self.button_FranklinGothic_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_FranklinGothic_cc, 3, 0, 1, 1)

        self.button_Trebuchet_MS_cc = QPushButton(self.scrollAreaWidgetContents_3)
        self.button_Trebuchet_MS_cc.setObjectName(u"button_Trebuchet_MS_cc")
        self.button_Trebuchet_MS_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_32.addWidget(self.button_Trebuchet_MS_cc, 5, 0, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_32, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_79.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.stackedWidget_5.addWidget(self.page_28)
        self.page_31 = QWidget()
        self.page_31.setObjectName(u"page_31")
        self.gridLayout_78 = QGridLayout(self.page_31)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.label_97 = QLabel(self.page_31)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font1)

        self.gridLayout_78.addWidget(self.label_97, 0, 0, 1, 1)

        self.spin_fontsize_cc = QSpinBox(self.page_31)
        self.spin_fontsize_cc.setObjectName(u"spin_fontsize_cc")
        self.spin_fontsize_cc.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.spin_fontsize_cc.setValue(20)

        self.gridLayout_78.addWidget(self.spin_fontsize_cc, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 477, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_78.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.stackedWidget_5.addWidget(self.page_31)
        self.page_32 = QWidget()
        self.page_32.setObjectName(u"page_32")
        self.gridLayout_77 = QGridLayout(self.page_32)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.scrollArea_4 = QScrollArea(self.page_32)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.VLine)
        self.scrollArea_4.setFrameShadow(QFrame.Plain)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 281, 115))
        self.gridLayout_37 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_116 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(81, 51))
        self.label_116.setMaximumSize(QSize(81, 51))
        self.label_116.setPixmap(QPixmap(u":/Alignmentcc/icons/gifs/Alignmentcc/2.gif"))
        self.label_116.setScaledContents(True)

        self.gridLayout_36.addWidget(self.label_116, 0, 0, 1, 1)

        self.button_Alignment_2_cc = QPushButton(self.scrollAreaWidgetContents_4)
        self.button_Alignment_2_cc.setObjectName(u"button_Alignment_2_cc")
        self.button_Alignment_2_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_36.addWidget(self.button_Alignment_2_cc, 2, 0, 1, 1)

        self.button_Alignment_3_cc = QPushButton(self.scrollAreaWidgetContents_4)
        self.button_Alignment_3_cc.setObjectName(u"button_Alignment_3_cc")
        self.button_Alignment_3_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_36.addWidget(self.button_Alignment_3_cc, 2, 1, 1, 1)

        self.label_117 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(81, 51))
        self.label_117.setMaximumSize(QSize(81, 51))
        self.label_117.setPixmap(QPixmap(u":/Alignmentcc/icons/gifs/Alignmentcc/3.gif"))
        self.label_117.setScaledContents(True)

        self.gridLayout_36.addWidget(self.label_117, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_36.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.label_118 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(81, 51))
        self.label_118.setMaximumSize(QSize(81, 51))
        self.label_118.setPixmap(QPixmap(u":/Alignmentcc/icons/gifs/Alignmentcc/4.gif"))
        self.label_118.setScaledContents(True)

        self.gridLayout_36.addWidget(self.label_118, 0, 2, 1, 1)

        self.button_Alignment_4_cc = QPushButton(self.scrollAreaWidgetContents_4)
        self.button_Alignment_4_cc.setObjectName(u"button_Alignment_4_cc")
        self.button_Alignment_4_cc.setStyleSheet(u"    QPushButton {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #0000FF, stop:0.5 #800080, stop:1 #000000);  /* Gradiente de azul para roxo e preto */\n"
"        color: white;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                                    stop:0 #4B0082, stop:1 #000000);  /* Gradiente alterado no hover */\n"
"    }")

        self.gridLayout_36.addWidget(self.button_Alignment_4_cc, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)


        self.gridLayout_37.addLayout(self.gridLayout_36, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_77.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.stackedWidget_5.addWidget(self.page_32)

        self.gridLayout_67.addWidget(self.stackedWidget_5, 1, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page_25)
        self.page_26 = QWidget()
        self.page_26.setObjectName(u"page_26")
        self.gridLayout_69 = QGridLayout(self.page_26)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.widget_4 = QWidget(self.page_26)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_68 = QGridLayout(self.widget_4)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.cc_font_button_2 = QPushButton(self.widget_4)
        self.cc_font_button_2.setObjectName(u"cc_font_button_2")
        self.cc_font_button_2.setMinimumSize(QSize(0, 35))
        self.cc_font_button_2.setMaximumSize(QSize(16777215, 35))
        self.cc_font_button_2.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        self.cc_font_button_2.setIcon(icon42)

        self.gridLayout_68.addWidget(self.cc_font_button_2, 0, 1, 1, 1)

        self.cc_Color_button_2 = QPushButton(self.widget_4)
        self.cc_Color_button_2.setObjectName(u"cc_Color_button_2")
        self.cc_Color_button_2.setMinimumSize(QSize(0, 35))
        self.cc_Color_button_2.setMaximumSize(QSize(16777215, 35))
        self.cc_Color_button_2.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        self.cc_Color_button_2.setIcon(icon43)

        self.gridLayout_68.addWidget(self.cc_Color_button_2, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 35))
        self.pushButton_4.setMaximumSize(QSize(16777215, 35))
        self.pushButton_4.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 12px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"")
        icon46 = QIcon()
        icon46.addFile(u":/Mediacuts/icons/mediacuts/icons8-efeitos-visuais-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon46)

        self.gridLayout_68.addWidget(self.pushButton_4, 0, 2, 1, 1)


        self.gridLayout_69.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stackedWidget_6 = QCustomQStackedWidget(self.page_26)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.page_29 = QWidget()
        self.page_29.setObjectName(u"page_29")
        self.gridLayout_72 = QGridLayout(self.page_29)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.groupBox_4 = QGroupBox(self.page_29)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_71 = QGridLayout(self.groupBox_4)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_70 = QGridLayout()
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.comboBox_5 = QComboBox(self.groupBox_4)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.comboBox_5, 0, 1, 1, 1)

        self.comboBox_7 = QComboBox(self.groupBox_4)
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.comboBox_7, 2, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.groupBox_4)
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.comboBox_6, 1, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_70.addWidget(self.label_19, 0, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_70.addItem(self.verticalSpacer_14, 4, 0, 1, 1)

        self.comboBox_8 = QComboBox(self.groupBox_4)
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.comboBox_8, 3, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_70.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_70.addWidget(self.label_22, 2, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_4)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_70.addWidget(self.label_23, 3, 0, 1, 1)


        self.gridLayout_71.addLayout(self.gridLayout_70, 0, 0, 1, 1)


        self.gridLayout_72.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.stackedWidget_6.addWidget(self.page_29)
        self.page_30 = QWidget()
        self.page_30.setObjectName(u"page_30")
        self.gridLayout_75 = QGridLayout(self.page_30)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.groupBox_5 = QGroupBox(self.page_30)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_73 = QGridLayout(self.groupBox_5)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.verticalSpacer_15 = QSpacerItem(20, 363, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_73.addItem(self.verticalSpacer_15, 1, 0, 1, 1)

        self.gridLayout_74 = QGridLayout()
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.comboBox_13 = QComboBox(self.groupBox_5)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_74.addWidget(self.comboBox_13, 8, 0, 1, 1)

        self.comboBox_9 = QComboBox(self.groupBox_5)
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_74.addWidget(self.comboBox_9, 1, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_74.addWidget(self.label_25, 0, 1, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox_5)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.spinBox_8.setValue(8)

        self.gridLayout_74.addWidget(self.spinBox_8, 1, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_74.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_5)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_74.addWidget(self.label_27, 4, 0, 1, 1)

        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_74.addWidget(self.label_31, 7, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_5)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_74.addWidget(self.label_29, 0, 2, 1, 1)

        self.label_30 = QLabel(self.groupBox_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_74.addWidget(self.label_30, 7, 0, 1, 1)

        self.comboBox_11 = QComboBox(self.groupBox_5)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_74.addWidget(self.comboBox_11, 5, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox_5)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_74.addWidget(self.label_28, 4, 1, 1, 1)

        self.comboBox_12 = QComboBox(self.groupBox_5)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_74.addWidget(self.comboBox_12, 5, 1, 1, 1)

        self.comboBox_14 = QComboBox(self.groupBox_5)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_74.addWidget(self.comboBox_14, 8, 1, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox_5)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px; /* Borda arredondada */\n"
"    color: black; /* Cor do texto */\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F7F7F7; /* Fundo dos bot\u00f5es */\n"
"    border: 1px solid #E0E0E0;\n"
"    width: 16px; /* Largura dos bot\u00f5es */\n"
"    margin: 0;\n"
"    border-radius: 5px; /* Borda arredondada para os bot\u00f5es */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #EDEDED; /* Fundo dos bot\u00f5es ao passar o mouse */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #DCDCDC; /* Fundo dos bot\u00f5es ao pressionar */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpin"
                        "Box::down-arrow {\n"
"    width: 10px; /* Tamanho das setas */\n"
"    height: 10px;\n"
"    color: black; /* Cor das setas */\n"
"}\n"
"")
        self.spinBox_9.setValue(3)

        self.gridLayout_74.addWidget(self.spinBox_9, 1, 2, 1, 1)

        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_74.addWidget(self.label_26, 4, 2, 1, 1)

        self.comboBox_10 = QComboBox(self.groupBox_5)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_74.addWidget(self.comboBox_10, 5, 2, 1, 1)


        self.gridLayout_73.addLayout(self.gridLayout_74, 0, 0, 1, 1)


        self.gridLayout_75.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.stackedWidget_6.addWidget(self.page_30)
        self.page_35 = QWidget()
        self.page_35.setObjectName(u"page_35")
        self.gridLayout_82 = QGridLayout(self.page_35)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.gridLayout_76 = QGridLayout()
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.label_36 = QLabel(self.page_35)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setIndent(7)

        self.gridLayout_76.addWidget(self.label_36, 4, 1, 1, 1)

        self.label_33 = QLabel(self.page_35)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setIndent(7)

        self.gridLayout_76.addWidget(self.label_33, 4, 0, 1, 1)

        self.checkBox_5 = QCustomCheckBox(self.page_35)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_76.addWidget(self.checkBox_5, 3, 0, 1, 1)

        self.comboBox_16 = QComboBox(self.page_35)
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_76.addWidget(self.comboBox_16, 2, 1, 1, 1)

        self.label_34 = QLabel(self.page_35)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setIndent(6)

        self.gridLayout_76.addWidget(self.label_34, 1, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_76.addItem(self.verticalSpacer_16, 6, 0, 1, 2)

        self.label_35 = QLabel(self.page_35)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setIndent(7)

        self.gridLayout_76.addWidget(self.label_35, 1, 1, 1, 1)

        self.comboBox_15 = QComboBox(self.page_35)
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")
        self.comboBox_15.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_76.addWidget(self.comboBox_15, 2, 0, 1, 1)

        self.checkBox_2 = QCustomCheckBox(self.page_35)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_76.addWidget(self.checkBox_2, 0, 0, 1, 1)

        self.comboBox_17 = QComboBox(self.page_35)
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_76.addWidget(self.comboBox_17, 5, 0, 1, 1)

        self.comboBox_18 = QComboBox(self.page_35)
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 16px;  /* Tamanho da fonte */\n"
"    padding: 5px 10px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #EDEDED; /* Fundo ao passar o mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #DCDCDC; /* Fundo ao pressionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: black;\n"
"    border-radius: 10px;  /* Borda arredondada para a lista */\n"
"    font-size: 16px; /* Ajuste de fonte para itens */\n"
"}\n"
"")

        self.gridLayout_76.addWidget(self.comboBox_18, 5, 1, 1, 1)


        self.gridLayout_82.addLayout(self.gridLayout_76, 0, 0, 1, 1)

        self.stackedWidget_6.addWidget(self.page_35)

        self.gridLayout_69.addWidget(self.stackedWidget_6, 1, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page_26)

        self.gridLayout_64.addWidget(self.stackedWidget_4, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_24)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_7.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(18)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_8.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget_5.setCurrentIndex(1)
        self.stackedWidget_6.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.subcolor_button.setText(QCoreApplication.translate("MainWindow", u"Sub Color", None))
        self.subfont_button.setText(QCoreApplication.translate("MainWindow", u"Sub Font", None))
        self.subfontsizre_button.setText(QCoreApplication.translate("MainWindow", u"Sub Fontsize", None))
        self.subannimation_button.setText(QCoreApplication.translate("MainWindow", u"Sub Animation", None))
        self.subeffects_button.setText(QCoreApplication.translate("MainWindow", u"Sub Effects", None))
        self.CutingTIME_button.setText(QCoreApplication.translate("MainWindow", u"Cutting time", None))
        self.Hardware_button.setText(QCoreApplication.translate("MainWindow", u"Hardware", None))
        self.thread_button.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.subreference_button.setText(QCoreApplication.translate("MainWindow", u"Sub Reference", None))
        self.scale_button.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.RemovingWords.setText(QCoreApplication.translate("MainWindow", u"Removing Words", None))
        self.watermask_button.setText(QCoreApplication.translate("MainWindow", u"Watermark", None))
        self.AI_button.setText(QCoreApplication.translate("MainWindow", u"AI", None))
        self.upload_secn_button.setText(QCoreApplication.translate("MainWindow", u"Shortify Section", None))
        self.UploadMedia_base_button.setText(QCoreApplication.translate("MainWindow", u"Upload Media base", None))
        self.Start_media_Cuts.setText(QCoreApplication.translate("MainWindow", u"Start Media Cuts", None))
        self.Caption.setText(QCoreApplication.translate("MainWindow", u"Caption", None))
        self.close_window_button.setText("")
        self.restore_window_button.setText("")
        self.pushButton_5.setText("")
        self.minimize_window_button.setText("")
        self.Vertical_Preview.setText("")
        self.Horizontalpreview.setText("")
        self.pushButton.setText("")
        self.button_upload_video.setText(QCoreApplication.translate("MainWindow", u"Upload Media base to software", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Media base: N/A", None))
        self.label_119.setText("")
        self.button_Comic_Sans_MS_sub.setText(QCoreApplication.translate("MainWindow", u"Comic Sans MS", None))
        self.label_120.setText("")
        self.button_CenturyGothic_sub.setText(QCoreApplication.translate("MainWindow", u"Century Gothic", None))
        self.label_121.setText("")
        self.button_Calibri_sub.setText(QCoreApplication.translate("MainWindow", u"Calibri", None))
        self.button_LucidaConsole_sub.setText(QCoreApplication.translate("MainWindow", u"Lucida Console", None))
        self.button_Tahoma_sub.setText(QCoreApplication.translate("MainWindow", u"Tahoma", None))
        self.label_122.setText("")
        self.button_Impact_sub.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.label_123.setText("")
        self.label_124.setText("")
        self.label_125.setText("")
        self.button_Garamond_sub.setText(QCoreApplication.translate("MainWindow", u"Garamond", None))
        self.label_126.setText("")
        self.label_127.setText("")
        self.button_FranklinGothic_sub.setText(QCoreApplication.translate("MainWindow", u"Franklin Gothic", None))
        self.button_Trebuchet_MS_sub.setText(QCoreApplication.translate("MainWindow", u"Trebuchet MS", None))
        self.button_gold_sub.setText(QCoreApplication.translate("MainWindow", u"gold", None))
        self.button_gray_sub.setText(QCoreApplication.translate("MainWindow", u"gray", None))
        self.button_green_sub.setText(QCoreApplication.translate("MainWindow", u"green", None))
        self.button_indigo_sub.setText(QCoreApplication.translate("MainWindow", u"indigo", None))
        self.button_khaki_sub.setText(QCoreApplication.translate("MainWindow", u"khaki", None))
        self.button_lavender_sub.setText(QCoreApplication.translate("MainWindow", u"lavender", None))
        self.button_sky_blue_sub.setText(QCoreApplication.translate("MainWindow", u"sky blue", None))
        self.button_pink_sub.setText(QCoreApplication.translate("MainWindow", u"pink", None))
        self.button_teal_sub.setText(QCoreApplication.translate("MainWindow", u"teal", None))
        self.button_turquoise_sub.setText(QCoreApplication.translate("MainWindow", u"turquoise", None))
        self.button_white_subb.setText(QCoreApplication.translate("MainWindow", u"white", None))
        self.button_violet_sub.setText(QCoreApplication.translate("MainWindow", u"violet", None))
        self.button_yellow_sub.setText(QCoreApplication.translate("MainWindow", u"yellow", None))
        self.button_orange_sub.setText(QCoreApplication.translate("MainWindow", u"orange", None))
        self.button_peach_sub.setText(QCoreApplication.translate("MainWindow", u"peach", None))
        self.button_light_blue_sub.setText(QCoreApplication.translate("MainWindow", u"light blue", None))
        self.button_light_gray_sub.setText(QCoreApplication.translate("MainWindow", u"light gray", None))
        self.button_salmon_sub.setText(QCoreApplication.translate("MainWindow", u"salmon", None))
        self.button_royal_blue_sub.setText(QCoreApplication.translate("MainWindow", u"royal blue", None))
        self.button_magenta_sub.setText(QCoreApplication.translate("MainWindow", u"magenta", None))
        self.button_purple_sub.setText(QCoreApplication.translate("MainWindow", u"purple", None))
        self.button_light_pink_sub.setText(QCoreApplication.translate("MainWindow", u"light pink", None))
        self.button_lime_green_sub.setText(QCoreApplication.translate("MainWindow", u"lime green", None))
        self.button_olive_sub.setText(QCoreApplication.translate("MainWindow", u"olive", None))
        self.button_red_sub.setText(QCoreApplication.translate("MainWindow", u"red", None))
        self.button_navy_blue_sub.setText(QCoreApplication.translate("MainWindow", u"navy blue", None))
        self.button_silver_sub.setText(QCoreApplication.translate("MainWindow", u"silver", None))
        self.label_106.setText("")
        self.label_292.setText("")
        self.label_293.setText("")
        self.label_309.setText("")
        self.label_294.setText("")
        self.label_295.setText("")
        self.label_296.setText("")
        self.label_310.setText("")
        self.label_347.setText("")
        self.label_356.setText("")
        self.label_358.setText("")
        self.button_aqua_sub.setText(QCoreApplication.translate("MainWindow", u"aqua", None))
        self.button_blue_sub.setText(QCoreApplication.translate("MainWindow", u"blue", None))
        self.button_brown_sub.setText(QCoreApplication.translate("MainWindow", u"brown", None))
        self.button_coral_sub.setText(QCoreApplication.translate("MainWindow", u"coral", None))
        self.button_cyan_sub.setText(QCoreApplication.translate("MainWindow", u"cyan", None))
        self.button_dark_green_sub.setText(QCoreApplication.translate("MainWindow", u"dark green", None))
        self.button_dark_blue_sub.setText(QCoreApplication.translate("MainWindow", u"dark blue", None))
        self.button_dark_red_sub.setText(QCoreApplication.translate("MainWindow", u"dark red", None))
        self.button_forest_green_sub.setText(QCoreApplication.translate("MainWindow", u"forest green", None))
        self.label_311.setText("")
        self.label_312.setText("")
        self.label_313.setText("")
        self.label_314.setText("")
        self.label_321.setText("")
        self.label_322.setText("")
        self.label_328.setText("")
        self.label_332.setText("")
        self.label_348.setText("")
        self.label_349.setText("")
        self.label_350.setText("")
        self.label_351.setText("")
        self.label_352.setText("")
        self.label_353.setText("")
        self.label_354.setText("")
        self.label_359.setText("")
        self.label_360.setText("")
        self.label_361.setText("")
        self.label_362.setText("")
        self.label_363.setText("")
        self.label_364.setText("")
        self.label_365.setText("")
        self.label_366.setText("")
        self.label_367.setText("")
        self.label_315.setText("")
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Subtitle Fontsize:", None))
        self.button_animation_Gradual_Blink_sub.setText(QCoreApplication.translate("MainWindow", u"Gradual Blink", None))
        self.button_animation_AppearDisappear_sub.setText(QCoreApplication.translate("MainWindow", u"Appear-Disappear", None))
        self.button_animation_StrobeEffect_sub.setText(QCoreApplication.translate("MainWindow", u"Strobe Effect", None))
        self.button_animation_Soft_Fade_In_Out_sub.setText(QCoreApplication.translate("MainWindow", u"Soft Fade-In-Out", None))
        self.button_animation_FadeInandHold_sub.setText(QCoreApplication.translate("MainWindow", u"Fade-In and Hold", None))
        self.button_animation_FadeOut_and_Hold_sub.setText(QCoreApplication.translate("MainWindow", u"Fade-Out and Hold", None))
        self.button_animation_PulseOut_sub.setText(QCoreApplication.translate("MainWindow", u"Pulse Out", None))
        self.button_animation_Pulse_sub.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.button_animation_SlowFadeIn_sub.setText(QCoreApplication.translate("MainWindow", u"Slow Fade-In", None))
        self.button_animation_FastBlink_sub.setText(QCoreApplication.translate("MainWindow", u"Fast Blink", None))
        self.button_animation_FadeIn_sub.setText(QCoreApplication.translate("MainWindow", u"Fade-In", None))
        self.button_animation_SlowFadeOut_sub.setText(QCoreApplication.translate("MainWindow", u"Slow Fade-Out", None))
        self.button_animation_BlinkingText_sub.setText(QCoreApplication.translate("MainWindow", u"Blinking Text", None))
        self.button_animation_QuickFadeOut_sub.setText(QCoreApplication.translate("MainWindow", u"Quick Fade-Out", None))
        self.button_animation_QuickFadeIn_sub.setText(QCoreApplication.translate("MainWindow", u"Quick Fade-In", None))
        self.button_animation_None_sub.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.button_GlowEffect_Shadow_sub.setText(QCoreApplication.translate("MainWindow", u"Glow Effect", None))
        self.button_effects_BoldShadow_sub.setText(QCoreApplication.translate("MainWindow", u"Bold Shadow", None))
        self.button_effects_DropShadow_sub.setText(QCoreApplication.translate("MainWindow", u"Drop Shadow", None))
        self.button_effects_DottedOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Dotted Outline", None))
        self.button_effects_NeonGlow_sub.setText(QCoreApplication.translate("MainWindow", u"Neon Glow", None))
        self.button_effects_InnerGlow_sub.setText(QCoreApplication.translate("MainWindow", u"Inner Glow", None))
        self.button_effects_HardGlow_sub.setText(QCoreApplication.translate("MainWindow", u"Hard Glow", None))
        self.button_effects_SoftShadow_sub.setText(QCoreApplication.translate("MainWindow", u"Soft Shadow", None))
        self.button_effects_WavyOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Wavy Outline", None))
        self.button_effects_BlurredShadow_sub.setText(QCoreApplication.translate("MainWindow", u"Blurred Shadow", None))
        self.button_effects_Emboss_sub.setText(QCoreApplication.translate("MainWindow", u"Emboss", None))
        self.button_effects_Outline_sub.setText(QCoreApplication.translate("MainWindow", u"Outline", None))
        self.button_effects_DoubleOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Double Outline", None))
        self.button_effects_TransparentOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Transparent Outline", None))
        self.button_effects_SoftGlow_sub.setText(QCoreApplication.translate("MainWindow", u"Soft Glow", None))
        self.button_effects_Shadow_sub.setText(QCoreApplication.translate("MainWindow", u"Shadow", None))
        self.button_effects_ThickOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Thick Outline", None))
        self.button_effects_None_sub.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"Subtitle Reference:", None))
        self.label_397.setText("")
        self.button_9_Thread.setText(QCoreApplication.translate("MainWindow", u"9 Thread", None))
        self.label_399.setText("")
        self.button_10_Thread.setText(QCoreApplication.translate("MainWindow", u"10 Thread", None))
        self.button_11_Thread.setText(QCoreApplication.translate("MainWindow", u"11 Thread", None))
        self.label_389.setText("")
        self.label_390.setText("")
        self.button_2_Thread.setText(QCoreApplication.translate("MainWindow", u"2 Thread", None))
        self.button_1_Thread.setText(QCoreApplication.translate("MainWindow", u"1 Thread", None))
        self.button_4_Thread.setText(QCoreApplication.translate("MainWindow", u"4 Thread", None))
        self.label_400.setText("")
        self.label_392.setText("")
        self.button_5_Thread.setText(QCoreApplication.translate("MainWindow", u"5 Thread", None))
        self.button_3_Thread.setText(QCoreApplication.translate("MainWindow", u"3 Thread", None))
        self.label_398.setText("")
        self.label_393.setText("")
        self.button_7_Thread.setText(QCoreApplication.translate("MainWindow", u"7 Thread", None))
        self.label_394.setText("")
        self.label_395.setText("")
        self.button_8_Thread.setText(QCoreApplication.translate("MainWindow", u"8 Thread", None))
        self.button_6_Thread.setText(QCoreApplication.translate("MainWindow", u"6 Thread", None))
        self.label_396.setText("")
        self.label_391.setText("")
        self.button_whisper_tiny.setText(QCoreApplication.translate("MainWindow", u"whisper tiny", None))
        self.button_whisper_medium.setText(QCoreApplication.translate("MainWindow", u"whisper medium", None))
        self.label_402.setText("")
        self.button_whisper_base.setText(QCoreApplication.translate("MainWindow", u"whisper base", None))
        self.button_whisper_small.setText(QCoreApplication.translate("MainWindow", u"whisper small", None))
        self.label_401.setText("")
        self.label_403.setText("")
        self.label_404.setText("")
        self.button_whisper_large.setText(QCoreApplication.translate("MainWindow", u"whisper large", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Model Description</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">tiny</span><span style=\" font-size:16px;\">:</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">"
                        "<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Size</span><span style=\" font-size:16px;\"> : 39 MB</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage</span><span style=\" font-size:16px;\"> : Ideal for applications that require maximum speed and have limited hardware requirements.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Accuracy</span><span style=\" font-size:16px;\"> : Less accurate for low-quality audio and overlapping voices.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage scenario</span><span style=\" font-size:16px;\"> : Mobile devices, fast transcriptions with less concern for accuracy.</span></li></ul>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">base</span><span style=\" font-size:16px;\">:</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Size</span><span style=\" font-size:16px;\"> : 74 MB</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage</span><span style=\" font-size:16px;\"> : Recommended for basic transcriptions, with a slightly better balance between accuracy and speed.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Accuracy</span><span style=\" font-size:16px;\"> : Better than </span><span style=\" font-family:'Courier New'; font-size:16px;\">tiny</span><span style=\" font-size:16px;\">, especially for clearer audio with less background noise.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage scenario</span><span style=\" font-size:16px;\"> : Applications on handheld devices, where accuracy is moderately important.</span></li></ul"
                        ">\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">small</span><span style=\" font-size:16px;\">:</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Size</span><span style=\" font-size:16px;\"> : 244 MB</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage</span><span style=\" font-size:16px;\"> : A balance between accuracy and speed, suitable for transcription tasks where quality needs to be reasonable.</span></li>\n"
"<li style"
                        "=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Accuracy</span><span style=\" font-size:16px;\"> : Good, covering most accents and nuances of speech.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage scenario</span><span style=\" font-size:16px;\"> : Mid-range GPU devices, projects with a good amount of diverse audio.</span></li></ul>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">medium</span><span style=\" font-size:16px;\">:</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><"
                        "li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Size</span><span style=\" font-size:16px;\"> : 769 MB</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage</span><span style=\" font-size:16px;\"> : High accuracy for more demanding transcription tasks.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Accuracy</span><span style=\" font-size:16px;\"> : Very high for a variety of speech scenarios and accents.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage scenario</span><span style=\" font-size:16px;\"> : Devices with more advanced GPU, designs that prioritize accuracy over speed.</span></li></ul>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">large</span><span style=\" font-size:16px;\">:</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Size</span><span style=\" font-size:16px;\"> : 1.55 GB</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-size:16px; font-weight:600;\">Usage</span><span style=\" font-size:16px;\"> : More accurate model, ideal for highly complex audio and where transcription needs to be as close as possible to natural speech.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Accuracy</span><span style=\" font-size:16px;\"> : Very high, with best performance for complex accents, different languages \u200b\u200band lower quality audio.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Usage scenario</span><span style=\" font-size:16px;\"> : High-end GPUs, projects that require the highest level of precision and detail.</span></li></ul></body></html>", None))
        self.label_409.setText("")
        self.label_408.setText("")
        self.button_Cutting60seconds.setText(QCoreApplication.translate("MainWindow", u"Cutting 60 seconds", None))
        self.button_Cutting90seconds.setText(QCoreApplication.translate("MainWindow", u"Cutting 90 seconds", None))
        self.button_Cutting120seconds.setText(QCoreApplication.translate("MainWindow", u"Cutting 120 seconds", None))
        self.button_Cutting160seconds.setText(QCoreApplication.translate("MainWindow", u"Cutting 160 seconds", None))
        self.button_Cutting260seconds.setText(QCoreApplication.translate("MainWindow", u"Cutting 260 seconds", None))
        self.label_405.setText("")
        self.label_407.setText("")
        self.label_406.setText("")
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">1. 60 seconds:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Duration</span><span style=\" font-size:16px;\"> : 1 minute.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Ideal for</span><span style=\" font-size:16px;\"> : Short, impactful videos like social media ads, Instagram Reels, TikToks, and Facebook Stories. Focus on a quick, to-the-point message.</span></li></ul>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2. 90 seconds:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Duration</span><span style=\" font-size:16px;\"> : 1 minute and 30 seconds.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Best for</span><span style=\" font-size:16px;\"> : Content that\u2019s a little more in-depth, like quick tutorials, short product demos, or marketing videos that need a little more time to explain an idea.</span></li></ul>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">3. 120 seconds:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Duration</span><span style=\" font-size:16px;\"> : 2 minutes.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Ideal for</span><span style=\" font-size:16px;\"> : Short explanatory or narrative videos, product presentations, event trailers, or introductions to longer content. Widely used in corporate videos or advertisements that seek to retain attention for longer.</span></li></ul>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">4. 160 seconds:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Duration</span><span style=\" font-size:16px;\"> : 2 minutes and 40 seconds.</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom"
                        ":12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Best for</span><span style=\" font-size:16px;\"> : Videos that detail a product or service, more elaborate stories, or more concise educational content. Good length for videos that seek to engage the viewer in a slightly longer narrative without exceeding their attention span.</span></li></ul>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">5. 260 seconds:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Duration</span><span style=\" font-size:16px;\"> : 4 minutes and 20 seconds.</span></"
                        "li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">Best for</span><span style=\" font-size:16px;\"> : Comprehensive, informative content, such as in-depth tutorials, vlogs, or event recaps. This length allows you more freedom to explore a topic or theme without rushing, while still focusing on keeping your audience\u2019s attention.</span></li></ul></body></html>", None))
        self.label_415.setText("")
        self.button_HwaccelCUDA.setText(QCoreApplication.translate("MainWindow", u"Hwaccel CUDA", None))
        self.label_410.setText("")
        self.button_HwaccelCPU.setText(QCoreApplication.translate("MainWindow", u"Hwaccel CPU", None))
        self.label_411.setText("")
        self.button_Vcodeclibx264.setText(QCoreApplication.translate("MainWindow", u"Vcodec libx264", None))
        self.label_416.setText("")
        self.button_Vcodech264_nvenc.setText(QCoreApplication.translate("MainWindow", u"Vcodec h264_nvenc", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Bitrate", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Maxrate", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Bufsize", None))
        self.button_Preset.setItemText(0, QCoreApplication.translate("MainWindow", u"medium", None))
        self.button_Preset.setItemText(1, QCoreApplication.translate("MainWindow", u"slow", None))
        self.button_Preset.setItemText(2, QCoreApplication.translate("MainWindow", u"slower", None))
        self.button_Preset.setItemText(3, QCoreApplication.translate("MainWindow", u"veryslow", None))
        self.button_Preset.setItemText(4, QCoreApplication.translate("MainWindow", u"placebo", None))

        self.button_gpu_or_cpu.setItemText(0, QCoreApplication.translate("MainWindow", u"gpu 0", None))
        self.button_gpu_or_cpu.setItemText(1, QCoreApplication.translate("MainWindow", u"cpu", None))

        self.label_168.setText(QCoreApplication.translate("MainWindow", u"gpu or cpu", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.button_Profile.setItemText(0, QCoreApplication.translate("MainWindow", u"high CUDA", None))
        self.button_Profile.setItemText(1, QCoreApplication.translate("MainWindow", u"high CPU", None))

        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Preset", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Hwaccel CPU</span><span style=\" font-size:8pt;\"> : Uses hardware acceleration, but using the CPU for video decoding. Typically used with codecs like </span><span style=\" font-family:'Courier New'; font-size:8pt;\">libx264</span><span style=\" font-size:8pt;\">or </span><span style=\" font-family:'Courier New'; font-size:8pt;\">libx265</span><span style=\" font-size:8pt;\">, without taking advantage of the GPU.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Hwaccel CUDA</span><span style=\" font-size:8pt;\"> : Uses hardware acceleration through the GPU, specifically with NVIDIA's CUDA API, to process and accelerate video decoding or encoding.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Vcodec h264_nvenc</span><span style=\" font-size:8pt;\"> : H.264 video codec that uses NVIDIA hardware acceleration (NVENC) for encoding, offloading the CPU and processing the video directly on the GPU.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Vcodec libx264</span><span style=\" font-size:8pt;\"> : H. 264 video codec that uses the CPU for encoding. is </span><span style=\" font-family:'Courier New'; font-si"
                        "ze:8pt;\">libx264</span><span style=\" font-size:8pt;\">a popular codec that supports a wide range of tweaks to control quality and performance.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Preset medium</span><span style=\" font-size:8pt;\"> : Sets the encoding speed to &quot;medium&quot; in the context of </span><span style=\" font-family:'Courier New'; font-size:8pt;\">libx264</span><span style=\" font-size:8pt;\">. It's a balance between speed and compression, ideal for many situations where you want decent quality without sacrificing too much performance.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Preset slow</span><span style=\" font-size:8pt;\"> : Sets the encoding speed to &quot;slow&quot;, prioritizing quality over speed"
                        ". Results in smaller, higher-quality files, but takes longer to encode.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Gpu 0</span><span style=\" font-size:8pt;\"> : Sets the GPU with index 0 to be used for hardware-accelerated video encoding or decoding (if more than one GPU is available).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Cpu</span><span style=\" font-size:8pt;\"> : Specifies that encoding/decoding should be performed by the CPU, rather than using hardware acceleration.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Profile CUDA high</span><span style=\" font-size:8pt;\"> : Uses the "
                        "&quot;high&quot; encoding profile for H.264 with CUDA acceleration, which means higher compression efficiency and support for higher resolutions and qualities.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Profile CPU</span><span style=\" font-size:8pt;\"> : Uses the default profile for H.264 video encoding on the CPU. Can be set to </span><span style=\" font-family:'Courier New'; font-size:8pt;\">baseline</span><span style=\" font-size:8pt;\">, </span><span style=\" font-family:'Courier New'; font-size:8pt;\">main</span><span style=\" font-size:8pt;\">, or </span><span style=\" font-family:'Courier New'; font-size:8pt;\">high</span><span style=\" font-size:8pt;\">, depending on compatibility and quality needs.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"
                        "8pt; font-weight:600;\">Bitrate</span><span style=\" font-size:8pt;\"> : Controls the output bitrate for encoding the video. Higher bitrates provide better quality, but result in larger files.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Maxrate</span><span style=\" font-size:8pt;\"> : Sets the maximum bitrate that can be used during encoding. This parameter is useful for limiting the size of data peaks in variable video encodings.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Bufsize</span><span style=\" font-size:8pt;\"> : Determines the buffer size for variable bit rate (VBR) encoding. This controls how much data can be temporarily stored to smooth out bit rate variations. A larger buffer allows for more flexible encoding.</span>"
                        "</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Scale width", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Scale height", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"scale", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Uniform scale", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Remove words", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Remove words in subtitles", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"llama3.2:1b", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"gpt-4o-mini", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"omni-latest", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Remove words in audio", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Select the model AI Moderation", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"llama3.2:3b", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"text-moderation-latest", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"omni-2024-09-26", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"word,word,word", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Add watermark", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Image Watermark", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.button_UploadWatermark.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Text Watermark", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Text:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"@cortesdofelquinhasss", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Opacity", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"FontSize", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"white", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"FontColor", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"FontName", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Overlay", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Top right", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Bottom left", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Bottom right", None))

        self.upload_refresh.setText("")
        self.SelectallAndroidDevice.setText("")
        self.RemoeallAndroidDevice.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Android Device:", None))
        self.Scheduledupload.setText(QCoreApplication.translate("MainWindow", u"Scheduled upload", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Cuts Upload Per Hour ", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Upload Per Day Per Acc", None))
        self.start_upload.setText(QCoreApplication.translate("MainWindow", u"Start Upload", None))
        self.ModesShortify.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Algoritimich Mode:", None))
        self.AlgoV1.setText(QCoreApplication.translate("MainWindow", u"Shortify V1", None))
        self.GetThreads.setText(QCoreApplication.translate("MainWindow", u"Algo Get Threads", None))
        self.Uploadyoutube_app.setText(QCoreApplication.translate("MainWindow", u"Youtube(App)", None))
        self.KwaiApp.setText(QCoreApplication.translate("MainWindow", u"Kwai(App)", None))
        self.TiktokApp.setText(QCoreApplication.translate("MainWindow", u"Tiktok(App)", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Add accounts", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Back to Select Acc", None))
        self.Tiktok_AddAcc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Acc in Tiktok", None))
        self.Day_AddAcc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"tuesday", None))
        self.ChannelYoutube_AddAcc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Youtube (bruninzor)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Time_AddAcc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"08:00:00", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tiktok(App)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Kwai(App)", None))
        self.Kwai_AddAcc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Acc in Kwai", None))
        self.Addacctoshortify_button.setText(QCoreApplication.translate("MainWindow", u"Add accounts to Shortify", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Back to Upload", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CC Type Srt", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"CC Type Ass", None))
        self.cc_font_button.setText(QCoreApplication.translate("MainWindow", u"CC Font", None))
        self.cc_Color_button.setText(QCoreApplication.translate("MainWindow", u"CC Color", None))
        self.cc_Fontsize_button.setText(QCoreApplication.translate("MainWindow", u"CC Fontsize", None))
        self.CC_slignment_button.setText(QCoreApplication.translate("MainWindow", u"CC Alignment", None))
        self.button_green_cc.setText(QCoreApplication.translate("MainWindow", u"green", None))
        self.button_gray_cc.setText(QCoreApplication.translate("MainWindow", u"gray", None))
        self.button_gold_cc.setText(QCoreApplication.translate("MainWindow", u"gold", None))
        self.button_khaki_cc.setText(QCoreApplication.translate("MainWindow", u"khaki", None))
        self.button_lavender_cc.setText(QCoreApplication.translate("MainWindow", u"lavender", None))
        self.button_indigo_cc.setText(QCoreApplication.translate("MainWindow", u"indigo", None))
        self.button_sky_blue_cc.setText(QCoreApplication.translate("MainWindow", u"sky blue", None))
        self.button_turquoise_cc.setText(QCoreApplication.translate("MainWindow", u"turquoise", None))
        self.button_pink_cc.setText(QCoreApplication.translate("MainWindow", u"pink", None))
        self.button_teal_cc.setText(QCoreApplication.translate("MainWindow", u"teal", None))
        self.button_yellow_cc.setText(QCoreApplication.translate("MainWindow", u"yellow", None))
        self.button_white_cc.setText(QCoreApplication.translate("MainWindow", u"white", None))
        self.button_violet_cc.setText(QCoreApplication.translate("MainWindow", u"violet", None))
        self.button_orange_cc.setText(QCoreApplication.translate("MainWindow", u"orange", None))
        self.button_peach_cc.setText(QCoreApplication.translate("MainWindow", u"peach", None))
        self.button_light_blue_cc.setText(QCoreApplication.translate("MainWindow", u"light blue", None))
        self.button_salmon_cc.setText(QCoreApplication.translate("MainWindow", u"salmon", None))
        self.button_light_gray_cc.setText(QCoreApplication.translate("MainWindow", u"light gray", None))
        self.button_purple_cc.setText(QCoreApplication.translate("MainWindow", u"purple", None))
        self.button_royal_blue_cc.setText(QCoreApplication.translate("MainWindow", u"royal blue", None))
        self.button_magenta_cc.setText(QCoreApplication.translate("MainWindow", u"magenta", None))
        self.button_olive_cc.setText(QCoreApplication.translate("MainWindow", u"olive", None))
        self.button_lime_green_cc.setText(QCoreApplication.translate("MainWindow", u"lime green", None))
        self.button_light_pink_cc.setText(QCoreApplication.translate("MainWindow", u"light pink", None))
        self.button_red_cc.setText(QCoreApplication.translate("MainWindow", u"red", None))
        self.button_navy_blue_cc.setText(QCoreApplication.translate("MainWindow", u"navy blue", None))
        self.button_silver_cc.setText(QCoreApplication.translate("MainWindow", u"silver", None))
        self.label_105.setText("")
        self.label_287.setText("")
        self.label_302.setText("")
        self.label_288.setText("")
        self.label_290.setText("")
        self.label_291.setText("")
        self.label_303.setText("")
        self.label_289.setText("")
        self.label_346.setText("")
        self.button_aqua_cc.setText(QCoreApplication.translate("MainWindow", u"aqua", None))
        self.label_355.setText("")
        self.label_357.setText("")
        self.button_coral_cc.setText(QCoreApplication.translate("MainWindow", u"coral", None))
        self.button_blue_cc.setText(QCoreApplication.translate("MainWindow", u"blue", None))
        self.button_brown_cc.setText(QCoreApplication.translate("MainWindow", u"brown", None))
        self.button_dark_red_cc.setText(QCoreApplication.translate("MainWindow", u"dark red", None))
        self.button_cyan_cc.setText(QCoreApplication.translate("MainWindow", u"cyan", None))
        self.button_dark_green_cc.setText(QCoreApplication.translate("MainWindow", u"dark green", None))
        self.button_dark_blue_cc.setText(QCoreApplication.translate("MainWindow", u"dark blue", None))
        self.button_forest_green_cc.setText(QCoreApplication.translate("MainWindow", u"forest green", None))
        self.label_307.setText("")
        self.label_305.setText("")
        self.label_308.setText("")
        self.label_306.setText("")
        self.label_320.setText("")
        self.label_329.setText("")
        self.label_326.setText("")
        self.label_327.setText("")
        self.label_319.setText("")
        self.label_334.setText("")
        self.label_331.setText("")
        self.label_330.setText("")
        self.label_333.setText("")
        self.label_335.setText("")
        self.label_336.setText("")
        self.label_338.setText("")
        self.label_337.setText("")
        self.label_343.setText("")
        self.label_340.setText("")
        self.label_339.setText("")
        self.label_341.setText("")
        self.label_304.setText("")
        self.label_344.setText("")
        self.label_342.setText("")
        self.label_345.setText("")
        self.label_111.setText("")
        self.button_Comic_Sans_MS_cc.setText(QCoreApplication.translate("MainWindow", u"Comic Sans MS", None))
        self.label_112.setText("")
        self.button_CenturyGothic_cc.setText(QCoreApplication.translate("MainWindow", u"Century Gothic", None))
        self.label_114.setText("")
        self.button_Calibri_cc.setText(QCoreApplication.translate("MainWindow", u"Calibri", None))
        self.button_LucidaConsole_cc.setText(QCoreApplication.translate("MainWindow", u"Lucida Console", None))
        self.button_Tahoma_cc.setText(QCoreApplication.translate("MainWindow", u"Tahoma", None))
        self.label_107.setText("")
        self.button_Impact_cc.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.label_110.setText("")
        self.label_109.setText("")
        self.label_113.setText("")
        self.button_Garamond_cc.setText(QCoreApplication.translate("MainWindow", u"Garamond", None))
        self.label_115.setText("")
        self.label_108.setText("")
        self.button_FranklinGothic_cc.setText(QCoreApplication.translate("MainWindow", u"Franklin Gothic", None))
        self.button_Trebuchet_MS_cc.setText(QCoreApplication.translate("MainWindow", u"Trebuchet MS", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Captions Fontsize:", None))
        self.label_116.setText("")
        self.button_Alignment_2_cc.setText(QCoreApplication.translate("MainWindow", u"Alignment 2", None))
        self.button_Alignment_3_cc.setText(QCoreApplication.translate("MainWindow", u"Alignment 3", None))
        self.label_117.setText("")
        self.label_118.setText("")
        self.button_Alignment_4_cc.setText(QCoreApplication.translate("MainWindow", u"Alignment 4", None))
        self.cc_font_button_2.setText(QCoreApplication.translate("MainWindow", u"CC Font", None))
        self.cc_Color_button_2.setText(QCoreApplication.translate("MainWindow", u"CC Color", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"CC Efects", None))
        self.groupBox_4.setTitle("")
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"&HC0C0C0", None))

        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"&H0", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"&H8080", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"PrimaryColour", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"&H0", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"SecondaryColour", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"OutlineColour", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"BackColour", None))
        self.groupBox_5.setTitle("")
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Future", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Fontsize", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Fontname", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Alignment", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Outline", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Shadow", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"False", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"True", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"False", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"True", None))

        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Final color", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Initial color", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Revelation effect", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"&HFFFFFF&", None))

        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Initial color", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Final color", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"&H00FFFF&", None))

        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"2 Color in Caption ", None))
        self.comboBox_17.setItemText(0, QCoreApplication.translate("MainWindow", u"&HCCCC33&", None))

        self.comboBox_18.setItemText(0, QCoreApplication.translate("MainWindow", u"&H0099FF&", None))

    # retranslateUi

