# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Araba_A103.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_arabalarA103_ekran(object):
    def setupUi(self, arabalarA103_ekran):
        arabalarA103_ekran.setObjectName("arabalarA103_ekran")
        arabalarA103_ekran.resize(1171, 883)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        arabalarA103_ekran.setFont(font)
        arabalarA103_ekran.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(arabalarA103_ekran)
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
        self.arabaA1_img.setGeometry(QtCore.QRect(230, 30, 81, 41))
        self.arabaA1_img.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.arabaA1_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.arabaA1_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.arabaA1_img.setObjectName("arabaA1_img")
        self.listele103_btn = QtWidgets.QPushButton(self.centralwidget)
        self.listele103_btn.setGeometry(QtCore.QRect(650, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listele103_btn.setFont(font)
        self.listele103_btn.setObjectName("listele103_btn")
        self.A103_tw = QtWidgets.QTableWidget(self.centralwidget)
        self.A103_tw.setGeometry(QtCore.QRect(0, 110, 1171, 751))
        self.A103_tw.setBaseSize(QtCore.QSize(0, 0))
        self.A103_tw.setRowCount(18)
        self.A103_tw.setColumnCount(3)
        self.A103_tw.setObjectName("A103_tw")
        self.A103_tw.horizontalHeader().setVisible(True)
        self.A103_tw.horizontalHeader().setCascadingSectionResizes(False)
        self.A103_tw.horizontalHeader().setDefaultSectionSize(382)
        self.A103_tw.horizontalHeader().setMinimumSectionSize(38)
        self.A103_tw.verticalHeader().setDefaultSectionSize(40)
        self.A103_tw.verticalHeader().setMinimumSectionSize(23)
        self.sil103_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sil103_btn.setGeometry(QtCore.QRect(930, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sil103_btn.setFont(font)
        self.sil103_btn.setObjectName("sil103_btn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(870, 60, 281, 41))
        self.textBrowser.setObjectName("textBrowser")
        arabalarA103_ekran.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(arabalarA103_ekran)
        self.statusbar.setObjectName("statusbar")
        arabalarA103_ekran.setStatusBar(self.statusbar)

        self.retranslateUi(arabalarA103_ekran)
        QtCore.QMetaObject.connectSlotsByName(arabalarA103_ekran)

    def retranslateUi(self, arabalarA103_ekran):
        _translate = QtCore.QCoreApplication.translate
        self.arabaA1yazi_lbl.setText(_translate("arabalarA103_ekran", " Araba A103"))
        self.listele103_btn.setText(_translate("arabalarA103_ekran", "Listele"))
        self.sil103_btn.setText(_translate("arabalarA103_ekran", "Sil"))
        self.textBrowser.setHtml(_translate("arabalarA103_ekran", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Silmek istediğiniz kumaş için &quot;LOT&quot; seçiniz ve daha sonra &quot;SİL&quot; butonuna tıklayınız!</span></p></body></html>"))
