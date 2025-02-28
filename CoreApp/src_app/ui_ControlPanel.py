# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_ControlPanel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomQPushButton import QCustomQPushButton
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from PySide2extn.RoundProgressBar import roundProgressBar
from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 777)
        MainWindow.setMinimumSize(QSize(1010, 533))
        MainWindow.setMaximumSize(QSize(1100, 16777215))
        MainWindow.setStyleSheet(u"background: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_slidemenu = QCustomSlideMenu(self.centralwidget)
        self.widget_slidemenu.setObjectName(u"widget_slidemenu")
        self.widget_slidemenu.setMinimumSize(QSize(160, 755))
        self.widget_slidemenu.setMaximumSize(QSize(160, 755))
        self.gridLayout_10 = QGridLayout(self.widget_slidemenu)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.Control_panel_report = QPushButton(self.widget_slidemenu)
        self.Control_panel_report.setObjectName(u"Control_panel_report")
        self.Control_panel_report.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/email.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Control_panel_report.setIcon(icon)
        self.Control_panel_report.setIconSize(QSize(30, 25))

        self.gridLayout_11.addWidget(self.Control_panel_report, 10, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_14, 9, 0, 1, 1)

        self.line_12 = QFrame(self.widget_slidemenu)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_12, 12, 0, 1, 1)

        self.Dashboard = QCustomQPushButton(self.widget_slidemenu)
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/bar-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard.setIcon(icon1)
        self.Dashboard.setIconSize(QSize(37, 25))

        self.gridLayout_11.addWidget(self.Dashboard, 0, 0, 1, 1)

        self.Control_panel = QPushButton(self.widget_slidemenu)
        self.Control_panel.setObjectName(u"Control_panel")
        self.Control_panel.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon2 = QIcon()
        icon2.addFile(u":/web_icons/icons/web_icons/setting0.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Control_panel.setIcon(icon2)
        self.Control_panel.setIconSize(QSize(37, 25))

        self.gridLayout_11.addWidget(self.Control_panel, 3, 0, 1, 1)

        self.line_13 = QFrame(self.widget_slidemenu)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_13, 16, 0, 1, 1)

        self.Control_panel_process = QPushButton(self.widget_slidemenu)
        self.Control_panel_process.setObjectName(u"Control_panel_process")
        self.Control_panel_process.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon3 = QIcon()
        icon3.addFile(u":/web_icons/icons/web_icons/setting1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Control_panel_process.setIcon(icon3)
        self.Control_panel_process.setIconSize(QSize(30, 25))

        self.gridLayout_11.addWidget(self.Control_panel_process, 6, 0, 1, 1)

        self.line_11 = QFrame(self.widget_slidemenu)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_11, 4, 0, 1, 1)

        self.line_2 = QFrame(self.widget_slidemenu)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_2, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 5, 0, 1, 1)

        self.myaccount = QPushButton(self.widget_slidemenu)
        self.myaccount.setObjectName(u"myaccount")
        self.myaccount.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon4 = QIcon()
        icon4.addFile(u":/web_icons/icons/web_icons/mask1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.myaccount.setIcon(icon4)
        self.myaccount.setIconSize(QSize(28, 22))

        self.gridLayout_11.addWidget(self.myaccount, 15, 0, 1, 1)

        self.Control_panel_Tasks = QPushButton(self.widget_slidemenu)
        self.Control_panel_Tasks.setObjectName(u"Control_panel_Tasks")
        self.Control_panel_Tasks.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/task_alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Control_panel_Tasks.setIcon(icon5)
        self.Control_panel_Tasks.setIconSize(QSize(30, 25))

        self.gridLayout_11.addWidget(self.Control_panel_Tasks, 8, 0, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_34, 7, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_6, 13, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_11, 1, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_7, 0, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(21, 885, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_10.addItem(self.verticalSpacer_10, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_slidemenu, 0, 0, 3, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 129))
        self.frame_2.setMaximumSize(QSize(16777215, 129))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_9 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.get_myaccount = QPushButton(self.frame_2)
        self.get_myaccount.setObjectName(u"get_myaccount")
        self.get_myaccount.setMinimumSize(QSize(254, 38))
        self.get_myaccount.setMaximumSize(QSize(243, 38))
        self.get_myaccount.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon6 = QIcon()
        icon6.addFile(u":/font_awesome/icons/font_awesome/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.get_myaccount.setIcon(icon6)
        self.get_myaccount.setIconSize(QSize(42, 34))

        self.gridLayout.addWidget(self.get_myaccount, 1, 8, 1, 1)

        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(145, 17))
        self.label_34.setMaximumSize(QSize(145, 17))
        font = QFont()
        font.setFamily(u"ABeeZee")
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"QLabel {\n"
"  color: #1a1e29;\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 14px;\n"
"\n"
"\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.label_34, 1, 1, 2, 1)

        self.horizontalSpacer_21 = QSpacerItem(16, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_21, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 6)

        self.label_datetime = QLabel(self.frame_2)
        self.label_datetime.setObjectName(u"label_datetime")
        self.label_datetime.setStyleSheet(u"QLabel{\n"
"  color: #707eae;\n"
"  font-family: \"Poppins\";\n"
"  font-size: 11px;\n"
"  letter-spacing: -0.02em;\n"
"  font-weight: 400;\n"
"}\n"
"")
        self.label_datetime.setIndent(0)

        self.gridLayout.addWidget(self.label_datetime, 0, 8, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(82, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 4, 2, 3)

        self.label_hello_5 = QLabel(self.frame_2)
        self.label_hello_5.setObjectName(u"label_hello_5")
        self.label_hello_5.setMinimumSize(QSize(60, 60))
        self.label_hello_5.setMaximumSize(QSize(60, 16777215))
        self.label_hello_5.setStyleSheet(u"")
        self.label_hello_5.setPixmap(QPixmap(u":/web_icons/icons/web_icons/rectangle-3370.png"))
        self.label_hello_5.setScaledContents(False)
        self.label_hello_5.setMargin(2)
        self.label_hello_5.setIndent(0)

        self.gridLayout.addWidget(self.label_hello_5, 0, 0, 4, 1)

        self.notifications = QPushButton(self.frame_2)
        self.notifications.setObjectName(u"notifications")
        self.notifications.setMinimumSize(QSize(25, 25))
        self.notifications.setMaximumSize(QSize(25, 25))
        self.notifications.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/notifications.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notifications.setIcon(icon7)
        self.notifications.setIconSize(QSize(37, 31))

        self.gridLayout.addWidget(self.notifications, 0, 9, 1, 1)

        self.label_hello = QLabel(self.frame_2)
        self.label_hello.setObjectName(u"label_hello")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_hello.sizePolicy().hasHeightForWidth())
        self.label_hello.setSizePolicy(sizePolicy)
        self.label_hello.setMinimumSize(QSize(257, 0))
        self.label_hello.setMaximumSize(QSize(257, 16777215))
        self.label_hello.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_hello, 1, 3, 2, 1)

        self.horizontalSpacer_8 = QSpacerItem(10, 14, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 9, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_27, 0, 1, 1, 6)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 1, 1, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.restore_window_button = QPushButton(self.centralwidget)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon8)
        self.restore_window_button.setIconSize(QSize(16, 16))

        self.gridLayout_14.addWidget(self.restore_window_button, 0, 4, 1, 1)

        self.close_window_button = QPushButton(self.centralwidget)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon9)

        self.gridLayout_14.addWidget(self.close_window_button, 0, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.pushButton_menu = QCustomQPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/align-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_menu.setIcon(icon10)

        self.gridLayout_14.addWidget(self.pushButton_menu, 0, 0, 1, 1)

        self.minimize_window_button = QPushButton(self.centralwidget)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon11)

        self.gridLayout_14.addWidget(self.minimize_window_button, 0, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_14, 0, 1, 1, 1)

        self.stackedWidget = QCustomQStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.widget_Selector_Reveal_Effect_Final_Colour_Captions = QWidget(self.page_12)
        self.widget_Selector_Reveal_Effect_Final_Colour_Captions.setObjectName(u"widget_Selector_Reveal_Effect_Final_Colour_Captions")
        self.widget_Selector_Reveal_Effect_Final_Colour_Captions.setGeometry(QRect(240, 0, 631, 411))
        self.gridLayout_56 = QGridLayout(self.widget_Selector_Reveal_Effect_Final_Colour_Captions)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_57 = QGridLayout()
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.label_50 = QLabel(self.widget_Selector_Reveal_Effect_Final_Colour_Captions)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_57.addWidget(self.label_50, 0, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_Selector_Reveal_Effect_Final_Colour_Captions)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(30, 30))
        self.pushButton_11.setMaximumSize(QSize(30, 30))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon12 = QIcon()
        icon12.addFile(u":/mediacuts/icons/mediacuts/icons8-c\u00edrculo-rgb-2-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon12)
        self.pushButton_11.setIconSize(QSize(37, 31))

        self.gridLayout_57.addWidget(self.pushButton_11, 0, 0, 1, 1)

        self.widget_Reveal_Effect_Final_Colour_Captions = QWidget(self.widget_Selector_Reveal_Effect_Final_Colour_Captions)
        self.widget_Reveal_Effect_Final_Colour_Captions.setObjectName(u"widget_Reveal_Effect_Final_Colour_Captions")
        self.widget_Reveal_Effect_Final_Colour_Captions.setMinimumSize(QSize(0, 271))
        self.widget_Reveal_Effect_Final_Colour_Captions.setMaximumSize(QSize(16777215, 271))

        self.gridLayout_57.addWidget(self.widget_Reveal_Effect_Final_Colour_Captions, 2, 0, 1, 2)

        self.verticalSpacer_52 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_57.addItem(self.verticalSpacer_52, 1, 0, 1, 2)

        self.verticalSpacer_53 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_57.addItem(self.verticalSpacer_53, 3, 0, 1, 2)


        self.gridLayout_56.addLayout(self.gridLayout_57, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_12)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.widget_Selector_Reveal_Effect_Initial_Colour_Captions = QWidget(self.page_11)
        self.widget_Selector_Reveal_Effect_Initial_Colour_Captions.setObjectName(u"widget_Selector_Reveal_Effect_Initial_Colour_Captions")
        self.widget_Selector_Reveal_Effect_Initial_Colour_Captions.setGeometry(QRect(240, 0, 631, 411))
        self.gridLayout_54 = QGridLayout(self.widget_Selector_Reveal_Effect_Initial_Colour_Captions)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_55 = QGridLayout()
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.label_49 = QLabel(self.widget_Selector_Reveal_Effect_Initial_Colour_Captions)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_55.addWidget(self.label_49, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.widget_Selector_Reveal_Effect_Initial_Colour_Captions)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(30, 30))
        self.pushButton_10.setMaximumSize(QSize(30, 30))
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_10.setIcon(icon12)
        self.pushButton_10.setIconSize(QSize(37, 31))

        self.gridLayout_55.addWidget(self.pushButton_10, 0, 0, 1, 1)

        self.widget_Reveal_Effect_Initial_Colour_Captions = QWidget(self.widget_Selector_Reveal_Effect_Initial_Colour_Captions)
        self.widget_Reveal_Effect_Initial_Colour_Captions.setObjectName(u"widget_Reveal_Effect_Initial_Colour_Captions")
        self.widget_Reveal_Effect_Initial_Colour_Captions.setMinimumSize(QSize(0, 271))
        self.widget_Reveal_Effect_Initial_Colour_Captions.setMaximumSize(QSize(16777215, 271))

        self.gridLayout_55.addWidget(self.widget_Reveal_Effect_Initial_Colour_Captions, 2, 0, 1, 2)

        self.verticalSpacer_50 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_55.addItem(self.verticalSpacer_50, 1, 0, 1, 2)

        self.verticalSpacer_51 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_55.addItem(self.verticalSpacer_51, 3, 0, 1, 2)


        self.gridLayout_54.addLayout(self.gridLayout_55, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_11)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.widget_Selector_Back_Colour_Captions = QWidget(self.page_10)
        self.widget_Selector_Back_Colour_Captions.setObjectName(u"widget_Selector_Back_Colour_Captions")
        self.widget_Selector_Back_Colour_Captions.setGeometry(QRect(200, 10, 661, 411))
        self.gridLayout_52 = QGridLayout(self.widget_Selector_Back_Colour_Captions)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.label_48 = QLabel(self.widget_Selector_Back_Colour_Captions)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_53.addWidget(self.label_48, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_Selector_Back_Colour_Captions)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(30, 30))
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_9.setIcon(icon12)
        self.pushButton_9.setIconSize(QSize(37, 31))

        self.gridLayout_53.addWidget(self.pushButton_9, 0, 0, 1, 1)

        self.widget_Back_Colour_Captions = QWidget(self.widget_Selector_Back_Colour_Captions)
        self.widget_Back_Colour_Captions.setObjectName(u"widget_Back_Colour_Captions")
        self.widget_Back_Colour_Captions.setMinimumSize(QSize(0, 271))
        self.widget_Back_Colour_Captions.setMaximumSize(QSize(16777215, 271))

        self.gridLayout_53.addWidget(self.widget_Back_Colour_Captions, 2, 0, 1, 2)

        self.verticalSpacer_48 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_53.addItem(self.verticalSpacer_48, 1, 0, 1, 2)

        self.verticalSpacer_49 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_53.addItem(self.verticalSpacer_49, 3, 0, 1, 2)


        self.gridLayout_52.addLayout(self.gridLayout_53, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_10)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.widget_Selector_Outline_Colour_Captions = QWidget(self.page_9)
        self.widget_Selector_Outline_Colour_Captions.setObjectName(u"widget_Selector_Outline_Colour_Captions")
        self.widget_Selector_Outline_Colour_Captions.setGeometry(QRect(120, 10, 661, 411))
        self.gridLayout_50 = QGridLayout(self.widget_Selector_Outline_Colour_Captions)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_51 = QGridLayout()
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_47 = QLabel(self.widget_Selector_Outline_Colour_Captions)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_51.addWidget(self.label_47, 0, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.widget_Selector_Outline_Colour_Captions)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(30, 30))
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_8.setIcon(icon12)
        self.pushButton_8.setIconSize(QSize(37, 31))

        self.gridLayout_51.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.widget_Outline_Colour_Captions = QWidget(self.widget_Selector_Outline_Colour_Captions)
        self.widget_Outline_Colour_Captions.setObjectName(u"widget_Outline_Colour_Captions")
        self.widget_Outline_Colour_Captions.setMinimumSize(QSize(0, 271))
        self.widget_Outline_Colour_Captions.setMaximumSize(QSize(16777215, 271))

        self.gridLayout_51.addWidget(self.widget_Outline_Colour_Captions, 2, 0, 1, 2)

        self.verticalSpacer_46 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_51.addItem(self.verticalSpacer_46, 1, 0, 1, 2)

        self.verticalSpacer_47 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_51.addItem(self.verticalSpacer_47, 3, 0, 1, 2)


        self.gridLayout_50.addLayout(self.gridLayout_51, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_9)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.widget_Selector_Secondary_Colour_Captions = QWidget(self.page_8)
        self.widget_Selector_Secondary_Colour_Captions.setObjectName(u"widget_Selector_Secondary_Colour_Captions")
        self.widget_Selector_Secondary_Colour_Captions.setGeometry(QRect(0, 0, 861, 411))
        self.gridLayout_48 = QGridLayout(self.widget_Selector_Secondary_Colour_Captions)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_49 = QGridLayout()
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_46 = QLabel(self.widget_Selector_Secondary_Colour_Captions)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_49.addWidget(self.label_46, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.widget_Selector_Secondary_Colour_Captions)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(30, 30))
        self.pushButton_7.setMaximumSize(QSize(30, 30))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_7.setIcon(icon12)
        self.pushButton_7.setIconSize(QSize(37, 31))

        self.gridLayout_49.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.widget_Secondary_Colour_Captions = QWidget(self.widget_Selector_Secondary_Colour_Captions)
        self.widget_Secondary_Colour_Captions.setObjectName(u"widget_Secondary_Colour_Captions")
        self.widget_Secondary_Colour_Captions.setMinimumSize(QSize(0, 271))
        self.widget_Secondary_Colour_Captions.setMaximumSize(QSize(16777215, 271))

        self.gridLayout_49.addWidget(self.widget_Secondary_Colour_Captions, 2, 0, 1, 2)

        self.verticalSpacer_44 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_49.addItem(self.verticalSpacer_44, 1, 0, 1, 2)

        self.verticalSpacer_45 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_49.addItem(self.verticalSpacer_45, 3, 0, 1, 2)


        self.gridLayout_48.addLayout(self.gridLayout_49, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_8)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.widget_Selector_Primary_Colour_Captions = QWidget(self.page_4)
        self.widget_Selector_Primary_Colour_Captions.setObjectName(u"widget_Selector_Primary_Colour_Captions")
        self.widget_Selector_Primary_Colour_Captions.setGeometry(QRect(50, 20, 811, 411))
        self.gridLayout_46 = QGridLayout(self.widget_Selector_Primary_Colour_Captions)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_47 = QGridLayout()
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.label_45 = QLabel(self.widget_Selector_Primary_Colour_Captions)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_47.addWidget(self.label_45, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.widget_Selector_Primary_Colour_Captions)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_6.setIcon(icon12)
        self.pushButton_6.setIconSize(QSize(37, 31))

        self.gridLayout_47.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.widget_Primary_Colour_Captions = QWidget(self.widget_Selector_Primary_Colour_Captions)
        self.widget_Primary_Colour_Captions.setObjectName(u"widget_Primary_Colour_Captions")
        self.widget_Primary_Colour_Captions.setMinimumSize(QSize(0, 271))
        self.widget_Primary_Colour_Captions.setMaximumSize(QSize(16777215, 271))

        self.gridLayout_47.addWidget(self.widget_Primary_Colour_Captions, 2, 0, 1, 2)

        self.verticalSpacer_42 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_47.addItem(self.verticalSpacer_42, 1, 0, 1, 2)

        self.verticalSpacer_43 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_47.addItem(self.verticalSpacer_43, 3, 0, 1, 2)


        self.gridLayout_46.addLayout(self.gridLayout_47, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.widget_Selector_Animation_Subtitles = QWidget(self.page_2)
        self.widget_Selector_Animation_Subtitles.setObjectName(u"widget_Selector_Animation_Subtitles")
        self.widget_Selector_Animation_Subtitles.setGeometry(QRect(0, 0, 371, 401))
        self.gridLayout_40 = QGridLayout(self.widget_Selector_Animation_Subtitles)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_41 = QLabel(self.widget_Selector_Animation_Subtitles)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_41.addWidget(self.label_41, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(33, 25))
        self.pushButton_3.setMaximumSize(QSize(33, 25))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon13 = QIcon()
        icon13.addFile(u":/material_design/icons/material_design/animation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon13)
        self.pushButton_3.setIconSize(QSize(37, 31))

        self.gridLayout_41.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.verticalSpacer_38 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_41.addItem(self.verticalSpacer_38, 3, 1, 1, 1)

        self.verticalSpacer_39 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_41.addItem(self.verticalSpacer_39, 1, 0, 1, 2)

        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setHorizontalSpacing(28)
        self.gridLayout_42.setVerticalSpacing(21)
        self.button_animation_Gradual_Blink_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_Gradual_Blink_sub.setObjectName(u"button_animation_Gradual_Blink_sub")
        self.button_animation_Gradual_Blink_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_Gradual_Blink_sub, 1, 2, 1, 1)

        self.button_animation_AppearDisappear_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_AppearDisappear_sub.setObjectName(u"button_animation_AppearDisappear_sub")
        self.button_animation_AppearDisappear_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_AppearDisappear_sub, 1, 1, 1, 1)

        self.button_animation_StrobeEffect_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_StrobeEffect_sub.setObjectName(u"button_animation_StrobeEffect_sub")
        self.button_animation_StrobeEffect_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_StrobeEffect_sub, 2, 0, 1, 1)

        self.button_animation_Soft_Fade_In_Out_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_Soft_Fade_In_Out_sub.setObjectName(u"button_animation_Soft_Fade_In_Out_sub")
        self.button_animation_Soft_Fade_In_Out_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_Soft_Fade_In_Out_sub, 1, 3, 1, 1)

        self.button_animation_FadeInandHold_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_FadeInandHold_sub.setObjectName(u"button_animation_FadeInandHold_sub")
        self.button_animation_FadeInandHold_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_FadeInandHold_sub, 2, 1, 1, 1)

        self.button_animation_FadeOut_and_Hold_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_FadeOut_and_Hold_sub.setObjectName(u"button_animation_FadeOut_and_Hold_sub")
        self.button_animation_FadeOut_and_Hold_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_FadeOut_and_Hold_sub, 2, 3, 1, 1)

        self.button_animation_PulseOut_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_PulseOut_sub.setObjectName(u"button_animation_PulseOut_sub")
        self.button_animation_PulseOut_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_PulseOut_sub, 2, 2, 1, 1)

        self.button_animation_Pulse_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_Pulse_sub.setObjectName(u"button_animation_Pulse_sub")
        self.button_animation_Pulse_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_Pulse_sub, 0, 1, 1, 1)

        self.button_animation_SlowFadeIn_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_SlowFadeIn_sub.setObjectName(u"button_animation_SlowFadeIn_sub")
        self.button_animation_SlowFadeIn_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_SlowFadeIn_sub, 0, 2, 1, 1)

        self.button_animation_FastBlink_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_FastBlink_sub.setObjectName(u"button_animation_FastBlink_sub")
        self.button_animation_FastBlink_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_FastBlink_sub, 1, 0, 1, 1)

        self.button_animation_FadeIn_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_FadeIn_sub.setObjectName(u"button_animation_FadeIn_sub")
        self.button_animation_FadeIn_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_FadeIn_sub, 0, 0, 1, 1)

        self.button_animation_SlowFadeOut_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_SlowFadeOut_sub.setObjectName(u"button_animation_SlowFadeOut_sub")
        self.button_animation_SlowFadeOut_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_SlowFadeOut_sub, 0, 3, 1, 1)

        self.button_animation_BlinkingText_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_BlinkingText_sub.setObjectName(u"button_animation_BlinkingText_sub")
        self.button_animation_BlinkingText_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_BlinkingText_sub, 3, 0, 1, 1)

        self.button_animation_QuickFadeOut_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_QuickFadeOut_sub.setObjectName(u"button_animation_QuickFadeOut_sub")
        self.button_animation_QuickFadeOut_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_QuickFadeOut_sub, 3, 1, 1, 1)

        self.button_animation_QuickFadeIn_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_QuickFadeIn_sub.setObjectName(u"button_animation_QuickFadeIn_sub")
        self.button_animation_QuickFadeIn_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_QuickFadeIn_sub, 3, 2, 1, 1)

        self.button_animation_None_sub = QPushButton(self.widget_Selector_Animation_Subtitles)
        self.button_animation_None_sub.setObjectName(u"button_animation_None_sub")
        self.button_animation_None_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_42.addWidget(self.button_animation_None_sub, 3, 3, 1, 1)


        self.gridLayout_41.addLayout(self.gridLayout_42, 2, 0, 1, 2)


        self.gridLayout_40.addLayout(self.gridLayout_41, 0, 0, 1, 1)

        self.widget_Selector_FontName_Subtitles = QWidget(self.page_2)
        self.widget_Selector_FontName_Subtitles.setObjectName(u"widget_Selector_FontName_Subtitles")
        self.widget_Selector_FontName_Subtitles.setGeometry(QRect(370, 0, 371, 401))
        self.gridLayout_43 = QGridLayout(self.widget_Selector_FontName_Subtitles)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_44 = QLabel(self.widget_Selector_FontName_Subtitles)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_44.addWidget(self.label_44, 0, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(33, 25))
        self.pushButton_5.setMaximumSize(QSize(33, 25))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon14 = QIcon()
        icon14.addFile(u":/material_design/icons/material_design/drive_file_rename_outline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon14)
        self.pushButton_5.setIconSize(QSize(37, 31))

        self.gridLayout_44.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.verticalSpacer_40 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_44.addItem(self.verticalSpacer_40, 3, 1, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_44.addItem(self.verticalSpacer_41, 1, 0, 1, 2)

        self.gridLayout_45 = QGridLayout()
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setHorizontalSpacing(29)
        self.gridLayout_45.setVerticalSpacing(71)
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.button_FranklinGothic_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_FranklinGothic_sub.setObjectName(u"button_FranklinGothic_sub")
        self.button_FranklinGothic_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_FranklinGothic_sub, 1, 0, 1, 1)

        self.button_Trebuchet_MS_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_Trebuchet_MS_sub.setObjectName(u"button_Trebuchet_MS_sub")
        self.button_Trebuchet_MS_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_Trebuchet_MS_sub, 2, 0, 1, 1)

        self.button_Comic_Sans_MS_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_Comic_Sans_MS_sub.setObjectName(u"button_Comic_Sans_MS_sub")
        self.button_Comic_Sans_MS_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_Comic_Sans_MS_sub, 1, 2, 1, 1)

        self.button_CenturyGothic_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_CenturyGothic_sub.setObjectName(u"button_CenturyGothic_sub")
        self.button_CenturyGothic_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_CenturyGothic_sub, 1, 1, 1, 1)

        self.button_Tahoma_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_Tahoma_sub.setObjectName(u"button_Tahoma_sub")
        self.button_Tahoma_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_Tahoma_sub, 0, 0, 1, 1)

        self.button_Calibri_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_Calibri_sub.setObjectName(u"button_Calibri_sub")
        self.button_Calibri_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_Calibri_sub, 0, 2, 1, 1)

        self.button_LucidaConsole_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_LucidaConsole_sub.setObjectName(u"button_LucidaConsole_sub")
        self.button_LucidaConsole_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_LucidaConsole_sub, 0, 3, 1, 1)

        self.button_Impact_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_Impact_sub.setObjectName(u"button_Impact_sub")
        self.button_Impact_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_Impact_sub, 0, 1, 1, 1)

        self.button_Garamond_sub = QPushButton(self.widget_Selector_FontName_Subtitles)
        self.button_Garamond_sub.setObjectName(u"button_Garamond_sub")
        self.button_Garamond_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_45.addWidget(self.button_Garamond_sub, 1, 3, 1, 1)


        self.gridLayout_44.addLayout(self.gridLayout_45, 2, 0, 1, 2)


        self.gridLayout_43.addLayout(self.gridLayout_44, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.widget_Selector_FontName_Captions = QWidget(self.page_14)
        self.widget_Selector_FontName_Captions.setObjectName(u"widget_Selector_FontName_Captions")
        self.widget_Selector_FontName_Captions.setGeometry(QRect(290, 50, 371, 401))
        self.gridLayout_59 = QGridLayout(self.widget_Selector_FontName_Captions)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_60 = QGridLayout()
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.label_51 = QLabel(self.widget_Selector_FontName_Captions)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_60.addWidget(self.label_51, 0, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.widget_Selector_FontName_Captions)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(33, 25))
        self.pushButton_16.setMaximumSize(QSize(33, 25))
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon15 = QIcon()
        icon15.addFile(u":/material_design/icons/material_design/font_download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon15)
        self.pushButton_16.setIconSize(QSize(37, 31))

        self.gridLayout_60.addWidget(self.pushButton_16, 0, 0, 1, 1)

        self.verticalSpacer_54 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_60.addItem(self.verticalSpacer_54, 3, 1, 1, 1)

        self.verticalSpacer_55 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_60.addItem(self.verticalSpacer_55, 1, 0, 1, 2)

        self.gridLayout_61 = QGridLayout()
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setHorizontalSpacing(29)
        self.gridLayout_61.setVerticalSpacing(71)
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.button_FranklinGothic_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_FranklinGothic_Captions.setObjectName(u"button_FranklinGothic_Captions")
        self.button_FranklinGothic_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_FranklinGothic_Captions, 1, 0, 1, 1)

        self.button_Trebuchet_MS_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_Trebuchet_MS_Captions.setObjectName(u"button_Trebuchet_MS_Captions")
        self.button_Trebuchet_MS_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_Trebuchet_MS_Captions, 2, 0, 1, 1)

        self.button_Comic_Sans_MS_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_Comic_Sans_MS_Captions.setObjectName(u"button_Comic_Sans_MS_Captions")
        self.button_Comic_Sans_MS_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_Comic_Sans_MS_Captions, 1, 2, 1, 1)

        self.button_CenturyGothic_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_CenturyGothic_Captions.setObjectName(u"button_CenturyGothic_Captions")
        self.button_CenturyGothic_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_CenturyGothic_Captions, 1, 1, 1, 1)

        self.button_Tahoma_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_Tahoma_Captions.setObjectName(u"button_Tahoma_Captions")
        self.button_Tahoma_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_Tahoma_Captions, 0, 0, 1, 1)

        self.button_Calibri_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_Calibri_Captions.setObjectName(u"button_Calibri_Captions")
        self.button_Calibri_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_Calibri_Captions, 0, 2, 1, 1)

        self.button_LucidaConsole_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_LucidaConsole_Captions.setObjectName(u"button_LucidaConsole_Captions")
        self.button_LucidaConsole_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_LucidaConsole_Captions, 0, 3, 1, 1)

        self.button_Impact_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_Impact_Captions.setObjectName(u"button_Impact_Captions")
        self.button_Impact_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_Impact_Captions, 0, 1, 1, 1)

        self.button_Garamond_Captions = QPushButton(self.widget_Selector_FontName_Captions)
        self.button_Garamond_Captions.setObjectName(u"button_Garamond_Captions")
        self.button_Garamond_Captions.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_61.addWidget(self.button_Garamond_Captions, 1, 3, 1, 1)


        self.gridLayout_60.addLayout(self.gridLayout_61, 2, 0, 1, 2)


        self.gridLayout_59.addLayout(self.gridLayout_60, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_14)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget_Selector_Color_Subtitles = QWidget(self.page)
        self.widget_Selector_Color_Subtitles.setObjectName(u"widget_Selector_Color_Subtitles")
        self.widget_Selector_Color_Subtitles.setGeometry(QRect(10, 10, 851, 581))
        self.gridLayout_34 = QGridLayout(self.widget_Selector_Color_Subtitles)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_39 = QLabel(self.widget_Selector_Color_Subtitles)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_35.addWidget(self.label_39, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_Selector_Color_Subtitles)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.pushButton_4.setIcon(icon12)
        self.pushButton_4.setIconSize(QSize(37, 31))

        self.gridLayout_35.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_35.addItem(self.verticalSpacer_32, 1, 0, 1, 2)

        self.widget_Color_Subtitles = QWidget(self.widget_Selector_Color_Subtitles)
        self.widget_Color_Subtitles.setObjectName(u"widget_Color_Subtitles")
        self.widget_Color_Subtitles.setMinimumSize(QSize(0, 461))
        self.widget_Color_Subtitles.setMaximumSize(QSize(16777215, 461))

        self.gridLayout_35.addWidget(self.widget_Color_Subtitles, 2, 0, 1, 2)


        self.gridLayout_34.addLayout(self.gridLayout_35, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.widget_Selector_Effects_Subtitles = QWidget(self.page_13)
        self.widget_Selector_Effects_Subtitles.setObjectName(u"widget_Selector_Effects_Subtitles")
        self.widget_Selector_Effects_Subtitles.setGeometry(QRect(300, 0, 371, 401))
        self.gridLayout_37 = QGridLayout(self.widget_Selector_Effects_Subtitles)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.verticalSpacer_36 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_38.addItem(self.verticalSpacer_36, 3, 1, 1, 1)

        self.label_40 = QLabel(self.widget_Selector_Effects_Subtitles)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_38.addWidget(self.label_40, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(25, 25))
        self.pushButton_2.setMaximumSize(QSize(25, 25))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon16 = QIcon()
        icon16.addFile(u":/mediacuts/icons/mediacuts/icons8-efeitos-visuais-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon16)
        self.pushButton_2.setIconSize(QSize(37, 31))

        self.gridLayout_38.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setHorizontalSpacing(4)
        self.gridLayout_39.setVerticalSpacing(23)
        self.button_GlowEffect_Shadow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_GlowEffect_Shadow_sub.setObjectName(u"button_GlowEffect_Shadow_sub")
        self.button_GlowEffect_Shadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_GlowEffect_Shadow_sub, 0, 1, 1, 1)

        self.button_effects_BoldShadow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_BoldShadow_sub.setObjectName(u"button_effects_BoldShadow_sub")
        self.button_effects_BoldShadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_BoldShadow_sub, 1, 3, 1, 1)

        self.button_effects_DropShadow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_DropShadow_sub.setObjectName(u"button_effects_DropShadow_sub")
        self.button_effects_DropShadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_DropShadow_sub, 1, 2, 1, 1)

        self.button_effects_DottedOutline_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_DottedOutline_sub.setObjectName(u"button_effects_DottedOutline_sub")
        self.button_effects_DottedOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_DottedOutline_sub, 0, 3, 1, 1)

        self.button_effects_NeonGlow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_NeonGlow_sub.setObjectName(u"button_effects_NeonGlow_sub")
        self.button_effects_NeonGlow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_NeonGlow_sub, 0, 2, 1, 1)

        self.button_effects_InnerGlow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_InnerGlow_sub.setObjectName(u"button_effects_InnerGlow_sub")
        self.button_effects_InnerGlow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_InnerGlow_sub, 1, 0, 1, 1)

        self.button_effects_HardGlow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_HardGlow_sub.setObjectName(u"button_effects_HardGlow_sub")
        self.button_effects_HardGlow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_HardGlow_sub, 2, 1, 1, 1)

        self.button_effects_SoftShadow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_SoftShadow_sub.setObjectName(u"button_effects_SoftShadow_sub")
        self.button_effects_SoftShadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_SoftShadow_sub, 2, 2, 1, 1)

        self.button_effects_WavyOutline_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_WavyOutline_sub.setObjectName(u"button_effects_WavyOutline_sub")
        self.button_effects_WavyOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_WavyOutline_sub, 1, 1, 1, 1)

        self.button_effects_BlurredShadow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_BlurredShadow_sub.setObjectName(u"button_effects_BlurredShadow_sub")
        self.button_effects_BlurredShadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_BlurredShadow_sub, 2, 0, 1, 1)

        self.button_effects_Emboss_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_Emboss_sub.setObjectName(u"button_effects_Emboss_sub")
        self.button_effects_Emboss_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_Emboss_sub, 3, 1, 1, 1)

        self.button_effects_Outline_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_Outline_sub.setObjectName(u"button_effects_Outline_sub")
        self.button_effects_Outline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_Outline_sub, 2, 3, 1, 1)

        self.button_effects_DoubleOutline_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_DoubleOutline_sub.setObjectName(u"button_effects_DoubleOutline_sub")
        self.button_effects_DoubleOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_DoubleOutline_sub, 3, 3, 1, 1)

        self.button_effects_TransparentOutline_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_TransparentOutline_sub.setObjectName(u"button_effects_TransparentOutline_sub")
        self.button_effects_TransparentOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_TransparentOutline_sub, 3, 2, 1, 1)

        self.button_effects_SoftGlow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_SoftGlow_sub.setObjectName(u"button_effects_SoftGlow_sub")
        self.button_effects_SoftGlow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_SoftGlow_sub, 3, 0, 1, 1)

        self.button_effects_Shadow_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_Shadow_sub.setObjectName(u"button_effects_Shadow_sub")
        self.button_effects_Shadow_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_Shadow_sub, 0, 0, 1, 1)

        self.button_effects_ThickOutline_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_ThickOutline_sub.setObjectName(u"button_effects_ThickOutline_sub")
        self.button_effects_ThickOutline_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_ThickOutline_sub, 4, 0, 1, 1)

        self.button_effects_None_sub = QPushButton(self.widget_Selector_Effects_Subtitles)
        self.button_effects_None_sub.setObjectName(u"button_effects_None_sub")
        self.button_effects_None_sub.setStyleSheet(u"    QPushButton {\n"
"        background: white; \n"
"        color: black;  /* Cor do texto do bot\u00e3o */\n"
"        border: none;  /* Remove a borda padr\u00e3o */\n"
"        border-radius: 10px;  /* Bordas arredondadas (opcional) */\n"
"        padding: 10px;  /* Espa\u00e7amento interno */\n"
"        font-size: 10px;  /* Tamanho da fonte */\n"
"    }\n"
"\n"
"   QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"   }\n"
"   QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"   }")

        self.gridLayout_39.addWidget(self.button_effects_None_sub, 4, 1, 1, 1)


        self.gridLayout_38.addLayout(self.gridLayout_39, 2, 0, 1, 2)

        self.verticalSpacer_33 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_38.addItem(self.verticalSpacer_33, 1, 0, 1, 2)


        self.gridLayout_37.addLayout(self.gridLayout_38, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_13)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.widget_Select_Time = QWidget(self.page_widgets)
        self.widget_Select_Time.setObjectName(u"widget_Select_Time")
        self.widget_Select_Time.setGeometry(QRect(10, 10, 301, 581))
        self.gridLayout_22 = QGridLayout(self.widget_Select_Time)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_12, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_19, 2, 5, 1, 1)

        self.label_33 = QLabel(self.widget_Select_Time)
        self.label_33.setObjectName(u"label_33")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy1)
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setMaximumSize(QSize(16777215, 16777215))
        self.label_33.setIndent(0)

        self.gridLayout_30.addWidget(self.label_33, 2, 1, 1, 1)

        self.label_37 = QLabel(self.widget_Select_Time)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)
        self.label_37.setMinimumSize(QSize(0, 0))
        self.label_37.setMaximumSize(QSize(16777215, 16777215))
        self.label_37.setIndent(0)

        self.gridLayout_30.addWidget(self.label_37, 2, 4, 1, 1)

        self.pushButton_15 = QPushButton(self.widget_Select_Time)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(30, 30))
        self.pushButton_15.setMaximumSize(QSize(30, 30))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/material_design/icons/material_design/hourglass_empty.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon17)
        self.pushButton_15.setIconSize(QSize(37, 31))

        self.gridLayout_30.addWidget(self.pushButton_15, 2, 3, 1, 1)

        self.Time_Weekly_Mode = QTextEdit(self.widget_Select_Time)
        self.Time_Weekly_Mode.setObjectName(u"Time_Weekly_Mode")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Time_Weekly_Mode.sizePolicy().hasHeightForWidth())
        self.Time_Weekly_Mode.setSizePolicy(sizePolicy2)
        self.Time_Weekly_Mode.setMinimumSize(QSize(0, 0))
        self.Time_Weekly_Mode.setMaximumSize(QSize(16777215, 48))
        self.Time_Weekly_Mode.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Time_Weekly_Mode.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Time_Weekly_Mode.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_30.addWidget(self.Time_Weekly_Mode, 3, 3, 1, 2)

        self.pushButton_14 = QPushButton(self.widget_Select_Time)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(30, 30))
        self.pushButton_14.setMaximumSize(QSize(30, 30))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"")
        icon18 = QIcon()
        icon18.addFile(u":/material_design/icons/material_design/today.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon18)
        self.pushButton_14.setIconSize(QSize(37, 31))

        self.gridLayout_30.addWidget(self.pushButton_14, 2, 0, 1, 1)

        self.Day_Weekly_Mode = QTextEdit(self.widget_Select_Time)
        self.Day_Weekly_Mode.setObjectName(u"Day_Weekly_Mode")
        sizePolicy2.setHeightForWidth(self.Day_Weekly_Mode.sizePolicy().hasHeightForWidth())
        self.Day_Weekly_Mode.setSizePolicy(sizePolicy2)
        self.Day_Weekly_Mode.setMinimumSize(QSize(0, 45))
        self.Day_Weekly_Mode.setMaximumSize(QSize(16777215, 48))
        self.Day_Weekly_Mode.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Day_Weekly_Mode.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Day_Weekly_Mode.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_30.addWidget(self.Day_Weekly_Mode, 3, 0, 1, 2)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_30.addItem(self.verticalSpacer_26, 4, 0, 1, 2)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_30.addItem(self.verticalSpacer_28, 4, 2, 1, 3)


        self.gridLayout_22.addLayout(self.gridLayout_30, 2, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget_Select_Time)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.Indefinite_Schedule_Weekly_Mode = QRadioButton(self.widget_Select_Time)
        self.Indefinite_Schedule_Weekly_Mode.setObjectName(u"Indefinite_Schedule_Weekly_Mode")

        self.gridLayout_3.addWidget(self.Indefinite_Schedule_Weekly_Mode, 3, 0, 1, 2)

        self.Schedule_the_month_Weekly_Mode = QRadioButton(self.widget_Select_Time)
        self.Schedule_the_month_Weekly_Mode.setObjectName(u"Schedule_the_month_Weekly_Mode")
        self.Schedule_the_month_Weekly_Mode.setChecked(True)

        self.gridLayout_3.addWidget(self.Schedule_the_month_Weekly_Mode, 2, 0, 1, 2)

        self.pushButton_12 = QPushButton(self.widget_Select_Time)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(30, 30))
        self.pushButton_12.setMaximumSize(QSize(30, 30))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"")
        icon19 = QIcon()
        icon19.addFile(u":/material_design/icons/material_design/date_range.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon19)
        self.pushButton_12.setIconSize(QSize(37, 31))

        self.gridLayout_3.addWidget(self.pushButton_12, 0, 0, 1, 1)

        self.checkBox_UTC_time_zone_Weekly_Mode = QCheckBox(self.widget_Select_Time)
        self.checkBox_UTC_time_zone_Weekly_Mode.setObjectName(u"checkBox_UTC_time_zone_Weekly_Mode")
        self.checkBox_UTC_time_zone_Weekly_Mode.setChecked(False)

        self.gridLayout_3.addWidget(self.checkBox_UTC_time_zone_Weekly_Mode, 4, 0, 1, 2)

        self.checkBox_Sao_Paulo_time_zone_Weekly_Mode = QCheckBox(self.widget_Select_Time)
        self.checkBox_Sao_Paulo_time_zone_Weekly_Mode.setObjectName(u"checkBox_Sao_Paulo_time_zone_Weekly_Mode")
        self.checkBox_Sao_Paulo_time_zone_Weekly_Mode.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_Sao_Paulo_time_zone_Weekly_Mode, 5, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 2)


        self.gridLayout_22.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.verticalSpacer_22 = QSpacerItem(280, 17, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_22.addItem(self.verticalSpacer_22, 1, 0, 1, 2)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_29, 3, 0, 1, 2)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_36 = QLabel(self.widget_Select_Time)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_31.addWidget(self.label_36, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_Select_Time)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(30, 30))
        self.pushButton_13.setMaximumSize(QSize(30, 30))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"")
        icon20 = QIcon()
        icon20.addFile(u":/material_design/icons/material_design/calendar_month.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon20)
        self.pushButton_13.setIconSize(QSize(37, 31))

        self.gridLayout_31.addWidget(self.pushButton_13, 0, 0, 1, 1)

        self.Execute_only_1_time_on_the_date_Date_Mode = QRadioButton(self.widget_Select_Time)
        self.Execute_only_1_time_on_the_date_Date_Mode.setObjectName(u"Execute_only_1_time_on_the_date_Date_Mode")

        self.gridLayout_31.addWidget(self.Execute_only_1_time_on_the_date_Date_Mode, 2, 0, 1, 2)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.Time_Date_Mode = QTextEdit(self.widget_Select_Time)
        self.Time_Date_Mode.setObjectName(u"Time_Date_Mode")
        sizePolicy2.setHeightForWidth(self.Time_Date_Mode.sizePolicy().hasHeightForWidth())
        self.Time_Date_Mode.setSizePolicy(sizePolicy2)
        self.Time_Date_Mode.setMinimumSize(QSize(0, 45))
        self.Time_Date_Mode.setMaximumSize(QSize(16777215, 48))
        self.Time_Date_Mode.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Time_Date_Mode.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Time_Date_Mode.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Time_Date_Mode.setTabStopWidth(80)

        self.gridLayout_32.addWidget(self.Time_Date_Mode, 3, 0, 1, 2)

        self.checkBox_UTC_time_zone_Date_Mode = QCheckBox(self.widget_Select_Time)
        self.checkBox_UTC_time_zone_Date_Mode.setObjectName(u"checkBox_UTC_time_zone_Date_Mode")
        self.checkBox_UTC_time_zone_Date_Mode.setChecked(False)

        self.gridLayout_32.addWidget(self.checkBox_UTC_time_zone_Date_Mode, 1, 0, 1, 2)

        self.pushButton_17 = QPushButton(self.widget_Select_Time)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(30, 30))
        self.pushButton_17.setMaximumSize(QSize(30, 30))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; /* N\u00e3o suportado, precisa ser ajustado via c\u00f3digo */\n"
