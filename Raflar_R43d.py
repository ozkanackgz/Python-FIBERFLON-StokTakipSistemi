import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Raflar_R43 import *
import sqlite3


uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_raflarR43_ekran()
ui.setupUi(pencere)
pencere.show()


baglanti = sqlite3.connect("admin.db")
islem = baglanti.cursor()

def kayit_listele():
    ui.R43_tw.clear()
    ui.R43_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
    ui.R43_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "SELECT * FROM R43"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem.fetchall()):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.R43_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

def kayit_sil():
    sil_mesaj = QMessageBox.question(pencere, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

    if sil_mesaj == QMessageBox.Yes:
        secilen_satir = ui.R43_tw.currentRow() 
        if secilen_satir == -1:
            ui.statusbar.showMessage("Silinecek bir satır seçilmedi!")
            return

       
        silinecek_lot = ui.R43_tw.item(secilen_satir, 0).text()
    
        try:
          
            baglanti.execute("BEGIN TRANSACTION")

            
            sorgu_r43 = "DELETE FROM R43 WHERE Lot = ?"
            islem.execute(sorgu_r43, (silinecek_lot,))

            
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


ui.listeleR43_btn.clicked.connect(kayit_listele)
ui.silR43_btn.clicked.connect(kayit_sil)


sys.exit(uygulama.exec_())