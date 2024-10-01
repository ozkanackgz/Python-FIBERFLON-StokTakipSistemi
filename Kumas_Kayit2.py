import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Kumaş_Kayıt import *
import sqlite3

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_kumaskayit_ekran()
ui.setupUi(pencere)
pencere.show()

baglanti = sqlite3.connect("admin.db")
islem = baglanti.cursor()
baglanti.commit()

def kayit_ekle():
    raw_text = ui.lotKK_entry.text()
    raw_text2 = ui.kaliteKK_entry.text()
    raw_text3 = ui.genislikKK_entry.text()
    raw_text4 = ui.araba_cb.currentText()
    raw_text5 = ui.raf_cb.currentText()

    lot = int(''.join(filter(str.isdigit, raw_text)))
    kalite = int(''.join(filter(str.isdigit, raw_text2)))
    genislik = int(''.join(filter(str.isdigit, raw_text3)))
    arabakod = int(''.join(filter(str.isdigit, raw_text4)))
    rafkod = int(''.join(filter(str.isdigit, raw_text5)))

    numeric_parta1 = 1
    numeric_partr1 = 1

    ekle = ""
    ekle2 = ""

    try:
        if arabakod == numeric_parta1:  
            ekle = "insert into A1 (Lot, Kalite, Genislik) values (?, ?, ?)"
            ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
        elif rafkod == numeric_partr1:
            ekle = "insert into R1 (Lot, Kalite, Genislik) values (?, ?, ?)"
            ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
        else:
            raise ValueError("Geçersiz durum, Araba veya Raf seçimi yapılmalıdır.")
        
        islem.execute(ekle, (lot, kalite, genislik))
        islem.execute(ekle2, (lot, kalite, genislik, arabakod, rafkod))

        baglanti.commit()
        
        
        QMessageBox.information(pencere, "Başarılı", "<b>Kayıt Ekleme İşlemi Başarılı!</b>")
        
        if arabakod == numeric_parta1:
            ui.raf_cb.setCurrentIndex(0)  
        elif rafkod == numeric_partr1:
            ui.araba_cb.setCurrentIndex(0)
    
    except Exception as error:
       
        QMessageBox.critical(pencere, "Hata", f"Kayıt Ekleme İşlemi Başarısız! Hata: {error}")

ui.kaydetKK_btn.clicked.connect(kayit_ekle)
sys.exit(uygulama.exec_())