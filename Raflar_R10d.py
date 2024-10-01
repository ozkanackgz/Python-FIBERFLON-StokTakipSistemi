import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Raflar_R10 import *
import sqlite3


uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_raflarR10_ekran()
ui.setupUi(pencere)
pencere.show()


baglanti = sqlite3.connect("admin.db")
islem = baglanti.cursor()

def kayit_listele():
    ui.R10_tw.clear()
    ui.R10_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
    ui.R10_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "SELECT * FROM R10"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem.fetchall()):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.R10_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

def kayit_sil():
    sil_mesaj = QMessageBox.question(pencere, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

    if sil_mesaj == QMessageBox.Yes:
        secilen_satir = ui.R10_tw.currentRow() 
        if secilen_satir == -1:
            ui.statusbar.showMessage("Silinecek bir satır seçilmedi!")
            return

     
        silinecek_lot = ui.R10_tw.item(secilen_satir, 0).text()
    
        try:
           
            baglanti.execute("BEGIN TRANSACTION")

            
            sorgu_r10 = "DELETE FROM R10 WHERE Lot = ?"
            islem.execute(sorgu_r10, (silinecek_lot,))

          
            sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
            islem.execute(sorgu_kumaslarT, (silinecek_lot,))

       
            baglanti.commit()
            QMessageBox.information(pencere, "Silme İşlemi", "Kayıt başarıyla silindi!")
            kayit_listele()  

        except Exception as error:
           
            baglanti.rollback()
            ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")

    else:
        ui.statusbar.showMessage("Kayıt Silinirken Hata Oluştu!")


ui.listeleR10_btn.clicked.connect(kayit_listele)
ui.silR10_btn.clicked.connect(kayit_sil)


sys.exit(uygulama.exec_())