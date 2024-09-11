# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledzisi.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(752, 585)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_6 = QCheckBox(Form)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(Form)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(Form)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout.addWidget(self.checkBox_8)

        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(Form)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.checkBox_9 = QCheckBox(Form)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(Form)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setMinimumSize(QSize(109, 20))

        self.verticalLayout.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(Form)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.verticalLayout.addWidget(self.checkBox_11)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(561, 401))

        self.gridLayout_2.addWidget(self.textBrowser, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(349, 19))

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 2, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 2, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 2, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u547d\u4ee4\u6df7\u6dc6", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u8bfb\u6587\u4ef6+\u6df7\u6dc6", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"\u8bfb\u6587\u4ef6", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"php\u8bfb\u6587\u4ef6", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"php\u4ee3\u7801\u6267\u884c", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u516b\u8fdb\u5236\u7f16\u7801", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u5341\u516d\u8fdb\u5236\u7f16\u7801", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"IP\u7f16\u7801", None))
        self.checkBox_9.setText(QCoreApplication.translate("Form", u"\u6c99\u7bb1\u9003\u9038", None))
        self.checkBox_10.setText(QCoreApplication.translate("Form", u"SSTI", None))
        self.checkBox_11.setText(QCoreApplication.translate("Form", u"phpinfo\u4fe1\u606f", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u53bb\u91cd", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u9ed1\u540d\u5355\u8fc7\u6ee4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
    # retranslateUi

