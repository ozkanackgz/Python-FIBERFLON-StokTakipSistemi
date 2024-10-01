# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Araba_A72.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_arabalarA72_ekran(object):
    def setupUi(self, arabalarA72_ekran):
        arabalarA72_ekran.setObjectName("arabalarA72_ekran")
        arabalarA72_ekran.resize(1171, 883)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        arabalarA72_ekran.setFont(font)
        arabalarA72_ekran.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(arabalarA72_ekran)
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
        self.arabaA1_img.setGeometry(QtCore.QRect(210, 30, 81, 41))
        self.arabaA1_img.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.arabaA1_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.arabaA1_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.arabaA1_img.setObjectName("arabaA1_img")
        self.listele72_btn = QtWidgets.QPushButton(self.centralwidget)
        self.listele72_btn.setGeometry(QtCore.QRect(650, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listele72_btn.setFont(font)
        self.listele72_btn.setObjectName("listele72_btn")
        self.A72_tw = QtWidgets.QTableWidget(self.centralwidget)
        self.A72_tw.setGeometry(QtCore.QRect(0, 110, 1171, 751))
        self.A72_tw.setBaseSize(QtCore.QSize(0, 0))
        self.A72_tw.setRowCount(18)
        self.A72_tw.setColumnCount(3)
        self.A72_tw.setObjectName("A72_tw")
        self.A72_tw.horizontalHeader().setVisible(True)
        self.A72_tw.horizontalHeader().setCascadingSectionResizes(False)
        self.A72_tw.horizontalHeader().setDefaultSectionSize(382)
        self.A72_tw.horizontalHeader().setMinimumSectionSize(38)
        self.A72_tw.verticalHeader().setDefaultSectionSize(40)
        self.A72_tw.verticalHeader().setMinimumSectionSize(23)
        self.sil72_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sil72_btn.setGeometry(QtCore.QRect(930, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sil72_btn.setFont(font)
        self.sil72_btn.setObjectName("sil72_btn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(870, 60, 281, 41))
        self.textBrowser.setObjectName("textBrowser")
        arabalarA72_ekran.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(arabalarA72_ekran)
        self.statusbar.setObjectName("statusbar")
        arabalarA72_ekran.setStatusBar(self.statusbar)

        self.retranslateUi(arabalarA72_ekran)
        QtCore.QMetaObject.connectSlotsByName(arabalarA72_ekran)

    def retranslateUi(self, arabalarA72_ekran):
        _translate = QtCore.QCoreApplication.translate
        self.arabaA1yazi_lbl.setText(_translate("arabalarA72_ekran", " Araba A72"))
        self.listele72_btn.setText(_translate("arabalarA72_ekran", "Listele"))
        self.sil72_btn.setText(_translate("arabalarA72_ekran", "Sil"))
        self.textBrowser.setHtml(_translate("arabalarA72_ekran", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Silmek istediğiniz kumaş için &quot;LOT&quot; seçiniz ve daha sonra &quot;SİL&quot; butonuna tıklayınız!</span></p></body></html>"))