"}\n"
"\n"
"")
        self.pushButton_17.setIcon(icon18)
        self.pushButton_17.setIconSize(QSize(37, 31))

        self.gridLayout_32.addWidget(self.pushButton_17, 0, 0, 1, 1)

        self.label_38 = QLabel(self.widget_Select_Time)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)
        self.label_38.setMinimumSize(QSize(0, 0))
        self.label_38.setMaximumSize(QSize(16777215, 16777215))
        self.label_38.setIndent(0)

        self.gridLayout_32.addWidget(self.label_38, 0, 1, 1, 1)

        self.checkBox_Sao_Paulo_time_zone_Date_Mode = QCheckBox(self.widget_Select_Time)
        self.checkBox_Sao_Paulo_time_zone_Date_Mode.setObjectName(u"checkBox_Sao_Paulo_time_zone_Date_Mode")

        self.gridLayout_32.addWidget(self.checkBox_Sao_Paulo_time_zone_Date_Mode, 2, 0, 1, 2)

        self.gridLayout_58 = QGridLayout()
        self.gridLayout_58.setObjectName(u"gridLayout_58")

        self.gridLayout_32.addLayout(self.gridLayout_58, 5, 0, 1, 2)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_30, 4, 0, 1, 2)


        self.gridLayout_31.addLayout(self.gridLayout_32, 5, 0, 1, 2)

        self.verticalSpacer_31 = QSpacerItem(20, 9, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_31.addItem(self.verticalSpacer_31, 3, 0, 1, 2)

        self.verticalSpacer_11 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_31.addItem(self.verticalSpacer_11, 1, 0, 1, 2)


        self.gridLayout_22.addLayout(self.gridLayout_31, 4, 0, 1, 2)

        self.widget_Upload_image_watermark = QWidget(self.page_widgets)
        self.widget_Upload_image_watermark.setObjectName(u"widget_Upload_image_watermark")
        self.widget_Upload_image_watermark.setGeometry(QRect(320, 10, 531, 481))
        self.gridLayout_33 = QGridLayout(self.widget_Upload_image_watermark)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.widget_preview_watermark = QWidget(self.widget_Upload_image_watermark)
        self.widget_preview_watermark.setObjectName(u"widget_preview_watermark")
        self.widget_preview_watermark.setMinimumSize(QSize(0, 319))
        self.widget_preview_watermark.setMaximumSize(QSize(16777215, 319))

        self.gridLayout_36.addWidget(self.widget_preview_watermark, 2, 0, 1, 3)

        self.label_43 = QLabel(self.widget_Upload_image_watermark)
        self.label_43.setObjectName(u"label_43")
        sizePolicy1.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy1)
        self.label_43.setMinimumSize(QSize(53, 0))
        self.label_43.setMaximumSize(QSize(53, 16777215))
        self.label_43.setPixmap(QPixmap(u":/web_icons/icons/web_icons/rectangle-3370.png"))
        self.label_43.setMargin(5)
        self.label_43.setIndent(5)

        self.gridLayout_36.addWidget(self.label_43, 0, 0, 1, 1)

        self.line_3 = QFrame(self.widget_Upload_image_watermark)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_36.addWidget(self.line_3, 1, 0, 1, 3)

        self.upload_image_watermark_ = QPushButton(self.widget_Upload_image_watermark)
        self.upload_image_watermark_.setObjectName(u"upload_image_watermark_")
        self.upload_image_watermark_.setMinimumSize(QSize(0, 0))
        self.upload_image_watermark_.setMaximumSize(QSize(16777215, 30))
        self.upload_image_watermark_.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon21 = QIcon()
        icon21.addFile(u":/feather/icons/feather/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_image_watermark_.setIcon(icon21)

        self.gridLayout_36.addWidget(self.upload_image_watermark_, 3, 0, 1, 3)

        self.label_42 = QLabel(self.widget_Upload_image_watermark)
        self.label_42.setObjectName(u"label_42")
        sizePolicy1.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy1)
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setMaximumSize(QSize(999999, 16777215))
        self.label_42.setIndent(13)

        self.gridLayout_36.addWidget(self.label_42, 0, 1, 1, 2)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_36.addItem(self.verticalSpacer_35, 4, 0, 1, 3)


        self.gridLayout_33.addLayout(self.gridLayout_36, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_widgets)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.gridLayout_29 = QGridLayout(self.page_login)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.widget = QWidget(self.page_login)
        self.widget.setObjectName(u"widget")
        self.gridLayout_25 = QGridLayout(self.widget)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.verticalSpacer_23 = QSpacerItem(20, 220, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_25.addItem(self.verticalSpacer_23, 2, 0, 1, 1)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.horizontalSpacer_18 = QSpacerItem(185, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_18, 0, 3, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_17, 0, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(165, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_23, 1, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #1a1e29;\n"
"    text-align: left;\n"
"    font-family: \"ABeeZee-Regular\", sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 0.016em;\n"
"\n"
"}")
        self.label_2.setIndent(7)

        self.gridLayout_26.addWidget(self.label_2, 1, 1, 1, 2)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_22, 1, 3, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(172, 63))
        self.pushButton.setMaximumSize(QSize(172, 63))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
" color: #1a1e29;\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"")
        icon22 = QIcon()
        icon22.addFile(u":/web_icons/icons/web_icons/rectangle-3370.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon22)
        self.pushButton.setIconSize(QSize(78, 80))

        self.gridLayout_26.addWidget(self.pushButton, 0, 1, 1, 2)


        self.gridLayout_25.addLayout(self.gridLayout_26, 0, 0, 1, 1)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"QLabel {\n"
"    color: #343c44;\n"
"    font-family: \"Poppins-Medium\", sans-serif;\n"
"    font-size: 12px;\n"
"    letter-spacing: 0.5px;\n"
"    font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_28.addWidget(self.label_32, 3, 1, 1, 1)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"QLabel {\n"
"    color: #343c44;\n"
"    font-family: \"Poppins-Medium\", sans-serif;\n"
"    font-size: 12px;\n"
"    letter-spacing: 0.5px;\n"
"    font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_28.addWidget(self.label_27, 0, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.widget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(25, 25))
        self.pushButton_18.setMaximumSize(QSize(25, 25))
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"\n"
"}\n"
"")
        icon23 = QIcon()
        icon23.addFile(u":/material_design/icons/material_design/local_post_office.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon23)
        self.pushButton_18.setIconSize(QSize(32, 32))

        self.gridLayout_28.addWidget(self.pushButton_18, 0, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.widget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(25, 25))
        self.pushButton_19.setMaximumSize(QSize(25, 25))
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"\n"
"}\n"
"")
        icon24 = QIcon()
        icon24.addFile(u":/material_design/icons/material_design/password.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon24)
        self.pushButton_19.setIconSize(QSize(32, 32))

        self.gridLayout_28.addWidget(self.pushButton_19, 3, 0, 1, 1)

        self.username_password = QTextEdit(self.widget)
        self.username_password.setObjectName(u"username_password")
        sizePolicy2.setHeightForWidth(self.username_password.sizePolicy().hasHeightForWidth())
        self.username_password.setSizePolicy(sizePolicy2)
        self.username_password.setMinimumSize(QSize(0, 48))
        self.username_password.setMaximumSize(QSize(16777215, 48))
        self.username_password.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.username_password.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.username_password.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_28.addWidget(self.username_password, 4, 0, 1, 2)

        self.username_input = QTextEdit(self.widget)
        self.username_input.setObjectName(u"username_input")
        sizePolicy2.setHeightForWidth(self.username_input.sizePolicy().hasHeightForWidth())
        self.username_input.setSizePolicy(sizePolicy2)
        self.username_input.setMinimumSize(QSize(0, 48))
        self.username_input.setMaximumSize(QSize(16777215, 48))
        self.username_input.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.username_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.username_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_28.addWidget(self.username_input, 1, 0, 1, 2)

        self.pushButton_login = QPushButton(self.widget)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setStyleSheet(u"QPushButton {\n"
"    background: #5a55d2;\n"
"    border-radius: 6px;\n"
"    padding: 8px 32px;\n"
"    color: #fbfbfb;\n"
"    font-family: \"Poppins-Regular\", sans-serif;\n"
"    font-size: 16px;\n"
"    line-height: 120%;\n"
"    letter-spacing: 0.25px;\n"
"    font-weight: 400;\n"
"    text-align: center;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Efeito ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background: #4c49b8;\n"
"}\n"
"\n"
"/* Efeito ao pressionar o bot\u00e3o */\n"
"QPushButton:pressed {\n"
"    background: #3e3d9f;\n"
"}\n"
"\n"
"/* Desabilitado */\n"
"QPushButton:disabled {\n"
"    background: #b0b0b0;\n"
"    color: #e0e0e0;\n"
"}\n"
"")
        icon25 = QIcon()
        icon25.addFile(u":/material_design/icons/material_design/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_login.setIcon(icon25)
        self.pushButton_login.setIconSize(QSize(22, 22))

        self.gridLayout_28.addWidget(self.pushButton_login, 6, 0, 1, 2)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_25, 5, 0, 1, 2)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_24, 2, 0, 1, 2)


        self.gridLayout_25.addLayout(self.gridLayout_28, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.page_login)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_27 = QGridLayout(self.widget_2)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_18 = QLabel(self.widget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setPixmap(QPixmap(u":/web_icons/icons/web_icons/group0.svg"))

        self.gridLayout_27.addWidget(self.label_18, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_login)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.gridLayout_75 = QGridLayout(self.page_16)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.log_agent = QTextEdit(self.page_16)
        self.log_agent.setObjectName(u"log_agent")
        self.log_agent.setMinimumSize(QSize(0, 0))
        self.log_agent.setMaximumSize(QSize(16777215, 16777215))
        self.log_agent.setStyleSheet(u"            QTextEdit {\n"
"          \n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"                font-family: Arial;\n"
"                font-size: 14px;\n"
"            }")

        self.gridLayout_75.addWidget(self.log_agent, 3, 0, 1, 1)

        self.TasksView_agent = QTreeView(self.page_16)
        self.TasksView_agent.setObjectName(u"TasksView_agent")
        self.TasksView_agent.setStyleSheet(u"QTreeView {\n"
"    background-color: #424242;  /* Cor de fundo escura */\n"
"    color: #dcdcdc;  /* Cor do texto */\n"
"    border: 1px solid #333;  /* Borda sutil ao redor do widget */\n"
"    alternate-background-color: #2c2c2c;  /* Cor alternada das linhas */\n"
"    selection-background-color: #4b6eaf;  /* Cor de fundo para o item selecionado */\n"
"    selection-color: #ffffff;  /* Cor do texto do item selecionado */\n"
"    show-decoration-selected: 1;  /* Mostrar o estilo de sele\u00e7\u00e3o completo */\n"
"    outline: none;  /* Remove a borda do foco */\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    height: 25px;  /* Define a altura dos itens */\n"
"    padding: 5px;  /* Espa\u00e7amento dentro de cada item */\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background-color: #3c3f41;  /* Cor de fundo ao passar o mouse */\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    background-color: #4b6eaf;  /* Cor de fundo do item selecionado */\n"
"    color: #ffffff;  /* Cor do texto do item selecionado */\n"
"}\n"
""
                        "\n"
"QTreeView::branch:open:has-children {\n"
"    image: url(':/font_awesome_solid/icons/font_awesome/solid/list-check.png');  /* \u00cdcone de ramo aberto (substitua pelo caminho do seu \u00edcone) */\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children {\n"
"    image: url(':/icons/branch_closed.png');  /* \u00cdcone de ramo fechado (substitua pelo caminho do seu \u00edcone) */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #3c3f41;  /* Cor de fundo do cabe\u00e7alho */\n"
"    color: #dcdcdc;  /* Cor do texto do cabe\u00e7alho */\n"
"    padding: 4px;\n"
"    border: 1px solid #333;  /* Borda do cabe\u00e7alho */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #2c2c2c;\n"
"    width: 12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #4b6eaf;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.TasksView_agent.setFrameShape(QFrame.NoFrame)
        self.TasksView_agent.setFrameShadow(QFrame.Plain)

        self.gridLayout_75.addWidget(self.TasksView_agent, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.page_16)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_71 = QGridLayout(self.groupBox)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_73 = QGridLayout()
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.verticalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_73.addItem(self.verticalSpacer_15, 3, 0, 1, 1)

        self.Agent_ID = QLabel(self.groupBox)
        self.Agent_ID.setObjectName(u"Agent_ID")
        self.Agent_ID.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_73.addWidget(self.Agent_ID, 0, 0, 1, 1)

        self.Agent_Thread = QLabel(self.groupBox)
        self.Agent_Thread.setObjectName(u"Agent_Thread")
        self.Agent_Thread.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_73.addWidget(self.Agent_Thread, 1, 0, 1, 1)

        self.Agent_Total_Report = QLabel(self.groupBox)
        self.Agent_Total_Report.setObjectName(u"Agent_Total_Report")
        self.Agent_Total_Report.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_73.addWidget(self.Agent_Total_Report, 2, 0, 1, 1)

        self.gridLayout_72 = QGridLayout()
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.checkBox_telegram_agent = QCustomCheckBox(self.groupBox)
        self.checkBox_telegram_agent.setObjectName(u"checkBox_telegram_agent")
        self.checkBox_telegram_agent.setMinimumSize(QSize(0, 20))

        self.gridLayout_72.addWidget(self.checkBox_telegram_agent, 3, 0, 1, 1)

        self.checkBox_discord_agent = QCustomCheckBox(self.groupBox)
        self.checkBox_discord_agent.setObjectName(u"checkBox_discord_agent")
        self.checkBox_discord_agent.setMinimumSize(QSize(0, 20))

        self.gridLayout_72.addWidget(self.checkBox_discord_agent, 1, 0, 1, 1)

        self.checkBox_gmail_agent = QCustomCheckBox(self.groupBox)
        self.checkBox_gmail_agent.setObjectName(u"checkBox_gmail_agent")
        self.checkBox_gmail_agent.setMinimumSize(QSize(0, 20))
        self.checkBox_gmail_agent.setChecked(True)

        self.gridLayout_72.addWidget(self.checkBox_gmail_agent, 0, 0, 1, 1)


        self.gridLayout_73.addLayout(self.gridLayout_72, 4, 0, 1, 1)


        self.gridLayout_71.addLayout(self.gridLayout_73, 0, 0, 1, 1)


        self.gridLayout_75.addWidget(self.groupBox, 1, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_75.addItem(self.verticalSpacer_16, 0, 0, 1, 1)

        self.gridLayout_74 = QGridLayout()
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.html_chat = QTextEdit(self.page_16)
        self.html_chat.setObjectName(u"html_chat")
        self.html_chat.setMinimumSize(QSize(200, 0))
        self.html_chat.setMaximumSize(QSize(16777215, 16777215))
        self.html_chat.setStyleSheet(u"            QTextEdit {\n"
"          \n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"                font-family: Arial;\n"
"                font-size: 14px;\n"
"            }")

        self.gridLayout_74.addWidget(self.html_chat, 1, 0, 1, 3)

        self.mensage_input = QTextEdit(self.page_16)
        self.mensage_input.setObjectName(u"mensage_input")
        sizePolicy2.setHeightForWidth(self.mensage_input.sizePolicy().hasHeightForWidth())
        self.mensage_input.setSizePolicy(sizePolicy2)
        self.mensage_input.setMinimumSize(QSize(312, 48))
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

        self.gridLayout_74.addWidget(self.mensage_input, 2, 0, 1, 1)

        self.send_mensage = QCustomQPushButton(self.page_16)
        self.send_mensage.setObjectName(u"send_mensage")
        self.send_mensage.setStyleSheet(u"            QPushButton {\n"
"                background-color: white;\n"
"\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 13px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon26 = QIcon()
        icon26.addFile(u":/feather/icons/feather/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_mensage.setIcon(icon26)
        self.send_mensage.setIconSize(QSize(27, 47))

        self.gridLayout_74.addWidget(self.send_mensage, 2, 1, 1, 1)

        self.label_hello_2 = QLabel(self.page_16)
        self.label_hello_2.setObjectName(u"label_hello_2")
        sizePolicy.setHeightForWidth(self.label_hello_2.sizePolicy().hasHeightForWidth())
        self.label_hello_2.setSizePolicy(sizePolicy)
        self.label_hello_2.setMinimumSize(QSize(0, 0))
        self.label_hello_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_hello_2.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_74.addWidget(self.label_hello_2, 0, 0, 1, 3)


        self.gridLayout_75.addLayout(self.gridLayout_74, 0, 1, 4, 1)

        self.stackedWidget.addWidget(self.page_16)
        self.groupBox.raise_()
        self.log_agent.raise_()
        self.TasksView_agent.raise_()
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.gridLayout_62 = QGridLayout(self.page_15)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.TasksView = QTreeView(self.page_15)
        self.TasksView.setObjectName(u"TasksView")
        self.TasksView.setStyleSheet(u"QTreeView {\n"
"    background-color: #424242;  /* Cor de fundo escura */\n"
"    color: #dcdcdc;  /* Cor do texto */\n"
"    border: 1px solid #333;  /* Borda sutil ao redor do widget */\n"
"    alternate-background-color: #2c2c2c;  /* Cor alternada das linhas */\n"
"    selection-background-color: #4b6eaf;  /* Cor de fundo para o item selecionado */\n"
"    selection-color: #ffffff;  /* Cor do texto do item selecionado */\n"
"    show-decoration-selected: 1;  /* Mostrar o estilo de sele\u00e7\u00e3o completo */\n"
"    outline: none;  /* Remove a borda do foco */\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    height: 25px;  /* Define a altura dos itens */\n"
"    padding: 5px;  /* Espa\u00e7amento dentro de cada item */\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background-color: #3c3f41;  /* Cor de fundo ao passar o mouse */\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    background-color: #4b6eaf;  /* Cor de fundo do item selecionado */\n"
"    color: #ffffff;  /* Cor do texto do item selecionado */\n"
"}\n"
""
                        "\n"
"QTreeView::branch:open:has-children {\n"
"    image: url(':/font_awesome_solid/icons/font_awesome/solid/list-check.png');  /* \u00cdcone de ramo aberto (substitua pelo caminho do seu \u00edcone) */\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children {\n"
"    image: url(':/icons/branch_closed.png');  /* \u00cdcone de ramo fechado (substitua pelo caminho do seu \u00edcone) */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #3c3f41;  /* Cor de fundo do cabe\u00e7alho */\n"
"    color: #dcdcdc;  /* Cor do texto do cabe\u00e7alho */\n"
"    padding: 4px;\n"
"    border: 1px solid #333;  /* Borda do cabe\u00e7alho */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #2c2c2c;\n"
"    width: 12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #4b6eaf;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.TasksView.setFrameShape(QFrame.NoFrame)
        self.TasksView.setFrameShadow(QFrame.Plain)

        self.gridLayout_62.addWidget(self.TasksView, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_15)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_66 = QGridLayout(self.page_7)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_63 = QGridLayout()
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.widget_Tasks_Created = roundProgressBar(self.page_7)
        self.widget_Tasks_Created.setObjectName(u"widget_Tasks_Created")
        self.widget_Tasks_Created.setMinimumSize(QSize(0, 200))
        self.widget_Tasks_Created.setMaximumSize(QSize(200, 200))
        self.widget_Tasks_Created.setStyleSheet(u"")

        self.gridLayout_63.addWidget(self.widget_Tasks_Created, 0, 1, 1, 1)

        self.label_31 = QLabel(self.page_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setIndent(35)

        self.gridLayout_63.addWidget(self.label_31, 0, 0, 1, 1)


        self.gridLayout_66.addLayout(self.gridLayout_63, 0, 0, 1, 1)

        self.gridLayout_64 = QGridLayout()
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.label_55 = QLabel(self.page_7)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setIndent(35)

        self.gridLayout_64.addWidget(self.label_55, 0, 0, 1, 1)

        self.widget_Tasks_Running = roundProgressBar(self.page_7)
        self.widget_Tasks_Running.setObjectName(u"widget_Tasks_Running")
        self.widget_Tasks_Running.setMinimumSize(QSize(0, 200))
        self.widget_Tasks_Running.setMaximumSize(QSize(200, 200))
        self.widget_Tasks_Running.setStyleSheet(u"")

        self.gridLayout_64.addWidget(self.widget_Tasks_Running, 0, 1, 1, 1)


        self.gridLayout_66.addLayout(self.gridLayout_64, 0, 1, 1, 1)

        self.gridLayout_65 = QGridLayout()
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.label_56 = QLabel(self.page_7)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setIndent(35)

        self.gridLayout_65.addWidget(self.label_56, 0, 0, 1, 1)

        self.widget_Tasks_Completed = roundProgressBar(self.page_7)
        self.widget_Tasks_Completed.setObjectName(u"widget_Tasks_Completed")
        self.widget_Tasks_Completed.setMinimumSize(QSize(0, 200))
        self.widget_Tasks_Completed.setMaximumSize(QSize(200, 200))
        self.widget_Tasks_Completed.setStyleSheet(u"")

        self.gridLayout_65.addWidget(self.widget_Tasks_Completed, 0, 1, 1, 1)


        self.gridLayout_66.addLayout(self.gridLayout_65, 0, 2, 1, 1)

        self.verticalSpacer_37 = QSpacerItem(846, 365, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_66.addItem(self.verticalSpacer_37, 1, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_7)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_13, 1, 1, 1, 3)

        self.horizontalSpacer_15 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_15, 1, 5, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_6, 1, 7, 1, 1)

        self.Mode_1_long_video = QPushButton(self.page_3)
        self.Mode_1_long_video.setObjectName(u"Mode_1_long_video")
        self.Mode_1_long_video.setMinimumSize(QSize(180, 35))
        self.Mode_1_long_video.setMaximumSize(QSize(180, 35))
        self.Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
" color: #1a1e29;\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.Mode_1_long_video.setIcon(icon22)
        self.Mode_1_long_video.setIconSize(QSize(31, 38))

        self.gridLayout_17.addWidget(self.Mode_1_long_video, 1, 6, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_12, 0, 0, 1, 8)

        self.verticalSpacer_13 = QSpacerItem(20, 14, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_13, 2, 0, 1, 8)

        self.Mode_Batch_processing = QPushButton(self.page_3)
        self.Mode_Batch_processing.setObjectName(u"Mode_Batch_processing")
        self.Mode_Batch_processing.setMinimumSize(QSize(180, 35))
        self.Mode_Batch_processing.setMaximumSize(QSize(180, 35))
        self.Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
" color: #1a1e29;\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.Mode_Batch_processing.setIcon(icon22)
        self.Mode_Batch_processing.setIconSize(QSize(31, 38))

        self.gridLayout_17.addWidget(self.Mode_Batch_processing, 1, 4, 1, 1)

        self.Mode_Shortify = QPushButton(self.page_3)
        self.Mode_Shortify.setObjectName(u"Mode_Shortify")
        self.Mode_Shortify.setMinimumSize(QSize(137, 35))
        self.Mode_Shortify.setMaximumSize(QSize(137, 35))
        self.Mode_Shortify.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
" color: #1a1e29;\n"
"  font-size: 12px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.Mode_Shortify.setIcon(icon22)
        self.Mode_Shortify.setIconSize(QSize(31, 38))

        self.gridLayout_17.addWidget(self.Mode_Shortify, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_17, 0, 0, 1, 1)

        self.stackedWidget_Main = QCustomQStackedWidget(self.page_3)
        self.stackedWidget_Main.setObjectName(u"stackedWidget_Main")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget_Main.sizePolicy().hasHeightForWidth())
        self.stackedWidget_Main.setSizePolicy(sizePolicy3)
        self.stackedWidget_Main.setMinimumSize(QSize(0, 0))
        self.stackedWidget_Main.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.stackedWidget_Main.setFrameShape(QFrame.NoFrame)
        self.page_Batch_processing = QWidget()
        self.page_Batch_processing.setObjectName(u"page_Batch_processing")
        self.gridLayout_7 = QGridLayout(self.page_Batch_processing)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_70 = QGridLayout()
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.Captions_PrimaryColour_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Captions_PrimaryColour_Mode_Batch_processing.setObjectName(u"Captions_PrimaryColour_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Captions_PrimaryColour_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Captions_PrimaryColour_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Captions_PrimaryColour_Mode_Batch_processing.setMinimumSize(QSize(215, 28))
        self.Captions_PrimaryColour_Mode_Batch_processing.setMaximumSize(QSize(215, 28))
        self.Captions_PrimaryColour_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_PrimaryColour_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_PrimaryColour_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_70.addWidget(self.Captions_PrimaryColour_Mode_Batch_processing, 6, 2, 1, 1)

        self.label_106 = QLabel(self.page_Batch_processing)
        self.label_106.setObjectName(u"label_106")
        sizePolicy3.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy3)
        self.label_106.setMinimumSize(QSize(0, 0))
        self.label_106.setMaximumSize(QSize(16777215, 16777215))
        self.label_106.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_106, 8, 1, 1, 1)

        self.label_91 = QLabel(self.page_Batch_processing)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_91.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_91.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_91, 4, 0, 1, 1)

        self.label_105 = QLabel(self.page_Batch_processing)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_105, 6, 1, 1, 1)

        self.label_107 = QLabel(self.page_Batch_processing)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_107, 4, 1, 1, 1)

        self.Captions_BackColour_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Captions_BackColour_Mode_Batch_processing.setObjectName(u"Captions_BackColour_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Captions_BackColour_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Captions_BackColour_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Captions_BackColour_Mode_Batch_processing.setMinimumSize(QSize(215, 28))
        self.Captions_BackColour_Mode_Batch_processing.setMaximumSize(QSize(215, 28))
        self.Captions_BackColour_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_BackColour_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_BackColour_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_70.addWidget(self.Captions_BackColour_Mode_Batch_processing, 13, 2, 1, 1)

        self.Captions_Bold_Bool_Mode_Batch_processing = QCustomCheckBox(self.page_Batch_processing)
        self.Captions_Bold_Bool_Mode_Batch_processing.setObjectName(u"Captions_Bold_Bool_Mode_Batch_processing")
        self.Captions_Bold_Bool_Mode_Batch_processing.setMinimumSize(QSize(182, 20))
        self.Captions_Bold_Bool_Mode_Batch_processing.setMaximumSize(QSize(182, 20))
        self.Captions_Bold_Bool_Mode_Batch_processing.setIconSize(QSize(16, 16))
        self.Captions_Bold_Bool_Mode_Batch_processing.setChecked(True)

        self.gridLayout_70.addWidget(self.Captions_Bold_Bool_Mode_Batch_processing, 15, 2, 1, 1)

        self.Captions_Underline_Bool_Mode_Batch_processing = QCustomCheckBox(self.page_Batch_processing)
        self.Captions_Underline_Bool_Mode_Batch_processing.setObjectName(u"Captions_Underline_Bool_Mode_Batch_processing")
        self.Captions_Underline_Bool_Mode_Batch_processing.setMinimumSize(QSize(182, 20))
        self.Captions_Underline_Bool_Mode_Batch_processing.setMaximumSize(QSize(182, 20))

        self.gridLayout_70.addWidget(self.Captions_Underline_Bool_Mode_Batch_processing, 20, 2, 1, 1)

        self.Captions_Italic_Bool_Mode_Batch_processing = QCustomCheckBox(self.page_Batch_processing)
        self.Captions_Italic_Bool_Mode_Batch_processing.setObjectName(u"Captions_Italic_Bool_Mode_Batch_processing")
        self.Captions_Italic_Bool_Mode_Batch_processing.setMinimumSize(QSize(182, 20))
        self.Captions_Italic_Bool_Mode_Batch_processing.setMaximumSize(QSize(182, 20))

        self.gridLayout_70.addWidget(self.Captions_Italic_Bool_Mode_Batch_processing, 19, 2, 1, 1)

        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.setObjectName(u"Captions_Reveal_Effect_Final_Color_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.setMinimumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.setMaximumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_70.addWidget(self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing, 24, 2, 1, 1)

        self.label_92 = QLabel(self.page_Batch_processing)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_92.setPixmap(QPixmap(u":/material_design/icons/material_design/invert_colors.png"))
        self.label_92.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_92, 24, 0, 1, 1)

        self.label_108 = QLabel(self.page_Batch_processing)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(0, 35))
        self.label_108.setMaximumSize(QSize(16777215, 35))
        self.label_108.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_108, 24, 1, 1, 1)

        self.label_93 = QLabel(self.page_Batch_processing)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_93.setPixmap(QPixmap(u":/material_design/icons/material_design/align_horizontal_left.png"))
        self.label_93.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_93, 2, 0, 1, 1)

        self.label_94 = QLabel(self.page_Batch_processing)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_94.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_94.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_94, 8, 0, 1, 1)

        self.label_95 = QLabel(self.page_Batch_processing)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_95.setPixmap(QPixmap(u":/material_design/icons/material_design/format_color_fill.png"))
        self.label_95.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_95, 23, 0, 1, 1)

        self.label_96 = QLabel(self.page_Batch_processing)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_96.setPixmap(QPixmap(u":/material_design/icons/material_design/format_bold.png"))
        self.label_96.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_96, 15, 0, 1, 1)

        self.label_109 = QLabel(self.page_Batch_processing)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_109, 13, 1, 1, 1)

        self.label_97 = QLabel(self.page_Batch_processing)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_97.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_97.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_97, 13, 0, 1, 1)

        self.label_111 = QLabel(self.page_Batch_processing)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_111, 2, 1, 1, 1)

        self.selector_BackColour_Captions_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_BackColour_Captions_Mode_Batch_processing.setObjectName(u"selector_BackColour_Captions_Mode_Batch_processing")
        self.selector_BackColour_Captions_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_BackColour_Captions_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_BackColour_Captions_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon27 = QIcon()
        icon27.addFile(u":/material_design/icons/material_design/color_lens.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selector_BackColour_Captions_Mode_Batch_processing.setIcon(icon27)

        self.gridLayout_70.addWidget(self.selector_BackColour_Captions_Mode_Batch_processing, 13, 3, 1, 1)

        self.Captions_Fontsize_Mode_Batch_processing = QSpinBox(self.page_Batch_processing)
        self.Captions_Fontsize_Mode_Batch_processing.setObjectName(u"Captions_Fontsize_Mode_Batch_processing")
        self.Captions_Fontsize_Mode_Batch_processing.setMinimumSize(QSize(215, 0))
        self.Captions_Fontsize_Mode_Batch_processing.setMaximumSize(QSize(215, 16777215))
        self.Captions_Fontsize_Mode_Batch_processing.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Fontsize_Mode_Batch_processing.setMinimum(8)

        self.gridLayout_70.addWidget(self.Captions_Fontsize_Mode_Batch_processing, 4, 2, 1, 2)

        self.Captions_Alignment_Mode_Batch_processing = QSpinBox(self.page_Batch_processing)
        self.Captions_Alignment_Mode_Batch_processing.setObjectName(u"Captions_Alignment_Mode_Batch_processing")
        self.Captions_Alignment_Mode_Batch_processing.setMinimumSize(QSize(215, 0))
        self.Captions_Alignment_Mode_Batch_processing.setMaximumSize(QSize(215, 16777215))
        self.Captions_Alignment_Mode_Batch_processing.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Alignment_Mode_Batch_processing.setMinimum(1)

        self.gridLayout_70.addWidget(self.Captions_Alignment_Mode_Batch_processing, 2, 2, 1, 2)

        self.selector_OutlineColour_Captions_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_OutlineColour_Captions_Mode_Batch_processing.setObjectName(u"selector_OutlineColour_Captions_Mode_Batch_processing")
        self.selector_OutlineColour_Captions_Mode_Batch_processing.setMinimumSize(QSize(20, 21))
        self.selector_OutlineColour_Captions_Mode_Batch_processing.setMaximumSize(QSize(22, 25))
        self.selector_OutlineColour_Captions_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_OutlineColour_Captions_Mode_Batch_processing.setIcon(icon27)

        self.gridLayout_70.addWidget(self.selector_OutlineColour_Captions_Mode_Batch_processing, 11, 3, 1, 1)

        self.Captions_OutlineColour_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Captions_OutlineColour_Mode_Batch_processing.setObjectName(u"Captions_OutlineColour_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Captions_OutlineColour_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Captions_OutlineColour_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Captions_OutlineColour_Mode_Batch_processing.setMinimumSize(QSize(215, 28))
        self.Captions_OutlineColour_Mode_Batch_processing.setMaximumSize(QSize(215, 28))
        self.Captions_OutlineColour_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_OutlineColour_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_OutlineColour_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_70.addWidget(self.Captions_OutlineColour_Mode_Batch_processing, 11, 2, 1, 1)

        self.label_98 = QLabel(self.page_Batch_processing)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_98.setPixmap(QPixmap(u":/material_design/icons/material_design/edit.png"))
        self.label_98.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_98, 6, 0, 1, 1)

        self.label_99 = QLabel(self.page_Batch_processing)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_99.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_99.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_99, 11, 0, 1, 1)

        self.selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing.setObjectName(u"selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing")
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing.setIcon(icon27)

        self.gridLayout_70.addWidget(self.selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing, 24, 3, 1, 1)

        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.setObjectName(u"Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.setMinimumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.setMaximumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_70.addWidget(self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing, 23, 2, 1, 1)

        self.label_125 = QLabel(self.page_Batch_processing)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(0, 35))
        self.label_125.setMaximumSize(QSize(16777215, 35))
        self.label_125.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_125, 23, 1, 1, 1)

        self.verticalSpacer_82 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_82, 1, 0, 1, 4)

        self.verticalSpacer_83 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_83, 3, 1, 1, 1)

        self.verticalSpacer_84 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_84, 7, 1, 1, 1)

        self.verticalSpacer_85 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_85, 5, 1, 1, 1)

        self.verticalSpacer_86 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_86, 9, 1, 1, 1)

        self.verticalSpacer_87 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_87, 12, 1, 1, 1)

        self.verticalSpacer_88 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_88, 14, 1, 1, 1)

        self.verticalSpacer_89 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_89, 16, 1, 1, 1)

        self.verticalSpacer_90 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_70.addItem(self.verticalSpacer_90, 18, 1, 1, 1)

        self.Captions_Outline_Mode_Batch_processing = QSpinBox(self.page_Batch_processing)
        self.Captions_Outline_Mode_Batch_processing.setObjectName(u"Captions_Outline_Mode_Batch_processing")
        self.Captions_Outline_Mode_Batch_processing.setMinimumSize(QSize(215, 0))
        self.Captions_Outline_Mode_Batch_processing.setMaximumSize(QSize(215, 16777215))
        self.Captions_Outline_Mode_Batch_processing.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Outline_Mode_Batch_processing.setMinimum(3)

        self.gridLayout_70.addWidget(self.Captions_Outline_Mode_Batch_processing, 21, 2, 1, 1)

        self.label_100 = QLabel(self.page_Batch_processing)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_100.setPixmap(QPixmap(u":/material_design/icons/material_design/format_underlined.png"))
        self.label_100.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_100, 20, 0, 1, 1)

        self.label_115 = QLabel(self.page_Batch_processing)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_115, 20, 1, 1, 1)

        self.label_101 = QLabel(self.page_Batch_processing)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_101.setPixmap(QPixmap(u":/material_design/icons/material_design/closed_caption.png"))
        self.label_101.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_101, 0, 0, 1, 1)

        self.label_mediabase_73 = QLabel(self.page_Batch_processing)
        self.label_mediabase_73.setObjectName(u"label_mediabase_73")
        self.label_mediabase_73.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_mediabase_73, 0, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_70.addItem(self.horizontalSpacer_26, 0, 4, 25, 1)

        self.Captions_FontName_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Captions_FontName_Mode_Batch_processing.setObjectName(u"Captions_FontName_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Captions_FontName_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Captions_FontName_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Captions_FontName_Mode_Batch_processing.setMinimumSize(QSize(215, 28))
        self.Captions_FontName_Mode_Batch_processing.setMaximumSize(QSize(215, 28))
        self.Captions_FontName_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_FontName_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_FontName_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_70.addWidget(self.Captions_FontName_Mode_Batch_processing, 0, 2, 1, 1)

        self.selector_Captions_FontName_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_Captions_FontName_Mode_Batch_processing.setObjectName(u"selector_Captions_FontName_Mode_Batch_processing")
        self.selector_Captions_FontName_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_Captions_FontName_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_Captions_FontName_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon28 = QIcon()
        icon28.addFile(u":/font_awesome/icons/font_awesome/font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selector_Captions_FontName_Mode_Batch_processing.setIcon(icon28)

        self.gridLayout_70.addWidget(self.selector_Captions_FontName_Mode_Batch_processing, 0, 3, 1, 1)

        self.label_102 = QLabel(self.page_Batch_processing)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_102.setPixmap(QPixmap(u":/material_design/icons/material_design/format_italic.png"))
        self.label_102.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_102, 19, 0, 1, 1)

        self.Captions_Shadow_Bool_Mode_Batch_processing = QCustomCheckBox(self.page_Batch_processing)
        self.Captions_Shadow_Bool_Mode_Batch_processing.setObjectName(u"Captions_Shadow_Bool_Mode_Batch_processing")
        self.Captions_Shadow_Bool_Mode_Batch_processing.setMinimumSize(QSize(214, 20))
        self.Captions_Shadow_Bool_Mode_Batch_processing.setMaximumSize(QSize(214, 20))
        self.Captions_Shadow_Bool_Mode_Batch_processing.setIconSize(QSize(16, 16))
        self.Captions_Shadow_Bool_Mode_Batch_processing.setChecked(True)

        self.gridLayout_70.addWidget(self.Captions_Shadow_Bool_Mode_Batch_processing, 17, 2, 1, 1)

        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing.setObjectName(u"selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing")
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing.setIcon(icon27)

        self.gridLayout_70.addWidget(self.selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing, 23, 3, 1, 1)

        self.label_113 = QLabel(self.page_Batch_processing)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_113, 19, 1, 1, 1)

        self.label_126 = QLabel(self.page_Batch_processing)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_126, 17, 1, 1, 1)

        self.selector_PrimaryColour_Captions_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_PrimaryColour_Captions_Mode_Batch_processing.setObjectName(u"selector_PrimaryColour_Captions_Mode_Batch_processing")
        self.selector_PrimaryColour_Captions_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_PrimaryColour_Captions_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_PrimaryColour_Captions_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_PrimaryColour_Captions_Mode_Batch_processing.setIcon(icon27)

        self.gridLayout_70.addWidget(self.selector_PrimaryColour_Captions_Mode_Batch_processing, 6, 3, 1, 1)

        self.label_103 = QLabel(self.page_Batch_processing)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_103.setPixmap(QPixmap(u":/material_design/icons/material_design/brush.png"))
        self.label_103.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_103, 17, 0, 1, 1)

        self.Captions_SecondaryColour_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Captions_SecondaryColour_Mode_Batch_processing.setObjectName(u"Captions_SecondaryColour_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Captions_SecondaryColour_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Captions_SecondaryColour_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Captions_SecondaryColour_Mode_Batch_processing.setMinimumSize(QSize(215, 28))
        self.Captions_SecondaryColour_Mode_Batch_processing.setMaximumSize(QSize(215, 28))
        self.Captions_SecondaryColour_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_SecondaryColour_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_SecondaryColour_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_70.addWidget(self.Captions_SecondaryColour_Mode_Batch_processing, 8, 2, 1, 1)

        self.label_123 = QLabel(self.page_Batch_processing)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_123, 15, 1, 1, 1)

        self.label_110 = QLabel(self.page_Batch_processing)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_110, 11, 1, 1, 1)

        self.selector_SecondaryColour_Captions_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_SecondaryColour_Captions_Mode_Batch_processing.setObjectName(u"selector_SecondaryColour_Captions_Mode_Batch_processing")
        self.selector_SecondaryColour_Captions_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_SecondaryColour_Captions_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_SecondaryColour_Captions_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_SecondaryColour_Captions_Mode_Batch_processing.setIcon(icon27)

        self.gridLayout_70.addWidget(self.selector_SecondaryColour_Captions_Mode_Batch_processing, 8, 3, 1, 1)

        self.label_104 = QLabel(self.page_Batch_processing)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_104.setPixmap(QPixmap(u":/material_design/icons/material_design/text_snippet.png"))
        self.label_104.setScaledContents(False)

        self.gridLayout_70.addWidget(self.label_104, 21, 0, 1, 1)

        self.label_127 = QLabel(self.page_Batch_processing)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_70.addWidget(self.label_127, 21, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_70, 1, 1, 1, 1)

        self.Start_Batch_processing = QPushButton(self.page_Batch_processing)
        self.Start_Batch_processing.setObjectName(u"Start_Batch_processing")
        self.Start_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.036em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon29 = QIcon()
        icon29.addFile(u":/mediacuts/icons/mediacuts/icons8-alinhar-\u00e0-direita-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_Batch_processing.setIcon(icon29)
        self.Start_Batch_processing.setIconSize(QSize(35, 34))
        self.Start_Batch_processing.setAutoRepeatDelay(300)

        self.gridLayout_7.addWidget(self.Start_Batch_processing, 0, 0, 1, 2)

        self.gridLayout_69 = QGridLayout()
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.gridLayout_69.setHorizontalSpacing(0)
        self.gridLayout_69.setVerticalSpacing(6)
        self.gridLayout_69.setContentsMargins(0, 13, 4, 3)
        self.text_watermark_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.text_watermark_Mode_Batch_processing.setObjectName(u"text_watermark_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.text_watermark_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.text_watermark_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.text_watermark_Mode_Batch_processing.setMinimumSize(QSize(0, 28))
        self.text_watermark_Mode_Batch_processing.setMaximumSize(QSize(16777215, 28))
        self.text_watermark_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.text_watermark_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_watermark_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_69.addWidget(self.text_watermark_Mode_Batch_processing, 2, 3, 1, 1)

        self.verticalSpacer_64 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_69.addItem(self.verticalSpacer_64, 3, 0, 1, 5)

        self.label_65 = QLabel(self.page_Batch_processing)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_65.setPixmap(QPixmap(u":/material_design/icons/material_design/water_drop.png"))

        self.gridLayout_69.addWidget(self.label_65, 2, 0, 1, 1)

        self.label_122 = QLabel(self.page_Batch_processing)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_122, 2, 2, 1, 1)

        self.verticalSpacer_75 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_69.addItem(self.verticalSpacer_75, 0, 0, 1, 5)

        self.verticalSpacer_76 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_69.addItem(self.verticalSpacer_76, 9, 0, 1, 5)

        self.verticalSpacer_77 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_69.addItem(self.verticalSpacer_77, 15, 0, 1, 5)

        self.label_114 = QLabel(self.page_Batch_processing)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_114, 18, 2, 1, 1)

        self.Subtitle_Fontsize_Mode_Batch_processing = QSpinBox(self.page_Batch_processing)
        self.Subtitle_Fontsize_Mode_Batch_processing.setObjectName(u"Subtitle_Fontsize_Mode_Batch_processing")
        self.Subtitle_Fontsize_Mode_Batch_processing.setMinimumSize(QSize(155, 0))
        self.Subtitle_Fontsize_Mode_Batch_processing.setMaximumSize(QSize(155, 16777215))
        self.Subtitle_Fontsize_Mode_Batch_processing.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Subtitle_Fontsize_Mode_Batch_processing.setMinimum(21)
        self.Subtitle_Fontsize_Mode_Batch_processing.setMaximum(999)

        self.gridLayout_69.addWidget(self.Subtitle_Fontsize_Mode_Batch_processing, 19, 3, 1, 1)

        self.label_120 = QLabel(self.page_Batch_processing)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_120, 19, 2, 1, 1)

        self.label_119 = QLabel(self.page_Batch_processing)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(0, 28))
        self.label_119.setMaximumSize(QSize(16777215, 28))
        self.label_119.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_119, 20, 2, 1, 1)

        self.Subtitle_Vertical_Reference_Mode_Batch_processing = QSpinBox(self.page_Batch_processing)
        self.Subtitle_Vertical_Reference_Mode_Batch_processing.setObjectName(u"Subtitle_Vertical_Reference_Mode_Batch_processing")
        self.Subtitle_Vertical_Reference_Mode_Batch_processing.setMinimumSize(QSize(155, 0))
        self.Subtitle_Vertical_Reference_Mode_Batch_processing.setMaximumSize(QSize(155, 16777215))
        self.Subtitle_Vertical_Reference_Mode_Batch_processing.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Subtitle_Vertical_Reference_Mode_Batch_processing.setMinimum(2)
        self.Subtitle_Vertical_Reference_Mode_Batch_processing.setMaximum(999)
        self.Subtitle_Vertical_Reference_Mode_Batch_processing.setValue(6)

        self.gridLayout_69.addWidget(self.Subtitle_Vertical_Reference_Mode_Batch_processing, 20, 3, 1, 1)

        self.selector_Effects_subtitles_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_Effects_subtitles_Mode_Batch_processing.setObjectName(u"selector_Effects_subtitles_Mode_Batch_processing")
        self.selector_Effects_subtitles_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_Effects_subtitles_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_Effects_subtitles_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon30 = QIcon()
        icon30.addFile(u":/material_design/icons/material_design/colorize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selector_Effects_subtitles_Mode_Batch_processing.setIcon(icon30)

        self.gridLayout_69.addWidget(self.selector_Effects_subtitles_Mode_Batch_processing, 16, 4, 1, 1)

        self.verticalSpacer_78 = QSpacerItem(20, 44, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_69.addItem(self.verticalSpacer_78, 21, 0, 1, 5)

        self.label_82 = QLabel(self.page_Batch_processing)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_82.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_82.setScaledContents(False)

        self.gridLayout_69.addWidget(self.label_82, 20, 0, 1, 1)

        self.label_83 = QLabel(self.page_Batch_processing)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_83.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_83.setScaledContents(False)

        self.gridLayout_69.addWidget(self.label_83, 19, 0, 1, 1)

        self.selector_color_subtitles_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_color_subtitles_Mode_Batch_processing.setObjectName(u"selector_color_subtitles_Mode_Batch_processing")
        self.selector_color_subtitles_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_color_subtitles_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_color_subtitles_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_color_subtitles_Mode_Batch_processing.setIcon(icon27)

        self.gridLayout_69.addWidget(self.selector_color_subtitles_Mode_Batch_processing, 10, 4, 1, 1)

        self.label_84 = QLabel(self.page_Batch_processing)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_84.setPixmap(QPixmap(u":/material_design/icons/material_design/view_timeline.png"))

        self.gridLayout_69.addWidget(self.label_84, 13, 0, 1, 1)

        self.label_118 = QLabel(self.page_Batch_processing)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_118, 13, 2, 1, 1)

        self.Subtitle_Animation_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Subtitle_Animation_Mode_Batch_processing.setObjectName(u"Subtitle_Animation_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Subtitle_Animation_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Subtitle_Animation_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Subtitle_Animation_Mode_Batch_processing.setMinimumSize(QSize(152, 28))
        self.Subtitle_Animation_Mode_Batch_processing.setMaximumSize(QSize(152, 28))
        self.Subtitle_Animation_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Animation_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Animation_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_69.addWidget(self.Subtitle_Animation_Mode_Batch_processing, 13, 3, 1, 1)

        self.verticalSpacer_79 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_69.addItem(self.verticalSpacer_79, 7, 0, 1, 5)

        self.verticalSpacer_80 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_69.addItem(self.verticalSpacer_80, 12, 0, 1, 5)

        self.verticalSpacer_81 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_69.addItem(self.verticalSpacer_81, 17, 0, 1, 5)

        self.selector_animation_subtitles_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_animation_subtitles_Mode_Batch_processing.setObjectName(u"selector_animation_subtitles_Mode_Batch_processing")
        self.selector_animation_subtitles_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_animation_subtitles_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_animation_subtitles_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_animation_subtitles_Mode_Batch_processing.setIcon(icon13)

        self.gridLayout_69.addWidget(self.selector_animation_subtitles_Mode_Batch_processing, 13, 4, 1, 1)

        self.label_85 = QLabel(self.page_Batch_processing)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_85.setPixmap(QPixmap(u":/feather/icons/feather/video.png"))

        self.gridLayout_69.addWidget(self.label_85, 1, 0, 1, 1)

        self.upload_Video_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.upload_Video_Mode_Batch_processing.setObjectName(u"upload_Video_Mode_Batch_processing")
        self.upload_Video_Mode_Batch_processing.setMinimumSize(QSize(0, 31))
        self.upload_Video_Mode_Batch_processing.setMaximumSize(QSize(16777215, 31))
        self.upload_Video_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon31 = QIcon()
        icon31.addFile(u":/feather/icons/feather/film.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_Video_Mode_Batch_processing.setIcon(icon31)

        self.gridLayout_69.addWidget(self.upload_Video_Mode_Batch_processing, 1, 3, 1, 1)

        self.label_112 = QLabel(self.page_Batch_processing)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_112, 1, 2, 1, 1)

        self.label_117 = QLabel(self.page_Batch_processing)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_117, 10, 2, 1, 1)

        self.label_86 = QLabel(self.page_Batch_processing)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_86.setPixmap(QPixmap(u":/feather/icons/feather/image.png"))

        self.gridLayout_69.addWidget(self.label_86, 4, 0, 1, 1)

        self.Subtitle_Color_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Subtitle_Color_Mode_Batch_processing.setObjectName(u"Subtitle_Color_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Subtitle_Color_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Subtitle_Color_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Subtitle_Color_Mode_Batch_processing.setMinimumSize(QSize(152, 28))
        self.Subtitle_Color_Mode_Batch_processing.setMaximumSize(QSize(152, 28))
        self.Subtitle_Color_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Color_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Color_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_69.addWidget(self.Subtitle_Color_Mode_Batch_processing, 10, 3, 1, 1)

        self.label_116 = QLabel(self.page_Batch_processing)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_116, 4, 2, 1, 1)

        self.label_87 = QLabel(self.page_Batch_processing)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_87.setPixmap(QPixmap(u":/material_design/icons/material_design/timer.png"))

        self.gridLayout_69.addWidget(self.label_87, 8, 0, 1, 1)

        self.Cutting_seconds_Mode_Batch_processing = QSpinBox(self.page_Batch_processing)
        self.Cutting_seconds_Mode_Batch_processing.setObjectName(u"Cutting_seconds_Mode_Batch_processing")
        self.Cutting_seconds_Mode_Batch_processing.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Cutting_seconds_Mode_Batch_processing.setMinimum(60)
        self.Cutting_seconds_Mode_Batch_processing.setMaximum(999999999)

        self.gridLayout_69.addWidget(self.Cutting_seconds_Mode_Batch_processing, 8, 3, 1, 2)

        self.upload_image_watermark_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.upload_image_watermark_Mode_Batch_processing.setObjectName(u"upload_image_watermark_Mode_Batch_processing")
        self.upload_image_watermark_Mode_Batch_processing.setMinimumSize(QSize(0, 31))
        self.upload_image_watermark_Mode_Batch_processing.setMaximumSize(QSize(16777215, 31))
        self.upload_image_watermark_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon32 = QIcon()
        icon32.addFile(u":/feather/icons/feather/upload-cloud.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_image_watermark_Mode_Batch_processing.setIcon(icon32)

        self.gridLayout_69.addWidget(self.upload_image_watermark_Mode_Batch_processing, 4, 3, 1, 2)

        self.Subtitle_Effects_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Subtitle_Effects_Mode_Batch_processing.setObjectName(u"Subtitle_Effects_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Subtitle_Effects_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Subtitle_Effects_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Subtitle_Effects_Mode_Batch_processing.setMinimumSize(QSize(152, 28))
        self.Subtitle_Effects_Mode_Batch_processing.setMaximumSize(QSize(152, 28))
        self.Subtitle_Effects_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Effects_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Effects_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_69.addWidget(self.Subtitle_Effects_Mode_Batch_processing, 16, 3, 1, 1)

        self.label_88 = QLabel(self.page_Batch_processing)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_88.setPixmap(QPixmap(u":/material_design/icons/material_design/font_download.png"))
        self.label_88.setScaledContents(False)

        self.gridLayout_69.addWidget(self.label_88, 18, 0, 1, 1)

        self.Subtitle_FontName_Mode_Batch_processing = QTextEdit(self.page_Batch_processing)
        self.Subtitle_FontName_Mode_Batch_processing.setObjectName(u"Subtitle_FontName_Mode_Batch_processing")
        sizePolicy2.setHeightForWidth(self.Subtitle_FontName_Mode_Batch_processing.sizePolicy().hasHeightForWidth())
        self.Subtitle_FontName_Mode_Batch_processing.setSizePolicy(sizePolicy2)
        self.Subtitle_FontName_Mode_Batch_processing.setMinimumSize(QSize(152, 28))
        self.Subtitle_FontName_Mode_Batch_processing.setMaximumSize(QSize(152, 28))
        self.Subtitle_FontName_Mode_Batch_processing.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_FontName_Mode_Batch_processing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_FontName_Mode_Batch_processing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_69.addWidget(self.Subtitle_FontName_Mode_Batch_processing, 18, 3, 1, 1)

        self.label_124 = QLabel(self.page_Batch_processing)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_124, 16, 2, 1, 1)

        self.label_89 = QLabel(self.page_Batch_processing)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_89.setPixmap(QPixmap(u":/material_design/icons/material_design/format_color_text.png"))

        self.gridLayout_69.addWidget(self.label_89, 10, 0, 1, 1)

        self.label_121 = QLabel(self.page_Batch_processing)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_69.addWidget(self.label_121, 8, 2, 1, 1)

        self.label_90 = QLabel(self.page_Batch_processing)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_90.setPixmap(QPixmap(u":/material_design/icons/material_design/subtitles.png"))
        self.label_90.setScaledContents(False)

        self.gridLayout_69.addWidget(self.label_90, 16, 0, 1, 1)

        self.selector_FontName_subtitles_Mode_Batch_processing = QPushButton(self.page_Batch_processing)
        self.selector_FontName_subtitles_Mode_Batch_processing.setObjectName(u"selector_FontName_subtitles_Mode_Batch_processing")
        self.selector_FontName_subtitles_Mode_Batch_processing.setMinimumSize(QSize(25, 25))
        self.selector_FontName_subtitles_Mode_Batch_processing.setMaximumSize(QSize(25, 25))
        self.selector_FontName_subtitles_Mode_Batch_processing.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_FontName_subtitles_Mode_Batch_processing.setIcon(icon28)

        self.gridLayout_69.addWidget(self.selector_FontName_subtitles_Mode_Batch_processing, 18, 4, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_69.addItem(self.horizontalSpacer_25, 1, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_69, 1, 0, 1, 1)

        self.stackedWidget_Main.addWidget(self.page_Batch_processing)
        self.page_1_long_video = QWidget()
        self.page_1_long_video.setObjectName(u"page_1_long_video")
        self.gridLayout_15 = QGridLayout(self.page_1_long_video)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.Start_1_long_video = QPushButton(self.page_1_long_video)
        self.Start_1_long_video.setObjectName(u"Start_1_long_video")
        self.Start_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.036em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon33 = QIcon()
        icon33.addFile(u":/material_design/icons/material_design/video_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_1_long_video.setIcon(icon33)
        self.Start_1_long_video.setIconSize(QSize(35, 34))
        self.Start_1_long_video.setAutoRepeatDelay(300)

        self.gridLayout_15.addWidget(self.Start_1_long_video, 0, 0, 1, 2)

        self.gridLayout_67 = QGridLayout()
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setHorizontalSpacing(0)
        self.gridLayout_67.setVerticalSpacing(6)
        self.gridLayout_67.setContentsMargins(0, 13, 4, 3)
        self.text_watermark_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.text_watermark_Mode_1_long_video.setObjectName(u"text_watermark_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.text_watermark_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.text_watermark_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.text_watermark_Mode_1_long_video.setMinimumSize(QSize(0, 28))
        self.text_watermark_Mode_1_long_video.setMaximumSize(QSize(16777215, 28))
        self.text_watermark_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.text_watermark_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_watermark_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_67.addWidget(self.text_watermark_Mode_1_long_video, 2, 3, 1, 1)

        self.verticalSpacer_57 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_67.addItem(self.verticalSpacer_57, 3, 0, 1, 5)

        self.label_60 = QLabel(self.page_1_long_video)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_60.setPixmap(QPixmap(u":/material_design/icons/material_design/water_drop.png"))

        self.gridLayout_67.addWidget(self.label_60, 2, 0, 1, 1)

        self.label_mediabase_32 = QLabel(self.page_1_long_video)
        self.label_mediabase_32.setObjectName(u"label_mediabase_32")
        self.label_mediabase_32.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_32, 2, 2, 1, 1)

        self.verticalSpacer_62 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_67.addItem(self.verticalSpacer_62, 0, 0, 1, 5)

        self.verticalSpacer_61 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_67.addItem(self.verticalSpacer_61, 9, 0, 1, 5)

        self.verticalSpacer_63 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_67.addItem(self.verticalSpacer_63, 15, 0, 1, 5)

        self.label_mediabase_39 = QLabel(self.page_1_long_video)
        self.label_mediabase_39.setObjectName(u"label_mediabase_39")
        self.label_mediabase_39.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_39, 18, 2, 1, 1)

        self.Subtitle_Fontsize_Mode_1_long_video = QSpinBox(self.page_1_long_video)
        self.Subtitle_Fontsize_Mode_1_long_video.setObjectName(u"Subtitle_Fontsize_Mode_1_long_video")
        self.Subtitle_Fontsize_Mode_1_long_video.setMinimumSize(QSize(155, 0))
        self.Subtitle_Fontsize_Mode_1_long_video.setMaximumSize(QSize(155, 16777215))
        self.Subtitle_Fontsize_Mode_1_long_video.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Subtitle_Fontsize_Mode_1_long_video.setMinimum(21)
        self.Subtitle_Fontsize_Mode_1_long_video.setMaximum(999)

        self.gridLayout_67.addWidget(self.Subtitle_Fontsize_Mode_1_long_video, 19, 3, 1, 1)

        self.label_mediabase_40 = QLabel(self.page_1_long_video)
        self.label_mediabase_40.setObjectName(u"label_mediabase_40")
        self.label_mediabase_40.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_40, 19, 2, 1, 1)

        self.label_mediabase_41 = QLabel(self.page_1_long_video)
        self.label_mediabase_41.setObjectName(u"label_mediabase_41")
        self.label_mediabase_41.setMinimumSize(QSize(0, 28))
        self.label_mediabase_41.setMaximumSize(QSize(16777215, 28))
        self.label_mediabase_41.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_41, 20, 2, 1, 1)

        self.Subtitle_Vertical_Reference_Mode_1_long_video = QSpinBox(self.page_1_long_video)
        self.Subtitle_Vertical_Reference_Mode_1_long_video.setObjectName(u"Subtitle_Vertical_Reference_Mode_1_long_video")
        self.Subtitle_Vertical_Reference_Mode_1_long_video.setMinimumSize(QSize(155, 0))
        self.Subtitle_Vertical_Reference_Mode_1_long_video.setMaximumSize(QSize(155, 16777215))
        self.Subtitle_Vertical_Reference_Mode_1_long_video.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Subtitle_Vertical_Reference_Mode_1_long_video.setMinimum(2)
        self.Subtitle_Vertical_Reference_Mode_1_long_video.setMaximum(999)
        self.Subtitle_Vertical_Reference_Mode_1_long_video.setValue(6)

        self.gridLayout_67.addWidget(self.Subtitle_Vertical_Reference_Mode_1_long_video, 20, 3, 1, 1)

        self.selector_Effects_subtitles_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_Effects_subtitles_Mode_1_long_video.setObjectName(u"selector_Effects_subtitles_Mode_1_long_video")
        self.selector_Effects_subtitles_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_Effects_subtitles_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_Effects_subtitles_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Effects_subtitles_Mode_1_long_video.setIcon(icon30)

        self.gridLayout_67.addWidget(self.selector_Effects_subtitles_Mode_1_long_video, 16, 4, 1, 1)

        self.verticalSpacer_65 = QSpacerItem(20, 44, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_67.addItem(self.verticalSpacer_65, 21, 0, 1, 5)

        self.label_66 = QLabel(self.page_1_long_video)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_66.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_66.setScaledContents(False)

        self.gridLayout_67.addWidget(self.label_66, 20, 0, 1, 1)

        self.label_67 = QLabel(self.page_1_long_video)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_67.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_67.setScaledContents(False)

        self.gridLayout_67.addWidget(self.label_67, 19, 0, 1, 1)

        self.selector_color_subtitles_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_color_subtitles_Mode_1_long_video.setObjectName(u"selector_color_subtitles_Mode_1_long_video")
        self.selector_color_subtitles_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_color_subtitles_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_color_subtitles_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_color_subtitles_Mode_1_long_video.setIcon(icon27)

        self.gridLayout_67.addWidget(self.selector_color_subtitles_Mode_1_long_video, 10, 4, 1, 1)

        self.label_64 = QLabel(self.page_1_long_video)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_64.setPixmap(QPixmap(u":/material_design/icons/material_design/view_timeline.png"))

        self.gridLayout_67.addWidget(self.label_64, 13, 0, 1, 1)

        self.label_mediabase_37 = QLabel(self.page_1_long_video)
        self.label_mediabase_37.setObjectName(u"label_mediabase_37")
        self.label_mediabase_37.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_37, 13, 2, 1, 1)

        self.Subtitle_Animation_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Subtitle_Animation_Mode_1_long_video.setObjectName(u"Subtitle_Animation_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Subtitle_Animation_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Subtitle_Animation_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Subtitle_Animation_Mode_1_long_video.setMinimumSize(QSize(152, 28))
        self.Subtitle_Animation_Mode_1_long_video.setMaximumSize(QSize(152, 28))
        self.Subtitle_Animation_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Animation_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Animation_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_67.addWidget(self.Subtitle_Animation_Mode_1_long_video, 13, 3, 1, 1)

        self.verticalSpacer_58 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_67.addItem(self.verticalSpacer_58, 7, 0, 1, 5)

        self.verticalSpacer_59 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_67.addItem(self.verticalSpacer_59, 12, 0, 1, 5)

        self.verticalSpacer_60 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_67.addItem(self.verticalSpacer_60, 17, 0, 1, 5)

        self.selector_animation_subtitles_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_animation_subtitles_Mode_1_long_video.setObjectName(u"selector_animation_subtitles_Mode_1_long_video")
        self.selector_animation_subtitles_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_animation_subtitles_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_animation_subtitles_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_animation_subtitles_Mode_1_long_video.setIcon(icon13)

        self.gridLayout_67.addWidget(self.selector_animation_subtitles_Mode_1_long_video, 13, 4, 1, 1)

        self.label_63 = QLabel(self.page_1_long_video)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_63.setPixmap(QPixmap(u":/feather/icons/feather/video.png"))

        self.gridLayout_67.addWidget(self.label_63, 1, 0, 1, 1)

        self.upload_image_watermark_3 = QPushButton(self.page_1_long_video)
        self.upload_image_watermark_3.setObjectName(u"upload_image_watermark_3")
        self.upload_image_watermark_3.setMinimumSize(QSize(0, 31))
        self.upload_image_watermark_3.setMaximumSize(QSize(16777215, 31))
        self.upload_image_watermark_3.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon34 = QIcon()
        icon34.addFile(u":/font_awesome/icons/font_awesome/arrow-up-from-bracket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_image_watermark_3.setIcon(icon34)

        self.gridLayout_67.addWidget(self.upload_image_watermark_3, 1, 3, 1, 1)

        self.label_mediabase_34 = QLabel(self.page_1_long_video)
        self.label_mediabase_34.setObjectName(u"label_mediabase_34")
        self.label_mediabase_34.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_34, 1, 2, 1, 1)

        self.label_mediabase_31 = QLabel(self.page_1_long_video)
        self.label_mediabase_31.setObjectName(u"label_mediabase_31")
        self.label_mediabase_31.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_31, 10, 2, 1, 1)

        self.label_57 = QLabel(self.page_1_long_video)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_57.setPixmap(QPixmap(u":/feather/icons/feather/image.png"))

        self.gridLayout_67.addWidget(self.label_57, 4, 0, 1, 1)

        self.Subtitle_Color_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Subtitle_Color_Mode_1_long_video.setObjectName(u"Subtitle_Color_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Subtitle_Color_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Subtitle_Color_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Subtitle_Color_Mode_1_long_video.setMinimumSize(QSize(152, 28))
        self.Subtitle_Color_Mode_1_long_video.setMaximumSize(QSize(152, 28))
        self.Subtitle_Color_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Color_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Color_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_67.addWidget(self.Subtitle_Color_Mode_1_long_video, 10, 3, 1, 1)

        self.label_mediabase_33 = QLabel(self.page_1_long_video)
        self.label_mediabase_33.setObjectName(u"label_mediabase_33")
        self.label_mediabase_33.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_33, 4, 2, 1, 1)

        self.label_58 = QLabel(self.page_1_long_video)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_58.setPixmap(QPixmap(u":/material_design/icons/material_design/timer.png"))

        self.gridLayout_67.addWidget(self.label_58, 8, 0, 1, 1)

        self.Cutting_seconds_Mode_1_long_video = QSpinBox(self.page_1_long_video)
        self.Cutting_seconds_Mode_1_long_video.setObjectName(u"Cutting_seconds_Mode_1_long_video")
        self.Cutting_seconds_Mode_1_long_video.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Cutting_seconds_Mode_1_long_video.setMinimum(60)
        self.Cutting_seconds_Mode_1_long_video.setMaximum(999999999)

        self.gridLayout_67.addWidget(self.Cutting_seconds_Mode_1_long_video, 8, 3, 1, 2)

        self.upload_image_watermark_2 = QPushButton(self.page_1_long_video)
        self.upload_image_watermark_2.setObjectName(u"upload_image_watermark_2")
        self.upload_image_watermark_2.setMinimumSize(QSize(0, 31))
        self.upload_image_watermark_2.setMaximumSize(QSize(16777215, 31))
        self.upload_image_watermark_2.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.upload_image_watermark_2.setIcon(icon32)

        self.gridLayout_67.addWidget(self.upload_image_watermark_2, 4, 3, 1, 2)

        self.Subtitle_Effects_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Subtitle_Effects_Mode_1_long_video.setObjectName(u"Subtitle_Effects_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Subtitle_Effects_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Subtitle_Effects_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Subtitle_Effects_Mode_1_long_video.setMinimumSize(QSize(152, 28))
        self.Subtitle_Effects_Mode_1_long_video.setMaximumSize(QSize(152, 28))
        self.Subtitle_Effects_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Effects_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Effects_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_67.addWidget(self.Subtitle_Effects_Mode_1_long_video, 16, 3, 1, 1)

        self.label_59 = QLabel(self.page_1_long_video)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_59.setPixmap(QPixmap(u":/material_design/icons/material_design/font_download.png"))
        self.label_59.setScaledContents(False)

        self.gridLayout_67.addWidget(self.label_59, 18, 0, 1, 1)

        self.Subtitle_FontName_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Subtitle_FontName_Mode_1_long_video.setObjectName(u"Subtitle_FontName_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Subtitle_FontName_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Subtitle_FontName_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Subtitle_FontName_Mode_1_long_video.setMinimumSize(QSize(152, 28))
        self.Subtitle_FontName_Mode_1_long_video.setMaximumSize(QSize(152, 28))
        self.Subtitle_FontName_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_FontName_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_FontName_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_67.addWidget(self.Subtitle_FontName_Mode_1_long_video, 18, 3, 1, 1)

        self.label_mediabase_35 = QLabel(self.page_1_long_video)
        self.label_mediabase_35.setObjectName(u"label_mediabase_35")
        self.label_mediabase_35.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_35, 16, 2, 1, 1)

        self.label_61 = QLabel(self.page_1_long_video)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_61.setPixmap(QPixmap(u":/material_design/icons/material_design/format_color_text.png"))

        self.gridLayout_67.addWidget(self.label_61, 10, 0, 1, 1)

        self.label_mediabase_36 = QLabel(self.page_1_long_video)
        self.label_mediabase_36.setObjectName(u"label_mediabase_36")
        self.label_mediabase_36.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_67.addWidget(self.label_mediabase_36, 8, 2, 1, 1)

        self.label_62 = QLabel(self.page_1_long_video)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_62.setPixmap(QPixmap(u":/material_design/icons/material_design/subtitles.png"))
        self.label_62.setScaledContents(False)

        self.gridLayout_67.addWidget(self.label_62, 16, 0, 1, 1)

        self.selector_FontName_subtitles_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_FontName_subtitles_Mode_1_long_video.setObjectName(u"selector_FontName_subtitles_Mode_1_long_video")
        self.selector_FontName_subtitles_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_FontName_subtitles_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_FontName_subtitles_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_FontName_subtitles_Mode_1_long_video.setIcon(icon28)

        self.gridLayout_67.addWidget(self.selector_FontName_subtitles_Mode_1_long_video, 18, 4, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_67.addItem(self.horizontalSpacer_20, 1, 1, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_67, 1, 0, 1, 1)

        self.gridLayout_68 = QGridLayout()
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.Captions_PrimaryColour_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Captions_PrimaryColour_Mode_1_long_video.setObjectName(u"Captions_PrimaryColour_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Captions_PrimaryColour_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Captions_PrimaryColour_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Captions_PrimaryColour_Mode_1_long_video.setMinimumSize(QSize(215, 28))
        self.Captions_PrimaryColour_Mode_1_long_video.setMaximumSize(QSize(215, 28))
        self.Captions_PrimaryColour_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_PrimaryColour_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_PrimaryColour_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_68.addWidget(self.Captions_PrimaryColour_Mode_1_long_video, 6, 2, 1, 1)

        self.label_163 = QLabel(self.page_1_long_video)
        self.label_163.setObjectName(u"label_163")
        sizePolicy3.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy3)
        self.label_163.setMinimumSize(QSize(0, 0))
        self.label_163.setMaximumSize(QSize(16777215, 16777215))
        self.label_163.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_163, 8, 1, 1, 1)

        self.label_68 = QLabel(self.page_1_long_video)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_68.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_68.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_68, 4, 0, 1, 1)

        self.label_154 = QLabel(self.page_1_long_video)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_154, 6, 1, 1, 1)

        self.label_156 = QLabel(self.page_1_long_video)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_156, 4, 1, 1, 1)

        self.Captions_BackColour_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Captions_BackColour_Mode_1_long_video.setObjectName(u"Captions_BackColour_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Captions_BackColour_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Captions_BackColour_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Captions_BackColour_Mode_1_long_video.setMinimumSize(QSize(215, 28))
        self.Captions_BackColour_Mode_1_long_video.setMaximumSize(QSize(215, 28))
        self.Captions_BackColour_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_BackColour_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_BackColour_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_68.addWidget(self.Captions_BackColour_Mode_1_long_video, 13, 2, 1, 1)

        self.Captions_Bold_Bool_Mode_1_long_video = QCustomCheckBox(self.page_1_long_video)
        self.Captions_Bold_Bool_Mode_1_long_video.setObjectName(u"Captions_Bold_Bool_Mode_1_long_video")
        self.Captions_Bold_Bool_Mode_1_long_video.setMinimumSize(QSize(182, 20))
        self.Captions_Bold_Bool_Mode_1_long_video.setMaximumSize(QSize(182, 20))
        self.Captions_Bold_Bool_Mode_1_long_video.setIconSize(QSize(16, 16))
        self.Captions_Bold_Bool_Mode_1_long_video.setChecked(True)

        self.gridLayout_68.addWidget(self.Captions_Bold_Bool_Mode_1_long_video, 15, 2, 1, 1)

        self.Captions_Underline_Bool_Mode_1_long_video = QCustomCheckBox(self.page_1_long_video)
        self.Captions_Underline_Bool_Mode_1_long_video.setObjectName(u"Captions_Underline_Bool_Mode_1_long_video")
        self.Captions_Underline_Bool_Mode_1_long_video.setMinimumSize(QSize(182, 20))
        self.Captions_Underline_Bool_Mode_1_long_video.setMaximumSize(QSize(182, 20))

        self.gridLayout_68.addWidget(self.Captions_Underline_Bool_Mode_1_long_video, 20, 2, 1, 1)

        self.Captions_Italic_Bool_Mode_1_long_video = QCustomCheckBox(self.page_1_long_video)
        self.Captions_Italic_Bool_Mode_1_long_video.setObjectName(u"Captions_Italic_Bool_Mode_1_long_video")
        self.Captions_Italic_Bool_Mode_1_long_video.setMinimumSize(QSize(182, 20))
        self.Captions_Italic_Bool_Mode_1_long_video.setMaximumSize(QSize(182, 20))

        self.gridLayout_68.addWidget(self.Captions_Italic_Bool_Mode_1_long_video, 19, 2, 1, 1)

        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.setObjectName(u"Captions_Reveal_Effect_Final_Color_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.setMinimumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.setMaximumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_68.addWidget(self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video, 24, 2, 1, 1)

        self.label_69 = QLabel(self.page_1_long_video)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_69.setPixmap(QPixmap(u":/material_design/icons/material_design/invert_colors.png"))
        self.label_69.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_69, 24, 0, 1, 1)

        self.label_160 = QLabel(self.page_1_long_video)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMinimumSize(QSize(0, 35))
        self.label_160.setMaximumSize(QSize(16777215, 35))
        self.label_160.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_160, 24, 1, 1, 1)

        self.label_71 = QLabel(self.page_1_long_video)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_71.setPixmap(QPixmap(u":/material_design/icons/material_design/align_horizontal_left.png"))
        self.label_71.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_71, 2, 0, 1, 1)

        self.label_72 = QLabel(self.page_1_long_video)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_72.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_72.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_72, 8, 0, 1, 1)

        self.label_70 = QLabel(self.page_1_long_video)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_70.setPixmap(QPixmap(u":/material_design/icons/material_design/format_color_fill.png"))
        self.label_70.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_70, 23, 0, 1, 1)

        self.label_73 = QLabel(self.page_1_long_video)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_73.setPixmap(QPixmap(u":/material_design/icons/material_design/format_bold.png"))
        self.label_73.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_73, 15, 0, 1, 1)

        self.label_165 = QLabel(self.page_1_long_video)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_165, 13, 1, 1, 1)

        self.label_74 = QLabel(self.page_1_long_video)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_74.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_74.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_74, 13, 0, 1, 1)

        self.label_159 = QLabel(self.page_1_long_video)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_159, 2, 1, 1, 1)

        self.selector_BackColour_Captions_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_BackColour_Captions_Mode_1_long_video.setObjectName(u"selector_BackColour_Captions_Mode_1_long_video")
        self.selector_BackColour_Captions_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_BackColour_Captions_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_BackColour_Captions_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_BackColour_Captions_Mode_1_long_video.setIcon(icon27)

        self.gridLayout_68.addWidget(self.selector_BackColour_Captions_Mode_1_long_video, 13, 3, 1, 1)

        self.Captions_Fontsize_Mode_1_long_video = QSpinBox(self.page_1_long_video)
        self.Captions_Fontsize_Mode_1_long_video.setObjectName(u"Captions_Fontsize_Mode_1_long_video")
        self.Captions_Fontsize_Mode_1_long_video.setMinimumSize(QSize(215, 0))
        self.Captions_Fontsize_Mode_1_long_video.setMaximumSize(QSize(215, 16777215))
        self.Captions_Fontsize_Mode_1_long_video.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Fontsize_Mode_1_long_video.setMinimum(8)

        self.gridLayout_68.addWidget(self.Captions_Fontsize_Mode_1_long_video, 4, 2, 1, 2)

        self.Captions_Alignment_Mode_1_long_video = QSpinBox(self.page_1_long_video)
        self.Captions_Alignment_Mode_1_long_video.setObjectName(u"Captions_Alignment_Mode_1_long_video")
        self.Captions_Alignment_Mode_1_long_video.setMinimumSize(QSize(215, 0))
        self.Captions_Alignment_Mode_1_long_video.setMaximumSize(QSize(215, 16777215))
        self.Captions_Alignment_Mode_1_long_video.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Alignment_Mode_1_long_video.setMinimum(1)

        self.gridLayout_68.addWidget(self.Captions_Alignment_Mode_1_long_video, 2, 2, 1, 2)

        self.selector_OutlineColour_Captions_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_OutlineColour_Captions_Mode_1_long_video.setObjectName(u"selector_OutlineColour_Captions_Mode_1_long_video")
        self.selector_OutlineColour_Captions_Mode_1_long_video.setMinimumSize(QSize(20, 21))
        self.selector_OutlineColour_Captions_Mode_1_long_video.setMaximumSize(QSize(22, 25))
        self.selector_OutlineColour_Captions_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_OutlineColour_Captions_Mode_1_long_video.setIcon(icon27)

        self.gridLayout_68.addWidget(self.selector_OutlineColour_Captions_Mode_1_long_video, 11, 3, 1, 1)

        self.Captions_OutlineColour_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Captions_OutlineColour_Mode_1_long_video.setObjectName(u"Captions_OutlineColour_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Captions_OutlineColour_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Captions_OutlineColour_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Captions_OutlineColour_Mode_1_long_video.setMinimumSize(QSize(215, 28))
        self.Captions_OutlineColour_Mode_1_long_video.setMaximumSize(QSize(215, 28))
        self.Captions_OutlineColour_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_OutlineColour_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_OutlineColour_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_68.addWidget(self.Captions_OutlineColour_Mode_1_long_video, 11, 2, 1, 1)

        self.label_76 = QLabel(self.page_1_long_video)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_76.setPixmap(QPixmap(u":/material_design/icons/material_design/edit.png"))
        self.label_76.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_76, 6, 0, 1, 1)

        self.label_75 = QLabel(self.page_1_long_video)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_75.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_75.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_75, 11, 0, 1, 1)

        self.selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video.setObjectName(u"selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video")
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video.setIcon(icon27)

        self.gridLayout_68.addWidget(self.selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video, 24, 3, 1, 1)

        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.setObjectName(u"Captions_Reveal_Effect_Initial_Color_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.setMinimumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.setMaximumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_68.addWidget(self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video, 23, 2, 1, 1)

        self.label_161 = QLabel(self.page_1_long_video)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMinimumSize(QSize(0, 35))
        self.label_161.setMaximumSize(QSize(16777215, 35))
        self.label_161.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_161, 23, 1, 1, 1)

        self.verticalSpacer_66 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_66, 1, 0, 1, 4)

        self.verticalSpacer_67 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_67, 3, 1, 1, 1)

        self.verticalSpacer_69 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_69, 7, 1, 1, 1)

        self.verticalSpacer_68 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_68, 5, 1, 1, 1)

        self.verticalSpacer_70 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_70, 9, 1, 1, 1)

        self.verticalSpacer_71 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_71, 12, 1, 1, 1)

        self.verticalSpacer_72 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_72, 14, 1, 1, 1)

        self.verticalSpacer_73 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_73, 16, 1, 1, 1)

        self.verticalSpacer_74 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_68.addItem(self.verticalSpacer_74, 18, 1, 1, 1)

        self.Captions_Outline_Mode_1_long_video = QSpinBox(self.page_1_long_video)
        self.Captions_Outline_Mode_1_long_video.setObjectName(u"Captions_Outline_Mode_1_long_video")
        self.Captions_Outline_Mode_1_long_video.setMinimumSize(QSize(215, 0))
        self.Captions_Outline_Mode_1_long_video.setMaximumSize(QSize(215, 16777215))
        self.Captions_Outline_Mode_1_long_video.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Outline_Mode_1_long_video.setMinimum(3)

        self.gridLayout_68.addWidget(self.Captions_Outline_Mode_1_long_video, 21, 2, 1, 1)

        self.label_80 = QLabel(self.page_1_long_video)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_80.setPixmap(QPixmap(u":/material_design/icons/material_design/format_underlined.png"))
        self.label_80.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_80, 20, 0, 1, 1)

        self.label_158 = QLabel(self.page_1_long_video)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_158, 20, 1, 1, 1)

        self.label_81 = QLabel(self.page_1_long_video)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_81.setPixmap(QPixmap(u":/font_awesome/icons/font_awesome/closed-captioning.png"))
        self.label_81.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_81, 0, 0, 1, 1)

        self.label_153 = QLabel(self.page_1_long_video)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_153, 0, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_68.addItem(self.horizontalSpacer_24, 0, 4, 25, 1)

        self.Captions_FontName_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Captions_FontName_Mode_1_long_video.setObjectName(u"Captions_FontName_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Captions_FontName_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Captions_FontName_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Captions_FontName_Mode_1_long_video.setMinimumSize(QSize(215, 28))
        self.Captions_FontName_Mode_1_long_video.setMaximumSize(QSize(215, 28))
        self.Captions_FontName_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_FontName_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_FontName_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_68.addWidget(self.Captions_FontName_Mode_1_long_video, 0, 2, 1, 1)

        self.selector_Captions_FontName_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_Captions_FontName_Mode_1_long_video.setObjectName(u"selector_Captions_FontName_Mode_1_long_video")
        self.selector_Captions_FontName_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_Captions_FontName_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_Captions_FontName_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon35 = QIcon()
        icon35.addFile(u":/material_design/icons/material_design/format_color_text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selector_Captions_FontName_Mode_1_long_video.setIcon(icon35)

        self.gridLayout_68.addWidget(self.selector_Captions_FontName_Mode_1_long_video, 0, 3, 1, 1)

        self.label_77 = QLabel(self.page_1_long_video)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_77.setPixmap(QPixmap(u":/material_design/icons/material_design/format_italic.png"))
        self.label_77.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_77, 19, 0, 1, 1)

        self.Captions_Shadow_Bool_Mode_1_long_video = QCustomCheckBox(self.page_1_long_video)
        self.Captions_Shadow_Bool_Mode_1_long_video.setObjectName(u"Captions_Shadow_Bool_Mode_1_long_video")
        self.Captions_Shadow_Bool_Mode_1_long_video.setMinimumSize(QSize(214, 20))
        self.Captions_Shadow_Bool_Mode_1_long_video.setMaximumSize(QSize(214, 20))
        self.Captions_Shadow_Bool_Mode_1_long_video.setIconSize(QSize(16, 16))
        self.Captions_Shadow_Bool_Mode_1_long_video.setChecked(True)

        self.gridLayout_68.addWidget(self.Captions_Shadow_Bool_Mode_1_long_video, 17, 2, 1, 1)

        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video.setObjectName(u"selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video")
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video.setIcon(icon27)

        self.gridLayout_68.addWidget(self.selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video, 23, 3, 1, 1)

        self.label_166 = QLabel(self.page_1_long_video)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_166, 19, 1, 1, 1)

        self.label_157 = QLabel(self.page_1_long_video)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_157, 17, 1, 1, 1)

        self.selector_PrimaryColour_Captions_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_PrimaryColour_Captions_Mode_1_long_video.setObjectName(u"selector_PrimaryColour_Captions_Mode_1_long_video")
        self.selector_PrimaryColour_Captions_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_PrimaryColour_Captions_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_PrimaryColour_Captions_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_PrimaryColour_Captions_Mode_1_long_video.setIcon(icon27)

        self.gridLayout_68.addWidget(self.selector_PrimaryColour_Captions_Mode_1_long_video, 6, 3, 1, 1)

        self.label_78 = QLabel(self.page_1_long_video)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_78.setPixmap(QPixmap(u":/material_design/icons/material_design/brush.png"))
        self.label_78.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_78, 17, 0, 1, 1)

        self.Captions_SecondaryColour_Mode_1_long_video = QTextEdit(self.page_1_long_video)
        self.Captions_SecondaryColour_Mode_1_long_video.setObjectName(u"Captions_SecondaryColour_Mode_1_long_video")
        sizePolicy2.setHeightForWidth(self.Captions_SecondaryColour_Mode_1_long_video.sizePolicy().hasHeightForWidth())
        self.Captions_SecondaryColour_Mode_1_long_video.setSizePolicy(sizePolicy2)
        self.Captions_SecondaryColour_Mode_1_long_video.setMinimumSize(QSize(215, 28))
        self.Captions_SecondaryColour_Mode_1_long_video.setMaximumSize(QSize(215, 28))
        self.Captions_SecondaryColour_Mode_1_long_video.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_SecondaryColour_Mode_1_long_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_SecondaryColour_Mode_1_long_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_68.addWidget(self.Captions_SecondaryColour_Mode_1_long_video, 8, 2, 1, 1)

        self.label_155 = QLabel(self.page_1_long_video)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_155, 15, 1, 1, 1)

        self.label_164 = QLabel(self.page_1_long_video)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_164, 11, 1, 1, 1)

        self.selector_SecondaryColour_Captions_Mode_1_long_video = QPushButton(self.page_1_long_video)
        self.selector_SecondaryColour_Captions_Mode_1_long_video.setObjectName(u"selector_SecondaryColour_Captions_Mode_1_long_video")
        self.selector_SecondaryColour_Captions_Mode_1_long_video.setMinimumSize(QSize(25, 25))
        self.selector_SecondaryColour_Captions_Mode_1_long_video.setMaximumSize(QSize(25, 25))
        self.selector_SecondaryColour_Captions_Mode_1_long_video.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  \n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"  text-align: left; \n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_SecondaryColour_Captions_Mode_1_long_video.setIcon(icon27)

        self.gridLayout_68.addWidget(self.selector_SecondaryColour_Captions_Mode_1_long_video, 8, 3, 1, 1)

        self.label_79 = QLabel(self.page_1_long_video)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_79.setPixmap(QPixmap(u":/material_design/icons/material_design/text_snippet.png"))
        self.label_79.setScaledContents(False)

        self.gridLayout_68.addWidget(self.label_79, 21, 0, 1, 1)

        self.label_162 = QLabel(self.page_1_long_video)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_68.addWidget(self.label_162, 21, 1, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_68, 1, 1, 1, 1)

        self.stackedWidget_Main.addWidget(self.page_1_long_video)
        self.page_shortify = QWidget()
        self.page_shortify.setObjectName(u"page_shortify")
        self.gridLayout_21 = QGridLayout(self.page_shortify)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.widget_shortify_settings_2 = QWidget(self.page_shortify)
        self.widget_shortify_settings_2.setObjectName(u"widget_shortify_settings_2")
        self.gridLayout_16 = QGridLayout(self.widget_shortify_settings_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.Captions_PrimaryColour = QTextEdit(self.widget_shortify_settings_2)
        self.Captions_PrimaryColour.setObjectName(u"Captions_PrimaryColour")
        sizePolicy2.setHeightForWidth(self.Captions_PrimaryColour.sizePolicy().hasHeightForWidth())
        self.Captions_PrimaryColour.setSizePolicy(sizePolicy2)
        self.Captions_PrimaryColour.setMinimumSize(QSize(215, 28))
        self.Captions_PrimaryColour.setMaximumSize(QSize(215, 28))
        self.Captions_PrimaryColour.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_PrimaryColour.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_PrimaryColour.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_19.addWidget(self.Captions_PrimaryColour, 3, 2, 1, 1)

        self.label_131 = QLabel(self.widget_shortify_settings_2)
        self.label_131.setObjectName(u"label_131")
        sizePolicy3.setHeightForWidth(self.label_131.sizePolicy().hasHeightForWidth())
        self.label_131.setSizePolicy(sizePolicy3)
        self.label_131.setMinimumSize(QSize(0, 0))
        self.label_131.setMaximumSize(QSize(16777215, 16777215))
        self.label_131.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_131, 5, 1, 1, 1)

        self.label_144 = QLabel(self.widget_shortify_settings_2)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_144, 2, 1, 1, 1)

        self.label_13 = QLabel(self.widget_shortify_settings_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_13.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_13.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_132 = QLabel(self.widget_shortify_settings_2)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_132, 3, 1, 1, 1)

        self.Captions_Bold_Bool = QCustomCheckBox(self.widget_shortify_settings_2)
        self.Captions_Bold_Bool.setObjectName(u"Captions_Bold_Bool")
        self.Captions_Bold_Bool.setMinimumSize(QSize(182, 20))
        self.Captions_Bold_Bool.setMaximumSize(QSize(182, 20))
        self.Captions_Bold_Bool.setIconSize(QSize(16, 16))
        self.Captions_Bold_Bool.setChecked(True)

        self.gridLayout_19.addWidget(self.Captions_Bold_Bool, 10, 2, 1, 1)

        self.Captions_BackColour = QTextEdit(self.widget_shortify_settings_2)
        self.Captions_BackColour.setObjectName(u"Captions_BackColour")
        sizePolicy2.setHeightForWidth(self.Captions_BackColour.sizePolicy().hasHeightForWidth())
        self.Captions_BackColour.setSizePolicy(sizePolicy2)
        self.Captions_BackColour.setMinimumSize(QSize(215, 28))
        self.Captions_BackColour.setMaximumSize(QSize(215, 28))
        self.Captions_BackColour.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_BackColour.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_BackColour.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_19.addWidget(self.Captions_BackColour, 9, 2, 1, 1)

        self.Captions_Underline_Bool = QCustomCheckBox(self.widget_shortify_settings_2)
        self.Captions_Underline_Bool.setObjectName(u"Captions_Underline_Bool")
        self.Captions_Underline_Bool.setMinimumSize(QSize(182, 20))
        self.Captions_Underline_Bool.setMaximumSize(QSize(182, 20))

        self.gridLayout_19.addWidget(self.Captions_Underline_Bool, 14, 2, 1, 1)

        self.Captions_Italic_Bool = QCustomCheckBox(self.widget_shortify_settings_2)
        self.Captions_Italic_Bool.setObjectName(u"Captions_Italic_Bool")
        self.Captions_Italic_Bool.setMinimumSize(QSize(182, 20))
        self.Captions_Italic_Bool.setMaximumSize(QSize(182, 20))

        self.gridLayout_19.addWidget(self.Captions_Italic_Bool, 13, 2, 1, 1)

        self.Captions_Reveal_Effect_Final_Color = QTextEdit(self.widget_shortify_settings_2)
        self.Captions_Reveal_Effect_Final_Color.setObjectName(u"Captions_Reveal_Effect_Final_Color")
        sizePolicy2.setHeightForWidth(self.Captions_Reveal_Effect_Final_Color.sizePolicy().hasHeightForWidth())
        self.Captions_Reveal_Effect_Final_Color.setSizePolicy(sizePolicy2)
        self.Captions_Reveal_Effect_Final_Color.setMinimumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Final_Color.setMaximumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Final_Color.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_Reveal_Effect_Final_Color.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_Reveal_Effect_Final_Color.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_19.addWidget(self.Captions_Reveal_Effect_Final_Color, 18, 2, 1, 1)

        self.label_136 = QLabel(self.widget_shortify_settings_2)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMinimumSize(QSize(0, 35))
        self.label_136.setMaximumSize(QSize(16777215, 35))
        self.label_136.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_136, 18, 1, 1, 1)

        self.label_25 = QLabel(self.widget_shortify_settings_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_25.setPixmap(QPixmap(u":/material_design/icons/material_design/invert_colors.png"))
        self.label_25.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_25, 18, 0, 1, 1)

        self.label_24 = QLabel(self.widget_shortify_settings_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_24.setPixmap(QPixmap(u":/material_design/icons/material_design/format_color_fill.png"))
        self.label_24.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_24, 17, 0, 1, 1)

        self.label_12 = QLabel(self.widget_shortify_settings_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_12.setPixmap(QPixmap(u":/material_design/icons/material_design/align_horizontal_left.png"))
        self.label_12.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_15 = QLabel(self.widget_shortify_settings_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_15.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_15.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_15, 5, 0, 1, 1)

        self.label_19 = QLabel(self.widget_shortify_settings_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_19.setPixmap(QPixmap(u":/material_design/icons/material_design/format_bold.png"))
        self.label_19.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_19, 10, 0, 1, 1)

        self.label_142 = QLabel(self.widget_shortify_settings_2)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_142, 9, 1, 1, 1)

        self.label_17 = QLabel(self.widget_shortify_settings_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_17.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_17.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_17, 9, 0, 1, 1)

        self.selector_BackColour_Captions = QPushButton(self.widget_shortify_settings_2)
        self.selector_BackColour_Captions.setObjectName(u"selector_BackColour_Captions")
        self.selector_BackColour_Captions.setMinimumSize(QSize(25, 25))
        self.selector_BackColour_Captions.setMaximumSize(QSize(25, 25))
        self.selector_BackColour_Captions.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_BackColour_Captions.setIcon(icon27)

        self.gridLayout_19.addWidget(self.selector_BackColour_Captions, 9, 3, 1, 1)

        self.label_138 = QLabel(self.widget_shortify_settings_2)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_138, 1, 1, 1, 1)

        self.Captions_Alignment = QSpinBox(self.widget_shortify_settings_2)
        self.Captions_Alignment.setObjectName(u"Captions_Alignment")
        self.Captions_Alignment.setMinimumSize(QSize(215, 0))
        self.Captions_Alignment.setMaximumSize(QSize(215, 16777215))
        self.Captions_Alignment.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Alignment.setMinimum(1)

        self.gridLayout_19.addWidget(self.Captions_Alignment, 1, 2, 1, 2)

        self.Captions_Fontsize = QSpinBox(self.widget_shortify_settings_2)
        self.Captions_Fontsize.setObjectName(u"Captions_Fontsize")
        self.Captions_Fontsize.setMinimumSize(QSize(215, 0))
        self.Captions_Fontsize.setMaximumSize(QSize(215, 16777215))
        self.Captions_Fontsize.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Fontsize.setMinimum(8)

        self.gridLayout_19.addWidget(self.Captions_Fontsize, 2, 2, 1, 2)

        self.Captions_OutlineColour = QTextEdit(self.widget_shortify_settings_2)
        self.Captions_OutlineColour.setObjectName(u"Captions_OutlineColour")
        sizePolicy2.setHeightForWidth(self.Captions_OutlineColour.sizePolicy().hasHeightForWidth())
        self.Captions_OutlineColour.setSizePolicy(sizePolicy2)
        self.Captions_OutlineColour.setMinimumSize(QSize(215, 28))
        self.Captions_OutlineColour.setMaximumSize(QSize(215, 28))
        self.Captions_OutlineColour.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_OutlineColour.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_OutlineColour.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_19.addWidget(self.Captions_OutlineColour, 8, 2, 1, 1)

        self.selector_OutlineColour_Captions = QPushButton(self.widget_shortify_settings_2)
        self.selector_OutlineColour_Captions.setObjectName(u"selector_OutlineColour_Captions")
        self.selector_OutlineColour_Captions.setMinimumSize(QSize(20, 21))
        self.selector_OutlineColour_Captions.setMaximumSize(QSize(22, 25))
        self.selector_OutlineColour_Captions.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_OutlineColour_Captions.setIcon(icon27)

        self.gridLayout_19.addWidget(self.selector_OutlineColour_Captions, 8, 3, 1, 1)

        self.label_16 = QLabel(self.widget_shortify_settings_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_16.setPixmap(QPixmap(u":/material_design/icons/material_design/border_color.png"))
        self.label_16.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_16, 8, 0, 1, 1)

        self.label_14 = QLabel(self.widget_shortify_settings_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_14.setPixmap(QPixmap(u":/material_design/icons/material_design/edit.png"))
        self.label_14.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_14, 3, 0, 1, 1)

        self.selector_Reveal_Effect_Final_Color_Captions = QPushButton(self.widget_shortify_settings_2)
        self.selector_Reveal_Effect_Final_Color_Captions.setObjectName(u"selector_Reveal_Effect_Final_Color_Captions")
        self.selector_Reveal_Effect_Final_Color_Captions.setMinimumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Final_Color_Captions.setMaximumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Final_Color_Captions.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Reveal_Effect_Final_Color_Captions.setIcon(icon27)

        self.gridLayout_19.addWidget(self.selector_Reveal_Effect_Final_Color_Captions, 18, 3, 1, 1)

        self.label_140 = QLabel(self.widget_shortify_settings_2)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(0, 35))
        self.label_140.setMaximumSize(QSize(16777215, 35))
        self.label_140.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_140, 17, 1, 1, 1)

        self.Captions_Reveal_Effect_Initial_Color = QTextEdit(self.widget_shortify_settings_2)
        self.Captions_Reveal_Effect_Initial_Color.setObjectName(u"Captions_Reveal_Effect_Initial_Color")
        sizePolicy2.setHeightForWidth(self.Captions_Reveal_Effect_Initial_Color.sizePolicy().hasHeightForWidth())
        self.Captions_Reveal_Effect_Initial_Color.setSizePolicy(sizePolicy2)
        self.Captions_Reveal_Effect_Initial_Color.setMinimumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Initial_Color.setMaximumSize(QSize(215, 28))
        self.Captions_Reveal_Effect_Initial_Color.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_Reveal_Effect_Initial_Color.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_Reveal_Effect_Initial_Color.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_19.addWidget(self.Captions_Reveal_Effect_Initial_Color, 17, 2, 1, 1)

        self.label_20 = QLabel(self.widget_shortify_settings_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_20.setPixmap(QPixmap(u":/material_design/icons/material_design/format_italic.png"))
        self.label_20.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_20, 13, 0, 1, 1)

        self.selector_Reveal_Effect_Initial_Color_Captions = QPushButton(self.widget_shortify_settings_2)
        self.selector_Reveal_Effect_Initial_Color_Captions.setObjectName(u"selector_Reveal_Effect_Initial_Color_Captions")
        self.selector_Reveal_Effect_Initial_Color_Captions.setMinimumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Initial_Color_Captions.setMaximumSize(QSize(25, 25))
        self.selector_Reveal_Effect_Initial_Color_Captions.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Reveal_Effect_Initial_Color_Captions.setIcon(icon27)

        self.gridLayout_19.addWidget(self.selector_Reveal_Effect_Initial_Color_Captions, 17, 3, 1, 1)

        self.label_152 = QLabel(self.widget_shortify_settings_2)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_152, 13, 1, 1, 1)

        self.Captions_Shadow_Bool = QCustomCheckBox(self.widget_shortify_settings_2)
        self.Captions_Shadow_Bool.setObjectName(u"Captions_Shadow_Bool")
        self.Captions_Shadow_Bool.setMinimumSize(QSize(214, 20))
        self.Captions_Shadow_Bool.setMaximumSize(QSize(214, 20))
        self.Captions_Shadow_Bool.setIconSize(QSize(16, 16))
        self.Captions_Shadow_Bool.setChecked(True)

        self.gridLayout_19.addWidget(self.Captions_Shadow_Bool, 12, 2, 1, 1)

        self.selector_PrimaryColour_Captions = QPushButton(self.widget_shortify_settings_2)
        self.selector_PrimaryColour_Captions.setObjectName(u"selector_PrimaryColour_Captions")
        self.selector_PrimaryColour_Captions.setMinimumSize(QSize(25, 25))
        self.selector_PrimaryColour_Captions.setMaximumSize(QSize(25, 25))
        self.selector_PrimaryColour_Captions.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_PrimaryColour_Captions.setIcon(icon27)

        self.gridLayout_19.addWidget(self.selector_PrimaryColour_Captions, 3, 3, 1, 1)

        self.label_23 = QLabel(self.widget_shortify_settings_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_23.setPixmap(QPixmap(u":/material_design/icons/material_design/brush.png"))
        self.label_23.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_23, 12, 0, 1, 1)

        self.label_145 = QLabel(self.widget_shortify_settings_2)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_145, 12, 1, 1, 1)

        self.Captions_SecondaryColour = QTextEdit(self.widget_shortify_settings_2)
        self.Captions_SecondaryColour.setObjectName(u"Captions_SecondaryColour")
        sizePolicy2.setHeightForWidth(self.Captions_SecondaryColour.sizePolicy().hasHeightForWidth())
        self.Captions_SecondaryColour.setSizePolicy(sizePolicy2)
        self.Captions_SecondaryColour.setMinimumSize(QSize(215, 28))
        self.Captions_SecondaryColour.setMaximumSize(QSize(215, 28))
        self.Captions_SecondaryColour.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_SecondaryColour.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_SecondaryColour.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_19.addWidget(self.Captions_SecondaryColour, 5, 2, 1, 1)

        self.label_151 = QLabel(self.widget_shortify_settings_2)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_151, 8, 1, 1, 1)

        self.selector_SecondaryColour_Captions = QPushButton(self.widget_shortify_settings_2)
        self.selector_SecondaryColour_Captions.setObjectName(u"selector_SecondaryColour_Captions")
        self.selector_SecondaryColour_Captions.setMinimumSize(QSize(25, 25))
        self.selector_SecondaryColour_Captions.setMaximumSize(QSize(25, 25))
        self.selector_SecondaryColour_Captions.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_SecondaryColour_Captions.setIcon(icon27)

        self.gridLayout_19.addWidget(self.selector_SecondaryColour_Captions, 5, 3, 1, 1)

        self.label_22 = QLabel(self.widget_shortify_settings_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_22.setPixmap(QPixmap(u":/material_design/icons/material_design/text_snippet.png"))
        self.label_22.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_22, 15, 0, 1, 1)

        self.label_149 = QLabel(self.widget_shortify_settings_2)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_149, 10, 1, 1, 1)

        self.label_150 = QLabel(self.widget_shortify_settings_2)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_150, 15, 1, 1, 1)

        self.label_21 = QLabel(self.widget_shortify_settings_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_21.setPixmap(QPixmap(u":/material_design/icons/material_design/format_underlined.png"))
        self.label_21.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_21, 14, 0, 1, 1)

        self.label_141 = QLabel(self.widget_shortify_settings_2)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_141, 14, 1, 1, 1)

        self.Captions_Outline = QSpinBox(self.widget_shortify_settings_2)
        self.Captions_Outline.setObjectName(u"Captions_Outline")
        self.Captions_Outline.setMinimumSize(QSize(215, 0))
        self.Captions_Outline.setMaximumSize(QSize(215, 16777215))
        self.Captions_Outline.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Captions_Outline.setMinimum(3)

        self.gridLayout_19.addWidget(self.Captions_Outline, 15, 2, 1, 1)

        self.label_52 = QLabel(self.widget_shortify_settings_2)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_52.setPixmap(QPixmap(u":/material_design/icons/material_design/text_fields.png"))
        self.label_52.setScaledContents(False)

        self.gridLayout_19.addWidget(self.label_52, 0, 0, 1, 1)

        self.label_128 = QLabel(self.widget_shortify_settings_2)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.label_128, 0, 1, 1, 1)

        self.Captions_FontName = QTextEdit(self.widget_shortify_settings_2)
        self.Captions_FontName.setObjectName(u"Captions_FontName")
        sizePolicy2.setHeightForWidth(self.Captions_FontName.sizePolicy().hasHeightForWidth())
        self.Captions_FontName.setSizePolicy(sizePolicy2)
        self.Captions_FontName.setMinimumSize(QSize(215, 28))
        self.Captions_FontName.setMaximumSize(QSize(215, 28))
        self.Captions_FontName.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Captions_FontName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Captions_FontName.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_19.addWidget(self.Captions_FontName, 0, 2, 1, 1)

        self.selector_Captions_FontName_ = QPushButton(self.widget_shortify_settings_2)
        self.selector_Captions_FontName_.setObjectName(u"selector_Captions_FontName_")
        self.selector_Captions_FontName_.setMinimumSize(QSize(25, 25))
        self.selector_Captions_FontName_.setMaximumSize(QSize(25, 25))
        self.selector_Captions_FontName_.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Captions_FontName_.setIcon(icon28)

        self.gridLayout_19.addWidget(self.selector_Captions_FontName_, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_4, 0, 4, 19, 1)


        self.gridLayout_16.addLayout(self.gridLayout_19, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_shortify_settings_2, 1, 1, 1, 1)

        self.widget_shortify_settings_1 = QWidget(self.page_shortify)
        self.widget_shortify_settings_1.setObjectName(u"widget_shortify_settings_1")
        self.widget_shortify_settings_1.setMinimumSize(QSize(0, 0))
        self.widget_shortify_settings_1.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_20 = QGridLayout(self.widget_shortify_settings_1)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.gridLayout_18.setVerticalSpacing(6)
        self.gridLayout_18.setContentsMargins(0, 13, 4, 3)
        self.label_139 = QLabel(self.widget_shortify_settings_1)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_139, 6, 2, 1, 1)

        self.label_129 = QLabel(self.widget_shortify_settings_1)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_129, 3, 2, 1, 1)

        self.Subtitle_Color = QTextEdit(self.widget_shortify_settings_1)
        self.Subtitle_Color.setObjectName(u"Subtitle_Color")
        sizePolicy2.setHeightForWidth(self.Subtitle_Color.sizePolicy().hasHeightForWidth())
        self.Subtitle_Color.setSizePolicy(sizePolicy2)
        self.Subtitle_Color.setMinimumSize(QSize(152, 28))
        self.Subtitle_Color.setMaximumSize(QSize(152, 28))
        self.Subtitle_Color.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Color.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Color.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_18.addWidget(self.Subtitle_Color, 6, 3, 1, 1)

        self.label_4 = QLabel(self.widget_shortify_settings_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_4.setPixmap(QPixmap(u":/feather/icons/feather/image.png"))

        self.gridLayout_18.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_148 = QLabel(self.widget_shortify_settings_1)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_148, 2, 2, 1, 1)

        self.label_7 = QLabel(self.widget_shortify_settings_1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_7.setPixmap(QPixmap(u":/material_design/icons/material_design/timer.png"))

        self.gridLayout_18.addWidget(self.label_7, 5, 0, 1, 1)

        self.Cutting_seconds = QSpinBox(self.widget_shortify_settings_1)
        self.Cutting_seconds.setObjectName(u"Cutting_seconds")
        self.Cutting_seconds.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Cutting_seconds.setMinimum(60)
        self.Cutting_seconds.setMaximum(999999999)

        self.gridLayout_18.addWidget(self.Cutting_seconds, 5, 3, 1, 2)

        self.label_133 = QLabel(self.widget_shortify_settings_1)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_133, 1, 2, 1, 1)

        self.upload_image_watermark = QPushButton(self.widget_shortify_settings_1)
        self.upload_image_watermark.setObjectName(u"upload_image_watermark")
        self.upload_image_watermark.setMinimumSize(QSize(0, 31))
        self.upload_image_watermark.setMaximumSize(QSize(16777215, 31))
        self.upload_image_watermark.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.upload_image_watermark.setIcon(icon32)

        self.gridLayout_18.addWidget(self.upload_image_watermark, 2, 3, 1, 2)

        self.Subtitle_Effects = QTextEdit(self.widget_shortify_settings_1)
        self.Subtitle_Effects.setObjectName(u"Subtitle_Effects")
        sizePolicy2.setHeightForWidth(self.Subtitle_Effects.sizePolicy().hasHeightForWidth())
        self.Subtitle_Effects.setSizePolicy(sizePolicy2)
        self.Subtitle_Effects.setMinimumSize(QSize(152, 28))
        self.Subtitle_Effects.setMaximumSize(QSize(152, 28))
        self.Subtitle_Effects.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Effects.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Effects.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_18.addWidget(self.Subtitle_Effects, 10, 3, 1, 1)

        self.label_11 = QLabel(self.widget_shortify_settings_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_11.setPixmap(QPixmap(u":/material_design/icons/material_design/font_download.png"))
        self.label_11.setScaledContents(False)

        self.gridLayout_18.addWidget(self.label_11, 11, 0, 1, 1)

        self.Subtitle_FontName = QTextEdit(self.widget_shortify_settings_1)
        self.Subtitle_FontName.setObjectName(u"Subtitle_FontName")
        sizePolicy2.setHeightForWidth(self.Subtitle_FontName.sizePolicy().hasHeightForWidth())
        self.Subtitle_FontName.setSizePolicy(sizePolicy2)
        self.Subtitle_FontName.setMinimumSize(QSize(152, 28))
        self.Subtitle_FontName.setMaximumSize(QSize(152, 28))
        self.Subtitle_FontName.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_FontName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_FontName.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_18.addWidget(self.Subtitle_FontName, 11, 3, 1, 1)

        self.label_6 = QLabel(self.widget_shortify_settings_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_6.setPixmap(QPixmap(u":/material_design/icons/material_design/water_drop.png"))

        self.gridLayout_18.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_137 = QLabel(self.widget_shortify_settings_1)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_137, 10, 2, 1, 1)

        self.label_8 = QLabel(self.widget_shortify_settings_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_8.setPixmap(QPixmap(u":/material_design/icons/material_design/format_color_text.png"))

        self.gridLayout_18.addWidget(self.label_8, 6, 0, 1, 1)

        self.selector_FontName_subtitles = QPushButton(self.widget_shortify_settings_1)
        self.selector_FontName_subtitles.setObjectName(u"selector_FontName_subtitles")
        self.selector_FontName_subtitles.setMinimumSize(QSize(25, 25))
        self.selector_FontName_subtitles.setMaximumSize(QSize(25, 25))
        self.selector_FontName_subtitles.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_FontName_subtitles.setIcon(icon28)

        self.gridLayout_18.addWidget(self.selector_FontName_subtitles, 11, 4, 1, 1)

        self.label_10 = QLabel(self.widget_shortify_settings_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_10.setPixmap(QPixmap(u":/material_design/icons/material_design/subtitles.png"))
        self.label_10.setScaledContents(False)

        self.gridLayout_18.addWidget(self.label_10, 10, 0, 1, 1)

        self.label_134 = QLabel(self.widget_shortify_settings_1)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_134, 5, 2, 1, 1)

        self.label_26 = QLabel(self.widget_shortify_settings_1)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_26.setPixmap(QPixmap(u":/material_design/icons/material_design/more_time.png"))

        self.gridLayout_18.addWidget(self.label_26, 1, 0, 1, 1)

        self.channel_yt = QTextEdit(self.widget_shortify_settings_1)
        self.channel_yt.setObjectName(u"channel_yt")
        sizePolicy2.setHeightForWidth(self.channel_yt.sizePolicy().hasHeightForWidth())
        self.channel_yt.setSizePolicy(sizePolicy2)
        self.channel_yt.setMinimumSize(QSize(0, 28))
        self.channel_yt.setMaximumSize(QSize(16777215, 28))
        self.channel_yt.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.channel_yt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel_yt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_18.addWidget(self.channel_yt, 0, 3, 1, 2)

        self.label_9 = QLabel(self.widget_shortify_settings_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_9.setPixmap(QPixmap(u":/material_design/icons/material_design/view_timeline.png"))

        self.gridLayout_18.addWidget(self.label_9, 8, 0, 1, 1)

        self.selector_color_subtitles = QPushButton(self.widget_shortify_settings_1)
        self.selector_color_subtitles.setObjectName(u"selector_color_subtitles")
        self.selector_color_subtitles.setMinimumSize(QSize(25, 25))
        self.selector_color_subtitles.setMaximumSize(QSize(25, 25))
        self.selector_color_subtitles.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_color_subtitles.setIcon(icon27)

        self.gridLayout_18.addWidget(self.selector_color_subtitles, 6, 4, 1, 1)

        self.text_watermark = QTextEdit(self.widget_shortify_settings_1)
        self.text_watermark.setObjectName(u"text_watermark")
        sizePolicy2.setHeightForWidth(self.text_watermark.sizePolicy().hasHeightForWidth())
        self.text_watermark.setSizePolicy(sizePolicy2)
        self.text_watermark.setMinimumSize(QSize(0, 28))
        self.text_watermark.setMaximumSize(QSize(16777215, 28))
        self.text_watermark.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.text_watermark.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_watermark.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_18.addWidget(self.text_watermark, 3, 3, 1, 2)

        self.label_135 = QLabel(self.widget_shortify_settings_1)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_135, 8, 2, 1, 1)

        self.Subtitle_Animation = QTextEdit(self.widget_shortify_settings_1)
        self.Subtitle_Animation.setObjectName(u"Subtitle_Animation")
        sizePolicy2.setHeightForWidth(self.Subtitle_Animation.sizePolicy().hasHeightForWidth())
        self.Subtitle_Animation.setSizePolicy(sizePolicy2)
        self.Subtitle_Animation.setMinimumSize(QSize(152, 28))
        self.Subtitle_Animation.setMaximumSize(QSize(152, 28))
        self.Subtitle_Animation.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 5px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.Subtitle_Animation.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Subtitle_Animation.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_18.addWidget(self.Subtitle_Animation, 8, 3, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(4, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_14, 0, 1, 1, 1)

        self.label_130 = QLabel(self.widget_shortify_settings_1)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_130, 0, 2, 1, 1)

        self.selector_animation_subtitles = QPushButton(self.widget_shortify_settings_1)
        self.selector_animation_subtitles.setObjectName(u"selector_animation_subtitles")
        self.selector_animation_subtitles.setMinimumSize(QSize(25, 25))
        self.selector_animation_subtitles.setMaximumSize(QSize(25, 25))
        self.selector_animation_subtitles.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_animation_subtitles.setIcon(icon13)

        self.gridLayout_18.addWidget(self.selector_animation_subtitles, 8, 4, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_18.addItem(self.verticalSpacer_18, 4, 0, 1, 5)

        self.label_3 = QLabel(self.widget_shortify_settings_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_3.setPixmap(QPixmap(u":/feather/icons/feather/youtube.png"))

        self.gridLayout_18.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_143 = QLabel(self.widget_shortify_settings_1)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_143, 11, 2, 1, 1)

        self.Select_Time = QPushButton(self.widget_shortify_settings_1)
        self.Select_Time.setObjectName(u"Select_Time")
        self.Select_Time.setMinimumSize(QSize(0, 31))
        self.Select_Time.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 11px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon36 = QIcon()
        icon36.addFile(u":/material_design/icons/material_design/more_time.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Select_Time.setIcon(icon36)

        self.gridLayout_18.addWidget(self.Select_Time, 1, 3, 1, 2)

        self.Subtitle_Fontsize = QSpinBox(self.widget_shortify_settings_1)
        self.Subtitle_Fontsize.setObjectName(u"Subtitle_Fontsize")
        self.Subtitle_Fontsize.setMinimumSize(QSize(155, 0))
        self.Subtitle_Fontsize.setMaximumSize(QSize(155, 16777215))
        self.Subtitle_Fontsize.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Subtitle_Fontsize.setMinimum(21)
        self.Subtitle_Fontsize.setMaximum(999)

        self.gridLayout_18.addWidget(self.Subtitle_Fontsize, 12, 3, 1, 1)

        self.label_147 = QLabel(self.widget_shortify_settings_1)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_147, 12, 2, 1, 1)

        self.label_146 = QLabel(self.widget_shortify_settings_1)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(0, 28))
        self.label_146.setMaximumSize(QSize(16777215, 28))
        self.label_146.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.label_146, 13, 2, 1, 1)

        self.Subtitle_Vertical_Reference = QSpinBox(self.widget_shortify_settings_1)
        self.Subtitle_Vertical_Reference.setObjectName(u"Subtitle_Vertical_Reference")
        self.Subtitle_Vertical_Reference.setMinimumSize(QSize(155, 0))
        self.Subtitle_Vertical_Reference.setMaximumSize(QSize(155, 16777215))
        self.Subtitle_Vertical_Reference.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno do bot\u00e3o ao ser pressionado */\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png) /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QSpinBox::down-arrow {\n"
"   image: url(:/material_design/icons/material_design/arrow_downward.png); /* Substitua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.Subtitle_Vertical_Reference.setMinimum(2)
        self.Subtitle_Vertical_Reference.setMaximum(999)
        self.Subtitle_Vertical_Reference.setValue(6)

        self.gridLayout_18.addWidget(self.Subtitle_Vertical_Reference, 13, 3, 1, 1)

        self.label_54 = QLabel(self.widget_shortify_settings_1)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_54.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_54.setScaledContents(False)

        self.gridLayout_18.addWidget(self.label_54, 13, 0, 1, 1)

        self.label_53 = QLabel(self.widget_shortify_settings_1)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_53.setPixmap(QPixmap(u":/material_design/icons/material_design/format_size.png"))
        self.label_53.setScaledContents(False)

        self.gridLayout_18.addWidget(self.label_53, 12, 0, 1, 1)

        self.selector_Effects_subtitles = QPushButton(self.widget_shortify_settings_1)
        self.selector_Effects_subtitles.setObjectName(u"selector_Effects_subtitles")
        self.selector_Effects_subtitles.setMinimumSize(QSize(25, 25))
        self.selector_Effects_subtitles.setMaximumSize(QSize(25, 25))
        self.selector_Effects_subtitles.setStyleSheet(u"QPushButton {\n"
"  background: #F7F7F7;\n"
"  border-radius: 5px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 10px;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        self.selector_Effects_subtitles.setIcon(icon30)

        self.gridLayout_18.addWidget(self.selector_Effects_subtitles, 10, 4, 1, 1)

        self.verticalSpacer_56 = QSpacerItem(20, 44, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_18.addItem(self.verticalSpacer_56, 14, 0, 1, 5)


        self.gridLayout_20.addLayout(self.gridLayout_18, 2, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_shortify_settings_1, 1, 0, 1, 1)

        self.Start_Shortify = QPushButton(self.page_shortify)
        self.Start_Shortify.setObjectName(u"Start_Shortify")
        self.Start_Shortify.setStyleSheet(u"QPushButton {\n"
"  background: white;\n"
"  border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */	\n"
"  font-family: \"ABeeZee\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.036em;\n"
"  font-weight: 400;\n"
"\n"
"}\n"
"            QPushButton:hover {\n"
"                background-color: #EDEDED;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #DCDCDC;\n"
"            }")
        icon37 = QIcon()
        icon37.addFile(u":/mediacuts/icons/mediacuts/icons8-ai-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_Shortify.setIcon(icon37)
        self.Start_Shortify.setIconSize(QSize(29, 26))
        self.Start_Shortify.setAutoRepeatDelay(300)

        self.gridLayout_21.addWidget(self.Start_Shortify, 0, 0, 1, 2)

        self.stackedWidget_Main.addWidget(self.page_shortify)

        self.gridLayout_5.addWidget(self.stackedWidget_Main, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_6 = QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_Thread_id = QLabel(self.page_5)
        self.label_Thread_id.setObjectName(u"label_Thread_id")
        self.label_Thread_id.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_Thread_id, 7, 1, 1, 1)

        self.label_accountinfo_9 = QLabel(self.page_5)
        self.label_accountinfo_9.setObjectName(u"label_accountinfo_9")
        self.label_accountinfo_9.setMinimumSize(QSize(31, 31))
        self.label_accountinfo_9.setMaximumSize(QSize(31, 31))
        self.label_accountinfo_9.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_9.setPixmap(QPixmap(u":/feather/icons/feather/target.png"))

        self.gridLayout_9.addWidget(self.label_accountinfo_9, 5, 0, 1, 1)

        self.label_accountinfo_7 = QLabel(self.page_5)
        self.label_accountinfo_7.setObjectName(u"label_accountinfo_7")
        self.label_accountinfo_7.setMinimumSize(QSize(25, 25))
        self.label_accountinfo_7.setMaximumSize(QSize(25, 31))
        self.label_accountinfo_7.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_7.setPixmap(QPixmap(u":/material_design/icons/material_design/timer.png"))

        self.gridLayout_9.addWidget(self.label_accountinfo_7, 3, 0, 1, 1)

        self.label_mediabase = QLabel(self.page_5)
        self.label_mediabase.setObjectName(u"label_mediabase")
        self.label_mediabase.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_mediabase, 1, 1, 1, 1)

        self.label_WeatherForecast = QLabel(self.page_5)
        self.label_WeatherForecast.setObjectName(u"label_WeatherForecast")
        self.label_WeatherForecast.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_WeatherForecast, 2, 1, 1, 1)

        self.label_Target = QLabel(self.page_5)
        self.label_Target.setObjectName(u"label_Target")
        self.label_Target.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_Target, 5, 1, 1, 1)

        self.label_File_path = QLabel(self.page_5)
        self.label_File_path.setObjectName(u"label_File_path")
        self.label_File_path.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_File_path, 4, 1, 1, 1)

        self.label_accountinfo_5 = QLabel(self.page_5)
        self.label_accountinfo_5.setObjectName(u"label_accountinfo_5")
        self.label_accountinfo_5.setMinimumSize(QSize(32, 25))
        self.label_accountinfo_5.setMaximumSize(QSize(25, 25))
        self.label_accountinfo_5.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_5.setPixmap(QPixmap(u":/material_design/icons/material_design/video_settings.png"))

        self.gridLayout_9.addWidget(self.label_accountinfo_5, 1, 0, 1, 1)

        self.label_Cuts_Duration = QLabel(self.page_5)
        self.label_Cuts_Duration.setObjectName(u"label_Cuts_Duration")
        self.label_Cuts_Duration.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_Cuts_Duration, 6, 1, 1, 1)

        self.label_accountinfo_6 = QLabel(self.page_5)
        self.label_accountinfo_6.setObjectName(u"label_accountinfo_6")
        self.label_accountinfo_6.setMinimumSize(QSize(25, 25))
        self.label_accountinfo_6.setMaximumSize(QSize(25, 25))
        self.label_accountinfo_6.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_6.setPixmap(QPixmap(u":/material_design/icons/material_design/av_timer.png"))

        self.gridLayout_9.addWidget(self.label_accountinfo_6, 2, 0, 1, 1)

        self.label_accountinfo_8 = QLabel(self.page_5)
        self.label_accountinfo_8.setObjectName(u"label_accountinfo_8")
        self.label_accountinfo_8.setMinimumSize(QSize(25, 31))
        self.label_accountinfo_8.setMaximumSize(QSize(25, 31))
        self.label_accountinfo_8.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_8.setPixmap(QPixmap(u":/font_awesome/icons/font_awesome/file-video.png"))

        self.gridLayout_9.addWidget(self.label_accountinfo_8, 4, 0, 1, 1)

        self.label_accountinfo_10 = QLabel(self.page_5)
        self.label_accountinfo_10.setObjectName(u"label_accountinfo_10")
        self.label_accountinfo_10.setMinimumSize(QSize(25, 31))
        self.label_accountinfo_10.setMaximumSize(QSize(25, 31))
        self.label_accountinfo_10.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_10.setPixmap(QPixmap(u":/feather/icons/feather/tag.png"))

        self.gridLayout_9.addWidget(self.label_accountinfo_10, 7, 0, 1, 1)

        self.label_Created_at = QLabel(self.page_5)
        self.label_Created_at.setObjectName(u"label_Created_at")
        self.label_Created_at.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_Created_at, 3, 1, 1, 1)

        self.label_accountinfo_11 = QLabel(self.page_5)
        self.label_accountinfo_11.setObjectName(u"label_accountinfo_11")
        self.label_accountinfo_11.setMinimumSize(QSize(25, 25))
        self.label_accountinfo_11.setMaximumSize(QSize(25, 25))
        self.label_accountinfo_11.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_11.setPixmap(QPixmap(u":/material_design/icons/material_design/timer.png"))

        self.gridLayout_9.addWidget(self.label_accountinfo_11, 6, 0, 1, 1)

        self.label_accountinfo_12 = QLabel(self.page_5)
        self.label_accountinfo_12.setObjectName(u"label_accountinfo_12")
        self.label_accountinfo_12.setMinimumSize(QSize(32, 25))
        self.label_accountinfo_12.setMaximumSize(QSize(25, 25))
        self.label_accountinfo_12.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_12.setPixmap(QPixmap(u":/material_design/icons/material_design/mode.png"))

        self.gridLayout_9.addWidget(self.label_accountinfo_12, 0, 0, 1, 1)

        self.label_mode = QLabel(self.page_5)
        self.label_mode.setObjectName(u"label_mode")
        self.label_mode.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.label_mode, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_23.addWidget(self.label_5, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.page_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setValue(0)

        self.gridLayout_23.addWidget(self.progressBar, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_23, 1, 0, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_30 = QLabel(self.page_5)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_24.addWidget(self.label_30, 0, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.page_5)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(0, 0))
        self.timeEdit.setStyleSheet(u"QTimeEdit {\n"
"    border: 1px solid #E0E0E0;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    background-color: #F7F7F7;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Remove a borda quando o widget est\u00e1 focado */\n"
"QTimeEdit:focus {\n"
"    border: 1px solid #A0A0A0;\n"
"}\n"
"\n"
"/* Estiliza os bot\u00f5es de incremento e decremento */\n"
"QTimeEdit::up-button, QTimeEdit::down-button {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"/* Remove o contorno dos bot\u00f5es ao serem pressionados */\n"
"QTimeEdit::up-button:pressed, QTimeEdit::down-button:pressed {\n"
"    background-color: #D6D6D6;\n"
"}\n"
"\n"
"/* Estiliza a seta para cima */\n"
"QTimeEdit::up-arrow {\n"
"    image: url(:/material_design/icons/material_design/arrow_upward.png); \n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Estiliza a seta para baixo */\n"
"QTimeEdit::down-arrow {\n"
"     image: url(:/material_design/icons/material_design/arrow_downward.png);/* Substit"
                        "ua pelo \u00edcone desejado */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")

        self.gridLayout_24.addWidget(self.timeEdit, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_24, 2, 0, 1, 1)

        self.log = QTextEdit(self.page_5)
        self.log.setObjectName(u"log")
        self.log.setMinimumSize(QSize(0, 0))
        self.log.setMaximumSize(QSize(16777215, 16777215))
        self.log.setStyleSheet(u"            QTextEdit {\n"
"          \n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto preto */\n"
"                font-family: Arial;\n"
"                font-size: 14px;\n"
"            }")

        self.gridLayout_6.addWidget(self.log, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_13 = QGridLayout(self.page_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_accountinfo = QLabel(self.page_6)
        self.label_accountinfo.setObjectName(u"label_accountinfo")
        self.label_accountinfo.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.label_accountinfo, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(734, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.label_accountinfo_4 = QLabel(self.page_6)
        self.label_accountinfo_4.setObjectName(u"label_accountinfo_4")
        self.label_accountinfo_4.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_4.setPixmap(QPixmap(u":/material_design/icons/material_design/person.png"))

        self.gridLayout_8.addWidget(self.label_accountinfo_4, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_10, 0, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_License_expiration = QLabel(self.page_6)
        self.label_License_expiration.setObjectName(u"label_License_expiration")
        self.label_License_expiration.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.label_License_expiration, 4, 1, 1, 2)

        self.label_29 = QLabel(self.page_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_29.setPixmap(QPixmap(u":/material_design/icons/material_design/access_time_filled.png"))

        self.gridLayout_12.addWidget(self.label_29, 4, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(26, 14, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_16, 4, 3, 1, 1)

        self.label_accountinfo_2 = QLabel(self.page_6)
        self.label_accountinfo_2.setObjectName(u"label_accountinfo_2")
        self.label_accountinfo_2.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_2.setPixmap(QPixmap(u":/material_design/icons/material_design/email.png"))

        self.gridLayout_12.addWidget(self.label_accountinfo_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(26, 14, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.label_mediabase_2 = QLabel(self.page_6)
        self.label_mediabase_2.setObjectName(u"label_mediabase_2")
        self.label_mediabase_2.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.label_mediabase_2, 1, 1, 1, 1)

        self.email_input = QTextEdit(self.page_6)
        self.email_input.setObjectName(u"email_input")
        sizePolicy2.setHeightForWidth(self.email_input.sizePolicy().hasHeightForWidth())
        self.email_input.setSizePolicy(sizePolicy2)
        self.email_input.setMinimumSize(QSize(0, 0))
        self.email_input.setMaximumSize(QSize(411, 37))
        self.email_input.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 3px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.email_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.email_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_12.addWidget(self.email_input, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_8, 0, 0, 1, 1)

        self.label_accountinfo_3 = QLabel(self.page_6)
        self.label_accountinfo_3.setObjectName(u"label_accountinfo_3")
        self.label_accountinfo_3.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_accountinfo_3.setPixmap(QPixmap(u":/feather/icons/feather/key.png"))

        self.gridLayout_12.addWidget(self.label_accountinfo_3, 2, 0, 1, 1)

        self.label_mediabase_3 = QLabel(self.page_6)
        self.label_mediabase_3.setObjectName(u"label_mediabase_3")
        self.label_mediabase_3.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.label_mediabase_3, 2, 1, 1, 1)

        self.api_key_input = QTextEdit(self.page_6)
        self.api_key_input.setObjectName(u"api_key_input")
        sizePolicy2.setHeightForWidth(self.api_key_input.sizePolicy().hasHeightForWidth())
        self.api_key_input.setSizePolicy(sizePolicy2)
        self.api_key_input.setMinimumSize(QSize(411, 34))
        self.api_key_input.setMaximumSize(QSize(411, 34))
        self.api_key_input.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 3px;\n"
"                border-radius: 3px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.api_key_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.api_key_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_12.addWidget(self.api_key_input, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(26, 14, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_11, 3, 3, 1, 1)

        self.label_28 = QLabel(self.page_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_28.setPixmap(QPixmap(u":/feather/icons/feather/database.png"))

        self.gridLayout_12.addWidget(self.label_28, 3, 0, 1, 1)

        self.label_mediabase_26 = QLabel(self.page_6)
        self.label_mediabase_26.setObjectName(u"label_mediabase_26")
        self.label_mediabase_26.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.label_mediabase_26, 3, 1, 1, 1)

        self.API_Server_AVAIBLE = QComboBox(self.page_6)
        self.API_Server_AVAIBLE.setObjectName(u"API_Server_AVAIBLE")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.API_Server_AVAIBLE.sizePolicy().hasHeightForWidth())
        self.API_Server_AVAIBLE.setSizePolicy(sizePolicy4)
        self.API_Server_AVAIBLE.setMinimumSize(QSize(0, 0))
        self.API_Server_AVAIBLE.setMaximumSize(QSize(411, 16777215))
        self.API_Server_AVAIBLE.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 13px;  /* Borda arredondada */\n"
"    color: black;  /* Cor do texto */\n"
"    font-size: 13px;  /* Tamanho da fonte */\n"
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

        self.gridLayout_12.addWidget(self.API_Server_AVAIBLE, 3, 2, 1, 1)

        self.label_35 = QLabel(self.page_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"QLabel {\n"
"  color: #00261c;\n"
"  text-align: left; /* N\u00e3o \u00e9 suportado em QSS */\n"
"  font-family: \"Poppins\";\n"
"  font-size: 18px;\n"
"  letter-spacing: 0.016em;\n"
"  font-weight: 700;\n"
"}\n"
"")
        self.label_35.setPixmap(QPixmap(u":/material_design/icons/material_design/notifications_active.png"))

        self.gridLayout_12.addWidget(self.label_35, 5, 0, 1, 1)

        self.Notifications = QCustomCheckBox(self.page_6)
        self.Notifications.setObjectName(u"Notifications")
        self.Notifications.setMinimumSize(QSize(302, 20))
        self.Notifications.setMaximumSize(QSize(302, 20))
        self.Notifications.setChecked(True)

        self.gridLayout_12.addWidget(self.Notifications, 5, 2, 1, 1)

        self.label_mediabase_27 = QLabel(self.page_6)
        self.label_mediabase_27.setObjectName(u"label_mediabase_27")
        self.label_mediabase_27.setStyleSheet(u"QLabel {\n"
"  color: #575c76;\n"
"  font-family: \"Inter\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.label_mediabase_27, 5, 1, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_12, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)

        self.gridLayout_4.addWidget(self.stackedWidget, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.raise_()
        self.frame_2.raise_()
        self.widget_slidemenu.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(11)
        self.stackedWidget_Main.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Control_panel_report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.Dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.Control_panel.setText(QCoreApplication.translate("MainWindow", u"Control Panel", None))
        self.Control_panel_process.setText(QCoreApplication.translate("MainWindow", u"Control Panel\n"
"Process", None))
        self.myaccount.setText(QCoreApplication.translate("MainWindow", u"my account", None))
        self.Control_panel_Tasks.setText(QCoreApplication.translate("MainWindow", u"Control Panel\n"
"Tasks", None))
        self.get_myaccount.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Media Cuts Studio\n"
"", None))
        self.label_datetime.setText(QCoreApplication.translate("MainWindow", u"4.45 pm 19 Jan 2025", None))
        self.label_hello_5.setText("")
        self.notifications.setText("")
        self.label_hello.setText(QCoreApplication.translate("MainWindow", u"Hello", None))
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.pushButton_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.minimize_window_button.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Selector Reveal Effect Final Colour Captions", None))
        self.pushButton_11.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Selector Reveal Effect Initial Colour Captions", None))
        self.pushButton_10.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Selector Back Colour Captions", None))
        self.pushButton_9.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Selector Outline Colour Captions", None))
        self.pushButton_8.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Selector Secondary Colour Captions", None))
        self.pushButton_7.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Selector Primary Colour Captions", None))
        self.pushButton_6.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Selector Animation for Subtitle", None))
        self.pushButton_3.setText("")
        self.button_animation_Gradual_Blink_sub.setText(QCoreApplication.translate("MainWindow", u"Gradual \n"
"Blink", None))
        self.button_animation_AppearDisappear_sub.setText(QCoreApplication.translate("MainWindow", u"Appear\n"
"Disappear", None))
        self.button_animation_StrobeEffect_sub.setText(QCoreApplication.translate("MainWindow", u"Strobe \n"
"Effect", None))
        self.button_animation_Soft_Fade_In_Out_sub.setText(QCoreApplication.translate("MainWindow", u"Soft \n"
"Fade-In-Out", None))
        self.button_animation_FadeInandHold_sub.setText(QCoreApplication.translate("MainWindow", u"Fade-In\n"
" and Hold", None))
        self.button_animation_FadeOut_and_Hold_sub.setText(QCoreApplication.translate("MainWindow", u"Fade-Out \n"
"and Hold", None))
        self.button_animation_PulseOut_sub.setText(QCoreApplication.translate("MainWindow", u"Pulse \n"
"Out", None))
        self.button_animation_Pulse_sub.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.button_animation_SlowFadeIn_sub.setText(QCoreApplication.translate("MainWindow", u"Slow \n"
"Fade-In", None))
        self.button_animation_FastBlink_sub.setText(QCoreApplication.translate("MainWindow", u"Fast Blink", None))
        self.button_animation_FadeIn_sub.setText(QCoreApplication.translate("MainWindow", u"Fade-In", None))
        self.button_animation_SlowFadeOut_sub.setText(QCoreApplication.translate("MainWindow", u"Slow \n"
"Fade-Out", None))
        self.button_animation_BlinkingText_sub.setText(QCoreApplication.translate("MainWindow", u"Blinking \n"
"Text", None))
        self.button_animation_QuickFadeOut_sub.setText(QCoreApplication.translate("MainWindow", u"Quick \n"
"Fade-Out", None))
        self.button_animation_QuickFadeIn_sub.setText(QCoreApplication.translate("MainWindow", u"Quick \n"
"Fade-In", None))
        self.button_animation_None_sub.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Selector Font Name for Subtitle", None))
        self.pushButton_5.setText("")
        self.button_FranklinGothic_sub.setText(QCoreApplication.translate("MainWindow", u"Franklin \n"
"Gothic", None))
        self.button_Trebuchet_MS_sub.setText(QCoreApplication.translate("MainWindow", u"Trebuchet\n"
" MS", None))
        self.button_Comic_Sans_MS_sub.setText(QCoreApplication.translate("MainWindow", u"Comic\n"
" Sans MS", None))
        self.button_CenturyGothic_sub.setText(QCoreApplication.translate("MainWindow", u"Century \n"
"Gothic", None))
        self.button_Tahoma_sub.setText(QCoreApplication.translate("MainWindow", u"Tahoma", None))
        self.button_Calibri_sub.setText(QCoreApplication.translate("MainWindow", u"Calibri", None))
        self.button_LucidaConsole_sub.setText(QCoreApplication.translate("MainWindow", u"Lucida \n"
"Console", None))
        self.button_Impact_sub.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.button_Garamond_sub.setText(QCoreApplication.translate("MainWindow", u"Garamond", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Selector Font Name for Captions", None))
        self.pushButton_16.setText("")
        self.button_FranklinGothic_Captions.setText(QCoreApplication.translate("MainWindow", u"Franklin \n"
"Gothic", None))
        self.button_Trebuchet_MS_Captions.setText(QCoreApplication.translate("MainWindow", u"Trebuchet\n"
" MS", None))
        self.button_Comic_Sans_MS_Captions.setText(QCoreApplication.translate("MainWindow", u"Comic\n"
" Sans MS", None))
        self.button_CenturyGothic_Captions.setText(QCoreApplication.translate("MainWindow", u"Century \n"
"Gothic", None))
        self.button_Tahoma_Captions.setText(QCoreApplication.translate("MainWindow", u"Tahoma", None))
        self.button_Calibri_Captions.setText(QCoreApplication.translate("MainWindow", u"Calibri", None))
        self.button_LucidaConsole_Captions.setText(QCoreApplication.translate("MainWindow", u"Lucida \n"
"Console", None))
        self.button_Impact_Captions.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.button_Garamond_Captions.setText(QCoreApplication.translate("MainWindow", u"Garamond", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Selector Color Subtitles", None))
        self.pushButton_4.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Selector Effects for Subtitle", None))
        self.pushButton_2.setText("")
        self.button_GlowEffect_Shadow_sub.setText(QCoreApplication.translate("MainWindow", u"Glow Effect", None))
        self.button_effects_BoldShadow_sub.setText(QCoreApplication.translate("MainWindow", u"Bold Shadow", None))
        self.button_effects_DropShadow_sub.setText(QCoreApplication.translate("MainWindow", u"Drop Shadow", None))
        self.button_effects_DottedOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Dotted Outline", None))
        self.button_effects_NeonGlow_sub.setText(QCoreApplication.translate("MainWindow", u"Neon Glow", None))
        self.button_effects_InnerGlow_sub.setText(QCoreApplication.translate("MainWindow", u"Inner Glow", None))
        self.button_effects_HardGlow_sub.setText(QCoreApplication.translate("MainWindow", u"Hard Glow", None))
        self.button_effects_SoftShadow_sub.setText(QCoreApplication.translate("MainWindow", u"Soft Shadow", None))
        self.button_effects_WavyOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Wavy Outline", None))
        self.button_effects_BlurredShadow_sub.setText(QCoreApplication.translate("MainWindow", u"Blurred\n"
"Shadow", None))
        self.button_effects_Emboss_sub.setText(QCoreApplication.translate("MainWindow", u"Emboss", None))
        self.button_effects_Outline_sub.setText(QCoreApplication.translate("MainWindow", u"Outline", None))
        self.button_effects_DoubleOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Double\n"
"Outline", None))
        self.button_effects_TransparentOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Transparent\n"
"Outline", None))
        self.button_effects_SoftGlow_sub.setText(QCoreApplication.translate("MainWindow", u"Soft Glow", None))
        self.button_effects_Shadow_sub.setText(QCoreApplication.translate("MainWindow", u"Shadow", None))
        self.button_effects_ThickOutline_sub.setText(QCoreApplication.translate("MainWindow", u"Thick Outline", None))
        self.button_effects_None_sub.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.pushButton_15.setText("")
        self.Time_Weekly_Mode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"14:30:00", None))
        self.pushButton_14.setText("")
        self.Day_Weekly_Mode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Weekly Mode", None))
        self.Indefinite_Schedule_Weekly_Mode.setText(QCoreApplication.translate("MainWindow", u"Maintain Indefinite Schedule", None))
        self.Schedule_the_month_Weekly_Mode.setText(QCoreApplication.translate("MainWindow", u"Maintain Schedule throughout the month", None))
        self.pushButton_12.setText("")
        self.checkBox_UTC_time_zone_Weekly_Mode.setText(QCoreApplication.translate("MainWindow", u"UTC time zone", None))
        self.checkBox_Sao_Paulo_time_zone_Weekly_Mode.setText(QCoreApplication.translate("MainWindow", u"America/Sao_Paulo Time zone", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Date Mode", None))
        self.pushButton_13.setText("")
        self.Execute_only_1_time_on_the_date_Date_Mode.setText(QCoreApplication.translate("MainWindow", u"Execute only 1 time on the date", None))
        self.Time_Date_Mode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2025-02-13T14:30:00Z", None))
        self.checkBox_UTC_time_zone_Date_Mode.setText(QCoreApplication.translate("MainWindow", u"UTC time zone", None))
        self.pushButton_17.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Exact Date", None))
        self.checkBox_Sao_Paulo_time_zone_Date_Mode.setText(QCoreApplication.translate("MainWindow", u"America/Sao_Paulo Time zone", None))
        self.label_43.setText("")
        self.upload_image_watermark_.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Upload Image Watermark", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Media Cuts Studio", None))
        self.pushButton.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.pushButton_18.setText("")
        self.pushButton_19.setText("")
        self.username_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your password", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your Email", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_18.setText("")
        self.log_agent.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Agent Info", None))
        self.Agent_ID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.Agent_Thread.setText(QCoreApplication.translate("MainWindow", u"Thread:", None))
        self.Agent_Total_Report.setText(QCoreApplication.translate("MainWindow", u"Total Reports:", None))
        self.checkBox_telegram_agent.setText(QCoreApplication.translate("MainWindow", u"Telegram", None))
        self.checkBox_discord_agent.setText(QCoreApplication.translate("MainWindow", u"Discord", None))
        self.checkBox_gmail_agent.setText(QCoreApplication.translate("MainWindow", u"Gmail", None))
        self.html_chat.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.mensage_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message...", None))
#if QT_CONFIG(tooltip)
        self.send_mensage.setToolTip(QCoreApplication.translate("MainWindow", u"Send message to agent", None))
#endif // QT_CONFIG(tooltip)
        self.send_mensage.setText("")
        self.label_hello_2.setText(QCoreApplication.translate("MainWindow", u"RealTime Conversation", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Tasks Created", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Tasks Running ", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Tasks Completed ", None))
        self.Mode_1_long_video.setText(QCoreApplication.translate("MainWindow", u"Mode 1 long video", None))
        self.Mode_Batch_processing.setText(QCoreApplication.translate("MainWindow", u"Mode Batch processing", None))
        self.Mode_Shortify.setText(QCoreApplication.translate("MainWindow", u"Mode Shortify", None))
        self.Captions_PrimaryColour_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&HC0C0C0", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Captions Secondary Colour:", None))
        self.label_91.setText("")
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Captions PrimaryColour:", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Captions Fontsize:", None))
        self.Captions_BackColour_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0", None))
        self.Captions_Bold_Bool_Mode_Batch_processing.setText("")
        self.Captions_Underline_Bool_Mode_Batch_processing.setText("")
        self.Captions_Italic_Bool_Mode_Batch_processing.setText("")
        self.Captions_Reveal_Effect_Final_Color_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0099FF&", None))
        self.label_92.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Captions Reveal Effect\n"
"Final Color:", None))
        self.label_93.setText("")
        self.label_94.setText("")
        self.label_95.setText("")
        self.label_96.setText("")
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Captions BackColour:", None))
        self.label_97.setText("")
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Captions Alignment:", None))
        self.selector_BackColour_Captions_Mode_Batch_processing.setText("")
        self.selector_OutlineColour_Captions_Mode_Batch_processing.setText("")
        self.Captions_OutlineColour_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0", None))
        self.label_98.setText("")
        self.label_99.setText("")
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_Batch_processing.setText("")
        self.Captions_Reveal_Effect_Initial_Color_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&HCCCC33&", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Captions Reveal Effect\n"
