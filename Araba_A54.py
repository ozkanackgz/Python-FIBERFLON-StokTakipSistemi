# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Araba_A54.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_arabalarA54_ekran(object):
    def setupUi(self, arabalarA54_ekran):
        arabalarA54_ekran.setObjectName("arabalarA54_ekran")
        arabalarA54_ekran.resize(1171, 883)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        arabalarA54_ekran.setFont(font)
        arabalarA54_ekran.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(arabalarA54_ekran)
        self.centralwidget.setObjectName("centralwidget")
        self.arabaA1yazi_lbl = QtWidgets.QLabel(self.centralwidget)
        self.arabaA1yazi_lbl.setGeometry(QtCore.QRect(0, 0, 1171, 111))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.arabaA1yazi_lbl.setFont(font)
        self.arabaA1yazi_lbl.setStyleSheet("background-color: rgb(163, 221, 229);\n"
"color: rgb(34, 50, 190);")
        self.arabaA1yazi_lbl.setObjectName("arabaA1yazi_lbl")
        self.arabaA1_img = QtWidgets.QFrame(self.centralwidget)
        self.arabaA1_img.setGeometry(QtCore.QRect(200, 30, 81, 41))
        self.arabaA1_img.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.arabaA1_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.arabaA1_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.arabaA1_img.setObjectName("arabaA1_img")
        self.listele54_btn = QtWidgets.QPushButton(self.centralwidget)
        self.listele54_btn.setGeometry(QtCore.QRect(650, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listele54_btn.setFont(font)
        self.listele54_btn.setObjectName("listele54_btn")
        self.A54_tw = QtWidgets.QTableWidget(self.centralwidget)
        self.A54_tw.setGeometry(QtCore.QRect(0, 110, 1171, 751))
        self.A54_tw.setBaseSize(QtCore.QSize(0, 0))
        self.A54_tw.setRowCount(18)
        self.A54_tw.setColumnCount(3)
        self.A54_tw.setObjectName("A54_tw")
        self.A54_tw.horizontalHeader().setVisible(True)
        self.A54_tw.horizontalHeader().setCascadingSectionResizes(False)
        self.A54_tw.horizontalHeader().setDefaultSectionSize(382)
        self.A54_tw.horizontalHeader().setMinimumSectionSize(38)
        self.A54_tw.verticalHeader().setDefaultSectionSize(40)
        self.A54_tw.verticalHeader().setMinimumSectionSize(23)
        self.sil54_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sil54_btn.setGeometry(QtCore.QRect(930, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sil54_btn.setFont(font)
        self.sil54_btn.setObjectName("sil54_btn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(870, 60, 281, 41))
        self.textBrowser.setObjectName("textBrowser")
        arabalarA54_ekran.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(arabalarA54_ekran)
        self.statusbar.setObjectName("statusbar")
        arabalarA54_ekran.setStatusBar(self.statusbar)

        self.retranslateUi(arabalarA54_ekran)
        QtCore.QMetaObject.connectSlotsByName(arabalarA54_ekran)

    def retranslateUi(self, arabalarA54_ekran):
        _translate = QtCore.QCoreApplication.translate
        self.arabaA1yazi_lbl.setText(_translate("arabalarA54_ekran", " Araba A54"))
        self.listele54_btn.setText(_translate("arabalarA54_ekran", "Listele"))
        self.sil54_btn.setText(_translate("arabalarA54_ekran", "Sil"))
        self.textBrowser.setHtml(_translate("arabalarA54_ekran", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Silmek istediğiniz kumaş için &quot;LOT&quot; seçiniz ve daha sonra &quot;SİL&quot; butonuna tıklayınız!</span></p></body></html>"))
