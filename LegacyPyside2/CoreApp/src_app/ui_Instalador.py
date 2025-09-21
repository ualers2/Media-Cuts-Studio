# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Instalador.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomQPushButton import QCustomQPushButton
from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_InstaladorSoftwareAI(object):
    def setupUi(self, InstaladorSoftwareAI):
        if not InstaladorSoftwareAI.objectName():
            InstaladorSoftwareAI.setObjectName(u"InstaladorSoftwareAI")
        InstaladorSoftwareAI.resize(518, 394)
        self.centralwidget = QWidget(InstaladorSoftwareAI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 500, 376))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_3 = QCustomQPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #4f4d4d; /* Cor de fundo */\n"
"    color: #2bab1a; /* Cor do texto */\n"
"    border: 2px solid #2bab1a; /* Cor da borda */\n"
"    border-radius: 8px; /* Borda arredondada */\n"
"    padding: 6px 12px; /* Espa\u00e7amento interno */\n"
"    font: bold 14px \"Arial\"; /* Estilo da fonte */\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 5, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setContentsMargins(-1, -1, -1, 2)
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(395, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.progressBar = QProgressBar(self.page_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_3.addWidget(self.progressBar, 3, 0, 1, 2)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 101))
        self.frame.setMaximumSize(QSize(16777215, 65))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: #2b2b2b; /* Cor de fundo escura */\n"
"    border: 1px solid #555555; /* Borda com um cinza mais claro */\n"
"    border-radius: 8px; /* Arredondamento dos cantos */\n"
"    padding: 10px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 1px solid #888888; /* Altera\u00e7\u00e3o da borda ao passar o mouse */\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(36)
        self.gridLayout_6.setVerticalSpacing(14)
        self.gridLayout_6.setContentsMargins(1, 0, 2, 4)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(438, 0))
        self.label_5.setMaximumSize(QSize(443, 16777215))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b; /* Fundo escuro */\n"
"    color: #f0f0f0; /* Texto claro para contraste */\n"
"    border: 1px solid #2b2b2b; /* Borda fina cinza escuro */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 5px; /* Espa\u00e7amento interno */\n"
"    font-family: \"Arial\"; /* Fonte personalizada */\n"
"    font-size: 14px; /* Tamanho da fonte */\n"
"    qproperty-alignment: 'AlignCenter'; /* Centraliza o texto no QLabel */\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 61))
        self.label_4.setMaximumSize(QSize(113, 61))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b; /* Fundo escuro */\n"
"    color: #2b2b2b; /* Texto claro para contraste */\n"
"    border: 1px solid #2b2b2b; /* Borda fina cinza escuro */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 5px; /* Espa\u00e7amento interno */\n"
"    font-family: \"Arial\"; /* Fonte personalizada */\n"
"    font-size: 14px; /* Tamanho da fonte */\n"
"    qproperty-alignment: 'AlignCenter'; /* Centraliza o texto no QLabel */\n"
"}\n"
"\n"
"\n"
"")
        self.label_4.setPixmap(QPixmap(u"../../Save disk C/Saas do site/Projetos de codigo aberto/SoftwareAI/logo.webp"))
        self.label_4.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_4, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        InstaladorSoftwareAI.setCentralWidget(self.centralwidget)

        self.retranslateUi(InstaladorSoftwareAI)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(InstaladorSoftwareAI)
    # setupUi

    def retranslateUi(self, InstaladorSoftwareAI):
        InstaladorSoftwareAI.setWindowTitle(QCoreApplication.translate("InstaladorSoftwareAI", u"Instalador SoftwareAI", None))
        self.pushButton_3.setText(QCoreApplication.translate("InstaladorSoftwareAI", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("InstaladorSoftwareAI", u"Aguarde enquanto o assistente de instala\u00e7\u00e3o trabalha", None))
        self.label_2.setText(QCoreApplication.translate("InstaladorSoftwareAI", u"Status:", None))
        self.label_3.setText(QCoreApplication.translate("InstaladorSoftwareAI", u"...", None))
        self.label_5.setText(QCoreApplication.translate("InstaladorSoftwareAI", u"Instalador SoftwareAI ", None))
        self.label_4.setText("")
    # retranslateUi

