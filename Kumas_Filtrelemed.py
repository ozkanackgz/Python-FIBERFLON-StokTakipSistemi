import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Kumas_Filtreleme import *

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_kumasfiltreleme_ekran()
ui.setupUi(pencere)
pencere.show()



import sqlite3

baglanti = sqlite3.connect("admin.db")
islem = baglanti.cursor()
baglanti.commit()


def kayit_listele():
    ui.kumaslar_tw.clear()
    ui.kumaslar_tw.setHorizontalHeaderLabels(("Lot","Kalite","Genişlik","ArabaKod","RafKod"))
    ui.kumaslar_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "select * from kumaslarT"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.kumaslar_tw.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

def kategoriye_gore_listele():
    listelenecek_kategori = ui.kalitesec_cb.currentText()
    ui.kumaslar_tw.clear()
    ui.kumaslar_tw.setHorizontalHeaderLabels(("Lot","Kalite","Genişlik","ArabaKod","RafKod"))
    ui.kumaslar_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "select * from kumaslarT where Kalite = ?"
    islem.execute(sorgu,(listelenecek_kategori,))
    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.kumaslar_tw.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))


ui.tumunulist_btn.clicked.connect(kayit_listele)
ui.ks_listele_btn.clicked.connect(kategoriye_gore_listele)


sys.exit(uygulama.exec_())