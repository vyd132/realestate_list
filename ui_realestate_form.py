# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'realestate_form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QGroupBox,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 639)
        self.name_edit = QLineEdit(Form)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setGeometry(QRect(60, 60, 671, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 121, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 110, 121, 16))
        self.address_edit = QLineEdit(Form)
        self.address_edit.setObjectName(u"address_edit")
        self.address_edit.setGeometry(QRect(60, 130, 671, 24))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 180, 121, 16))
        self.value_box = QSpinBox(Form)
        self.value_box.setObjectName(u"value_box")
        self.value_box.setGeometry(QRect(61, 200, 671, 25))
        self.value_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.value_box.setProperty(u"showGroupSeparator", True)
        self.value_box.setMaximum(999999999)
        self.actuality_box = QCheckBox(Form)
        self.actuality_box.setObjectName(u"actuality_box")
        self.actuality_box.setGeometry(QRect(64, 240, 101, 21))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(610, 240, 120, 80))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 50, 101, 21))
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 30, 111, 21))
        self.description_edit = QTextEdit(Form)
        self.description_edit.setObjectName(u"description_edit")
        self.description_edit.setGeometry(QRect(60, 360, 671, 191))
        self.okbutton = QPushButton(Form)
        self.okbutton.setObjectName(u"okbutton")
        self.okbutton.setGeometry(QRect(540, 570, 80, 24))
        self.cancel_button = QPushButton(Form)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(650, 570, 80, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name_edit.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.address_edit.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.actuality_box.setText(QCoreApplication.translate("Form", u"\u0410\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u043d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u0416\u0438\u043b\u043e\u0435", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u043e\u0435", None))
        self.okbutton.setText(QCoreApplication.translate("Form", u"\u041e\u043a", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