"Initial Color:", None))
        self.label_100.setText("")
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Captions Underline:", None))
        self.label_101.setText("")
        self.label_mediabase_73.setText(QCoreApplication.translate("MainWindow", u"Captions FontName:", None))
        self.Captions_FontName_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Future", None))
        self.selector_Captions_FontName_Mode_Batch_processing.setText("")
        self.label_102.setText("")
        self.Captions_Shadow_Bool_Mode_Batch_processing.setText("")
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_Batch_processing.setText("")
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Captions Italic:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Captions Shadow:", None))
        self.selector_PrimaryColour_Captions_Mode_Batch_processing.setText("")
        self.label_103.setText("")
        self.Captions_SecondaryColour_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H8080", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Captions Bold:", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Captions OutlineColour:", None))
        self.selector_SecondaryColour_Captions_Mode_Batch_processing.setText("")
        self.label_104.setText("")
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Captions Outline:", None))
        self.Start_Batch_processing.setText(QCoreApplication.translate("MainWindow", u"Start Batch processing", None))
        self.text_watermark_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"@CutsMrBeast", None))
        self.label_65.setText("")
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"text watermark:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Subtitle FontName:", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Subtitle Fontsize:", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Subtitle Vertical\n"
"Reference:", None))
        self.selector_Effects_subtitles_Mode_Batch_processing.setText("")
        self.label_82.setText("")
        self.label_83.setText("")
        self.selector_color_subtitles_Mode_Batch_processing.setText("")
        self.label_84.setText("")
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Subtitle Animation:", None))
        self.Subtitle_Animation_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Slow Fade-Out", None))
        self.selector_animation_subtitles_Mode_Batch_processing.setText("")
        self.label_85.setText("")
        self.upload_Video_Mode_Batch_processing.setText(QCoreApplication.translate("MainWindow", u"Upload List Video", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"List Media Base:", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Subtitle Color:", None))
        self.label_86.setText("")
        self.Subtitle_Color_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#292D8E", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"watermark image:", None))
        self.label_87.setText("")
        self.upload_image_watermark_Mode_Batch_processing.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.Subtitle_Effects_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Glow Effect", None))
        self.label_88.setText("")
        self.Subtitle_FontName_Mode_Batch_processing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Future", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Subtitle Effects:", None))
        self.label_89.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Cutting seconds:", None))
        self.label_90.setText("")
        self.selector_FontName_subtitles_Mode_Batch_processing.setText("")
        self.Start_1_long_video.setText(QCoreApplication.translate("MainWindow", u"Start 1 long video", None))
        self.text_watermark_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"@CutsMrBeast", None))
        self.label_60.setText("")
        self.label_mediabase_32.setText(QCoreApplication.translate("MainWindow", u"text watermark:", None))
        self.label_mediabase_39.setText(QCoreApplication.translate("MainWindow", u"Subtitle FontName:", None))
        self.label_mediabase_40.setText(QCoreApplication.translate("MainWindow", u"Subtitle Fontsize:", None))
        self.label_mediabase_41.setText(QCoreApplication.translate("MainWindow", u"Subtitle Vertical\n"
"Reference:", None))
        self.selector_Effects_subtitles_Mode_1_long_video.setText("")
        self.label_66.setText("")
        self.label_67.setText("")
        self.selector_color_subtitles_Mode_1_long_video.setText("")
        self.label_64.setText("")
        self.label_mediabase_37.setText(QCoreApplication.translate("MainWindow", u"Subtitle Animation:", None))
        self.Subtitle_Animation_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Slow Fade-Out", None))
        self.selector_animation_subtitles_Mode_1_long_video.setText("")
        self.label_63.setText("")
        self.upload_image_watermark_3.setText(QCoreApplication.translate("MainWindow", u"Upload Video", None))
        self.label_mediabase_34.setText(QCoreApplication.translate("MainWindow", u"Media Base:", None))
        self.label_mediabase_31.setText(QCoreApplication.translate("MainWindow", u"Subtitle Color:", None))
        self.label_57.setText("")
        self.Subtitle_Color_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#292D8E", None))
        self.label_mediabase_33.setText(QCoreApplication.translate("MainWindow", u"watermark image:", None))
        self.label_58.setText("")
        self.upload_image_watermark_2.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.Subtitle_Effects_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Glow Effect", None))
        self.label_59.setText("")
        self.Subtitle_FontName_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Future", None))
        self.label_mediabase_35.setText(QCoreApplication.translate("MainWindow", u"Subtitle Effects:", None))
        self.label_61.setText("")
        self.label_mediabase_36.setText(QCoreApplication.translate("MainWindow", u"Cutting seconds:", None))
        self.label_62.setText("")
        self.selector_FontName_subtitles_Mode_1_long_video.setText("")
        self.Captions_PrimaryColour_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&HC0C0C0", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Captions Secondary Colour:", None))
        self.label_68.setText("")
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Captions PrimaryColour:", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Captions Fontsize:", None))
        self.Captions_BackColour_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0", None))
        self.Captions_Bold_Bool_Mode_1_long_video.setText("")
        self.Captions_Underline_Bool_Mode_1_long_video.setText("")
        self.Captions_Italic_Bool_Mode_1_long_video.setText("")
        self.Captions_Reveal_Effect_Final_Color_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0099FF&", None))
        self.label_69.setText("")
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Captions Reveal Effect\n"
"Final Color:", None))
        self.label_71.setText("")
        self.label_72.setText("")
        self.label_70.setText("")
        self.label_73.setText("")
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Captions BackColour:", None))
        self.label_74.setText("")
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Captions Alignment:", None))
        self.selector_BackColour_Captions_Mode_1_long_video.setText("")
        self.selector_OutlineColour_Captions_Mode_1_long_video.setText("")
        self.Captions_OutlineColour_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0", None))
        self.label_76.setText("")
        self.label_75.setText("")
        self.selector_Reveal_Effect_Final_Color_Captions_Mode_1_long_video.setText("")
        self.Captions_Reveal_Effect_Initial_Color_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&HCCCC33&", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Captions Reveal Effect\n"
