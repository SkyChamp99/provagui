# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'provagui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(620, 583)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.elTipo = QLineEdit(self.centralwidget)
        self.elTipo.setObjectName(u"elTipo")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.elTipo.setFont(font1)
        self.elTipo.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_3.addWidget(self.elTipo)

        self.elSede = QLineEdit(self.centralwidget)
        self.elSede.setObjectName(u"elSede")
        self.elSede.setFont(font1)
        self.elSede.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_3.addWidget(self.elSede)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.spCosto = QDoubleSpinBox(self.centralwidget)
        self.spCosto.setObjectName(u"spCosto")
        self.spCosto.setFont(font1)
        self.spCosto.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spCosto.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spCosto.setMaximum(9999.989999999999782)

        self.verticalLayout_3.addWidget(self.spCosto)

        self.btnInsertTipo = QPushButton(self.centralwidget)
        self.btnInsertTipo.setObjectName(u"btnInsertTipo")
        font3 = QFont()
        font3.setPointSize(16)
        self.btnInsertTipo.setFont(font3)

        self.verticalLayout_3.addWidget(self.btnInsertTipo)

        self.cbTipo = QComboBox(self.centralwidget)
        self.cbTipo.setObjectName(u"cbTipo")

        self.verticalLayout_3.addWidget(self.cbTipo)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.elLastname = QLineEdit(self.centralwidget)
        self.elLastname.setObjectName(u"elLastname")
        self.elLastname.setFont(font1)
        self.elLastname.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_3.addWidget(self.elLastname)

        self.elFirstname = QLineEdit(self.centralwidget)
        self.elFirstname.setObjectName(u"elFirstname")
        self.elFirstname.setFont(font1)
        self.elFirstname.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_3.addWidget(self.elFirstname)

        self.elMail = QLineEdit(self.centralwidget)
        self.elMail.setObjectName(u"elMail")
        self.elMail.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_3.addWidget(self.elMail)

        self.elPwd = QLineEdit(self.centralwidget)
        self.elPwd.setObjectName(u"elPwd")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.elPwd.setFont(font4)
        self.elPwd.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_3.addWidget(self.elPwd)

        self.btnInsertUser = QPushButton(self.centralwidget)
        self.btnInsertUser.setObjectName(u"btnInsertUser")

        self.verticalLayout_3.addWidget(self.btnInsertUser)

        self.cbUser = QComboBox(self.centralwidget)
        self.cbUser.setObjectName(u"cbUser")

        self.verticalLayout_3.addWidget(self.cbUser)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnRefresh = QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.verticalLayout_4.addWidget(self.btnRefresh)

        self.lblMsg = QLabel(self.centralwidget)
        self.lblMsg.setObjectName(u"lblMsg")
        self.lblMsg.setMaximumSize(QSize(16777215, 100))
        self.lblMsg.setAutoFillBackground(False)
        self.lblMsg.setStyleSheet(u"background-color:rgb(49, 42, 255);\n"
"\n"
"\n"
"font: 75 24pt \"MS Serif\";\n"
"\n"
"\n"
"\n"
"color:#ffff00;")

        self.verticalLayout_4.addWidget(self.lblMsg)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_4.addWidget(self.lineEdit_4)

        self.btnWelcome = QPushButton(self.centralwidget)
        self.btnWelcome.setObjectName(u"btnWelcome")
        font5 = QFont()
        font5.setFamilies([u"Arial Narrow"])
        font5.setPointSize(10)
        self.btnWelcome.setFont(font5)

        self.verticalLayout_4.addWidget(self.btnWelcome)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Gestione Tipi Visite", None))
        self.elTipo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins tipo prenotazione", None))
        self.elSede.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins sede  visita", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inserire costo visita", None))
        self.btnInsertTipo.setText(QCoreApplication.translate("MainWindow", u"ins nuovo tipo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gestione Utenti", None))
        self.elLastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins cognome", None))
        self.elFirstname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins nome", None))
        self.elMail.setText("")
        self.elMail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins mail", None))
        self.elPwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins password", None))
        self.btnInsertUser.setText(QCoreApplication.translate("MainWindow", u"ins nuovo utente", None))
        self.btnRefresh.setText(QCoreApplication.translate("MainWindow", u"refresh", None))
        self.lblMsg.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.btnWelcome.setText(QCoreApplication.translate("MainWindow", u"visualizza messaggio", None))
    # retranslateUi

