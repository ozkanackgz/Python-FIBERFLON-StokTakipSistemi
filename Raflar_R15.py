# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Raflar_R15.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_raflarR15_ekran(object):
    def setupUi(self, raflarR15_ekran):
        raflarR15_ekran.setObjectName("raflarR15_ekran")
        raflarR15_ekran.resize(1172, 883)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        raflarR15_ekran.setFont(font)
        raflarR15_ekran.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(raflarR15_ekran)
        self.centralwidget.setObjectName("centralwidget")
        self.raflarR1yazi_lbl = QtWidgets.QLabel(self.centralwidget)
        self.raflarR1yazi_lbl.setGeometry(QtCore.QRect(0, 0, 1171, 111))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.raflarR1yazi_lbl.setFont(font)
        self.raflarR1yazi_lbl.setStyleSheet("background-color: rgb(163, 221, 229);\n"
"color: rgb(34, 50, 190);")
        self.raflarR1yazi_lbl.setObjectName("raflarR1yazi_lbl")
        self.raflarR1_img = QtWidgets.QFrame(self.centralwidget)
        self.raflarR1_img.setGeometry(QtCore.QRect(210, 30, 81, 41))
        self.raflarR1_img.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.raflarR1_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raflarR1_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raflarR1_img.setObjectName("raflarR1_img")
        self.R15_tw = QtWidgets.QTableWidget(self.centralwidget)
        self.R15_tw.setGeometry(QtCore.QRect(0, 110, 1171, 751))
        self.R15_tw.setBaseSize(QtCore.QSize(0, 0))
        self.R15_tw.setRowCount(18)
        self.R15_tw.setColumnCount(3)
        self.R15_tw.setObjectName("R15_tw")
        self.R15_tw.horizontalHeader().setVisible(True)
        self.R15_tw.horizontalHeader().setCascadingSectionResizes(False)
        self.R15_tw.horizontalHeader().setDefaultSectionSize(382)
        self.R15_tw.horizontalHeader().setMinimumSectionSize(38)
        self.R15_tw.verticalHeader().setDefaultSectionSize(40)
        self.R15_tw.verticalHeader().setMinimumSectionSize(23)
        self.listeleR15_btn = QtWidgets.QPushButton(self.centralwidget)
        self.listeleR15_btn.setGeometry(QtCore.QRect(620, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listeleR15_btn.setFont(font)
        self.listeleR15_btn.setObjectName("listeleR15_btn")
        self.silR15_btn = QtWidgets.QPushButton(self.centralwidget)
        self.silR15_btn.setGeometry(QtCore.QRect(910, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.silR15_btn.setFont(font)
        self.silR15_btn.setObjectName("silR15_btn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(850, 60, 281, 41))
        self.textBrowser.setObjectName("textBrowser")
        raflarR15_ekran.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(raflarR15_ekran)
        self.statusbar.setObjectName("statusbar")
        raflarR15_ekran.setStatusBar(self.statusbar)

        self.retranslateUi(raflarR15_ekran)
        QtCore.QMetaObject.connectSlotsByName(raflarR15_ekran)

    def retranslateUi(self, raflarR15_ekran):
        _translate = QtCore.QCoreApplication.translate
        self.raflarR1yazi_lbl.setText(_translate("raflarR15_ekran", " Raflar R15"))
        self.listeleR15_btn.setText(_translate("raflarR15_ekran", "Listele"))
        self.silR15_btn.setText(_translate("raflarR15_ekran", "Sil"))
        self.textBrowser.setHtml(_translate("raflarR15_ekran", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Silmek istediğiniz kumaş için &quot;LOT&quot; seçiniz ve daha sonra &quot;SİL&quot; butonuna tıklayınız!</span></p></body></html>"))