"Initial Color:", None))
        self.label_80.setText("")
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Captions Underline:", None))
        self.label_81.setText("")
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Captions FontName:", None))
        self.Captions_FontName_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Future", None))
        self.selector_Captions_FontName_Mode_1_long_video.setText("")
        self.label_77.setText("")
        self.Captions_Shadow_Bool_Mode_1_long_video.setText("")
        self.selector_Reveal_Effect_Initial_Color_Captions_Mode_1_long_video.setText("")
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Captions Italic:", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Captions Shadow:", None))
        self.selector_PrimaryColour_Captions_Mode_1_long_video.setText("")
        self.label_78.setText("")
        self.Captions_SecondaryColour_Mode_1_long_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H8080", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Captions Bold:", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Captions OutlineColour:", None))
        self.selector_SecondaryColour_Captions_Mode_1_long_video.setText("")
        self.label_79.setText("")
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Captions Outline:", None))
        self.Captions_PrimaryColour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&HC0C0C0", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Captions Secondary Colour:", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Captions Fontsize:", None))
        self.label_13.setText("")
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Captions PrimaryColour:", None))
        self.Captions_Bold_Bool.setText("")
        self.Captions_BackColour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0", None))
        self.Captions_Underline_Bool.setText("")
        self.Captions_Italic_Bool.setText("")
        self.Captions_Reveal_Effect_Final_Color.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0099FF&", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Captions Reveal Effect\n"
