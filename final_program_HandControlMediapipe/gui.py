# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(798, 630)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.v1 = QFrame(Form)
        self.v1.setObjectName(u"v1")
        self.v1.setStyleSheet(u"background-color:rgb(10,20,40);")
        self.v1.setFrameShape(QFrame.StyledPanel)
        self.v1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.v1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.l1 = QLabel(self.v1)
        self.l1.setObjectName(u"l1")
        font = QFont()
        font.setPointSize(19)
        self.l1.setFont(font)
        self.l1.setStyleSheet(u"color:white;")

        self.verticalLayout_2.addWidget(self.l1)

        self.b1 = QPushButton(self.v1)
        self.b1.setObjectName(u"b1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1.sizePolicy().hasHeightForWidth())
        self.b1.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setUnderline(True)
        self.b1.setFont(font1)
        self.b1.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(10,20,40);\n"
"color:white;\n"
"}")

        self.verticalLayout_2.addWidget(self.b1)


        self.verticalLayout_4.addWidget(self.v1)

        self.h2 = QFrame(Form)
        self.h2.setObjectName(u"h2")
        self.h2.setStyleSheet(u"background-color:rgb(100,200,240);")
        self.h2.setFrameShape(QFrame.StyledPanel)
        self.h2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.h2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.r1 = QRadioButton(self.h2)
        self.r1.setObjectName(u"r1")
        font2 = QFont()
        font2.setPointSize(12)
        self.r1.setFont(font2)

        self.verticalLayout_3.addWidget(self.r1)

        self.r2 = QRadioButton(self.h2)
        self.r2.setObjectName(u"r2")
        self.r2.setFont(font2)

        self.verticalLayout_3.addWidget(self.r2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.l2 = QLabel(self.h2)
        self.l2.setObjectName(u"l2")
        self.l2.setStyleSheet(u"background-color:rgb(200,200,200);\n"
"border:1px solid white;")
        self.l2.setScaledContents(True)
        self.l2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.l2)

        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_4.addWidget(self.h2)

        self.h3 = QHBoxLayout()
        self.h3.setObjectName(u"h3")
        self.r3 = QRadioButton(Form)
        self.r3.setObjectName(u"r3")
        sizePolicy.setHeightForWidth(self.r3.sizePolicy().hasHeightForWidth())
        self.r3.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.r3)


        self.verticalLayout_4.addLayout(self.h3)

        self.h4 = QHBoxLayout()
        self.h4.setObjectName(u"h4")
        self.start = QPushButton(Form)
        self.start.setObjectName(u"start")
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setMinimumSize(QSize(0, 8))
        self.start.setFont(font2)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(20,40,100);\n"
"color:white;\n"
"border:1px solid white;\n"
"width:100px;\n"
"height:50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(20,40,50);\n"
"color:white;\n"
"border:1px solid white;\n"
"}")
        self.start.setIconSize(QSize(16, 16))

        self.h4.addWidget(self.start)

        self.stop = QPushButton(Form)
        self.stop.setObjectName(u"stop")
        sizePolicy.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy)
        self.stop.setMinimumSize(QSize(0, 8))
        self.stop.setFont(font2)
        self.stop.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(20,40,100);\n"
"color:white;\n"
"border:1px solid white;\n"
"width:100px;\n"
"height:50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(20,40,50);\n"
"color:white;\n"
"border:1px solid white;\n"
"}")

        self.h4.addWidget(self.stop)


        self.verticalLayout_4.addLayout(self.h4)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u624b\u52bf\u63a7\u5236\u7cfb\u7edf", None))
        self.l1.setText(QCoreApplication.translate("Form", u"\u624b\u52bf\u63a7\u5236\u7cfb\u7edf", None))
        self.b1.setText(QCoreApplication.translate("Form", u"\u8bf4\u660e\u6587\u6863", None))
        self.r1.setText(QCoreApplication.translate("Form", u"\u952e\u76d8\u63a7\u5236\u6a21\u5f0f", None))
        self.r2.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u63a7\u5236\u6a21\u5f0f", None))
        self.l2.setText("")
        self.r3.setText(QCoreApplication.translate("Form", u"\u5141\u8bb8\u8c03\u7528\u6444\u50cf\u5934", None))
        self.start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
    # retranslateUi

