import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Araba_A38 import *
import sqlite3


uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_arabalarA38_ekran()
ui.setupUi(pencere)
pencere.show()


baglanti = sqlite3.connect("admin.db")
islem = baglanti.cursor()

def kayit_listele():
    ui.A38_tw.clear()
    ui.A38_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
    ui.A38_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "SELECT * FROM A38"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem.fetchall()):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.A38_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

def kayit_sil():
    sil_mesaj = QMessageBox.question(pencere, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

    if sil_mesaj == QMessageBox.Yes:
        secilen_satir = ui.A38_tw.currentRow() 
        if secilen_satir == -1:
            ui.statusbar.showMessage("Silinecek bir satır seçilmedi!")
            return

        
        silinecek_lot = ui.A38_tw.item(secilen_satir, 0).text()
    
        try:
            
            baglanti.execute("BEGIN TRANSACTION")

            
            sorgu_a38 = "DELETE FROM A38 WHERE Lot = ?"
            islem.execute(sorgu_a38, (silinecek_lot,))

            
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


ui.listele38_btn.clicked.connect(kayit_listele)
ui.sil38_btn.clicked.connect(kayit_sil)


sys.exit(uygulama.exec_())