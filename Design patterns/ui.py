# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(596, 130)
        Form.setMaximumSize(QSize(16777215, 130))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.btn_convert = QPushButton(Form)
        self.btn_convert.setObjectName(u"btn_convert")

        self.gridLayout.addWidget(self.btn_convert, 3, 0, 1, 1)

        self.btn_locate_file = QPushButton(Form)
        self.btn_locate_file.setObjectName(u"btn_locate_file")

        self.gridLayout.addWidget(self.btn_locate_file, 0, 3, 1, 1)

        self.btn_locate_folder_2 = QPushButton(Form)
        self.btn_locate_folder_2.setObjectName(u"btn_locate_folder_2")

        self.gridLayout.addWidget(self.btn_locate_folder_2, 1, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rbtn_tocsv = QRadioButton(Form)
        self.rbtn_tocsv.setObjectName(u"rbtn_tocsv")
        self.rbtn_tocsv.setChecked(True)

        self.horizontalLayout_2.addWidget(self.rbtn_tocsv)

        self.rbtn_toxml = QRadioButton(Form)
        self.rbtn_toxml.setObjectName(u"rbtn_toxml")

        self.horizontalLayout_2.addWidget(self.rbtn_toxml)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.textEdit = QLineEdit(Form)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.textEdit_2 = QLineEdit(Form)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)


        self.retranslateUi(Form)
        self.btn_locate_file.clicked.connect(Form.btn_locate_file_clicked)
        self.btn_locate_folder_2.clicked.connect(Form.btn_locate_folder_clicked)
        self.btn_convert.clicked.connect(Form.btn_convert_clicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Input file:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Output file:", None))
        self.btn_convert.setText(QCoreApplication.translate("Form", u"Convert", None))
        self.btn_locate_file.setText(QCoreApplication.translate("Form", u"Locate", None))
        self.btn_locate_folder_2.setText(QCoreApplication.translate("Form", u"Locate", None))
        self.rbtn_tocsv.setText(QCoreApplication.translate("Form", u"to CSV", None))
        self.rbtn_toxml.setText(QCoreApplication.translate("Form", u"to XML", None))
    # retranslateUi