"Final Color:", None))
        self.label_25.setText("")
        self.label_24.setText("")
        self.label_12.setText("")
        self.label_15.setText("")
        self.label_19.setText("")
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Captions BackColour:", None))
        self.label_17.setText("")
        self.selector_BackColour_Captions.setText("")
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Captions Alignment:", None))
        self.Captions_OutlineColour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H0", None))
        self.selector_OutlineColour_Captions.setText("")
        self.label_16.setText("")
        self.label_14.setText("")
        self.selector_Reveal_Effect_Final_Color_Captions.setText("")
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Captions Reveal Effect\n"
"Initial Color:", None))
        self.Captions_Reveal_Effect_Initial_Color.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&HCCCC33&", None))
        self.label_20.setText("")
        self.selector_Reveal_Effect_Initial_Color_Captions.setText("")
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Captions Italic:", None))
        self.Captions_Shadow_Bool.setText("")
        self.selector_PrimaryColour_Captions.setText("")
        self.label_23.setText("")
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Captions Shadow:", None))
        self.Captions_SecondaryColour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"&H8080", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Captions OutlineColour:", None))
        self.selector_SecondaryColour_Captions.setText("")
        self.label_22.setText("")
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Captions Bold:", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Captions Outline:", None))
        self.label_21.setText("")
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Captions Underline:", None))
        self.label_52.setText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Captions FontName:", None))
        self.Captions_FontName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Future", None))
        self.selector_Captions_FontName_.setText("")
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Subtitle Color:", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"text watermark:", None))
        self.Subtitle_Color.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#292D8E", None))
        self.label_4.setText("")
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"watermark image:", None))
        self.label_7.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Date and time:", None))
        self.upload_image_watermark.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.Subtitle_Effects.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Glow Effect", None))
        self.label_11.setText("")
        self.Subtitle_FontName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Future", None))
        self.label_6.setText("")
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Subtitle Effects:", None))
        self.label_8.setText("")
        self.selector_FontName_subtitles.setText("")
        self.label_10.setText("")
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Cutting seconds:", None))
        self.label_26.setText("")
        self.channel_yt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MrBeast", None))
        self.label_9.setText("")
        self.selector_color_subtitles.setText("")
        self.text_watermark.setPlaceholderText(QCoreApplication.translate("MainWindow", u"@CutsMrBeast", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Subtitle Animation:", None))
        self.Subtitle_Animation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Slow Fade-Out", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"yt channel:", None))
        self.selector_animation_subtitles.setText("")
        self.label_3.setText("")
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Subtitle FontName:", None))
        self.Select_Time.setText(QCoreApplication.translate("MainWindow", u"Select Time", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Subtitle Fontsize:", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Subtitle Vertical\n"
"Reference:", None))
        self.label_54.setText("")
        self.label_53.setText("")
        self.selector_Effects_subtitles.setText("")
        self.Start_Shortify.setText(QCoreApplication.translate("MainWindow", u"Start Shortify", None))
        self.label_Thread_id.setText(QCoreApplication.translate("MainWindow", u"Thread id:", None))
        self.label_accountinfo_9.setText("")
        self.label_accountinfo_7.setText("")
        self.label_mediabase.setText(QCoreApplication.translate("MainWindow", u"Mediabase:", None))
        self.label_WeatherForecast.setText(QCoreApplication.translate("MainWindow", u"Weather Forecast:", None))
        self.label_Target.setText(QCoreApplication.translate("MainWindow", u"Target:", None))
        self.label_File_path.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.label_accountinfo_5.setText("")
        self.label_Cuts_Duration.setText(QCoreApplication.translate("MainWindow", u"Cuts Duration:", None))
        self.label_accountinfo_6.setText("")
        self.label_accountinfo_8.setText("")
        self.label_accountinfo_10.setText("")
        self.label_Created_at.setText(QCoreApplication.translate("MainWindow", u"Created at:", None))
        self.label_accountinfo_11.setText("")
        self.label_accountinfo_12.setText("")
        self.label_mode.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Progress Create:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Running time:", None))
        self.log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_accountinfo.setText(QCoreApplication.translate("MainWindow", u"Account info", None))
        self.label_accountinfo_4.setText("")
        self.label_License_expiration.setText(QCoreApplication.translate("MainWindow", u"License expiration: 00/00/0000 00:00", None))
        self.label_29.setText("")
        self.label_accountinfo_2.setText("")
        self.label_mediabase_2.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@gmail.com", None))
        self.label_accountinfo_3.setText("")
        self.label_mediabase_3.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.api_key_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.api_key_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"apikey-content-creator", None))
        self.label_28.setText("")
        self.label_mediabase_26.setText(QCoreApplication.translate("MainWindow", u"API Server:", None))
        self.label_35.setText("")
        self.Notifications.setText("")
        self.label_mediabase_27.setText(QCoreApplication.translate("MainWindow", u"Notifications:", None))
    # retranslateUi

