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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(777, 583)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.elTipo = QLineEdit(self.centralwidget)
        self.elTipo.setObjectName(u"elTipo")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        self.elTipo.setFont(font)
        self.elTipo.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_3.addWidget(self.elTipo)

        self.elSede = QLineEdit(self.centralwidget)
        self.elSede.setObjectName(u"elSede")
        self.elSede.setFont(font)
        self.elSede.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_3.addWidget(self.elSede)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.spCosto = QDoubleSpinBox(self.centralwidget)
        self.spCosto.setObjectName(u"spCosto")
        self.spCosto.setFont(font)
        self.spCosto.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spCosto.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spCosto.setMaximum(9999.989999999999782)

        self.verticalLayout_3.addWidget(self.spCosto)

        self.btnPlus = QPushButton(self.centralwidget)
        self.btnPlus.setObjectName(u"btnPlus")
        font2 = QFont()
        font2.setPointSize(16)
        self.btnPlus.setFont(font2)

        self.verticalLayout_3.addWidget(self.btnPlus)

        self.cbTipo = QComboBox(self.centralwidget)
        self.cbTipo.setObjectName(u"cbTipo")

        self.verticalLayout_3.addWidget(self.cbTipo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnRefresh = QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.verticalLayout_4.addWidget(self.btnRefresh)

        self.elCognome = QLineEdit(self.centralwidget)
        self.elCognome.setObjectName(u"elCognome")
        self.elCognome.setFont(font)
        self.elCognome.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_4.addWidget(self.elCognome)

        self.elNome = QLineEdit(self.centralwidget)
        self.elNome.setObjectName(u"elNome")
        self.elNome.setFont(font)
        self.elNome.setStyleSheet(u"border:2px solid #899999;border-radius:6;\n"
"padding:4px;")

        self.verticalLayout_4.addWidget(self.elNome)

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

        self.btnWelcome = QPushButton(self.centralwidget)
        self.btnWelcome.setObjectName(u"btnWelcome")
        font3 = QFont()
        font3.setFamilies([u"Arial Narrow"])
        font3.setPointSize(10)
        self.btnWelcome.setFont(font3)

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
        self.elTipo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins tipo prenotazione", None))
        self.elSede.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins sede  visita", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inserire costo visita", None))
        self.btnPlus.setText(QCoreApplication.translate("MainWindow", u"ins nuovo tipo", None))
        self.btnRefresh.setText(QCoreApplication.translate("MainWindow", u"refresh", None))
        self.elCognome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins cognome", None))
        self.elNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins nome", None))
        self.lblMsg.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.btnWelcome.setText(QCoreApplication.translate("MainWindow", u"visualizza messaggio", None))
    # retranslateUi

