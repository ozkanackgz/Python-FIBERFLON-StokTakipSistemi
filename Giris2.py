import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QHeaderView, QTableWidgetItem
from Giris import Ui_giris_ekran
from Depo import Ui_depo_ekran
from Arabalar import Ui_arabalar_ekran
from Araba_A1 import Ui_arabalarA1_ekran
from Araba_A2 import Ui_arabalarA2_ekran
from Araba_A3 import Ui_arabalarA3_ekran
from Araba_A4 import Ui_arabalarA4_ekran
from Araba_A5 import Ui_arabalarA5_ekran
from Araba_A6 import Ui_arabalarA6_ekran
from Araba_A7 import Ui_arabalarA7_ekran
from Araba_A8 import Ui_arabalarA8_ekran
from Araba_A9 import Ui_arabalarA9_ekran
from Araba_A10 import Ui_arabalarA10_ekran
from Araba_A11 import Ui_arabalarA11_ekran
from Araba_A12 import Ui_arabalarA12_ekran
from Araba_A13 import Ui_arabalarA13_ekran
from Araba_A14 import Ui_arabalarA14_ekran
from Araba_A15 import Ui_arabalarA15_ekran
from Araba_A16 import Ui_arabalarA16_ekran
from Araba_A17 import Ui_arabalarA17_ekran
from Araba_A18 import Ui_arabalarA18_ekran
from Araba_A19 import Ui_arabalarA19_ekran
from Araba_A20 import Ui_arabalarA20_ekran
from Araba_A21 import Ui_arabalarA21_ekran
from Araba_A22 import Ui_arabalarA22_ekran
from Araba_A23 import Ui_arabalarA23_ekran
from Araba_A24 import Ui_arabalarA24_ekran
from Araba_A25 import Ui_arabalarA25_ekran
from Araba_A26 import Ui_arabalarA26_ekran
from Araba_A27 import Ui_arabalarA27_ekran
from Araba_A28 import Ui_arabalarA28_ekran
from Araba_A29 import Ui_arabalarA29_ekran
from Araba_A30 import Ui_arabalarA30_ekran
from Araba_A31 import Ui_arabalarA31_ekran
from Araba_A32 import Ui_arabalarA32_ekran
from Araba_A33 import Ui_arabalarA33_ekran
from Araba_A34 import Ui_arabalarA34_ekran
from Araba_A35 import Ui_arabalarA35_ekran
from Araba_A36 import Ui_arabalarA36_ekran
from Araba_A37 import Ui_arabalarA37_ekran
from Araba_A38 import Ui_arabalarA38_ekran
from Araba_A39 import Ui_arabalarA39_ekran
from Araba_A40 import Ui_arabalarA40_ekran
from Araba_A41 import Ui_arabalarA41_ekran
from Araba_A42 import Ui_arabalarA42_ekran
from Araba_A43 import Ui_arabalarA43_ekran
from Araba_A44 import Ui_arabalarA44_ekran
from Araba_A45 import Ui_arabalarA45_ekran
from Araba_A46 import Ui_arabalarA46_ekran
from Araba_A47 import Ui_arabalarA47_ekran
from Araba_A48 import Ui_arabalarA48_ekran
from Araba_A49 import Ui_arabalarA49_ekran
from Araba_A50 import Ui_arabalarA50_ekran
from Araba_A51 import Ui_arabalarA51_ekran
from Araba_A52 import Ui_arabalarA52_ekran
from Araba_A53 import Ui_arabalarA53_ekran
from Araba_A54 import Ui_arabalarA54_ekran
from Araba_A55 import Ui_arabalarA55_ekran
from Araba_A56 import Ui_arabalarA56_ekran
from Araba_A57 import Ui_arabalarA57_ekran
from Araba_A58 import Ui_arabalarA58_ekran
from Araba_A59 import Ui_arabalarA59_ekran
from Araba_A60 import Ui_arabalarA60_ekran
from Araba_A61 import Ui_arabalarA61_ekran
from Araba_A62 import Ui_arabalarA62_ekran
from Araba_A63 import Ui_arabalarA63_ekran
from Araba_A64 import Ui_arabalarA64_ekran
from Araba_A65 import Ui_arabalarA65_ekran
from Araba_A66 import Ui_arabalarA66_ekran
from Araba_A67 import Ui_arabalarA67_ekran
from Araba_A68 import Ui_arabalarA68_ekran
from Araba_A69 import Ui_arabalarA69_ekran
from Araba_A70 import Ui_arabalarA70_ekran
from Araba_A71 import Ui_arabalarA71_ekran
from Araba_A72 import Ui_arabalarA72_ekran
from Araba_A73 import Ui_arabalarA73_ekran
from Araba_A74 import Ui_arabalarA74_ekran
from Araba_A75 import Ui_arabalarA75_ekran
from Araba_A76 import Ui_arabalarA76_ekran
from Araba_A77 import Ui_arabalarA77_ekran
from Araba_A78 import Ui_arabalarA78_ekran
from Araba_A79 import Ui_arabalarA79_ekran
from Araba_A80 import Ui_arabalarA80_ekran
from Araba_A81 import Ui_arabalarA81_ekran
from Araba_A82 import Ui_arabalarA82_ekran
from Araba_A83 import Ui_arabalarA83_ekran
from Araba_A84 import Ui_arabalarA84_ekran
from Araba_A85 import Ui_arabalarA85_ekran
from Araba_A86 import Ui_arabalarA86_ekran
from Araba_A87 import Ui_arabalarA87_ekran
from Araba_A88 import Ui_arabalarA88_ekran
from Araba_A89 import Ui_arabalarA89_ekran
from Araba_A90 import Ui_arabalarA90_ekran
from Araba_A91 import Ui_arabalarA91_ekran
from Araba_A92 import Ui_arabalarA92_ekran
from Araba_A93 import Ui_arabalarA93_ekran
from Araba_A94 import Ui_arabalarA94_ekran
from Araba_A95 import Ui_arabalarA95_ekran
from Araba_A96 import Ui_arabalarA96_ekran
from Araba_A97 import Ui_arabalarA97_ekran
from Araba_A98 import Ui_arabalarA98_ekran
from Araba_A99 import Ui_arabalarA99_ekran
from Araba_A100 import Ui_arabalarA100_ekran
from Araba_A101 import Ui_arabalarA101_ekran
from Araba_A102 import Ui_arabalarA102_ekran
from Araba_A103 import Ui_arabalarA103_ekran
from Raflar import Ui_raflar_ekran
from Raflar_R1 import Ui_raflarR1_ekran
from Raflar_R2 import Ui_raflarR2_ekran
from Raflar_R3 import Ui_raflarR3_ekran
from Raflar_R4 import Ui_raflarR4_ekran
from Raflar_R5 import Ui_raflarR5_ekran
from Raflar_R6 import Ui_raflarR6_ekran
from Raflar_R7 import Ui_raflarR7_ekran
from Raflar_R8 import Ui_raflarR8_ekran
from Raflar_R9 import Ui_raflarR9_ekran
from Raflar_R10 import Ui_raflarR10_ekran
from Raflar_R11 import Ui_raflarR11_ekran
from Raflar_R12 import Ui_raflarR12_ekran
from Raflar_R13 import Ui_raflarR13_ekran
from Raflar_R14 import Ui_raflarR14_ekran
from Raflar_R15 import Ui_raflarR15_ekran
from Raflar_R16 import Ui_raflarR16_ekran
from Raflar_R17 import Ui_raflarR17_ekran
from Raflar_R18 import Ui_raflarR18_ekran
from Raflar_R19 import Ui_raflarR19_ekran
from Raflar_R20 import Ui_raflarR20_ekran
from Raflar_R21 import Ui_raflarR21_ekran
from Raflar_R22 import Ui_raflarR22_ekran
from Raflar_R23 import Ui_raflarR23_ekran
from Raflar_R24 import Ui_raflarR24_ekran
from Raflar_R25 import Ui_raflarR25_ekran
from Raflar_R26 import Ui_raflarR26_ekran
from Raflar_R27 import Ui_raflarR27_ekran
from Raflar_R28 import Ui_raflarR28_ekran
from Raflar_R29 import Ui_raflarR29_ekran
from Raflar_R30 import Ui_raflarR30_ekran
from Raflar_R31 import Ui_raflarR31_ekran
from Raflar_R32 import Ui_raflarR32_ekran
from Raflar_R33 import Ui_raflarR33_ekran
from Raflar_R34 import Ui_raflarR34_ekran
from Raflar_R35 import Ui_raflarR35_ekran
from Raflar_R36 import Ui_raflarR36_ekran
from Raflar_R37 import Ui_raflarR37_ekran
from Raflar_R38 import Ui_raflarR38_ekran
from Raflar_R39 import Ui_raflarR39_ekran
from Raflar_R40 import Ui_raflarR40_ekran
from Raflar_R41 import Ui_raflarR41_ekran
from Raflar_R42 import Ui_raflarR42_ekran
from Raflar_R43 import Ui_raflarR43_ekran
from Raflar_R44 import Ui_raflarR44_ekran
from Raflar_R45 import Ui_raflarR45_ekran
from Raflar_R46 import Ui_raflarR46_ekran
from Raflar_R47 import Ui_raflarR47_ekran
from Raflar_R48 import Ui_raflarR48_ekran
from Raflar_R49 import Ui_raflarR49_ekran
from Raflar_R50 import Ui_raflarR50_ekran
from Raflar_R51 import Ui_raflarR51_ekran
from Raflar_R52 import Ui_raflarR52_ekran
from Raflar_R53 import Ui_raflarR53_ekran
from Raflar_R54 import Ui_raflarR54_ekran
from Raflar_R55 import Ui_raflarR55_ekran
from Raflar_R56 import Ui_raflarR56_ekran
from Raflar_R57 import Ui_raflarR57_ekran
from Kumas_Kayit import Ui_kumaskayit_ekran
from Kumas_Filtreleme import Ui_kumasfiltreleme_ekran


class LoginApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_giris_ekran()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.giris_btn.clicked.connect(self.login)
        self.baglanti = sqlite3.connect("admin.db")
        self.islem = self.baglanti.cursor()

    def login(self):
        username = self.ui.kullaniciadi_entry.text()
        password = self.ui.sifre_entry.text()

        query = "SELECT * FROM admint WHERE kullaniciadi=? AND sifre=?"
        self.islem.execute(query, (username, password))
        user = self.islem.fetchone()

        if user:
            self.openDepoWindow()
        else:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı veya şifre yanlış!')

        
        self.ui.kullaniciadi_entry.clear()
        self.ui.sifre_entry.clear()

    def openDepoWindow(self):
        self.hide()  
        self.depoWindow = QMainWindow()
        self.depoUi = Ui_depo_ekran()
        self.depoUi.setupUi(self.depoWindow)
    
   
        self.depoUi.arabalar_btn.clicked.connect(self.openArabalarWindow)
        self.depoUi.raflar_btn.clicked.connect(self.openRaflarWindow)
        self.depoUi.kumaskayit_btn.clicked.connect(self.openKumasKayitWindow)
        self.depoUi.kumaskayit_btn_2.clicked.connect(self.openKumasFiltrelemeWindow)

   
        self.depoWindow.closeEvent = self.showMainWindow
        self.depoWindow.show()

    def showMainWindow(self, event):
        self.show()  
        event.accept()  
        self.depoWindow.show()

    def openArabalarWindow(self):
        self.depoWindow.close()
        self.arabalarWindow = QMainWindow()
        self.arabalarUi = Ui_arabalar_ekran()
        self.arabalarUi.setupUi(self.arabalarWindow)
        self.arabalarUi.a1_btn.clicked.connect(self.openArabalarA1Window)
        self.arabalarUi.a2_btn.clicked.connect(self.openArabalarA2Window)
        self.arabalarUi.a3_btn.clicked.connect(self.openArabalarA3Window)
        self.arabalarUi.a4_btn.clicked.connect(self.openArabalarA4Window)
        self.arabalarUi.a5_btn.clicked.connect(self.openArabalarA5Window)
        self.arabalarUi.a6_btn.clicked.connect(self.openArabalarA6Window)
        self.arabalarUi.a7_btn.clicked.connect(self.openArabalarA7Window)
        self.arabalarUi.a8_btn.clicked.connect(self.openArabalarA8Window)
        self.arabalarUi.a9_btn.clicked.connect(self.openArabalarA9Window)
        self.arabalarUi.a10_btn.clicked.connect(self.openArabalarA10Window)
        self.arabalarUi.a11_btn.clicked.connect(self.openArabalarA11Window)
        self.arabalarUi.a12_btn.clicked.connect(self.openArabalarA12Window)
        self.arabalarUi.a13_btn.clicked.connect(self.openArabalarA13Window)
        self.arabalarUi.a14_btn.clicked.connect(self.openArabalarA14Window)
        self.arabalarUi.a15_btn.clicked.connect(self.openArabalarA15Window)
        self.arabalarUi.a16_btn.clicked.connect(self.openArabalarA16Window)
        self.arabalarUi.a17_btn.clicked.connect(self.openArabalarA17Window)
        self.arabalarUi.a18_btn.clicked.connect(self.openArabalarA18Window)
        self.arabalarUi.a19_btn.clicked.connect(self.openArabalarA19Window)
        self.arabalarUi.a20_btn.clicked.connect(self.openArabalarA20Window)
        self.arabalarUi.a21_btn.clicked.connect(self.openArabalarA21Window)
        self.arabalarUi.a22_btn.clicked.connect(self.openArabalarA22Window)
        self.arabalarUi.a23_btn.clicked.connect(self.openArabalarA23Window)
        self.arabalarUi.a24_btn.clicked.connect(self.openArabalarA24Window)
        self.arabalarUi.a25_btn.clicked.connect(self.openArabalarA25Window)
        self.arabalarUi.a26_btn.clicked.connect(self.openArabalarA26Window)
        self.arabalarUi.a27_btn.clicked.connect(self.openArabalarA27Window)
        self.arabalarUi.a28_btn.clicked.connect(self.openArabalarA28Window)
        self.arabalarUi.a29_btn.clicked.connect(self.openArabalarA29Window)
        self.arabalarUi.a30_btn.clicked.connect(self.openArabalarA30Window)
        self.arabalarUi.a31_btn.clicked.connect(self.openArabalarA31Window)
        self.arabalarUi.a32_btn.clicked.connect(self.openArabalarA32Window)
        self.arabalarUi.a33_btn.clicked.connect(self.openArabalarA33Window)
        self.arabalarUi.a34_btn.clicked.connect(self.openArabalarA34Window)
        self.arabalarUi.a35_btn.clicked.connect(self.openArabalarA35Window)
        self.arabalarUi.a36_btn.clicked.connect(self.openArabalarA36Window)
        self.arabalarUi.a37_btn.clicked.connect(self.openArabalarA37Window)
        self.arabalarUi.a38_btn.clicked.connect(self.openArabalarA38Window)
        self.arabalarUi.a39_btn.clicked.connect(self.openArabalarA39Window)
        self.arabalarUi.a40_btn.clicked.connect(self.openArabalarA40Window)
        self.arabalarUi.a41_btn.clicked.connect(self.openArabalarA41Window)
        self.arabalarUi.a42_btn.clicked.connect(self.openArabalarA42Window)
        self.arabalarUi.a43_btn.clicked.connect(self.openArabalarA43Window)
        self.arabalarUi.a44_btn.clicked.connect(self.openArabalarA44Window)
        self.arabalarUi.a45_btn.clicked.connect(self.openArabalarA45Window)
        self.arabalarUi.a46_btn.clicked.connect(self.openArabalarA46Window)
        self.arabalarUi.a47_btn.clicked.connect(self.openArabalarA47Window)
        self.arabalarUi.a48_btn.clicked.connect(self.openArabalarA48Window)
        self.arabalarUi.a49_btn.clicked.connect(self.openArabalarA49Window)
        self.arabalarUi.a50_btn.clicked.connect(self.openArabalarA50Window)
        self.arabalarUi.a51_btn.clicked.connect(self.openArabalarA51Window)
        self.arabalarUi.a52_btn.clicked.connect(self.openArabalarA52Window)
        self.arabalarUi.a53_btn.clicked.connect(self.openArabalarA53Window)
        self.arabalarUi.a54_btn.clicked.connect(self.openArabalarA54Window)
        self.arabalarUi.a55_btn.clicked.connect(self.openArabalarA55Window)
        self.arabalarUi.a56_btn.clicked.connect(self.openArabalarA56Window)
        self.arabalarUi.a57_btn.clicked.connect(self.openArabalarA57Window)
        self.arabalarUi.a58_btn.clicked.connect(self.openArabalarA58Window)
        self.arabalarUi.a59_btn.clicked.connect(self.openArabalarA59Window)
        self.arabalarUi.a60_btn.clicked.connect(self.openArabalarA60Window)
        self.arabalarUi.a61_btn.clicked.connect(self.openArabalarA61Window)
        self.arabalarUi.a62_btn.clicked.connect(self.openArabalarA62Window)
        self.arabalarUi.a63_btn.clicked.connect(self.openArabalarA63Window)
        self.arabalarUi.a64_btn.clicked.connect(self.openArabalarA64Window)
        self.arabalarUi.a65_btn.clicked.connect(self.openArabalarA65Window)
        self.arabalarUi.a66_btn.clicked.connect(self.openArabalarA66Window)
        self.arabalarUi.a67_btn.clicked.connect(self.openArabalarA67Window)
        self.arabalarUi.a68_btn.clicked.connect(self.openArabalarA68Window)
        self.arabalarUi.a69_btn.clicked.connect(self.openArabalarA69Window)
        self.arabalarUi.a70_btn.clicked.connect(self.openArabalarA70Window)
        self.arabalarUi.a71_btn.clicked.connect(self.openArabalarA71Window)
        self.arabalarUi.a72_btn.clicked.connect(self.openArabalarA72Window)
        self.arabalarUi.a73_btn.clicked.connect(self.openArabalarA73Window)
        self.arabalarUi.a74_btn.clicked.connect(self.openArabalarA74Window)
        self.arabalarUi.a75_btn.clicked.connect(self.openArabalarA75Window)
        self.arabalarUi.a75_btn.clicked.connect(self.openArabalarA75Window)
        self.arabalarUi.a76_btn.clicked.connect(self.openArabalarA76Window)
        self.arabalarUi.a76_btn.clicked.connect(self.openArabalarA76Window)
        self.arabalarUi.a77_btn.clicked.connect(self.openArabalarA77Window)
        self.arabalarUi.a78_btn.clicked.connect(self.openArabalarA78Window)
        self.arabalarUi.a79_btn.clicked.connect(self.openArabalarA79Window)
        self.arabalarUi.a80_btn.clicked.connect(self.openArabalarA80Window)
        self.arabalarUi.a81_btn.clicked.connect(self.openArabalarA81Window)
        self.arabalarUi.a82_btn.clicked.connect(self.openArabalarA82Window)
        self.arabalarUi.a83_btn.clicked.connect(self.openArabalarA83Window)
        self.arabalarUi.a84_btn.clicked.connect(self.openArabalarA84Window)
        self.arabalarUi.a85_btn.clicked.connect(self.openArabalarA85Window)
        self.arabalarUi.a86_btn.clicked.connect(self.openArabalarA86Window)
        self.arabalarUi.a87_btn.clicked.connect(self.openArabalarA87Window)
        self.arabalarUi.a88_btn.clicked.connect(self.openArabalarA88Window)
        self.arabalarUi.a89_btn.clicked.connect(self.openArabalarA89Window)
        self.arabalarUi.a90_btn.clicked.connect(self.openArabalarA90Window)
        self.arabalarUi.a91_btn.clicked.connect(self.openArabalarA91Window)
        self.arabalarUi.a92_btn.clicked.connect(self.openArabalarA92Window)
        self.arabalarUi.a93_btn.clicked.connect(self.openArabalarA93Window)
        self.arabalarUi.a94_btn.clicked.connect(self.openArabalarA94Window)
        self.arabalarUi.a95_btn.clicked.connect(self.openArabalarA95Window)
        self.arabalarUi.a96_btn.clicked.connect(self.openArabalarA96Window)
        self.arabalarUi.a97_btn.clicked.connect(self.openArabalarA97Window)
        self.arabalarUi.a98_btn.clicked.connect(self.openArabalarA98Window)
        self.arabalarUi.a99_btn.clicked.connect(self.openArabalarA99Window)
        self.arabalarUi.a100_btn.clicked.connect(self.openArabalarA100Window)
        self.arabalarUi.a101_btn.clicked.connect(self.openArabalarA101Window)
        self.arabalarUi.a102_btn.clicked.connect(self.openArabalarA102Window)
        self.arabalarUi.a103_btn.clicked.connect(self.openArabalarA103Window)
        self.arabalarWindow.show()
    
    
    
    def openArabalarA103Window(self):
        self.arabalarWindow.close()
        self.arabalarA103Window = QMainWindow()
        self.arabalarA103Ui = Ui_arabalarA103_ekran()
        self.arabalarA103Ui.setupUi(self.arabalarA103Window)
        self.arabalarA103Ui.listele103_btn.clicked.connect(self.kayit_listele_a103)
        self.arabalarA103Ui.sil103_btn.clicked.connect(self.kayit_sil_a103)
        self.arabalarA103Window.show()
    
    def openArabalarA102Window(self):
        self.arabalarWindow.close()
        self.arabalarA102Window = QMainWindow()
        self.arabalarA102Ui = Ui_arabalarA102_ekran()
        self.arabalarA102Ui.setupUi(self.arabalarA102Window)
        self.arabalarA102Ui.listele102_btn.clicked.connect(self.kayit_listele_a102)
        self.arabalarA102Ui.sil102_btn.clicked.connect(self.kayit_sil_a102)
        self.arabalarA102Window.show()
    
    def openArabalarA101Window(self):
        self.arabalarWindow.close()
        self.arabalarA101Window = QMainWindow()
        self.arabalarA101Ui = Ui_arabalarA101_ekran()
        self.arabalarA101Ui.setupUi(self.arabalarA101Window)
        self.arabalarA101Ui.listele101_btn.clicked.connect(self.kayit_listele_a101)
        self.arabalarA101Ui.sil101_btn.clicked.connect(self.kayit_sil_a101)
        self.arabalarA101Window.show()

    def openArabalarA100Window(self):
        self.arabalarWindow.close()
        self.arabalarA100Window = QMainWindow()
        self.arabalarA100Ui = Ui_arabalarA100_ekran()
        self.arabalarA100Ui.setupUi(self.arabalarA100Window)
        self.arabalarA100Ui.listele100_btn.clicked.connect(self.kayit_listele_a100)
        self.arabalarA100Ui.sil100_btn.clicked.connect(self.kayit_sil_a100)
        self.arabalarA100Window.show()

    def openArabalarA99Window(self):
        self.arabalarWindow.close()
        self.arabalarA99Window = QMainWindow()
        self.arabalarA99Ui = Ui_arabalarA99_ekran()
        self.arabalarA99Ui.setupUi(self.arabalarA99Window)
        self.arabalarA99Ui.listele99_btn.clicked.connect(self.kayit_listele_a99)
        self.arabalarA99Ui.sil99_btn.clicked.connect(self.kayit_sil_a99)
        self.arabalarA99Window.show()

    def openArabalarA98Window(self):
        self.arabalarWindow.close()
        self.arabalarA98Window = QMainWindow()
        self.arabalarA98Ui = Ui_arabalarA98_ekran()
        self.arabalarA98Ui.setupUi(self.arabalarA98Window)
        self.arabalarA98Ui.listele98_btn.clicked.connect(self.kayit_listele_a98)
        self.arabalarA98Ui.sil98_btn.clicked.connect(self.kayit_sil_a98)
        self.arabalarA98Window.show()

    def openArabalarA97Window(self):
        self.arabalarWindow.close()
        self.arabalarA97Window = QMainWindow()
        self.arabalarA97Ui = Ui_arabalarA97_ekran()
        self.arabalarA97Ui.setupUi(self.arabalarA97Window)
        self.arabalarA97Ui.listele97_btn.clicked.connect(self.kayit_listele_a97)
        self.arabalarA97Ui.sil97_btn.clicked.connect(self.kayit_sil_a97)
        self.arabalarA97Window.show()

    def openArabalarA96Window(self):
        self.arabalarWindow.close()
        self.arabalarA96Window = QMainWindow()
        self.arabalarA96Ui = Ui_arabalarA96_ekran()
        self.arabalarA96Ui.setupUi(self.arabalarA96Window)
        self.arabalarA96Ui.listele96_btn.clicked.connect(self.kayit_listele_a96)
        self.arabalarA96Ui.sil96_btn.clicked.connect(self.kayit_sil_a96)
        self.arabalarA96Window.show()

    def openArabalarA95Window(self):
        self.arabalarWindow.close()
        self.arabalarA95Window = QMainWindow()
        self.arabalarA95Ui = Ui_arabalarA95_ekran()
        self.arabalarA95Ui.setupUi(self.arabalarA95Window)
        self.arabalarA95Ui.listele95_btn.clicked.connect(self.kayit_listele_a95)
        self.arabalarA95Ui.sil95_btn.clicked.connect(self.kayit_sil_a95)
        self.arabalarA95Window.show()

    def openArabalarA94Window(self):
        self.arabalarWindow.close()
        self.arabalarA94Window = QMainWindow()
        self.arabalarA94Ui = Ui_arabalarA94_ekran()
        self.arabalarA94Ui.setupUi(self.arabalarA94Window)
        self.arabalarA94Ui.listele94_btn.clicked.connect(self.kayit_listele_a94)
        self.arabalarA94Ui.sil94_btn.clicked.connect(self.kayit_sil_a94)
        self.arabalarA94Window.show()
    
    def openArabalarA93Window(self):
        self.arabalarWindow.close()
        self.arabalarA93Window = QMainWindow()
        self.arabalarA93Ui = Ui_arabalarA93_ekran()
        self.arabalarA93Ui.setupUi(self.arabalarA93Window)
        self.arabalarA93Ui.listele93_btn.clicked.connect(self.kayit_listele_a93)
        self.arabalarA93Ui.sil93_btn.clicked.connect(self.kayit_sil_a93)
        self.arabalarA93Window.show()

    def openArabalarA92Window(self):
        self.arabalarWindow.close()
        self.arabalarA92Window = QMainWindow()
        self.arabalarA92Ui = Ui_arabalarA92_ekran()
        self.arabalarA92Ui.setupUi(self.arabalarA92Window)
        self.arabalarA92Ui.listele92_btn.clicked.connect(self.kayit_listele_a92)
        self.arabalarA92Ui.sil92_btn.clicked.connect(self.kayit_sil_a92)
        self.arabalarA92Window.show()

    def openArabalarA91Window(self):
        self.arabalarWindow.close()
        self.arabalarA91Window = QMainWindow()
        self.arabalarA91Ui = Ui_arabalarA91_ekran()
        self.arabalarA91Ui.setupUi(self.arabalarA91Window)
        self.arabalarA91Ui.listele91_btn.clicked.connect(self.kayit_listele_a91)
        self.arabalarA91Ui.sil91_btn.clicked.connect(self.kayit_sil_a91)
        self.arabalarA91Window.show()

    def openArabalarA90Window(self):
        self.arabalarWindow.close()
        self.arabalarA90Window = QMainWindow()
        self.arabalarA90Ui = Ui_arabalarA90_ekran()
        self.arabalarA90Ui.setupUi(self.arabalarA90Window)
        self.arabalarA90Ui.listele90_btn.clicked.connect(self.kayit_listele_a90)
        self.arabalarA90Ui.sil90_btn.clicked.connect(self.kayit_sil_a90)
        self.arabalarA90Window.show()

    def openArabalarA89Window(self):
        self.arabalarWindow.close()
        self.arabalarA89Window = QMainWindow()
        self.arabalarA89Ui = Ui_arabalarA89_ekran()
        self.arabalarA89Ui.setupUi(self.arabalarA89Window)
        self.arabalarA89Ui.listele89_btn.clicked.connect(self.kayit_listele_a89)
        self.arabalarA89Ui.sil89_btn.clicked.connect(self.kayit_sil_a89)
        self.arabalarA89Window.show()

    def openArabalarA88Window(self):
        self.arabalarWindow.close()
        self.arabalarA88Window = QMainWindow()
        self.arabalarA88Ui = Ui_arabalarA88_ekran()
        self.arabalarA88Ui.setupUi(self.arabalarA88Window)
        self.arabalarA88Ui.listele88_btn.clicked.connect(self.kayit_listele_a88)
        self.arabalarA88Ui.sil88_btn.clicked.connect(self.kayit_sil_a88)
        self.arabalarA88Window.show()

    def openArabalarA87Window(self):
        self.arabalarWindow.close()
        self.arabalarA87Window = QMainWindow()
        self.arabalarA87Ui = Ui_arabalarA87_ekran()
        self.arabalarA87Ui.setupUi(self.arabalarA87Window)
        self.arabalarA87Ui.listele87_btn.clicked.connect(self.kayit_listele_a87)
        self.arabalarA87Ui.sil87_btn.clicked.connect(self.kayit_sil_a87)
        self.arabalarA87Window.show()

    def openArabalarA86Window(self):
        self.arabalarWindow.close()
        self.arabalarA86Window = QMainWindow()
        self.arabalarA86Ui = Ui_arabalarA86_ekran()
        self.arabalarA86Ui.setupUi(self.arabalarA86Window)
        self.arabalarA86Ui.listele86_btn.clicked.connect(self.kayit_listele_a86)
        self.arabalarA86Ui.sil86_btn.clicked.connect(self.kayit_sil_a86)
        self.arabalarA86Window.show()
    
    def openArabalarA85Window(self):
        self.arabalarWindow.close()
        self.arabalarA85Window = QMainWindow()
        self.arabalarA85Ui = Ui_arabalarA85_ekran()
        self.arabalarA85Ui.setupUi(self.arabalarA85Window)
        self.arabalarA85Ui.listele85_btn.clicked.connect(self.kayit_listele_a85)
        self.arabalarA85Ui.sil85_btn.clicked.connect(self.kayit_sil_a85)
        self.arabalarA85Window.show()

    def openArabalarA84Window(self):
        self.arabalarWindow.close()
        self.arabalarA84Window = QMainWindow()
        self.arabalarA84Ui = Ui_arabalarA84_ekran()
        self.arabalarA84Ui.setupUi(self.arabalarA84Window)
        self.arabalarA84Ui.listele84_btn.clicked.connect(self.kayit_listele_a84)
        self.arabalarA84Ui.sil84_btn.clicked.connect(self.kayit_sil_a84)
        self.arabalarA84Window.show()

    def openArabalarA83Window(self):
        self.arabalarWindow.close()
        self.arabalarA83Window = QMainWindow()
        self.arabalarA83Ui = Ui_arabalarA83_ekran()
        self.arabalarA83Ui.setupUi(self.arabalarA83Window)
        self.arabalarA83Ui.listele83_btn.clicked.connect(self.kayit_listele_a83)
        self.arabalarA83Ui.sil83_btn.clicked.connect(self.kayit_sil_a83)
        self.arabalarA83Window.show()

    def openArabalarA82Window(self):
        self.arabalarWindow.close()
        self.arabalarA82Window = QMainWindow()
        self.arabalarA82Ui = Ui_arabalarA82_ekran()
        self.arabalarA82Ui.setupUi(self.arabalarA82Window)
        self.arabalarA82Ui.listele82_btn.clicked.connect(self.kayit_listele_a82)
        self.arabalarA82Ui.sil82_btn.clicked.connect(self.kayit_sil_a82)
        self.arabalarA82Window.show()

    def openArabalarA81Window(self):
        self.arabalarWindow.close()
        self.arabalarA81Window = QMainWindow()
        self.arabalarA81Ui = Ui_arabalarA81_ekran()
        self.arabalarA81Ui.setupUi(self.arabalarA81Window)
        self.arabalarA81Ui.listele81_btn.clicked.connect(self.kayit_listele_a81)
        self.arabalarA81Ui.sil81_btn.clicked.connect(self.kayit_sil_a81)
        self.arabalarA81Window.show()

    def openArabalarA80Window(self):
        self.arabalarWindow.close()
        self.arabalarA80Window = QMainWindow()
        self.arabalarA80Ui = Ui_arabalarA80_ekran()
        self.arabalarA80Ui.setupUi(self.arabalarA80Window)
        self.arabalarA80Ui.listele80_btn.clicked.connect(self.kayit_listele_a80)
        self.arabalarA80Ui.sil80_btn.clicked.connect(self.kayit_sil_a80)
        self.arabalarA80Window.show()

    def openArabalarA79Window(self):
        self.arabalarWindow.close()
        self.arabalarA79Window = QMainWindow()
        self.arabalarA79Ui = Ui_arabalarA79_ekran()
        self.arabalarA79Ui.setupUi(self.arabalarA79Window)
        self.arabalarA79Ui.listele79_btn.clicked.connect(self.kayit_listele_a79)
        self.arabalarA79Ui.sil79_btn.clicked.connect(self.kayit_sil_a79)
        self.arabalarA79Window.show()

    def openArabalarA78Window(self):
        self.arabalarWindow.close()
        self.arabalarA78Window = QMainWindow()
        self.arabalarA78Ui = Ui_arabalarA78_ekran()
        self.arabalarA78Ui.setupUi(self.arabalarA78Window)
        self.arabalarA78Ui.listele78_btn.clicked.connect(self.kayit_listele_a78)
        self.arabalarA78Ui.sil78_btn.clicked.connect(self.kayit_sil_a78)
        self.arabalarA78Window.show()
    
    def openArabalarA77Window(self):
        self.arabalarWindow.close()
        self.arabalarA77Window = QMainWindow()
        self.arabalarA77Ui = Ui_arabalarA77_ekran()
        self.arabalarA77Ui.setupUi(self.arabalarA77Window)
        self.arabalarA77Ui.listele77_btn.clicked.connect(self.kayit_listele_a77)
        self.arabalarA77Ui.sil77_btn.clicked.connect(self.kayit_sil_a77)
        self.arabalarA77Window.show()

    def openArabalarA76Window(self):
        self.arabalarWindow.close()
        self.arabalarA76Window = QMainWindow()
        self.arabalarA76Ui = Ui_arabalarA76_ekran()
        self.arabalarA76Ui.setupUi(self.arabalarA76Window)
        self.arabalarA76Ui.listele76_btn.clicked.connect(self.kayit_listele_a76)
        self.arabalarA76Ui.sil76_btn.clicked.connect(self.kayit_sil_a76)
        self.arabalarA76Window.show()

    def openArabalarA75Window(self):
        self.arabalarWindow.close()
        self.arabalarA75Window = QMainWindow()
        self.arabalarA75Ui = Ui_arabalarA75_ekran()
        self.arabalarA75Ui.setupUi(self.arabalarA75Window)
        self.arabalarA75Ui.listele75_btn.clicked.connect(self.kayit_listele_a75)
        self.arabalarA75Ui.sil75_btn.clicked.connect(self.kayit_sil_a75)
        self.arabalarA75Window.show()

    def openArabalarA74Window(self):
        self.arabalarWindow.close()
        self.arabalarA74Window = QMainWindow()
        self.arabalarA74Ui = Ui_arabalarA74_ekran()
        self.arabalarA74Ui.setupUi(self.arabalarA74Window)
        self.arabalarA74Ui.listele74_btn.clicked.connect(self.kayit_listele_a74)
        self.arabalarA74Ui.sil74_btn.clicked.connect(self.kayit_sil_a74)
        self.arabalarA74Window.show()

    def openArabalarA73Window(self):
        self.arabalarWindow.close()
        self.arabalarA73Window = QMainWindow()
        self.arabalarA73Ui = Ui_arabalarA73_ekran()
        self.arabalarA73Ui.setupUi(self.arabalarA73Window)
        self.arabalarA73Ui.listele73_btn.clicked.connect(self.kayit_listele_a73)
        self.arabalarA73Ui.sil73_btn.clicked.connect(self.kayit_sil_a73)
        self.arabalarA73Window.show()

    def openArabalarA72Window(self):
        self.arabalarWindow.close()
        self.arabalarA72Window = QMainWindow()
        self.arabalarA72Ui = Ui_arabalarA72_ekran()
        self.arabalarA72Ui.setupUi(self.arabalarA72Window)
        self.arabalarA72Ui.listele72_btn.clicked.connect(self.kayit_listele_a72)
        self.arabalarA72Ui.sil72_btn.clicked.connect(self.kayit_sil_a72)
        self.arabalarA72Window.show()

    def openArabalarA71Window(self):
        self.arabalarWindow.close()
        self.arabalarA71Window = QMainWindow()
        self.arabalarA71Ui = Ui_arabalarA71_ekran()
        self.arabalarA71Ui.setupUi(self.arabalarA71Window)
        self.arabalarA71Ui.listele71_btn.clicked.connect(self.kayit_listele_a71)
        self.arabalarA71Ui.sil71_btn.clicked.connect(self.kayit_sil_a71)
        self.arabalarA71Window.show()

    def openArabalarA70Window(self):
        self.arabalarWindow.close()
        self.arabalarA70Window = QMainWindow()
        self.arabalarA70Ui = Ui_arabalarA70_ekran()
        self.arabalarA70Ui.setupUi(self.arabalarA70Window)
        self.arabalarA70Ui.listele70_btn.clicked.connect(self.kayit_listele_a70)
        self.arabalarA70Ui.sil70_btn.clicked.connect(self.kayit_sil_a70)
        self.arabalarA70Window.show()
    
    def openArabalarA69Window(self):
        self.arabalarWindow.close()
        self.arabalarA69Window = QMainWindow()
        self.arabalarA69Ui = Ui_arabalarA69_ekran()
        self.arabalarA69Ui.setupUi(self.arabalarA69Window)
        self.arabalarA69Ui.listele69_btn.clicked.connect(self.kayit_listele_a69)
        self.arabalarA69Ui.sil69_btn.clicked.connect(self.kayit_sil_a69)
        self.arabalarA69Window.show()

    def openArabalarA68Window(self):
        self.arabalarWindow.close()
        self.arabalarA68Window = QMainWindow()
        self.arabalarA68Ui = Ui_arabalarA68_ekran()
        self.arabalarA68Ui.setupUi(self.arabalarA68Window)
        self.arabalarA68Ui.listele68_btn.clicked.connect(self.kayit_listele_a68)
        self.arabalarA68Ui.sil68_btn.clicked.connect(self.kayit_sil_a68)
        self.arabalarA68Window.show()

    def openArabalarA67Window(self):
        self.arabalarWindow.close()
        self.arabalarA67Window = QMainWindow()
        self.arabalarA67Ui = Ui_arabalarA67_ekran()
        self.arabalarA67Ui.setupUi(self.arabalarA67Window)
        self.arabalarA67Ui.listele67_btn.clicked.connect(self.kayit_listele_a67)
        self.arabalarA67Ui.sil67_btn.clicked.connect(self.kayit_sil_a67)
        self.arabalarA67Window.show()

    def openArabalarA66Window(self):
        self.arabalarWindow.close()
        self.arabalarA66Window = QMainWindow()
        self.arabalarA66Ui = Ui_arabalarA66_ekran()
        self.arabalarA66Ui.setupUi(self.arabalarA66Window)
        self.arabalarA66Ui.listele66_btn.clicked.connect(self.kayit_listele_a66)
        self.arabalarA66Ui.sil66_btn.clicked.connect(self.kayit_sil_a66)
        self.arabalarA66Window.show()

    def openArabalarA65Window(self):
        self.arabalarWindow.close()
        self.arabalarA65Window = QMainWindow()
        self.arabalarA65Ui = Ui_arabalarA65_ekran()
        self.arabalarA65Ui.setupUi(self.arabalarA65Window)
        self.arabalarA65Ui.listele65_btn.clicked.connect(self.kayit_listele_a65)
        self.arabalarA65Ui.sil65_btn.clicked.connect(self.kayit_sil_a65)
        self.arabalarA65Window.show()

    def openArabalarA64Window(self):
        self.arabalarWindow.close()
        self.arabalarA64Window = QMainWindow()
        self.arabalarA64Ui = Ui_arabalarA64_ekran()
        self.arabalarA64Ui.setupUi(self.arabalarA64Window)
        self.arabalarA64Ui.listele64_btn.clicked.connect(self.kayit_listele_a64)
        self.arabalarA64Ui.sil64_btn.clicked.connect(self.kayit_sil_a64)
        self.arabalarA64Window.show()

    def openArabalarA63Window(self):
        self.arabalarWindow.close()
        self.arabalarA63Window = QMainWindow()
        self.arabalarA63Ui = Ui_arabalarA63_ekran()
        self.arabalarA63Ui.setupUi(self.arabalarA63Window)
        self.arabalarA63Ui.listele63_btn.clicked.connect(self.kayit_listele_a63)
        self.arabalarA63Ui.sil63_btn.clicked.connect(self.kayit_sil_a63)
        self.arabalarA63Window.show()

    def openArabalarA62Window(self):
        self.arabalarWindow.close()
        self.arabalarA62Window = QMainWindow()
        self.arabalarA62Ui = Ui_arabalarA62_ekran()
        self.arabalarA62Ui.setupUi(self.arabalarA62Window)
        self.arabalarA62Ui.listele62_btn.clicked.connect(self.kayit_listele_a62)
        self.arabalarA62Ui.sil62_btn.clicked.connect(self.kayit_sil_a62)
        self.arabalarA62Window.show()
    
    def openArabalarA61Window(self):
        self.arabalarWindow.close()
        self.arabalarA61Window = QMainWindow()
        self.arabalarA61Ui = Ui_arabalarA61_ekran()
        self.arabalarA61Ui.setupUi(self.arabalarA61Window)
        self.arabalarA61Ui.listele61_btn.clicked.connect(self.kayit_listele_a61)
        self.arabalarA61Ui.sil61_btn.clicked.connect(self.kayit_sil_a61)
        self.arabalarA61Window.show()

    def openArabalarA60Window(self):
        self.arabalarWindow.close()
        self.arabalarA60Window = QMainWindow()
        self.arabalarA60Ui = Ui_arabalarA60_ekran()
        self.arabalarA60Ui.setupUi(self.arabalarA60Window)
        self.arabalarA60Ui.listele60_btn.clicked.connect(self.kayit_listele_a60)
        self.arabalarA60Ui.sil60_btn.clicked.connect(self.kayit_sil_a60)
        self.arabalarA60Window.show()

    def openArabalarA59Window(self):
        self.arabalarWindow.close()
        self.arabalarA59Window = QMainWindow()
        self.arabalarA59Ui = Ui_arabalarA59_ekran()
        self.arabalarA59Ui.setupUi(self.arabalarA59Window)
        self.arabalarA59Ui.listele59_btn.clicked.connect(self.kayit_listele_a59)
        self.arabalarA59Ui.sil59_btn.clicked.connect(self.kayit_sil_a59)
        self.arabalarA59Window.show()
    
    def openArabalarA58Window(self):
        self.arabalarWindow.close()
        self.arabalarA58Window = QMainWindow()
        self.arabalarA58Ui = Ui_arabalarA58_ekran()
        self.arabalarA58Ui.setupUi(self.arabalarA58Window)
        self.arabalarA58Ui.listele58_btn.clicked.connect(self.kayit_listele_a58)
        self.arabalarA58Ui.sil58_btn.clicked.connect(self.kayit_sil_a58)
        self.arabalarA58Window.show()
    
    def openArabalarA57Window(self):
        self.arabalarWindow.close()
        self.arabalarA57Window = QMainWindow()
        self.arabalarA57Ui = Ui_arabalarA57_ekran()
        self.arabalarA57Ui.setupUi(self.arabalarA57Window)
        self.arabalarA57Ui.listele57_btn.clicked.connect(self.kayit_listele_a57)
        self.arabalarA57Ui.sil57_btn.clicked.connect(self.kayit_sil_a57)
        self.arabalarA57Window.show()
    
    def openArabalarA56Window(self):
        self.arabalarWindow.close()
        self.arabalarA56Window = QMainWindow()
        self.arabalarA56Ui = Ui_arabalarA56_ekran()
        self.arabalarA56Ui.setupUi(self.arabalarA56Window)
        self.arabalarA56Ui.listele56_btn.clicked.connect(self.kayit_listele_a56)
        self.arabalarA56Ui.sil56_btn.clicked.connect(self.kayit_sil_a56)
        self.arabalarA56Window.show()
    
    def openArabalarA55Window(self):
        self.arabalarWindow.close()
        self.arabalarA55Window = QMainWindow()
        self.arabalarA55Ui = Ui_arabalarA55_ekran()
        self.arabalarA55Ui.setupUi(self.arabalarA55Window)
        self.arabalarA55Ui.listele55_btn.clicked.connect(self.kayit_listele_a55)
        self.arabalarA55Ui.sil55_btn.clicked.connect(self.kayit_sil_a55)
        self.arabalarA55Window.show()
    
    def openArabalarA54Window(self):
        self.arabalarWindow.close()
        self.arabalarA54Window = QMainWindow()
        self.arabalarA54Ui = Ui_arabalarA54_ekran()
        self.arabalarA54Ui.setupUi(self.arabalarA54Window)
        self.arabalarA54Ui.listele54_btn.clicked.connect(self.kayit_listele_a54)
        self.arabalarA54Ui.sil54_btn.clicked.connect(self.kayit_sil_a54)
        self.arabalarA54Window.show()
    
    def openArabalarA53Window(self):
        self.arabalarWindow.close()
        self.arabalarA53Window = QMainWindow()
        self.arabalarA53Ui = Ui_arabalarA53_ekran()
        self.arabalarA53Ui.setupUi(self.arabalarA53Window)
        self.arabalarA53Ui.listele53_btn.clicked.connect(self.kayit_listele_a53)
        self.arabalarA53Ui.sil53_btn.clicked.connect(self.kayit_sil_a53)
        self.arabalarA53Window.show()
    
    def openArabalarA52Window(self):
        self.arabalarWindow.close()
        self.arabalarA52Window = QMainWindow()
        self.arabalarA52Ui = Ui_arabalarA52_ekran()
        self.arabalarA52Ui.setupUi(self.arabalarA52Window)
        self.arabalarA52Ui.listele52_btn.clicked.connect(self.kayit_listele_a52)
        self.arabalarA52Ui.sil52_btn.clicked.connect(self.kayit_sil_a52)
        self.arabalarA52Window.show()
    
    def openArabalarA51Window(self):
        self.arabalarWindow.close()
        self.arabalarA51Window = QMainWindow()
        self.arabalarA51Ui = Ui_arabalarA51_ekran()
        self.arabalarA51Ui.setupUi(self.arabalarA51Window)
        self.arabalarA51Ui.listele51_btn.clicked.connect(self.kayit_listele_a51)
        self.arabalarA51Ui.sil51_btn.clicked.connect(self.kayit_sil_a51)
        self.arabalarA51Window.show()
    
    def openArabalarA50Window(self):
        self.arabalarWindow.close()
        self.arabalarA50Window = QMainWindow()
        self.arabalarA50Ui = Ui_arabalarA50_ekran()
        self.arabalarA50Ui.setupUi(self.arabalarA50Window)
        self.arabalarA50Ui.listele50_btn.clicked.connect(self.kayit_listele_a50)
        self.arabalarA50Ui.sil50_btn.clicked.connect(self.kayit_sil_a50)
        self.arabalarA50Window.show()
    
    def openArabalarA49Window(self):
        self.arabalarWindow.close()
        self.arabalarA49Window = QMainWindow()
        self.arabalarA49Ui = Ui_arabalarA49_ekran()
        self.arabalarA49Ui.setupUi(self.arabalarA49Window)
        self.arabalarA49Ui.listele49_btn.clicked.connect(self.kayit_listele_a49)
        self.arabalarA49Ui.sil49_btn.clicked.connect(self.kayit_sil_a49)
        self.arabalarA49Window.show()
    
    def openArabalarA48Window(self):
        self.arabalarWindow.close()
        self.arabalarA48Window = QMainWindow()
        self.arabalarA48Ui = Ui_arabalarA48_ekran()
        self.arabalarA48Ui.setupUi(self.arabalarA48Window)
        self.arabalarA48Ui.listele48_btn.clicked.connect(self.kayit_listele_a48)
        self.arabalarA48Ui.sil48_btn.clicked.connect(self.kayit_sil_a48)
        self.arabalarA48Window.show()
    
    def openArabalarA47Window(self):
        self.arabalarWindow.close()
        self.arabalarA47Window = QMainWindow()
        self.arabalarA47Ui = Ui_arabalarA47_ekran()
        self.arabalarA47Ui.setupUi(self.arabalarA47Window)
        self.arabalarA47Ui.listele47_btn.clicked.connect(self.kayit_listele_a47)
        self.arabalarA47Ui.sil47_btn.clicked.connect(self.kayit_sil_a47)
        self.arabalarA47Window.show()
    
    def openArabalarA46Window(self):
        self.arabalarWindow.close()
        self.arabalarA46Window = QMainWindow()
        self.arabalarA46Ui = Ui_arabalarA46_ekran()
        self.arabalarA46Ui.setupUi(self.arabalarA46Window)
        self.arabalarA46Ui.listele46_btn.clicked.connect(self.kayit_listele_a46)
        self.arabalarA46Ui.sil46_btn.clicked.connect(self.kayit_sil_a46)
        self.arabalarA46Window.show()
    
    def openArabalarA45Window(self):
        self.arabalarWindow.close()
        self.arabalarA45Window = QMainWindow()
        self.arabalarA45Ui = Ui_arabalarA45_ekran()
        self.arabalarA45Ui.setupUi(self.arabalarA45Window)
        self.arabalarA45Ui.listele45_btn.clicked.connect(self.kayit_listele_a45)
        self.arabalarA45Ui.sil45_btn.clicked.connect(self.kayit_sil_a45)
        self.arabalarA45Window.show()
    
    def openArabalarA44Window(self):
        self.arabalarWindow.close()
        self.arabalarA44Window = QMainWindow()
        self.arabalarA44Ui = Ui_arabalarA44_ekran()
        self.arabalarA44Ui.setupUi(self.arabalarA44Window)
        self.arabalarA44Ui.listele44_btn.clicked.connect(self.kayit_listele_a44)
        self.arabalarA44Ui.sil44_btn.clicked.connect(self.kayit_sil_a44)
        self.arabalarA44Window.show()
    
    def openArabalarA43Window(self):
        self.arabalarWindow.close()
        self.arabalarA43Window = QMainWindow()
        self.arabalarA43Ui = Ui_arabalarA43_ekran()
        self.arabalarA43Ui.setupUi(self.arabalarA43Window)
        self.arabalarA43Ui.listele43_btn.clicked.connect(self.kayit_listele_a43)
        self.arabalarA43Ui.sil43_btn.clicked.connect(self.kayit_sil_a43)
        self.arabalarA43Window.show()
    
    def openArabalarA42Window(self):
        self.arabalarWindow.close()
        self.arabalarA42Window = QMainWindow()
        self.arabalarA42Ui = Ui_arabalarA42_ekran()
        self.arabalarA42Ui.setupUi(self.arabalarA42Window)
        self.arabalarA42Ui.listele42_btn.clicked.connect(self.kayit_listele_a42)
        self.arabalarA42Ui.sil42_btn.clicked.connect(self.kayit_sil_a42)
        self.arabalarA42Window.show()
    
    def openArabalarA41Window(self):
        self.arabalarWindow.close()
        self.arabalarA41Window = QMainWindow()
        self.arabalarA41Ui = Ui_arabalarA41_ekran()
        self.arabalarA41Ui.setupUi(self.arabalarA41Window)
        self.arabalarA41Ui.listele41_btn.clicked.connect(self.kayit_listele_a41)
        self.arabalarA41Ui.sil41_btn.clicked.connect(self.kayit_sil_a41)
        self.arabalarA41Window.show()
    
    def openArabalarA40Window(self):
        self.arabalarWindow.close()
        self.arabalarA40Window = QMainWindow()
        self.arabalarA40Ui = Ui_arabalarA40_ekran()
        self.arabalarA40Ui.setupUi(self.arabalarA40Window)
        self.arabalarA40Ui.listele40_btn.clicked.connect(self.kayit_listele_a40)
        self.arabalarA40Ui.sil40_btn.clicked.connect(self.kayit_sil_a40)
        self.arabalarA40Window.show()
    
    def openArabalarA39Window(self):
        self.arabalarWindow.close()
        self.arabalarA39Window = QMainWindow()
        self.arabalarA39Ui = Ui_arabalarA39_ekran()
        self.arabalarA39Ui.setupUi(self.arabalarA39Window)
        self.arabalarA39Ui.listele39_btn.clicked.connect(self.kayit_listele_a39)
        self.arabalarA39Ui.sil39_btn.clicked.connect(self.kayit_sil_a39)
        self.arabalarA39Window.show()
    
    def openArabalarA38Window(self):
        self.arabalarWindow.close()
        self.arabalarA38Window = QMainWindow()
        self.arabalarA38Ui = Ui_arabalarA38_ekran()
        self.arabalarA38Ui.setupUi(self.arabalarA38Window)
        self.arabalarA38Ui.listele38_btn.clicked.connect(self.kayit_listele_a38)
        self.arabalarA38Ui.sil38_btn.clicked.connect(self.kayit_sil_a38)
        self.arabalarA38Window.show()
    
    def openArabalarA37Window(self):
        self.arabalarWindow.close()
        self.arabalarA37Window = QMainWindow()
        self.arabalarA37Ui = Ui_arabalarA37_ekran()
        self.arabalarA37Ui.setupUi(self.arabalarA37Window)
        self.arabalarA37Ui.listele37_btn.clicked.connect(self.kayit_listele_a37)
        self.arabalarA37Ui.sil37_btn.clicked.connect(self.kayit_sil_a37)
        self.arabalarA37Window.show()
    
    def openArabalarA36Window(self):
        self.arabalarWindow.close()
        self.arabalarA36Window = QMainWindow()
        self.arabalarA36Ui = Ui_arabalarA36_ekran()
        self.arabalarA36Ui.setupUi(self.arabalarA36Window)
        self.arabalarA36Ui.listele36_btn.clicked.connect(self.kayit_listele_a36)
        self.arabalarA36Ui.sil36_btn.clicked.connect(self.kayit_sil_a36)
        self.arabalarA36Window.show()
    
    def openArabalarA35Window(self):
        self.arabalarWindow.close()
        self.arabalarA35Window = QMainWindow()
        self.arabalarA35Ui = Ui_arabalarA35_ekran()
        self.arabalarA35Ui.setupUi(self.arabalarA35Window)
        self.arabalarA35Ui.listele35_btn.clicked.connect(self.kayit_listele_a35)
        self.arabalarA35Ui.sil35_btn.clicked.connect(self.kayit_sil_a35)
        self.arabalarA35Window.show()
    
    def openArabalarA34Window(self):
        self.arabalarWindow.close()
        self.arabalarA34Window = QMainWindow()
        self.arabalarA34Ui = Ui_arabalarA34_ekran()
        self.arabalarA34Ui.setupUi(self.arabalarA34Window)
        self.arabalarA34Ui.listele34_btn.clicked.connect(self.kayit_listele_a34)
        self.arabalarA34Ui.sil34_btn.clicked.connect(self.kayit_sil_a34)
        self.arabalarA34Window.show()
    
    def openArabalarA33Window(self):
        self.arabalarWindow.close()
        self.arabalarA33Window = QMainWindow()
        self.arabalarA33Ui = Ui_arabalarA33_ekran()
        self.arabalarA33Ui.setupUi(self.arabalarA33Window)
        self.arabalarA33Ui.listele33_btn.clicked.connect(self.kayit_listele_a33)
        self.arabalarA33Ui.sil33_btn.clicked.connect(self.kayit_sil_a33)
        self.arabalarA33Window.show()
    
    def openArabalarA32Window(self):
        self.arabalarWindow.close()
        self.arabalarA32Window = QMainWindow()
        self.arabalarA32Ui = Ui_arabalarA32_ekran()
        self.arabalarA32Ui.setupUi(self.arabalarA32Window)
        self.arabalarA32Ui.listele32_btn.clicked.connect(self.kayit_listele_a32)
        self.arabalarA32Ui.sil32_btn.clicked.connect(self.kayit_sil_a32)
        self.arabalarA32Window.show()
    
    def openArabalarA31Window(self):
        self.arabalarWindow.close()
        self.arabalarA31Window = QMainWindow()
        self.arabalarA31Ui = Ui_arabalarA31_ekran()
        self.arabalarA31Ui.setupUi(self.arabalarA31Window)
        self.arabalarA31Ui.listele31_btn.clicked.connect(self.kayit_listele_a31)
        self.arabalarA31Ui.sil31_btn.clicked.connect(self.kayit_sil_a31)
        self.arabalarA31Window.show()
    
    def openArabalarA30Window(self):
        self.arabalarWindow.close()
        self.arabalarA30Window = QMainWindow()
        self.arabalarA30Ui = Ui_arabalarA30_ekran()
        self.arabalarA30Ui.setupUi(self.arabalarA30Window)
        self.arabalarA30Ui.listele30_btn.clicked.connect(self.kayit_listele_a30)
        self.arabalarA30Ui.sil30_btn.clicked.connect(self.kayit_sil_a30)
        self.arabalarA30Window.show()
    
    def openArabalarA29Window(self):
        self.arabalarWindow.close()
        self.arabalarA29Window = QMainWindow()
        self.arabalarA29Ui = Ui_arabalarA29_ekran()
        self.arabalarA29Ui.setupUi(self.arabalarA29Window)
        self.arabalarA29Ui.listele29_btn.clicked.connect(self.kayit_listele_a29)
        self.arabalarA29Ui.sil29_btn.clicked.connect(self.kayit_sil_a29)
        self.arabalarA29Window.show()
    
    def openArabalarA28Window(self):
        self.arabalarWindow.close()
        self.arabalarA28Window = QMainWindow()
        self.arabalarA28Ui = Ui_arabalarA28_ekran()
        self.arabalarA28Ui.setupUi(self.arabalarA28Window)
        self.arabalarA28Ui.listele28_btn.clicked.connect(self.kayit_listele_a28)
        self.arabalarA28Ui.sil28_btn.clicked.connect(self.kayit_sil_a28)
        self.arabalarA28Window.show()
    
    def openArabalarA27Window(self):
        self.arabalarWindow.close()
        self.arabalarA27Window = QMainWindow()
        self.arabalarA27Ui = Ui_arabalarA27_ekran()
        self.arabalarA27Ui.setupUi(self.arabalarA27Window)
        self.arabalarA27Ui.listele27_btn.clicked.connect(self.kayit_listele_a27)
        self.arabalarA27Ui.sil27_btn.clicked.connect(self.kayit_sil_a27)
        self.arabalarA27Window.show()
    
    def openArabalarA26Window(self):
        self.arabalarWindow.close()
        self.arabalarA26Window = QMainWindow()
        self.arabalarA26Ui = Ui_arabalarA26_ekran()
        self.arabalarA26Ui.setupUi(self.arabalarA26Window)
        self.arabalarA26Ui.listele26_btn.clicked.connect(self.kayit_listele_a26)
        self.arabalarA26Ui.sil26_btn.clicked.connect(self.kayit_sil_a26)
        self.arabalarA26Window.show()
    
    def openArabalarA25Window(self):
        self.arabalarWindow.close()
        self.arabalarA25Window = QMainWindow()
        self.arabalarA25Ui = Ui_arabalarA25_ekran()
        self.arabalarA25Ui.setupUi(self.arabalarA25Window)
        self.arabalarA25Ui.listele25_btn.clicked.connect(self.kayit_listele_a25)
        self.arabalarA25Ui.sil25_btn.clicked.connect(self.kayit_sil_a25)
        self.arabalarA25Window.show()
    
    def openArabalarA24Window(self):
        self.arabalarWindow.close()
        self.arabalarA24Window = QMainWindow()
        self.arabalarA24Ui = Ui_arabalarA24_ekran()
        self.arabalarA24Ui.setupUi(self.arabalarA24Window)
        self.arabalarA24Ui.listele24_btn.clicked.connect(self.kayit_listele_a24)
        self.arabalarA24Ui.sil24_btn.clicked.connect(self.kayit_sil_a24)
        self.arabalarA24Window.show()
    
    def openArabalarA23Window(self):
        self.arabalarWindow.close()
        self.arabalarA23Window = QMainWindow()
        self.arabalarA23Ui = Ui_arabalarA23_ekran()
        self.arabalarA23Ui.setupUi(self.arabalarA23Window)
        self.arabalarA23Ui.listele23_btn.clicked.connect(self.kayit_listele_a23)
        self.arabalarA23Ui.sil23_btn.clicked.connect(self.kayit_sil_a23)
        self.arabalarA23Window.show()
    
    def openArabalarA22Window(self):
        self.arabalarWindow.close()
        self.arabalarA22Window = QMainWindow()
        self.arabalarA22Ui = Ui_arabalarA22_ekran()
        self.arabalarA22Ui.setupUi(self.arabalarA22Window)
        self.arabalarA22Ui.listele22_btn.clicked.connect(self.kayit_listele_a22)
        self.arabalarA22Ui.sil22_btn.clicked.connect(self.kayit_sil_a22)
        self.arabalarA22Window.show()
    
    def openArabalarA21Window(self):
        self.arabalarWindow.close()
        self.arabalarA21Window = QMainWindow()
        self.arabalarA21Ui = Ui_arabalarA21_ekran()
        self.arabalarA21Ui.setupUi(self.arabalarA21Window)
        self.arabalarA21Ui.listele21_btn.clicked.connect(self.kayit_listele_a21)
        self.arabalarA21Ui.sil21_btn.clicked.connect(self.kayit_sil_a21)
        self.arabalarA21Window.show()
    
    def openArabalarA20Window(self):
        self.arabalarWindow.close()
        self.arabalarA20Window = QMainWindow()
        self.arabalarA20Ui = Ui_arabalarA20_ekran()
        self.arabalarA20Ui.setupUi(self.arabalarA20Window)
        self.arabalarA20Ui.listele20_btn.clicked.connect(self.kayit_listele_a20)
        self.arabalarA20Ui.sil20_btn.clicked.connect(self.kayit_sil_a20)
        self.arabalarA20Window.show()
    
    def openArabalarA19Window(self):
        self.arabalarWindow.close()
        self.arabalarA19Window = QMainWindow()
        self.arabalarA19Ui = Ui_arabalarA19_ekran()
        self.arabalarA19Ui.setupUi(self.arabalarA19Window)
        self.arabalarA19Ui.listele19_btn.clicked.connect(self.kayit_listele_a19)
        self.arabalarA19Ui.sil19_btn.clicked.connect(self.kayit_sil_a19)
        self.arabalarA19Window.show()
    
    def openArabalarA18Window(self):
        self.arabalarWindow.close()
        self.arabalarA18Window = QMainWindow()
        self.arabalarA18Ui = Ui_arabalarA18_ekran()
        self.arabalarA18Ui.setupUi(self.arabalarA18Window)
        self.arabalarA18Ui.listele18_btn.clicked.connect(self.kayit_listele_a18)
        self.arabalarA18Ui.sil18_btn.clicked.connect(self.kayit_sil_a18)
        self.arabalarA18Window.show()
    
    def openArabalarA17Window(self):
        self.arabalarWindow.close()
        self.arabalarA17Window = QMainWindow()
        self.arabalarA17Ui = Ui_arabalarA17_ekran()
        self.arabalarA17Ui.setupUi(self.arabalarA17Window)
        self.arabalarA17Ui.listele17_btn.clicked.connect(self.kayit_listele_a17)
        self.arabalarA17Ui.sil17_btn.clicked.connect(self.kayit_sil_a17)
        self.arabalarA17Window.show()
    
    def openArabalarA16Window(self):
        self.arabalarWindow.close()
        self.arabalarA16Window = QMainWindow()
        self.arabalarA16Ui = Ui_arabalarA16_ekran()
        self.arabalarA16Ui.setupUi(self.arabalarA16Window)
        self.arabalarA16Ui.listele16_btn.clicked.connect(self.kayit_listele_a16)
        self.arabalarA16Ui.sil16_btn.clicked.connect(self.kayit_sil_a16)
        self.arabalarA16Window.show()
    
    def openArabalarA15Window(self):
        self.arabalarWindow.close()
        self.arabalarA15Window = QMainWindow()
        self.arabalarA15Ui = Ui_arabalarA15_ekran()
        self.arabalarA15Ui.setupUi(self.arabalarA15Window)
        self.arabalarA15Ui.listele15_btn.clicked.connect(self.kayit_listele_a15)
        self.arabalarA15Ui.sil15_btn.clicked.connect(self.kayit_sil_a15)
        self.arabalarA15Window.show()
    
    def openArabalarA14Window(self):
        self.arabalarWindow.close()
        self.arabalarA14Window = QMainWindow()
        self.arabalarA14Ui = Ui_arabalarA14_ekran()
        self.arabalarA14Ui.setupUi(self.arabalarA14Window)
        self.arabalarA14Ui.listele14_btn.clicked.connect(self.kayit_listele_a14)
        self.arabalarA14Ui.sil14_btn.clicked.connect(self.kayit_sil_a14)
        self.arabalarA14Window.show()
    
    def openArabalarA13Window(self):
        self.arabalarWindow.close()
        self.arabalarA13Window = QMainWindow()
        self.arabalarA13Ui = Ui_arabalarA13_ekran()
        self.arabalarA13Ui.setupUi(self.arabalarA13Window)
        self.arabalarA13Ui.listele13_btn.clicked.connect(self.kayit_listele_a13)
        self.arabalarA13Ui.sil13_btn.clicked.connect(self.kayit_sil_a13)
        self.arabalarA13Window.show()
    
    def openArabalarA12Window(self):
        self.arabalarWindow.close()
        self.arabalarA12Window = QMainWindow()
        self.arabalarA12Ui = Ui_arabalarA12_ekran()
        self.arabalarA12Ui.setupUi(self.arabalarA12Window)
        self.arabalarA12Ui.listele12_btn.clicked.connect(self.kayit_listele_a12)
        self.arabalarA12Ui.sil12_btn.clicked.connect(self.kayit_sil_a12)
        self.arabalarA12Window.show()
    
    def openArabalarA11Window(self):
        self.arabalarWindow.close()
        self.arabalarA11Window = QMainWindow()
        self.arabalarA11Ui = Ui_arabalarA11_ekran()
        self.arabalarA11Ui.setupUi(self.arabalarA11Window)
        self.arabalarA11Ui.listele11_btn.clicked.connect(self.kayit_listele_a11)
        self.arabalarA11Ui.sil11_btn.clicked.connect(self.kayit_sil_a11)
        self.arabalarA11Window.show()
    
    def openArabalarA10Window(self):
        self.arabalarWindow.close()
        self.arabalarA10Window = QMainWindow()
        self.arabalarA10Ui = Ui_arabalarA10_ekran()
        self.arabalarA10Ui.setupUi(self.arabalarA10Window)
        self.arabalarA10Ui.listele10_btn.clicked.connect(self.kayit_listele_a10)
        self.arabalarA10Ui.sil10_btn.clicked.connect(self.kayit_sil_a10)
        self.arabalarA10Window.show()
    
    def openArabalarA9Window(self):
        self.arabalarWindow.close()
        self.arabalarA9Window = QMainWindow()
        self.arabalarA9Ui = Ui_arabalarA9_ekran()
        self.arabalarA9Ui.setupUi(self.arabalarA9Window)
        self.arabalarA9Ui.listele9_btn.clicked.connect(self.kayit_listele_a9)
        self.arabalarA9Ui.sil9_btn.clicked.connect(self.kayit_sil_a9)
        self.arabalarA9Window.show()
    
    def openArabalarA8Window(self):
        self.arabalarWindow.close()
        self.arabalarA8Window = QMainWindow()
        self.arabalarA8Ui = Ui_arabalarA8_ekran()
        self.arabalarA8Ui.setupUi(self.arabalarA8Window)
        self.arabalarA8Ui.listele8_btn.clicked.connect(self.kayit_listele_a8)
        self.arabalarA8Ui.sil8_btn.clicked.connect(self.kayit_sil_a8)
        self.arabalarA8Window.show()
    
    def openArabalarA7Window(self):
        self.arabalarWindow.close()
        self.arabalarA7Window = QMainWindow()
        self.arabalarA7Ui = Ui_arabalarA7_ekran()
        self.arabalarA7Ui.setupUi(self.arabalarA7Window)
        self.arabalarA7Ui.listele7_btn.clicked.connect(self.kayit_listele_a7)
        self.arabalarA7Ui.sil7_btn.clicked.connect(self.kayit_sil_a7)
        self.arabalarA7Window.show()
    
    def openArabalarA6Window(self):
        self.arabalarWindow.close()
        self.arabalarA6Window = QMainWindow()
        self.arabalarA6Ui = Ui_arabalarA6_ekran()
        self.arabalarA6Ui.setupUi(self.arabalarA6Window)
        self.arabalarA6Ui.listele6_btn.clicked.connect(self.kayit_listele_a6)
        self.arabalarA6Ui.sil6_btn.clicked.connect(self.kayit_sil_a6)
        self.arabalarA6Window.show()
        
    def openArabalarA5Window(self):
        self.arabalarWindow.close()
        self.arabalarA5Window = QMainWindow()
        self.arabalarA5Ui = Ui_arabalarA5_ekran()
        self.arabalarA5Ui.setupUi(self.arabalarA5Window)
        self.arabalarA5Ui.listele5_btn.clicked.connect(self.kayit_listele_a5)
        self.arabalarA5Ui.sil5_btn.clicked.connect(self.kayit_sil_a5)
        self.arabalarA5Window.show()
    
    def openArabalarA4Window(self):
        self.arabalarWindow.close()
        self.arabalarA4Window = QMainWindow()
        self.arabalarA4Ui = Ui_arabalarA4_ekran()
        self.arabalarA4Ui.setupUi(self.arabalarA4Window)
        self.arabalarA4Ui.listele4_btn.clicked.connect(self.kayit_listele_a4)
        self.arabalarA4Ui.sil4_btn.clicked.connect(self.kayit_sil_a4)
        self.arabalarA4Window.show()
    
    def openArabalarA3Window(self):
        self.arabalarWindow.close()
        self.arabalarA3Window = QMainWindow()
        self.arabalarA3Ui = Ui_arabalarA3_ekran()
        self.arabalarA3Ui.setupUi(self.arabalarA3Window)
        self.arabalarA3Ui.listele3_btn.clicked.connect(self.kayit_listele_a3)
        self.arabalarA3Ui.sil3_btn.clicked.connect(self.kayit_sil_a3)
        self.arabalarA3Window.show()

    def openArabalarA2Window(self):
        self.arabalarWindow.close()
        self.arabalarA2Window = QMainWindow()
        self.arabalarA2Ui = Ui_arabalarA2_ekran()
        self.arabalarA2Ui.setupUi(self.arabalarA2Window)
        self.arabalarA2Ui.listele2_btn.clicked.connect(self.kayit_listele_a2)
        self.arabalarA2Ui.sil2_btn.clicked.connect(self.kayit_sil_a2)
        self.arabalarA2Window.show()
    
    def openArabalarA1Window(self):
        self.arabalarWindow.close()
        self.arabalarA1Window = QMainWindow()
        self.arabalarA1Ui = Ui_arabalarA1_ekran()
        self.arabalarA1Ui.setupUi(self.arabalarA1Window)
        self.arabalarA1Ui.listele1_btn.clicked.connect(self.kayit_listele_a1)
        self.arabalarA1Ui.sil1_btn.clicked.connect(self.kayit_sil_a1)
        self.arabalarA1Window.show()

    def openRaflarWindow(self):
        self.depoWindow.close()
        self.raflarWindow = QMainWindow()
        self.raflarUi = Ui_raflar_ekran()
        self.raflarUi.setupUi(self.raflarWindow)
        self.raflarUi.r1_btn.clicked.connect(self.openRaflarR1Window)
        self.raflarUi.r2_btn.clicked.connect(self.openRaflarR2Window)
        self.raflarUi.r3_btn.clicked.connect(self.openRaflarR3Window)
        self.raflarUi.r4_btn.clicked.connect(self.openRaflarR4Window)
        self.raflarUi.r5_btn.clicked.connect(self.openRaflarR5Window)
        self.raflarUi.r6_btn.clicked.connect(self.openRaflarR6Window)
        self.raflarUi.r7_btn.clicked.connect(self.openRaflarR7Window)
        self.raflarUi.r8_btn.clicked.connect(self.openRaflarR8Window)
        self.raflarUi.r9_btn.clicked.connect(self.openRaflarR9Window)
        self.raflarUi.r10_btn.clicked.connect(self.openRaflarR10Window)
        self.raflarUi.r11_btn.clicked.connect(self.openRaflarR11Window)
        self.raflarUi.r12_btn.clicked.connect(self.openRaflarR12Window)
        self.raflarUi.r13_btn.clicked.connect(self.openRaflarR13Window)
        self.raflarUi.r14_btn.clicked.connect(self.openRaflarR14Window)
        self.raflarUi.r15_btn.clicked.connect(self.openRaflarR15Window)
        self.raflarUi.r16_btn.clicked.connect(self.openRaflarR16Window)
        self.raflarUi.r17_btn.clicked.connect(self.openRaflarR17Window)
        self.raflarUi.r18_btn.clicked.connect(self.openRaflarR18Window)
        self.raflarUi.r19_btn.clicked.connect(self.openRaflarR19Window)
        self.raflarUi.r20_btn.clicked.connect(self.openRaflarR20Window)
        self.raflarUi.r21_btn.clicked.connect(self.openRaflarR21Window)
        self.raflarUi.r22_btn.clicked.connect(self.openRaflarR22Window)
        self.raflarUi.r23_btn.clicked.connect(self.openRaflarR23Window)
        self.raflarUi.r24_btn.clicked.connect(self.openRaflarR24Window)
        self.raflarUi.r25_btn.clicked.connect(self.openRaflarR25Window)
        self.raflarUi.r26_btn.clicked.connect(self.openRaflarR26Window)
        self.raflarUi.r27_btn.clicked.connect(self.openRaflarR27Window)
        self.raflarUi.r28_btn.clicked.connect(self.openRaflarR28Window)
        self.raflarUi.r29_btn.clicked.connect(self.openRaflarR29Window)
        self.raflarUi.r30_btn.clicked.connect(self.openRaflarR30Window)
        self.raflarUi.r31_btn.clicked.connect(self.openRaflarR31Window)
        self.raflarUi.r32_btn.clicked.connect(self.openRaflarR32Window)
        self.raflarUi.r33_btn.clicked.connect(self.openRaflarR33Window)
        self.raflarUi.r34_btn.clicked.connect(self.openRaflarR34Window)
        self.raflarUi.r35_btn.clicked.connect(self.openRaflarR35Window)
        self.raflarUi.r36_btn.clicked.connect(self.openRaflarR36Window)
        self.raflarUi.r37_btn.clicked.connect(self.openRaflarR37Window)
        self.raflarUi.r38_btn.clicked.connect(self.openRaflarR38Window)
        self.raflarUi.r39_btn.clicked.connect(self.openRaflarR39Window)
        self.raflarUi.r40_btn.clicked.connect(self.openRaflarR40Window)
        self.raflarUi.r41_btn.clicked.connect(self.openRaflarR41Window)
        self.raflarUi.r42_btn.clicked.connect(self.openRaflarR42Window)
        self.raflarUi.r43_btn.clicked.connect(self.openRaflarR43Window)
        self.raflarUi.r44_btn.clicked.connect(self.openRaflarR44Window)
        self.raflarUi.r45_btn.clicked.connect(self.openRaflarR45Window)
        self.raflarUi.r46_btn.clicked.connect(self.openRaflarR46Window)
        self.raflarUi.r47_btn.clicked.connect(self.openRaflarR47Window)
        self.raflarUi.r48_btn.clicked.connect(self.openRaflarR48Window)
        self.raflarUi.r49_btn.clicked.connect(self.openRaflarR49Window)
        self.raflarUi.r50_btn.clicked.connect(self.openRaflarR50Window)
        self.raflarUi.r51_btn.clicked.connect(self.openRaflarR51Window)
        self.raflarUi.r52_btn.clicked.connect(self.openRaflarR52Window)
        self.raflarUi.r53_btn.clicked.connect(self.openRaflarR53Window)
        self.raflarUi.r54_btn.clicked.connect(self.openRaflarR54Window)
        self.raflarUi.r55_btn.clicked.connect(self.openRaflarR55Window)
        self.raflarUi.r56_btn.clicked.connect(self.openRaflarR56Window)
        self.raflarUi.r57_btn.clicked.connect(self.openRaflarR57Window)
        self.raflarWindow.show()
    
    def openRaflarR57Window(self):
        self.raflarWindow.close()
        self.raflarR57Window = QMainWindow()
        self.raflarR57Ui = Ui_raflarR57_ekran()
        self.raflarR57Ui.setupUi(self.raflarR57Window)
        self.raflarR57Ui.listeleR57_btn.clicked.connect(self.kayit_listele_r57)
        self.raflarR57Ui.silR57_btn.clicked.connect(self.kayit_sil_r57)
        self.raflarR57Window.show()

    def openRaflarR56Window(self):
        self.raflarWindow.close()
        self.raflarR56Window = QMainWindow()
        self.raflarR56Ui = Ui_raflarR56_ekran()
        self.raflarR56Ui.setupUi(self.raflarR56Window)
        self.raflarR56Ui.listeleR56_btn.clicked.connect(self.kayit_listele_r56)
        self.raflarR56Ui.silR56_btn.clicked.connect(self.kayit_sil_r56)
        self.raflarR56Window.show()

    def openRaflarR55Window(self):
        self.raflarWindow.close()
        self.raflarR55Window = QMainWindow()
        self.raflarR55Ui = Ui_raflarR55_ekran()
        self.raflarR55Ui.setupUi(self.raflarR55Window)
        self.raflarR55Ui.listeleR55_btn.clicked.connect(self.kayit_listele_r55)
        self.raflarR55Ui.silR55_btn.clicked.connect(self.kayit_sil_r55)
        self.raflarR55Window.show()

    def openRaflarR54Window(self):
        self.raflarWindow.close()
        self.raflarR54Window = QMainWindow()
        self.raflarR54Ui = Ui_raflarR54_ekran()
        self.raflarR54Ui.setupUi(self.raflarR54Window)
        self.raflarR54Ui.listeleR54_btn.clicked.connect(self.kayit_listele_r54)
        self.raflarR54Ui.silR54_btn.clicked.connect(self.kayit_sil_r54)
        self.raflarR54Window.show()

    def openRaflarR53Window(self):
        self.raflarWindow.close()
        self.raflarR53Window = QMainWindow()
        self.raflarR53Ui = Ui_raflarR53_ekran()
        self.raflarR53Ui.setupUi(self.raflarR53Window)
        self.raflarR53Ui.listeleR53_btn.clicked.connect(self.kayit_listele_r53)
        self.raflarR53Ui.silR53_btn.clicked.connect(self.kayit_sil_r53)
        self.raflarR53Window.show()

    def openRaflarR52Window(self):
        self.raflarWindow.close()
        self.raflarR52Window = QMainWindow()
        self.raflarR52Ui = Ui_raflarR52_ekran()
        self.raflarR52Ui.setupUi(self.raflarR52Window)
        self.raflarR52Ui.listeleR52_btn.clicked.connect(self.kayit_listele_r52)
        self.raflarR52Ui.silR52_btn.clicked.connect(self.kayit_sil_r52)
        self.raflarR52Window.show()
  
    def openRaflarR51Window(self):
        self.raflarWindow.close()
        self.raflarR51Window = QMainWindow()
        self.raflarR51Ui = Ui_raflarR51_ekran()
        self.raflarR51Ui.setupUi(self.raflarR51Window)
        self.raflarR51Ui.listeleR51_btn.clicked.connect(self.kayit_listele_r51)
        self.raflarR51Ui.silR51_btn.clicked.connect(self.kayit_sil_r51)
        self.raflarR51Window.show()

    def openRaflarR50Window(self):
        self.raflarWindow.close()
        self.raflarR50Window = QMainWindow()
        self.raflarR50Ui = Ui_raflarR50_ekran()
        self.raflarR50Ui.setupUi(self.raflarR50Window)
        self.raflarR50Ui.listeleR50_btn.clicked.connect(self.kayit_listele_r50)
        self.raflarR50Ui.silR50_btn.clicked.connect(self.kayit_sil_r50)
        self.raflarR50Window.show()
    
    def openRaflarR49Window(self):
        self.raflarWindow.close()
        self.raflarR49Window = QMainWindow()
        self.raflarR49Ui = Ui_raflarR49_ekran()
        self.raflarR49Ui.setupUi(self.raflarR49Window)
        self.raflarR49Ui.listeleR49_btn.clicked.connect(self.kayit_listele_r49)
        self.raflarR49Ui.silR49_btn.clicked.connect(self.kayit_sil_r49)
        self.raflarR49Window.show()

    def openRaflarR48Window(self):
        self.raflarWindow.close()
        self.raflarR48Window = QMainWindow()
        self.raflarR48Ui = Ui_raflarR48_ekran()
        self.raflarR48Ui.setupUi(self.raflarR48Window)
        self.raflarR48Ui.listeleR48_btn.clicked.connect(self.kayit_listele_r48)
        self.raflarR48Ui.silR48_btn.clicked.connect(self.kayit_sil_r48)
        self.raflarR48Window.show()

    def openRaflarR47Window(self):
        self.raflarWindow.close()
        self.raflarR47Window = QMainWindow()
        self.raflarR47Ui = Ui_raflarR47_ekran()
        self.raflarR47Ui.setupUi(self.raflarR47Window)
        self.raflarR47Ui.listeleR47_btn.clicked.connect(self.kayit_listele_r47)
        self.raflarR47Ui.silR47_btn.clicked.connect(self.kayit_sil_r47)
        self.raflarR47Window.show()

    def openRaflarR46Window(self):
        self.raflarWindow.close()
        self.raflarR46Window = QMainWindow()
        self.raflarR46Ui = Ui_raflarR46_ekran()
        self.raflarR46Ui.setupUi(self.raflarR46Window)
        self.raflarR46Ui.listeleR46_btn.clicked.connect(self.kayit_listele_r46)
        self.raflarR46Ui.silR46_btn.clicked.connect(self.kayit_sil_r46)
        self.raflarR46Window.show()

    def openRaflarR45Window(self):
        self.raflarWindow.close()
        self.raflarR45Window = QMainWindow()
        self.raflarR45Ui = Ui_raflarR45_ekran()
        self.raflarR45Ui.setupUi(self.raflarR45Window)
        self.raflarR45Ui.listeleR45_btn.clicked.connect(self.kayit_listele_r45)
        self.raflarR45Ui.silR45_btn.clicked.connect(self.kayit_sil_r45)
        self.raflarR45Window.show()

    def openRaflarR44Window(self):
        self.raflarWindow.close()
        self.raflarR44Window = QMainWindow()
        self.raflarR44Ui = Ui_raflarR44_ekran()
        self.raflarR44Ui.setupUi(self.raflarR44Window)
        self.raflarR44Ui.listeleR44_btn.clicked.connect(self.kayit_listele_r44)
        self.raflarR44Ui.silR44_btn.clicked.connect(self.kayit_sil_r44)
        self.raflarR44Window.show()

    def openRaflarR43Window(self):
        self.raflarWindow.close()
        self.raflarR43Window = QMainWindow()
        self.raflarR43Ui = Ui_raflarR43_ekran()
        self.raflarR43Ui.setupUi(self.raflarR43Window)
        self.raflarR43Ui.listeleR43_btn.clicked.connect(self.kayit_listele_r43)
        self.raflarR43Ui.silR43_btn.clicked.connect(self.kayit_sil_r43)
        self.raflarR43Window.show()

    def openRaflarR42Window(self):
        self.raflarWindow.close()
        self.raflarR42Window = QMainWindow()
        self.raflarR42Ui = Ui_raflarR42_ekran()
        self.raflarR42Ui.setupUi(self.raflarR42Window)
        self.raflarR42Ui.listeleR42_btn.clicked.connect(self.kayit_listele_r42)
        self.raflarR42Ui.silR42_btn.clicked.connect(self.kayit_sil_r42)
        self.raflarR42Window.show()
    
    def openRaflarR41Window(self):
        self.raflarWindow.close()
        self.raflarR41Window = QMainWindow()
        self.raflarR41Ui = Ui_raflarR41_ekran()
        self.raflarR41Ui.setupUi(self.raflarR41Window)
        self.raflarR41Ui.listeleR41_btn.clicked.connect(self.kayit_listele_r41)
        self.raflarR41Ui.silR41_btn.clicked.connect(self.kayit_sil_r41)
        self.raflarR41Window.show()

    def openRaflarR40Window(self):
        self.raflarWindow.close()
        self.raflarR40Window = QMainWindow()
        self.raflarR40Ui = Ui_raflarR40_ekran()
        self.raflarR40Ui.setupUi(self.raflarR40Window)
        self.raflarR40Ui.listeleR40_btn.clicked.connect(self.kayit_listele_r40)
        self.raflarR40Ui.silR40_btn.clicked.connect(self.kayit_sil_r40)
        self.raflarR40Window.show()

    def openRaflarR39Window(self):
        self.raflarWindow.close()
        self.raflarR39Window = QMainWindow()
        self.raflarR39Ui = Ui_raflarR39_ekran()
        self.raflarR39Ui.setupUi(self.raflarR39Window)
        self.raflarR39Ui.listeleR39_btn.clicked.connect(self.kayit_listele_r39)
        self.raflarR39Ui.silR39_btn.clicked.connect(self.kayit_sil_r39)
        self.raflarR39Window.show()

    def openRaflarR38Window(self):
        self.raflarWindow.close()
        self.raflarR38Window = QMainWindow()
        self.raflarR38Ui = Ui_raflarR38_ekran()
        self.raflarR38Ui.setupUi(self.raflarR38Window)
        self.raflarR38Ui.listeleR38_btn.clicked.connect(self.kayit_listele_r38)
        self.raflarR38Ui.silR38_btn.clicked.connect(self.kayit_sil_r38)
        self.raflarR38Window.show()

    def openRaflarR37Window(self):
        self.raflarWindow.close()
        self.raflarR37Window = QMainWindow()
        self.raflarR37Ui = Ui_raflarR37_ekran()
        self.raflarR37Ui.setupUi(self.raflarR37Window)
        self.raflarR37Ui.listeleR37_btn.clicked.connect(self.kayit_listele_r37)
        self.raflarR37Ui.silR37_btn.clicked.connect(self.kayit_sil_r37)
        self.raflarR37Window.show()

    def openRaflarR36Window(self):
        self.raflarWindow.close()
        self.raflarR36Window = QMainWindow()
        self.raflarR36Ui = Ui_raflarR36_ekran()
        self.raflarR36Ui.setupUi(self.raflarR36Window)
        self.raflarR36Ui.listeleR36_btn.clicked.connect(self.kayit_listele_r36)
        self.raflarR36Ui.silR36_btn.clicked.connect(self.kayit_sil_r36)
        self.raflarR36Window.show()

    def openRaflarR35Window(self):
        self.raflarWindow.close()
        self.raflarR35Window = QMainWindow()
        self.raflarR35Ui = Ui_raflarR35_ekran()
        self.raflarR35Ui.setupUi(self.raflarR35Window)
        self.raflarR35Ui.listeleR35_btn.clicked.connect(self.kayit_listele_r35)
        self.raflarR35Ui.silR35_btn.clicked.connect(self.kayit_sil_r35)
        self.raflarR35Window.show()

    def openRaflarR34Window(self):
        self.raflarWindow.close()
        self.raflarR34Window = QMainWindow()
        self.raflarR34Ui = Ui_raflarR34_ekran()
        self.raflarR34Ui.setupUi(self.raflarR34Window)
        self.raflarR34Ui.listeleR34_btn.clicked.connect(self.kayit_listele_r34)
        self.raflarR34Ui.silR34_btn.clicked.connect(self.kayit_sil_r34)
        self.raflarR34Window.show()
    
    def openRaflarR33Window(self):
        self.raflarWindow.close()
        self.raflarR33Window = QMainWindow()
        self.raflarR33Ui = Ui_raflarR33_ekran()
        self.raflarR33Ui.setupUi(self.raflarR33Window)
        self.raflarR33Ui.listeleR33_btn.clicked.connect(self.kayit_listele_r33)
        self.raflarR33Ui.silR33_btn.clicked.connect(self.kayit_sil_r33)
        self.raflarR33Window.show()

    def openRaflarR32Window(self):
        self.raflarWindow.close()
        self.raflarR32Window = QMainWindow()
        self.raflarR32Ui = Ui_raflarR32_ekran()
        self.raflarR32Ui.setupUi(self.raflarR32Window)
        self.raflarR32Ui.listeleR32_btn.clicked.connect(self.kayit_listele_r32)
        self.raflarR32Ui.silR32_btn.clicked.connect(self.kayit_sil_r32)
        self.raflarR32Window.show()

    def openRaflarR31Window(self):
        self.raflarWindow.close()
        self.raflarR31Window = QMainWindow()
        self.raflarR31Ui = Ui_raflarR31_ekran()
        self.raflarR31Ui.setupUi(self.raflarR31Window)
        self.raflarR31Ui.listeleR31_btn.clicked.connect(self.kayit_listele_r31)
        self.raflarR31Ui.silR31_btn.clicked.connect(self.kayit_sil_r31)
        self.raflarR31Window.show()

    def openRaflarR30Window(self):
        self.raflarWindow.close()
        self.raflarR30Window = QMainWindow()
        self.raflarR30Ui = Ui_raflarR30_ekran()
        self.raflarR30Ui.setupUi(self.raflarR30Window)
        self.raflarR30Ui.listeleR30_btn.clicked.connect(self.kayit_listele_r30)
        self.raflarR30Ui.silR30_btn.clicked.connect(self.kayit_sil_r30)
        self.raflarR30Window.show()

    def openRaflarR29Window(self):
        self.raflarWindow.close()
        self.raflarR29Window = QMainWindow()
        self.raflarR29Ui = Ui_raflarR29_ekran()
        self.raflarR29Ui.setupUi(self.raflarR29Window)
        self.raflarR29Ui.listeleR29_btn.clicked.connect(self.kayit_listele_r29)
        self.raflarR29Ui.silR29_btn.clicked.connect(self.kayit_sil_r29)
        self.raflarR29Window.show()

    def openRaflarR28Window(self):
        self.raflarWindow.close()
        self.raflarR28Window = QMainWindow()
        self.raflarR28Ui = Ui_raflarR28_ekran()
        self.raflarR28Ui.setupUi(self.raflarR28Window)
        self.raflarR28Ui.listeleR28_btn.clicked.connect(self.kayit_listele_r28)
        self.raflarR28Ui.silR28_btn.clicked.connect(self.kayit_sil_r28)
        self.raflarR28Window.show()

    def openRaflarR27Window(self):
        self.raflarWindow.close()
        self.raflarR27Window = QMainWindow()
        self.raflarR27Ui = Ui_raflarR27_ekran()
        self.raflarR27Ui.setupUi(self.raflarR27Window)
        self.raflarR27Ui.listeleR27_btn.clicked.connect(self.kayit_listele_r27)
        self.raflarR27Ui.silR27_btn.clicked.connect(self.kayit_sil_r27)
        self.raflarR27Window.show()

    def openRaflarR26Window(self):
        self.raflarWindow.close()
        self.raflarR26Window = QMainWindow()
        self.raflarR26Ui = Ui_raflarR26_ekran()
        self.raflarR26Ui.setupUi(self.raflarR26Window)
        self.raflarR26Ui.listeleR26_btn.clicked.connect(self.kayit_listele_r26)
        self.raflarR26Ui.silR26_btn.clicked.connect(self.kayit_sil_r26)
        self.raflarR26Window.show()
    
    def openRaflarR25Window(self):
        self.raflarWindow.close()
        self.raflarR25Window = QMainWindow()
        self.raflarR25Ui = Ui_raflarR25_ekran()
        self.raflarR25Ui.setupUi(self.raflarR25Window)
        self.raflarR25Ui.listeleR25_btn.clicked.connect(self.kayit_listele_r25)
        self.raflarR25Ui.silR25_btn.clicked.connect(self.kayit_sil_r25)
        self.raflarR25Window.show()

    def openRaflarR24Window(self):
        self.raflarWindow.close()
        self.raflarR24Window = QMainWindow()
        self.raflarR24Ui = Ui_raflarR24_ekran()
        self.raflarR24Ui.setupUi(self.raflarR24Window)
        self.raflarR24Ui.listeleR24_btn.clicked.connect(self.kayit_listele_r24)
        self.raflarR24Ui.silR24_btn.clicked.connect(self.kayit_sil_r24)
        self.raflarR24Window.show()

    def openRaflarR23Window(self):
        self.raflarWindow.close()
        self.raflarR23Window = QMainWindow()
        self.raflarR23Ui = Ui_raflarR23_ekran()
        self.raflarR23Ui.setupUi(self.raflarR23Window)
        self.raflarR23Ui.listeleR23_btn.clicked.connect(self.kayit_listele_r23)
        self.raflarR23Ui.silR23_btn.clicked.connect(self.kayit_sil_r23)
        self.raflarR23Window.show()

    def openRaflarR22Window(self):
        self.raflarWindow.close()
        self.raflarR22Window = QMainWindow()
        self.raflarR22Ui = Ui_raflarR22_ekran()
        self.raflarR22Ui.setupUi(self.raflarR22Window)
        self.raflarR22Ui.listeleR22_btn.clicked.connect(self.kayit_listele_r22)
        self.raflarR22Ui.silR22_btn.clicked.connect(self.kayit_sil_r22)
        self.raflarR22Window.show()

    def openRaflarR21Window(self):
        self.raflarWindow.close()
        self.raflarR21Window = QMainWindow()
        self.raflarR21Ui = Ui_raflarR21_ekran()
        self.raflarR21Ui.setupUi(self.raflarR21Window)
        self.raflarR21Ui.listeleR21_btn.clicked.connect(self.kayit_listele_r21)
        self.raflarR21Ui.silR21_btn.clicked.connect(self.kayit_sil_r21)
        self.raflarR21Window.show()

    def openRaflarR20Window(self):
        self.raflarWindow.close()
        self.raflarR20Window = QMainWindow()
        self.raflarR20Ui = Ui_raflarR20_ekran()
        self.raflarR20Ui.setupUi(self.raflarR20Window)
        self.raflarR20Ui.listeleR20_btn.clicked.connect(self.kayit_listele_r20)
        self.raflarR20Ui.silR20_btn.clicked.connect(self.kayit_sil_r20)
        self.raflarR20Window.show()

    def openRaflarR19Window(self):
        self.raflarWindow.close()
        self.raflarR19Window = QMainWindow()
        self.raflarR19Ui = Ui_raflarR19_ekran()
        self.raflarR19Ui.setupUi(self.raflarR19Window)
        self.raflarR19Ui.listeleR19_btn.clicked.connect(self.kayit_listele_r19)
        self.raflarR19Ui.silR19_btn.clicked.connect(self.kayit_sil_r19)
        self.raflarR19Window.show()

    def openRaflarR18Window(self):
        self.raflarWindow.close()
        self.raflarR18Window = QMainWindow()
        self.raflarR18Ui = Ui_raflarR18_ekran()
        self.raflarR18Ui.setupUi(self.raflarR18Window)
        self.raflarR18Ui.listeleR18_btn.clicked.connect(self.kayit_listele_r18)
        self.raflarR18Ui.silR18_btn.clicked.connect(self.kayit_sil_r18)
        self.raflarR18Window.show()
    
    def openRaflarR17Window(self):
        self.raflarWindow.close()
        self.raflarR17Window = QMainWindow()
        self.raflarR17Ui = Ui_raflarR17_ekran()
        self.raflarR17Ui.setupUi(self.raflarR17Window)
        self.raflarR17Ui.listeleR17_btn.clicked.connect(self.kayit_listele_r17)
        self.raflarR17Ui.silR17_btn.clicked.connect(self.kayit_sil_r17)
        self.raflarR17Window.show()

    def openRaflarR16Window(self):
        self.raflarWindow.close()
        self.raflarR16Window = QMainWindow()
        self.raflarR16Ui = Ui_raflarR16_ekran()
        self.raflarR16Ui.setupUi(self.raflarR16Window)
        self.raflarR16Ui.listeleR16_btn.clicked.connect(self.kayit_listele_r16)
        self.raflarR16Ui.silR16_btn.clicked.connect(self.kayit_sil_r16)
        self.raflarR16Window.show()

    def openRaflarR15Window(self):
        self.raflarWindow.close()
        self.raflarR15Window = QMainWindow()
        self.raflarR15Ui = Ui_raflarR15_ekran()
        self.raflarR15Ui.setupUi(self.raflarR15Window)
        self.raflarR15Ui.listeleR15_btn.clicked.connect(self.kayit_listele_r15)
        self.raflarR15Ui.silR15_btn.clicked.connect(self.kayit_sil_r15)
        self.raflarR15Window.show()

    def openRaflarR14Window(self):
        self.raflarWindow.close()
        self.raflarR14Window = QMainWindow()
        self.raflarR14Ui = Ui_raflarR14_ekran()
        self.raflarR14Ui.setupUi(self.raflarR14Window)
        self.raflarR14Ui.listeleR14_btn.clicked.connect(self.kayit_listele_r14)
        self.raflarR14Ui.silR14_btn.clicked.connect(self.kayit_sil_r14)
        self.raflarR14Window.show()

    def openRaflarR13Window(self):
        self.raflarWindow.close()
        self.raflarR13Window = QMainWindow()
        self.raflarR13Ui = Ui_raflarR13_ekran()
        self.raflarR13Ui.setupUi(self.raflarR13Window)
        self.raflarR13Ui.listeleR13_btn.clicked.connect(self.kayit_listele_r13)
        self.raflarR13Ui.silR13_btn.clicked.connect(self.kayit_sil_r13)
        self.raflarR13Window.show()

    def openRaflarR12Window(self):
        self.raflarWindow.close()
        self.raflarR12Window = QMainWindow()
        self.raflarR12Ui = Ui_raflarR12_ekran()
        self.raflarR12Ui.setupUi(self.raflarR12Window)
        self.raflarR12Ui.listeleR12_btn.clicked.connect(self.kayit_listele_r12)
        self.raflarR12Ui.silR12_btn.clicked.connect(self.kayit_sil_r12)
        self.raflarR12Window.show()

    def openRaflarR11Window(self):
        self.raflarWindow.close()
        self.raflarR11Window = QMainWindow()
        self.raflarR11Ui = Ui_raflarR11_ekran()
        self.raflarR11Ui.setupUi(self.raflarR11Window)
        self.raflarR11Ui.listeleR11_btn.clicked.connect(self.kayit_listele_r11)
        self.raflarR11Ui.silR11_btn.clicked.connect(self.kayit_sil_r11)
        self.raflarR11Window.show()

    def openRaflarR10Window(self):
        self.raflarWindow.close()
        self.raflarR10Window = QMainWindow()
        self.raflarR10Ui = Ui_raflarR10_ekran()
        self.raflarR10Ui.setupUi(self.raflarR10Window)
        self.raflarR10Ui.listeleR10_btn.clicked.connect(self.kayit_listele_r10)
        self.raflarR10Ui.silR10_btn.clicked.connect(self.kayit_sil_r10)
        self.raflarR10Window.show()
    
    def openRaflarR9Window(self):
        self.raflarWindow.close()
        self.raflarR9Window = QMainWindow()
        self.raflarR9Ui = Ui_raflarR9_ekran()
        self.raflarR9Ui.setupUi(self.raflarR9Window)
        self.raflarR9Ui.listeleR9_btn.clicked.connect(self.kayit_listele_r9)
        self.raflarR9Ui.silR9_btn.clicked.connect(self.kayit_sil_r9)
        self.raflarR9Window.show()

    def openRaflarR8Window(self):
        self.raflarWindow.close()
        self.raflarR8Window = QMainWindow()
        self.raflarR8Ui = Ui_raflarR8_ekran()
        self.raflarR8Ui.setupUi(self.raflarR8Window)
        self.raflarR8Ui.listeleR8_btn.clicked.connect(self.kayit_listele_r8)
        self.raflarR8Ui.silR8_btn.clicked.connect(self.kayit_sil_r8)
        self.raflarR8Window.show()

    def openRaflarR7Window(self):
        self.raflarWindow.close()
        self.raflarR7Window = QMainWindow()
        self.raflarR7Ui = Ui_raflarR7_ekran()
        self.raflarR7Ui.setupUi(self.raflarR7Window)
        self.raflarR7Ui.listeleR7_btn.clicked.connect(self.kayit_listele_r7)
        self.raflarR7Ui.silR7_btn.clicked.connect(self.kayit_sil_r7)
        self.raflarR7Window.show()

    def openRaflarR6Window(self):
        self.raflarWindow.close()
        self.raflarR6Window = QMainWindow()
        self.raflarR6Ui = Ui_raflarR6_ekran()
        self.raflarR6Ui.setupUi(self.raflarR6Window)
        self.raflarR6Ui.listeleR6_btn.clicked.connect(self.kayit_listele_r6)
        self.raflarR6Ui.silR6_btn.clicked.connect(self.kayit_sil_r6)
        self.raflarR6Window.show()

    def openRaflarR5Window(self):
        self.raflarWindow.close()
        self.raflarR5Window = QMainWindow()
        self.raflarR5Ui = Ui_raflarR5_ekran()
        self.raflarR5Ui.setupUi(self.raflarR5Window)
        self.raflarR5Ui.listeleR5_btn.clicked.connect(self.kayit_listele_r5)
        self.raflarR5Ui.silR5_btn.clicked.connect(self.kayit_sil_r5)
        self.raflarR5Window.show()

    def openRaflarR4Window(self):
        self.raflarWindow.close()
        self.raflarR4Window = QMainWindow()
        self.raflarR4Ui = Ui_raflarR4_ekran()
        self.raflarR4Ui.setupUi(self.raflarR4Window)
        self.raflarR4Ui.listeleR4_btn.clicked.connect(self.kayit_listele_r4)
        self.raflarR4Ui.silR4_btn.clicked.connect(self.kayit_sil_r4)
        self.raflarR4Window.show()

    def openRaflarR3Window(self):
        self.raflarWindow.close()
        self.raflarR3Window = QMainWindow()
        self.raflarR3Ui = Ui_raflarR3_ekran()
        self.raflarR3Ui.setupUi(self.raflarR3Window)
        self.raflarR3Ui.listeleR3_btn.clicked.connect(self.kayit_listele_r3)
        self.raflarR3Ui.silR3_btn.clicked.connect(self.kayit_sil_r3)
        self.raflarR3Window.show()

    def openRaflarR2Window(self):
        self.raflarWindow.close()
        self.raflarR2Window = QMainWindow()
        self.raflarR2Ui = Ui_raflarR2_ekran()
        self.raflarR2Ui.setupUi(self.raflarR2Window)
        self.raflarR2Ui.listeleR2_btn.clicked.connect(self.kayit_listele_r2)
        self.raflarR2Ui.silR2_btn.clicked.connect(self.kayit_sil_r2)
        self.raflarR2Window.show()

    def openRaflarR1Window(self):
        self.raflarWindow.close()
        self.raflarR1Window = QMainWindow()
        self.raflarR1Ui = Ui_raflarR1_ekran()
        self.raflarR1Ui.setupUi(self.raflarR1Window)
        self.raflarR1Ui.listeleR1_btn.clicked.connect(self.kayit_listele_r1)
        self.raflarR1Ui.silR1_btn.clicked.connect(self.kayit_sil_r1)
        self.raflarR1Window.show()

    def openKumasKayitWindow(self):
        self.depoWindow.close()
        self.kumasKayitWindow = QMainWindow()
        self.kumasKayitUi = Ui_kumaskayit_ekran()
        self.kumasKayitUi.setupUi(self.kumasKayitWindow)
        self.kumasKayitUi.kaydetKK_btn.clicked.connect(self.kayit_ekle)
        self.kumasKayitWindow.show()

    def openKumasFiltrelemeWindow(self):
        self.depoWindow.close()
        self.kumasFiltrelemeWindow = QMainWindow()
        self.kumasFiltrelemeUi = Ui_kumasfiltreleme_ekran()
        self.kumasFiltrelemeUi.setupUi(self.kumasFiltrelemeWindow)
        self.kumasFiltrelemeUi.tumunulist_btn.clicked.connect(self.kayit_listele)
        self.kumasFiltrelemeUi.ks_listele_btn.clicked.connect(self.kategoriye_gore_listele)
        self.kumasFiltrelemeWindow.show()

    def kayit_ekle(self):
        ui = self.kumasKayitUi
        raw_text = ui.lotKK_entry.text()
        raw_text2 = ui.kaliteKK_entry.text()
        raw_text3 = ui.genislikKK_entry.text()
        raw_text4 = ui.araba_cb.currentText()
        raw_text5 = ui.raf_cb.currentText()

    
        if not raw_text or not raw_text2 or not raw_text3 or not raw_text4 or not raw_text5:
           QMessageBox.warning(self, "Uyarı", "Tüm alanları doldurun! Boş bırakılamaz.")
           return  

    
        try:
            lot = int(''.join(filter(str.isdigit, raw_text)))
            kalite = int(''.join(filter(str.isdigit, raw_text2)))
            genislik = int(''.join(filter(str.isdigit, raw_text3)))
            arabakod = int(''.join(filter(str.isdigit, raw_text4)))
            rafkod = int(''.join(filter(str.isdigit, raw_text5)))

        
        
        except ValueError:
            QMessageBox.warning(self, "Uyarı", "Geçersiz değer girilemez!")
        
        
        

        numeric_parta1 = 1
        numeric_parta2 = 2
        numeric_parta3 = 3
        numeric_parta4 = 4
        numeric_parta5 = 5
        numeric_parta6 = 6
        numeric_parta7 = 7
        numeric_parta8 = 8
        numeric_parta9 = 9
        numeric_parta10 = 10
        numeric_parta11 = 11
        numeric_parta12 = 12
        numeric_parta13 = 13
        numeric_parta14 = 14
        numeric_parta15 = 15
        numeric_parta16 = 16
        numeric_parta17 = 17
        numeric_parta18 = 18
        numeric_parta19 = 19
        numeric_parta20 = 20
        numeric_parta21 = 21
        numeric_parta22 = 22
        numeric_parta23 = 23
        numeric_parta24 = 24
        numeric_parta25 = 25
        numeric_parta26 = 26
        numeric_parta27 = 27
        numeric_parta28 = 28
        numeric_parta29 = 29
        numeric_parta30 = 30
        numeric_parta31 = 31
        numeric_parta32 = 32
        numeric_parta33 = 33
        numeric_parta34 = 34
        numeric_parta35 = 35
        numeric_parta36 = 36
        numeric_parta37 = 37
        numeric_parta38 = 38
        numeric_parta39 = 39
        numeric_parta40 = 40
        numeric_parta41 = 41
        numeric_parta42 = 42
        numeric_parta43 = 43
        numeric_parta44 = 44
        numeric_parta45 = 45
        numeric_parta46 = 46
        numeric_parta46 = 46
        numeric_parta47 = 47
        numeric_parta48 = 48
        numeric_parta49 = 49
        numeric_parta50 = 50
        numeric_parta51 = 51
        numeric_parta52 = 52
        numeric_parta53 = 53
        numeric_parta54 = 54
        numeric_parta55 = 55
        numeric_parta56 = 56
        numeric_parta57 = 57
        numeric_parta58 = 58
        numeric_parta59 = 59
        numeric_parta60 = 60
        numeric_parta61 = 61
        numeric_parta62 = 62
        numeric_parta63 = 63
        numeric_parta64 = 64
        numeric_parta65 = 65
        numeric_parta66 = 66
        numeric_parta67 = 67
        numeric_parta68 = 68
        numeric_parta69 = 69
        numeric_parta70 = 70
        numeric_parta71 = 71
        numeric_parta72 = 72
        numeric_parta73 = 73
        numeric_parta74 = 74
        numeric_parta75 = 75
        numeric_parta76 = 76
        numeric_parta77 = 77
        numeric_parta78 = 78
        numeric_parta79 = 79
        numeric_parta80 = 80
        numeric_parta81 = 81
        numeric_parta82 = 82
        numeric_parta83 = 83
        numeric_parta84 = 84
        numeric_parta85 = 85
        numeric_parta86 = 86
        numeric_parta87 = 87
        numeric_parta88 = 88
        numeric_parta89 = 89
        numeric_parta90 = 90
        numeric_parta91 = 91
        numeric_parta92 = 92
        numeric_parta93 = 93
        numeric_parta94= 94
        numeric_parta95 = 95
        numeric_parta96 = 96
        numeric_parta97 = 97
        numeric_parta98 = 98
        numeric_parta98 = 98
        numeric_parta99 = 99
        numeric_parta100 = 100
        numeric_parta101 = 101
        numeric_parta102 = 102
        numeric_parta103 = 103
        numeric_partr1 = 1
        numeric_partr2 = 2
        numeric_partr3 = 3
        numeric_partr4 = 4
        numeric_partr5 = 5
        numeric_partr6 = 6
        numeric_partr7 = 7
        numeric_partr8 = 8
        numeric_partr9 = 9
        numeric_partr10 = 10
        numeric_partr11 = 11
        numeric_partr12 = 12
        numeric_partr13 = 13
        numeric_partr14 = 14
        numeric_partr15 = 15
        numeric_partr16 = 16
        numeric_partr17 = 17
        numeric_partr18 = 18
        numeric_partr19 = 19
        numeric_partr20 = 20
        numeric_partr21 = 21
        numeric_partr22 = 22
        numeric_partr23 = 23
        numeric_partr24 = 24
        numeric_partr25 = 25
        numeric_partr26 = 26
        numeric_partr27 = 27
        numeric_partr28 = 28
        numeric_partr29 = 29
        numeric_partr30 = 30
        numeric_partr31 = 31
        numeric_partr32 = 32
        numeric_partr33 = 33
        numeric_partr34 = 34
        numeric_partr35 = 35
        numeric_partr36 = 36
        numeric_partr37 = 37
        numeric_partr38 = 38
        numeric_partr39 = 39
        numeric_partr40 = 40
        numeric_partr41 = 41
        numeric_partr42 = 42
        numeric_partr43 = 43
        numeric_partr44 = 44
        numeric_partr45 = 45
        numeric_partr46 = 46
        numeric_partr47 = 47
        numeric_partr48 = 48
        numeric_partr49 = 49
        numeric_partr50 = 50
        numeric_partr51 = 51
        numeric_partr52 = 52
        numeric_partr53 = 53
        numeric_partr54 = 54
        numeric_partr55 = 55
        numeric_partr56 = 56
        numeric_partr57 = 57

        ekle = ""
        ekle2 = ""

        try:
            if arabakod == numeric_parta1:
                ekle = "insert into A1 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta2:
                ekle = "insert into A2 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta3:
                ekle = "insert into A3 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta4:
                ekle = "insert into A4 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta5:
                ekle = "insert into A5 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta6:
                ekle = "insert into A6 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta7:
                ekle = "insert into A7 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta8:
                ekle = "insert into A8 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta9:
                ekle = "insert into A9 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta10:
                ekle = "insert into A10 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta11:
                ekle = "insert into A11 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta12:
                ekle = "insert into A12 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta13:
                ekle = "insert into A13 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta14:
                ekle = "insert into A14 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta15:
                ekle = "insert into A15 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta16:
                ekle = "insert into A16 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta17:
                ekle = "insert into A17 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta18:
                ekle = "insert into A18 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta19:
                ekle = "insert into A19 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta20:
                ekle = "insert into A20 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta21:
                ekle = "insert into A21 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta22:
                ekle = "insert into A22 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta23:
                ekle = "insert into A23 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta24:
                ekle = "insert into A24 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta25:
                ekle = "insert into A25 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta26:
                ekle = "insert into A26 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta27:
                ekle = "insert into A27 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta28:
                ekle = "insert into A28 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta29:
                ekle = "insert into A29 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta30:
                ekle = "insert into A30 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta31:
                ekle = "insert into A31 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta32:
                ekle = "insert into A32 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta33:
                ekle = "insert into A33 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta34:
                ekle = "insert into A34 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta35:
                ekle = "insert into A35 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta36:
                ekle = "insert into A36 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta37:
                ekle = "insert into A37 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta38:
                ekle = "insert into A38 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta39:
                ekle = "insert into A39 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta40:
                ekle = "insert into A40 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta41:
                ekle = "insert into A41 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta42:
                ekle = "insert into A42 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta43:
                ekle = "insert into A43 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta44:
                ekle = "insert into A44 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta45:
                ekle = "insert into A45 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta46:
                ekle = "insert into A46 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta47:
                ekle = "insert into A47 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta48:
                ekle = "insert into A48 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta49:
                ekle = "insert into A49 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta50:
                ekle = "insert into A50 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta51:
                ekle = "insert into A51 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta52:
                ekle = "insert into A52 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta53:
                ekle = "insert into A53 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta54:
                ekle = "insert into A54 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta55:
                ekle = "insert into A55 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta56:
                ekle = "insert into A56 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta57:
                ekle = "insert into A57 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta58:
                ekle = "insert into A58 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta59:
                ekle = "insert into A59 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta60:
                ekle = "insert into A60 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta61:
                ekle = "insert into A61 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta62:
                ekle = "insert into A62 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta63:
                ekle = "insert into A63 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta64:
                ekle = "insert into A64 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta65:
                ekle = "insert into A65 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta66:
                ekle = "insert into A66 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta67:
                ekle = "insert into A67 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta68:
                ekle = "insert into A68 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta69:
                ekle = "insert into A69 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta70:
                ekle = "insert into A70 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta71:
                ekle = "insert into A71 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta72:
                ekle = "insert into A72 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta73:
                ekle = "insert into A73 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta74:
                ekle = "insert into A74 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta75:
                ekle = "insert into A75 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta76:
                ekle = "insert into A76 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta77:
                ekle = "insert into A77 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta78:
                ekle = "insert into A78 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta79:
                ekle = "insert into A79 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta80:
                ekle = "insert into A80 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta81:
                ekle = "insert into A81 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta82:
                ekle = "insert into A82 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta83:
                ekle = "insert into A83 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta84:
                ekle = "insert into A84 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta85:
                ekle = "insert into A85 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta86:
                ekle = "insert into A86 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta87:
                ekle = "insert into A87 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta88:
                ekle = "insert into A88 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta89:
                ekle = "insert into A89 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta90:
                ekle = "insert into A90 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta91:
                ekle = "insert into A91 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta92:
                ekle = "insert into A92 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta93:
                ekle = "insert into A93 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta94:
                ekle = "insert into A94 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta95:
                ekle = "insert into A95 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta96:
                ekle = "insert into A96 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta97:
                ekle = "insert into A97 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta98:
                ekle = "insert into A98 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta99:
                ekle = "insert into A99 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta100:
                ekle = "insert into A100 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta101:
                ekle = "insert into A101 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta102:
                ekle = "insert into A102 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif arabakod == numeric_parta103:
                ekle = "insert into A103 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr1:
                ekle = "insert into R1 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr2:
                ekle = "insert into R2 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr3:
                ekle = "insert into R3 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr4:
                ekle = "insert into R4 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr5:
                ekle = "insert into R5 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr6:
                ekle = "insert into R6 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr7:
                ekle = "insert into R7 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr8:
                ekle = "insert into R8 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr9:
                ekle = "insert into R9 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr10:
                ekle = "insert into R10 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr11:
                ekle = "insert into R11 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr12:
                ekle = "insert into R12 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr13:
                ekle = "insert into R13 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr14:
                ekle = "insert into R14 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr15:
                ekle = "insert into R15 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr16:
                ekle = "insert into R16 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr17:
                ekle = "insert into R17 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr18:
                ekle = "insert into R18 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr19:
                ekle = "insert into R19 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr20:
                ekle = "insert into R20 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr21:
                ekle = "insert into R21 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr22:
                ekle = "insert into R22 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr23:
                ekle = "insert into R23 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr24:
                ekle = "insert into R24 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr25:
                ekle = "insert into R25 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr26:
                ekle = "insert into R26 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr27:
                ekle = "insert into R27 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr28:
                ekle = "insert into R28 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr29:
                ekle = "insert into R29 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr30:
                ekle = "insert into R30 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr31:
                ekle = "insert into R31 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr32:
                ekle = "insert into R32 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr33:
                ekle = "insert into R33 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr34:
                ekle = "insert into R34 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr35:
                ekle = "insert into R35 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr35:
                ekle = "insert into R35 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr36:
                ekle = "insert into R36 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr37:
                ekle = "insert into R37 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr38:
                ekle = "insert into R38 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr39:
                ekle = "insert into R39 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr40:
                ekle = "insert into R40 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr41:
                ekle = "insert into R41 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr42:
                ekle = "insert into R42 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr43:
                ekle = "insert into R43 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr44:
                ekle = "insert into R44 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr45:
                ekle = "insert into R45 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr46:
                ekle = "insert into R46 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr47:
                ekle = "insert into R47 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr48:
                ekle = "insert into R48 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr49:
                ekle = "insert into R49 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr50:
                ekle = "insert into R50 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr51:
                ekle = "insert into R51 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr52:
                ekle = "insert into R52 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr53:
                ekle = "insert into R53 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr54:
                ekle = "insert into R54 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr55:
                ekle = "insert into R55 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr56:
                ekle = "insert into R56 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            elif rafkod == numeric_partr57:
                ekle = "insert into R57 (Lot, Kalite, Genislik) values (?, ?, ?)"
                ekle2 = "insert into kumaslarT (Lot, Kalite, Genislik, Arabakod, RafKod) values (?, ?, ?, ?, ?)"
            else:
                raise ValueError("Geçersiz durum, Araba veya Raf seçimi yapılmalıdır.")
            
            self.islem.execute(ekle, (lot, kalite, genislik))
            self.islem.execute(ekle2, (lot, kalite, genislik, arabakod, rafkod))
            self.baglanti.commit()
            
            QMessageBox.information(self.kumasKayitWindow, "Başarılı", "<b>Kayıt Ekleme İşlemi Başarılı!</b>")
            
            
        
        except Exception as error:
            QMessageBox.critical(self.kumasKayitWindow, "Hata", f"Kayıt Ekleme İşlemi Başarısız!")
        
    def kayit_listele(self):
        self.kumasFiltrelemeUi.kumaslar_tw.clear()
        self.kumasFiltrelemeUi.kumaslar_tw.setHorizontalHeaderLabels(("Lot","Kalite","Genişlik","ArabaKod","RafKod"))
        self.kumasFiltrelemeUi.kumaslar_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "select * from kumaslarT"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.kumasFiltrelemeUi.kumaslar_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kategoriye_gore_listele(self):
        listelenecek_kategori = self.kumasFiltrelemeUi.kalitesec_cb.currentText()
        self.kumasFiltrelemeUi.kumaslar_tw.clear()
        self.kumasFiltrelemeUi.kumaslar_tw.setHorizontalHeaderLabels(("Lot","Kalite","Genişlik","ArabaKod","RafKod"))
        self.kumasFiltrelemeUi.kumaslar_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "select * from kumaslarT where Kalite = ?"
        self.islem.execute(sorgu, (listelenecek_kategori,))
        for indexSatir, kayitNumarasi in enumerate(self.islem):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.kumasFiltrelemeUi.kumaslar_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_listele_a1(self):
        self.arabalarA1Ui.A1_tw.clear()
        self.arabalarA1Ui.A1_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA1Ui.A1_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A1"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA1Ui.A1_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a1(self):
        sil_mesaj = QMessageBox.question(self.arabalarA1Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)
        
        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA1Ui.A1_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA1Ui.A1_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a1 = "DELETE FROM A1 WHERE Lot = ?"
                self.islem.execute(sorgu_a1, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA1Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a1()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA1Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a2(self):
        self.arabalarA2Ui.A2_tw.clear()
        self.arabalarA2Ui.A2_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA2Ui.A2_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A2"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA2Ui.A2_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a2(self):
        sil_mesaj = QMessageBox.question(self.arabalarA2Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA2Ui.A2_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA2Ui.A2_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a2 = "DELETE FROM A2 WHERE Lot = ?"
                self.islem.execute(sorgu_a2, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA2Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a2()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA2Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a3(self):
        self.arabalarA3Ui.A3_tw.clear()
        self.arabalarA3Ui.A3_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA3Ui.A3_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A3"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA3Ui.A3_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a3(self):
        sil_mesaj = QMessageBox.question(self.arabalarA3Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA3Ui.A3_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA3Ui.A3_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a3 = "DELETE FROM A3 WHERE Lot = ?"
                self.islem.execute(sorgu_a3, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA3Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a3()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA3Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a4(self):
        self.arabalarA4Ui.A4_tw.clear()
        self.arabalarA4Ui.A4_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA4Ui.A4_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A4"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA4Ui.A4_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a4(self):
        sil_mesaj = QMessageBox.question(self.arabalarA4Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA4Ui.A4_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA4Ui.A4_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a4 = "DELETE FROM A4 WHERE Lot = ?"
                self.islem.execute(sorgu_a4, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA4Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a4()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA4Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a5(self):
        self.arabalarA5Ui.A5_tw.clear()
        self.arabalarA5Ui.A5_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA5Ui.A5_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A5"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA5Ui.A5_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a5(self):
        sil_mesaj = QMessageBox.question(self.arabalarA5Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA5Ui.A5_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA5Ui.A5_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a5 = "DELETE FROM A5 WHERE Lot = ?"
                self.islem.execute(sorgu_a5, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA5Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a5()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA5Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a6(self):
        self.arabalarA6Ui.A6_tw.clear()
        self.arabalarA6Ui.A6_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA6Ui.A6_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A6"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA6Ui.A6_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a6(self):
        sil_mesaj = QMessageBox.question(self.arabalarA6Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA6Ui.A6_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA6Ui.A6_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a6 = "DELETE FROM A6 WHERE Lot = ?"
                self.islem.execute(sorgu_a6, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA6Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a6()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA6Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
                
    def kayit_listele_a7(self):
        self.arabalarA7Ui.A7_tw.clear()
        self.arabalarA7Ui.A7_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA7Ui.A7_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A7"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA7Ui.A7_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a7(self):
        sil_mesaj = QMessageBox.question(self.arabalarA7Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA7Ui.A7_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA7Ui.A7_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a7 = "DELETE FROM A7 WHERE Lot = ?"
                self.islem.execute(sorgu_a7, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA7Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a7()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA7Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a8(self):
        self.arabalarA8Ui.A8_tw.clear()
        self.arabalarA8Ui.A8_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA8Ui.A8_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A8"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA8Ui.A8_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a8(self):
        sil_mesaj = QMessageBox.question(self.arabalarA8Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA8Ui.A8_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA8Ui.A8_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a8 = "DELETE FROM A8 WHERE Lot = ?"
                self.islem.execute(sorgu_a8, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA8Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a8()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA8Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a9(self):
        self.arabalarA9Ui.A9_tw.clear()
        self.arabalarA9Ui.A9_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA9Ui.A9_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A9"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA9Ui.A9_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a9(self):
        sil_mesaj = QMessageBox.question(self.arabalarA9Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA9Ui.A9_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA9Ui.A9_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a9 = "DELETE FROM A9 WHERE Lot = ?"
                self.islem.execute(sorgu_a9, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA9Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a9()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA9Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a10(self):
        self.arabalarA10Ui.A10_tw.clear()
        self.arabalarA10Ui.A10_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA10Ui.A10_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A10"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA10Ui.A10_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a10(self):
        sil_mesaj = QMessageBox.question(self.arabalarA10Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA10Ui.A10_tw.currentRow()
            if secilen_satir == -1:
                QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
                return

            silinecek_lot = self.arabalarA10Ui.A10_tw.item(secilen_satir, 0).text()
        
            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a10 = "DELETE FROM A10 WHERE Lot = ?"
                self.islem.execute(sorgu_a10, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA10Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a10()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA10Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a11(self):
        self.arabalarA11Ui.A11_tw.clear()
        self.arabalarA11Ui.A11_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA11Ui.A11_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A11"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA11Ui.A11_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a11(self):
        sil_mesaj = QMessageBox.question(self.arabalarA11Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA11Ui.A11_tw.currentRow()
           if secilen_satir == -1:
               QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
               return

           silinecek_lot = self.arabalarA11Ui.A11_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a11 = "DELETE FROM A11 WHERE Lot = ?"
               self.islem.execute(sorgu_a11, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA11Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a11()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA11Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a12(self):
        self.arabalarA12Ui.A12_tw.clear()
        self.arabalarA12Ui.A12_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA12Ui.A12_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A12"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA12Ui.A12_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a12(self):
        sil_mesaj = QMessageBox.question(self.arabalarA12Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA12Ui.A12_tw.currentRow()
           if secilen_satir == -1:
               QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
               return

           silinecek_lot = self.arabalarA12Ui.A12_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a12 = "DELETE FROM A12 WHERE Lot = ?"
               self.islem.execute(sorgu_a12, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA12Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a12()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA12Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a13(self):
        self.arabalarA13Ui.A13_tw.clear()
        self.arabalarA13Ui.A13_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA13Ui.A13_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A13"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA13Ui.A13_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a13(self):
        sil_mesaj = QMessageBox.question(self.arabalarA13Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA13Ui.A13_tw.currentRow()
           if secilen_satir == -1:
               QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
               return

           silinecek_lot = self.arabalarA13Ui.A13_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a13 = "DELETE FROM A13 WHERE Lot = ?"
               self.islem.execute(sorgu_a13, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA13Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a13()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA13Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a14(self):
        self.arabalarA14Ui.A14_tw.clear()
        self.arabalarA14Ui.A14_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA14Ui.A14_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A14"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA14Ui.A14_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a14(self):
        sil_mesaj = QMessageBox.question(self.arabalarA14Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA14Ui.A14_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA14Ui.A14_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a14 = "DELETE FROM A14 WHERE Lot = ?"
               self.islem.execute(sorgu_a14, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA14Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a14()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA14Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a15(self):
        self.arabalarA15Ui.A15_tw.clear()
        self.arabalarA15Ui.A15_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA15Ui.A15_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A15"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA15Ui.A15_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a15(self):
        sil_mesaj = QMessageBox.question(self.arabalarA15Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA15Ui.A15_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA15Ui.A15_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a15 = "DELETE FROM A15 WHERE Lot = ?"
               self.islem.execute(sorgu_a15, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA15Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a15()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA15Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a16(self):
        self.arabalarA16Ui.A16_tw.clear()
        self.arabalarA16Ui.A16_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA16Ui.A16_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A16"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA16Ui.A16_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a16(self):
        sil_mesaj = QMessageBox.question(self.arabalarA16Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA16Ui.A16_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA16Ui.A16_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a16 = "DELETE FROM A16 WHERE Lot = ?"
               self.islem.execute(sorgu_a16, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA16Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a16()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA16Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a17(self):
        self.arabalarA17Ui.A17_tw.clear()
        self.arabalarA17Ui.A17_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA17Ui.A17_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A17"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA17Ui.A17_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a17(self):
        sil_mesaj = QMessageBox.question(self.arabalarA17Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA17Ui.A17_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA17Ui.A17_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a17 = "DELETE FROM A17 WHERE Lot = ?"
               self.islem.execute(sorgu_a17, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA17Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a17()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA17Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a18(self):
        self.arabalarA18Ui.A18_tw.clear()
        self.arabalarA18Ui.A18_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA18Ui.A18_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A18"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA18Ui.A18_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a18(self):
        sil_mesaj = QMessageBox.question(self.arabalarA18Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA18Ui.A18_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA18Ui.A18_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a18 = "DELETE FROM A18 WHERE Lot = ?"
               self.islem.execute(sorgu_a18, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA18Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a18()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA18Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a19(self):
        self.arabalarA19Ui.A19_tw.clear()
        self.arabalarA19Ui.A19_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA19Ui.A19_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A19"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA19Ui.A19_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a19(self):
        sil_mesaj = QMessageBox.question(self.arabalarA19Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA19Ui.A19_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA19Ui.A19_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a19 = "DELETE FROM A19 WHERE Lot = ?"
               self.islem.execute(sorgu_a19, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA19Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a19()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA19Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a20(self):
        self.arabalarA20Ui.A20_tw.clear()
        self.arabalarA20Ui.A20_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA20Ui.A20_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A20"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA20Ui.A20_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a20(self):
        sil_mesaj = QMessageBox.question(self.arabalarA20Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA20Ui.A20_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA20Ui.A20_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a20 = "DELETE FROM A20 WHERE Lot = ?"
               self.islem.execute(sorgu_a20, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA20Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a20()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA20Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a21(self):
        self.arabalarA21Ui.A21_tw.clear()
        self.arabalarA21Ui.A21_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA21Ui.A21_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A21"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA21Ui.A21_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a21(self):
        sil_mesaj = QMessageBox.question(self.arabalarA21Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA21Ui.A21_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA21Ui.A21_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a21 = "DELETE FROM A21 WHERE Lot = ?"
               self.islem.execute(sorgu_a21, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA21Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a21()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA21Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a22(self):
        self.arabalarA22Ui.A22_tw.clear()
        self.arabalarA22Ui.A22_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA22Ui.A22_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A22"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA22Ui.A22_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a22(self):
        sil_mesaj = QMessageBox.question(self.arabalarA22Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA22Ui.A22_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA22Ui.A22_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a22 = "DELETE FROM A22 WHERE Lot = ?"
               self.islem.execute(sorgu_a22, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA22Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a22()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA22Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a23(self):
        self.arabalarA23Ui.A23_tw.clear()
        self.arabalarA23Ui.A23_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA23Ui.A23_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A23"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA23Ui.A23_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a23(self):
        sil_mesaj = QMessageBox.question(self.arabalarA23Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA23Ui.A23_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA23Ui.A23_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a23 = "DELETE FROM A23 WHERE Lot = ?"
               self.islem.execute(sorgu_a23, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA23Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a23()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA23Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a24(self):
        self.arabalarA24Ui.A24_tw.clear()
        self.arabalarA24Ui.A24_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA24Ui.A24_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A24"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA24Ui.A24_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a24(self):
        sil_mesaj = QMessageBox.question(self.arabalarA24Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA24Ui.A24_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA24Ui.A24_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a24 = "DELETE FROM A24 WHERE Lot = ?"
               self.islem.execute(sorgu_a24, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA24Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a24()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA24Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a25(self):
        self.arabalarA25Ui.A25_tw.clear()
        self.arabalarA25Ui.A25_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA25Ui.A25_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A25"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA25Ui.A25_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a25(self):
        sil_mesaj = QMessageBox.question(self.arabalarA25Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA25Ui.A25_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA25Ui.A25_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a25 = "DELETE FROM A25 WHERE Lot = ?"
               self.islem.execute(sorgu_a25, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA25Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a25()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA25Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a26(self):
        self.arabalarA26Ui.A26_tw.clear()
        self.arabalarA26Ui.A26_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA26Ui.A26_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A26"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA26Ui.A26_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a26(self):
        sil_mesaj = QMessageBox.question(self.arabalarA26Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA26Ui.A26_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA26Ui.A26_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a26 = "DELETE FROM A26 WHERE Lot = ?"
               self.islem.execute(sorgu_a26, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA26Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a26()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA26Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a27(self):
        self.arabalarA27Ui.A27_tw.clear()
        self.arabalarA27Ui.A27_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA27Ui.A27_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A27"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA27Ui.A27_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a27(self):
        sil_mesaj = QMessageBox.question(self.arabalarA27Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA27Ui.A27_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA27Ui.A27_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a27 = "DELETE FROM A27 WHERE Lot = ?"
               self.islem.execute(sorgu_a27, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA27Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a27()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA27Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a28(self):
        self.arabalarA28Ui.A28_tw.clear()
        self.arabalarA28Ui.A28_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA28Ui.A28_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A28"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA28Ui.A28_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a28(self):
        sil_mesaj = QMessageBox.question(self.arabalarA28Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA28Ui.A28_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA28Ui.A28_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a28 = "DELETE FROM A28 WHERE Lot = ?"
               self.islem.execute(sorgu_a28, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA28Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a28()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA28Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a29(self):
        self.arabalarA29Ui.A29_tw.clear()
        self.arabalarA29Ui.A29_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA29Ui.A29_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A29"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA29Ui.A29_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a29(self):
        sil_mesaj = QMessageBox.question(self.arabalarA29Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA29Ui.A29_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA29Ui.A29_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a29 = "DELETE FROM A29 WHERE Lot = ?"
               self.islem.execute(sorgu_a29, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA29Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a29()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA29Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a30(self):
        self.arabalarA30Ui.A30_tw.clear()
        self.arabalarA30Ui.A30_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA30Ui.A30_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A30"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA30Ui.A30_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a30(self):
        sil_mesaj = QMessageBox.question(self.arabalarA30Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA30Ui.A30_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA30Ui.A30_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a30 = "DELETE FROM A30 WHERE Lot = ?"
               self.islem.execute(sorgu_a30, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA30Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a30()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA30Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a31(self):
        self.arabalarA31Ui.A31_tw.clear()
        self.arabalarA31Ui.A31_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA31Ui.A31_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A31"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA31Ui.A31_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a31(self):
        sil_mesaj = QMessageBox.question(self.arabalarA31Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA31Ui.A31_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA31Ui.A31_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a31 = "DELETE FROM A31 WHERE Lot = ?"
               self.islem.execute(sorgu_a31, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA31Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a31()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA31Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a32(self):
        self.arabalarA32Ui.A32_tw.clear()
        self.arabalarA32Ui.A32_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA32Ui.A32_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A32"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA32Ui.A32_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a32(self):
        sil_mesaj = QMessageBox.question(self.arabalarA32Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA32Ui.A32_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA32Ui.A32_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a32 = "DELETE FROM A32 WHERE Lot = ?"
               self.islem.execute(sorgu_a32, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA32Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a32()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA32Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a33(self):
        self.arabalarA33Ui.A33_tw.clear()
        self.arabalarA33Ui.A33_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA33Ui.A33_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A33"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA33Ui.A33_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a33(self):
        sil_mesaj = QMessageBox.question(self.arabalarA33Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA33Ui.A33_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA33Ui.A33_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a33 = "DELETE FROM A33 WHERE Lot = ?"
               self.islem.execute(sorgu_a33, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA33Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a33()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA33Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a34(self):
        self.arabalarA34Ui.A34_tw.clear()
        self.arabalarA34Ui.A34_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA34Ui.A34_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A34"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA34Ui.A34_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a34(self):
        sil_mesaj = QMessageBox.question(self.arabalarA34Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA34Ui.A34_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA34Ui.A34_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a34 = "DELETE FROM A34 WHERE Lot = ?"
               self.islem.execute(sorgu_a34, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA34Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a34()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA34Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a35(self):
        self.arabalarA35Ui.A35_tw.clear()
        self.arabalarA35Ui.A35_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA35Ui.A35_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A35"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA35Ui.A35_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a35(self):
        sil_mesaj = QMessageBox.question(self.arabalarA35Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA35Ui.A35_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA35Ui.A35_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a35 = "DELETE FROM A35 WHERE Lot = ?"
               self.islem.execute(sorgu_a35, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA35Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a35()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA35Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a36(self):
        self.arabalarA36Ui.A36_tw.clear()
        self.arabalarA36Ui.A36_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA36Ui.A36_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A36"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA36Ui.A36_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a36(self):
        sil_mesaj = QMessageBox.question(self.arabalarA36Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA36Ui.A36_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA36Ui.A36_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a36 = "DELETE FROM A36 WHERE Lot = ?"
               self.islem.execute(sorgu_a36, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA36Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a36()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA36Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a37(self):
        self.arabalarA37Ui.A37_tw.clear()
        self.arabalarA37Ui.A37_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA37Ui.A37_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A37"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA37Ui.A37_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a37(self):
        sil_mesaj = QMessageBox.question(self.arabalarA37Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA37Ui.A37_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA37Ui.A37_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a37 = "DELETE FROM A37 WHERE Lot = ?"
               self.islem.execute(sorgu_a37, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA37Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a37()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA37Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a38(self):
        self.arabalarA38Ui.A38_tw.clear()
        self.arabalarA38Ui.A38_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA38Ui.A38_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A38"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA38Ui.A38_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a38(self):
        sil_mesaj = QMessageBox.question(self.arabalarA38Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA38Ui.A38_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA38Ui.A38_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a38 = "DELETE FROM A38 WHERE Lot = ?"
               self.islem.execute(sorgu_a38, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA38Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a38()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA38Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a39(self):
        self.arabalarA39Ui.A39_tw.clear()
        self.arabalarA39Ui.A39_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA39Ui.A39_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A39"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA39Ui.A39_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a39(self):
        sil_mesaj = QMessageBox.question(self.arabalarA39Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA39Ui.A39_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA39Ui.A39_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a39 = "DELETE FROM A39 WHERE Lot = ?"
               self.islem.execute(sorgu_a39, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA39Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a39()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA39Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a40(self):
        self.arabalarA40Ui.A40_tw.clear()
        self.arabalarA40Ui.A40_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA40Ui.A40_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A40"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA40Ui.A40_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a40(self):
        sil_mesaj = QMessageBox.question(self.arabalarA40Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA40Ui.A40_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA40Ui.A40_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a40 = "DELETE FROM A40 WHERE Lot = ?"
               self.islem.execute(sorgu_a40, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA40Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a40()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA40Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a41(self):
        self.arabalarA41Ui.A41_tw.clear()
        self.arabalarA41Ui.A41_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA41Ui.A41_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A41"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA41Ui.A41_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a41(self):
        sil_mesaj = QMessageBox.question(self.arabalarA41Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA41Ui.A41_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA41Ui.A41_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a41 = "DELETE FROM A41 WHERE Lot = ?"
               self.islem.execute(sorgu_a41, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA41Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a41()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA41Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a42(self):
        self.arabalarA42Ui.A42_tw.clear()
        self.arabalarA42Ui.A42_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA42Ui.A42_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A42"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA42Ui.A42_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a42(self):
        sil_mesaj = QMessageBox.question(self.arabalarA42Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA42Ui.A42_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA42Ui.A42_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a42 = "DELETE FROM A42 WHERE Lot = ?"
               self.islem.execute(sorgu_a42, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA42Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a42()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA42Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a43(self):
        self.arabalarA43Ui.A43_tw.clear()
        self.arabalarA43Ui.A43_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA43Ui.A43_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A43"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA43Ui.A43_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a43(self):
        sil_mesaj = QMessageBox.question(self.arabalarA43Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA43Ui.A43_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA43Ui.A43_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a43 = "DELETE FROM A43 WHERE Lot = ?"
               self.islem.execute(sorgu_a43, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA43Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a43()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA43Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a44(self):
        self.arabalarA44Ui.A44_tw.clear()
        self.arabalarA44Ui.A44_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA44Ui.A44_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A44"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA44Ui.A44_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a44(self):
        sil_mesaj = QMessageBox.question(self.arabalarA44Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA44Ui.A44_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA44Ui.A44_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a44 = "DELETE FROM A44 WHERE Lot = ?"
               self.islem.execute(sorgu_a44, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA44Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a44()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA44Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a45(self):
        self.arabalarA45Ui.A45_tw.clear()
        self.arabalarA45Ui.A45_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA45Ui.A45_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A45"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA45Ui.A45_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a45(self):
        sil_mesaj = QMessageBox.question(self.arabalarA45Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA45Ui.A45_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA45Ui.A45_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a45 = "DELETE FROM A45 WHERE Lot = ?"
               self.islem.execute(sorgu_a45, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA45Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a45()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA45Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a46(self):
        self.arabalarA46Ui.A46_tw.clear()
        self.arabalarA46Ui.A46_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA46Ui.A46_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A46"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA46Ui.A46_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a46(self):
        sil_mesaj = QMessageBox.question(self.arabalarA46Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA46Ui.A46_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA46Ui.A46_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a46 = "DELETE FROM A46 WHERE Lot = ?"
               self.islem.execute(sorgu_a46, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA46Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a46()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA46Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a47(self):
        self.arabalarA47Ui.A47_tw.clear()
        self.arabalarA47Ui.A47_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA47Ui.A47_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A47"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA47Ui.A47_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a47(self):
        sil_mesaj = QMessageBox.question(self.arabalarA47Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA47Ui.A47_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA47Ui.A47_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a47 = "DELETE FROM A47 WHERE Lot = ?"
               self.islem.execute(sorgu_a47, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA47Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a47()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA47Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    def kayit_listele_a48(self):
        self.arabalarA48Ui.A48_tw.clear()
        self.arabalarA48Ui.A48_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA48Ui.A48_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A48"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA48Ui.A48_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a48(self):
        sil_mesaj = QMessageBox.question(self.arabalarA48Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA48Ui.A48_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA48Ui.A48_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a48 = "DELETE FROM A48 WHERE Lot = ?"
               self.islem.execute(sorgu_a48, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA48Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a48()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA48Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    def kayit_listele_a49(self):
        self.arabalarA49Ui.A49_tw.clear()
        self.arabalarA49Ui.A49_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA49Ui.A49_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A49"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA49Ui.A49_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a49(self):
        sil_mesaj = QMessageBox.question(self.arabalarA49Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA49Ui.A49_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA49Ui.A49_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a49 = "DELETE FROM A49 WHERE Lot = ?"
               self.islem.execute(sorgu_a49, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA49Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a49()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA49Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    def kayit_listele_a50(self):
        self.arabalarA50Ui.A50_tw.clear()
        self.arabalarA50Ui.A50_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA50Ui.A50_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A50"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA50Ui.A50_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a50(self):
        sil_mesaj = QMessageBox.question(self.arabalarA50Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA50Ui.A50_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA50Ui.A50_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a50 = "DELETE FROM A50 WHERE Lot = ?"
               self.islem.execute(sorgu_a50, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA50Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a50()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA50Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a51(self):
        self.arabalarA51Ui.A51_tw.clear()
        self.arabalarA51Ui.A51_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA51Ui.A51_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A51"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA51Ui.A51_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a51(self):
        sil_mesaj = QMessageBox.question(self.arabalarA51Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA51Ui.A51_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA51Ui.A51_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a51 = "DELETE FROM A51 WHERE Lot = ?"
               self.islem.execute(sorgu_a51, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA51Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a51()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA51Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    def kayit_listele_a52(self):
        self.arabalarA52Ui.A52_tw.clear()
        self.arabalarA52Ui.A52_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA52Ui.A52_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A52"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA52Ui.A52_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a52(self):
        sil_mesaj = QMessageBox.question(self.arabalarA52Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA52Ui.A52_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA52Ui.A52_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a52 = "DELETE FROM A52 WHERE Lot = ?"
               self.islem.execute(sorgu_a52, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA52Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a52()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA52Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a53(self):
        self.arabalarA53Ui.A53_tw.clear()
        self.arabalarA53Ui.A53_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA53Ui.A53_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A53"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA53Ui.A53_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a53(self):
        sil_mesaj = QMessageBox.question(self.arabalarA53Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA53Ui.A53_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA53Ui.A53_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a53 = "DELETE FROM A53 WHERE Lot = ?"
               self.islem.execute(sorgu_a53, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA53Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a53()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA53Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a54(self):
        self.arabalarA54Ui.A54_tw.clear()
        self.arabalarA54Ui.A54_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA54Ui.A54_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A54"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA54Ui.A54_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a54(self):
        sil_mesaj = QMessageBox.question(self.arabalarA54Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA54Ui.A54_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA54Ui.A54_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a54 = "DELETE FROM A54 WHERE Lot = ?"
               self.islem.execute(sorgu_a54, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA54Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a54()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA54Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
               
    def kayit_listele_a55(self):
        self.arabalarA55Ui.A55_tw.clear()
        self.arabalarA55Ui.A55_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA55Ui.A55_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A55"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA55Ui.A55_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a55(self):
        sil_mesaj = QMessageBox.question(self.arabalarA55Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA55Ui.A55_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA55Ui.A55_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a55 = "DELETE FROM A55 WHERE Lot = ?"
               self.islem.execute(sorgu_a55, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA55Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a55()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA55Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a56(self):
        self.arabalarA56Ui.A56_tw.clear()
        self.arabalarA56Ui.A56_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA56Ui.A56_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A56"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA56Ui.A56_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a56(self):
        sil_mesaj = QMessageBox.question(self.arabalarA56Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA56Ui.A56_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA56Ui.A56_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a56 = "DELETE FROM A56 WHERE Lot = ?"
               self.islem.execute(sorgu_a56, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA56Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a56()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA56Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a57(self):
        self.arabalarA57Ui.A57_tw.clear()
        self.arabalarA57Ui.A57_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA57Ui.A57_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A57"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA57Ui.A57_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a57(self):
        sil_mesaj = QMessageBox.question(self.arabalarA57Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA57Ui.A57_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA57Ui.A57_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a57 = "DELETE FROM A57 WHERE Lot = ?"
               self.islem.execute(sorgu_a57, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA57Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a57()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA57Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a58(self):
        self.arabalarA58Ui.A58_tw.clear()
        self.arabalarA58Ui.A58_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA58Ui.A58_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A58"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA58Ui.A58_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a58(self):
        sil_mesaj = QMessageBox.question(self.arabalarA58Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA58Ui.A58_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA58Ui.A58_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a58 = "DELETE FROM A58 WHERE Lot = ?"
               self.islem.execute(sorgu_a58, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA58Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a58()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA58Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a59(self):
        self.arabalarA59Ui.A59_tw.clear()
        self.arabalarA59Ui.A59_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA59Ui.A59_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A59"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA59Ui.A59_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a59(self):
        sil_mesaj = QMessageBox.question(self.arabalarA59Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA59Ui.A59_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA59Ui.A59_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a59 = "DELETE FROM A59 WHERE Lot = ?"
               self.islem.execute(sorgu_a59, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA59Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a59()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA59Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a60(self):
        self.arabalarA60Ui.A60_tw.clear()
        self.arabalarA60Ui.A60_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA60Ui.A60_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A60"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA60Ui.A60_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a60(self):
        sil_mesaj = QMessageBox.question(self.arabalarA60Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA60Ui.A60_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA60Ui.A60_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a60 = "DELETE FROM A60 WHERE Lot = ?"
               self.islem.execute(sorgu_a60, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA60Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a60()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA60Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a61(self):
        self.arabalarA61Ui.A61_tw.clear()
        self.arabalarA61Ui.A61_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA61Ui.A61_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A61"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA61Ui.A61_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a61(self):
        sil_mesaj = QMessageBox.question(self.arabalarA61Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA61Ui.A61_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA61Ui.A61_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a61 = "DELETE FROM A61 WHERE Lot = ?"
               self.islem.execute(sorgu_a61, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA61Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a61()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA61Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a62(self):
        self.arabalarA62Ui.A62_tw.clear()
        self.arabalarA62Ui.A62_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA62Ui.A62_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A62"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA62Ui.A62_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a62(self):
        sil_mesaj = QMessageBox.question(self.arabalarA62Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA62Ui.A62_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA62Ui.A62_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a62 = "DELETE FROM A62 WHERE Lot = ?"
               self.islem.execute(sorgu_a62, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA62Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a62()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA62Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a63(self):
        self.arabalarA63Ui.A63_tw.clear()
        self.arabalarA63Ui.A63_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA63Ui.A63_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A63"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA63Ui.A63_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a63(self):
        sil_mesaj = QMessageBox.question(self.arabalarA63Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA63Ui.A63_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA63Ui.A63_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a63 = "DELETE FROM A63 WHERE Lot = ?"
               self.islem.execute(sorgu_a63, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA63Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a63()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA63Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a64(self):
        self.arabalarA64Ui.A64_tw.clear()
        self.arabalarA64Ui.A64_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA64Ui.A64_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A64"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA64Ui.A64_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a64(self):
        sil_mesaj = QMessageBox.question(self.arabalarA64Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA64Ui.A64_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA64Ui.A64_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a64 = "DELETE FROM A64 WHERE Lot = ?"
               self.islem.execute(sorgu_a64, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA64Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a64()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA64Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
        
    def kayit_listele_a65(self):
        self.arabalarA65Ui.A65_tw.clear()
        self.arabalarA65Ui.A65_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA65Ui.A65_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A65"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA65Ui.A65_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a65(self):
        sil_mesaj = QMessageBox.question(self.arabalarA65Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA65Ui.A65_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA65Ui.A65_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a65 = "DELETE FROM A65 WHERE Lot = ?"
               self.islem.execute(sorgu_a65, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA65Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a65()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA65Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a66(self):
        self.arabalarA66Ui.A66_tw.clear()
        self.arabalarA66Ui.A66_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA66Ui.A66_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A66"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA66Ui.A66_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a66(self):
        sil_mesaj = QMessageBox.question(self.arabalarA66Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA66Ui.A66_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA66Ui.A66_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a66 = "DELETE FROM A66 WHERE Lot = ?"
               self.islem.execute(sorgu_a66, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA66Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a66()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA66Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a67(self):
        self.arabalarA67Ui.A67_tw.clear()
        self.arabalarA67Ui.A67_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA67Ui.A67_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A67"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA67Ui.A67_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a67(self):
        sil_mesaj = QMessageBox.question(self.arabalarA67Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA67Ui.A67_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA67Ui.A67_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a67 = "DELETE FROM A67 WHERE Lot = ?"
               self.islem.execute(sorgu_a67, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA67Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a67()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA67Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
        
    def kayit_listele_a68(self):
        self.arabalarA68Ui.A68_tw.clear()
        self.arabalarA68Ui.A68_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA68Ui.A68_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A68"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA68Ui.A68_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a68(self):
        sil_mesaj = QMessageBox.question(self.arabalarA68Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA68Ui.A68_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA68Ui.A68_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a68 = "DELETE FROM A68 WHERE Lot = ?"
               self.islem.execute(sorgu_a68, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA68Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a68()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA68Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a69(self):
        self.arabalarA69Ui.A69_tw.clear()
        self.arabalarA69Ui.A69_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA69Ui.A69_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A69"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA69Ui.A69_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a69(self):
        sil_mesaj = QMessageBox.question(self.arabalarA69Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA69Ui.A69_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA69Ui.A69_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a69 = "DELETE FROM A69 WHERE Lot = ?"
               self.islem.execute(sorgu_a69, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA69Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a69()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA69Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a70(self):
        self.arabalarA70Ui.A70_tw.clear()
        self.arabalarA70Ui.A70_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA70Ui.A70_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A70"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA70Ui.A70_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a70(self):
        sil_mesaj = QMessageBox.question(self.arabalarA70Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA70Ui.A70_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA70Ui.A70_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a70 = "DELETE FROM A70 WHERE Lot = ?"
               self.islem.execute(sorgu_a70, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA70Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a70()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA70Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a71(self):
        self.arabalarA71Ui.A71_tw.clear()
        self.arabalarA71Ui.A71_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA71Ui.A71_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A71"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA71Ui.A71_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a71(self):
        sil_mesaj = QMessageBox.question(self.arabalarA71Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA71Ui.A71_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA71Ui.A71_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a71 = "DELETE FROM A71 WHERE Lot = ?"
               self.islem.execute(sorgu_a71, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA71Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a71()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA71Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a72(self):
        self.arabalarA72Ui.A72_tw.clear()
        self.arabalarA72Ui.A72_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA72Ui.A72_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A72"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA72Ui.A72_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a72(self):
        sil_mesaj = QMessageBox.question(self.arabalarA72Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA72Ui.A72_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA72Ui.A72_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a72 = "DELETE FROM A72 WHERE Lot = ?"
               self.islem.execute(sorgu_a72, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA72Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a72()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA72Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a73(self):
        self.arabalarA73Ui.A73_tw.clear()
        self.arabalarA73Ui.A73_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA73Ui.A73_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A73"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA73Ui.A73_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a73(self):
        sil_mesaj = QMessageBox.question(self.arabalarA73Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA73Ui.A73_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA73Ui.A73_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a73 = "DELETE FROM A73 WHERE Lot = ?"
               self.islem.execute(sorgu_a73, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA73Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a73()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA73Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a74(self):
        self.arabalarA74Ui.A74_tw.clear()
        self.arabalarA74Ui.A74_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA74Ui.A74_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A74"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA74Ui.A74_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a74(self):
        sil_mesaj = QMessageBox.question(self.arabalarA74Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA74Ui.A74_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA74Ui.A74_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a74 = "DELETE FROM A74 WHERE Lot = ?"
               self.islem.execute(sorgu_a74, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA74Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a74()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA74Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a75(self):
        self.arabalarA75Ui.A75_tw.clear()
        self.arabalarA75Ui.A75_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA75Ui.A75_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A75"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA75Ui.A75_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a75(self):
        sil_mesaj = QMessageBox.question(self.arabalarA75Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA75Ui.A75_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA75Ui.A75_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a75 = "DELETE FROM A75 WHERE Lot = ?"
               self.islem.execute(sorgu_a75, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA75Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a75()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA75Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    
    def kayit_listele_a76(self):
        self.arabalarA76Ui.A76_tw.clear()
        self.arabalarA76Ui.A76_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA76Ui.A76_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A76"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA76Ui.A76_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a76(self):
        sil_mesaj = QMessageBox.question(self.arabalarA76Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA76Ui.A76_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA76Ui.A76_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a76 = "DELETE FROM A76 WHERE Lot = ?"
               self.islem.execute(sorgu_a76, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA76Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a76()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA76Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a77(self):
        self.arabalarA77Ui.A77_tw.clear()
        self.arabalarA77Ui.A77_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA77Ui.A77_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A77"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA77Ui.A77_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a77(self):
        sil_mesaj = QMessageBox.question(self.arabalarA77Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA77Ui.A77_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA77Ui.A77_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a77 = "DELETE FROM A77 WHERE Lot = ?"
               self.islem.execute(sorgu_a77, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA77Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a77()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA77Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a78(self):
        self.arabalarA78Ui.A78_tw.clear()
        self.arabalarA78Ui.A78_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA78Ui.A78_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A78"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA78Ui.A78_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a78(self):
        sil_mesaj = QMessageBox.question(self.arabalarA78Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA78Ui.A78_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA78Ui.A78_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a78 = "DELETE FROM A78 WHERE Lot = ?"
               self.islem.execute(sorgu_a78, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA78Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a78()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA78Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a79(self):
        self.arabalarA79Ui.A79_tw.clear()
        self.arabalarA79Ui.A79_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA79Ui.A79_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A79"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA79Ui.A79_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a79(self):
        sil_mesaj = QMessageBox.question(self.arabalarA79Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
            secilen_satir = self.arabalarA79Ui.A79_tw.currentRow()
            if secilen_satir == -1:
               QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
               return

            silinecek_lot = self.arabalarA79Ui.A79_tw.item(secilen_satir, 0).text()

            try:
                self.baglanti.execute("BEGIN TRANSACTION")

                sorgu_a79 = "DELETE FROM A79 WHERE Lot = ?"
                self.islem.execute(sorgu_a79, (silinecek_lot,))

                sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
                self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

                self.baglanti.commit()
                QMessageBox.information(self.arabalarA79Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
                self.kayit_listele_a79()

            except Exception as error:
                self.baglanti.rollback()
                self.arabalarA79Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    def kayit_listele_a80(self):
        self.arabalarA80Ui.A80_tw.clear()
        self.arabalarA80Ui.A80_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA80Ui.A80_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A80"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA80Ui.A80_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a80(self):
        sil_mesaj = QMessageBox.question(self.arabalarA80Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA80Ui.A80_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA80Ui.A80_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a80 = "DELETE FROM A80 WHERE Lot = ?"
               self.islem.execute(sorgu_a80, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA80Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a80()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA80Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a81(self):
        self.arabalarA81Ui.A81_tw.clear()
        self.arabalarA81Ui.A81_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA81Ui.A81_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A81"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA81Ui.A81_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a81(self):
        sil_mesaj = QMessageBox.question(self.arabalarA81Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA81Ui.A81_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA81Ui.A81_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a81 = "DELETE FROM A81 WHERE Lot = ?"
               self.islem.execute(sorgu_a81, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA81Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a81()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA81Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a82(self):
        self.arabalarA82Ui.A82_tw.clear()
        self.arabalarA82Ui.A82_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA82Ui.A82_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A82"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA82Ui.A82_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a82(self):
        sil_mesaj = QMessageBox.question(self.arabalarA82Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA82Ui.A82_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA82Ui.A82_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a82 = "DELETE FROM A82 WHERE Lot = ?"
               self.islem.execute(sorgu_a82, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA82Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a82()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA82Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a83(self):
        self.arabalarA83Ui.A83_tw.clear()
        self.arabalarA83Ui.A83_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA83Ui.A83_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A83"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA83Ui.A83_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a83(self):
        sil_mesaj = QMessageBox.question(self.arabalarA83Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA83Ui.A83_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA83Ui.A83_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a83 = "DELETE FROM A83 WHERE Lot = ?"
               self.islem.execute(sorgu_a83, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA83Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a83()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA83Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a84(self):
        self.arabalarA84Ui.A84_tw.clear()
        self.arabalarA84Ui.A84_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA84Ui.A84_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A84"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA84Ui.A84_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a84(self):
        sil_mesaj = QMessageBox.question(self.arabalarA84Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA84Ui.A84_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA84Ui.A84_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a84 = "DELETE FROM A84 WHERE Lot = ?"
               self.islem.execute(sorgu_a84, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA84Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a84()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA84Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
              
    def kayit_listele_a85(self):
        self.arabalarA85Ui.A85_tw.clear()
        self.arabalarA85Ui.A85_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA85Ui.A85_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A85"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA85Ui.A85_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a85(self):
        sil_mesaj = QMessageBox.question(self.arabalarA85Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA85Ui.A85_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA85Ui.A85_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a85 = "DELETE FROM A85 WHERE Lot = ?"
               self.islem.execute(sorgu_a85, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA85Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a85()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA85Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a86(self):
        self.arabalarA86Ui.A86_tw.clear()
        self.arabalarA86Ui.A86_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA86Ui.A86_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A86"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA86Ui.A86_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a86(self):
        sil_mesaj = QMessageBox.question(self.arabalarA86Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA86Ui.A86_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA86Ui.A86_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a86 = "DELETE FROM A86 WHERE Lot = ?"
               self.islem.execute(sorgu_a86, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA86Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a86()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA86Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
               
    def kayit_listele_a87(self):
        self.arabalarA87Ui.A87_tw.clear()
        self.arabalarA87Ui.A87_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA87Ui.A87_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A87"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA87Ui.A87_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a87(self):
        sil_mesaj = QMessageBox.question(self.arabalarA87Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA87Ui.A87_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA87Ui.A87_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a87 = "DELETE FROM A87 WHERE Lot = ?"
               self.islem.execute(sorgu_a87, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA87Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a87()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA87Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a88(self):
        self.arabalarA88Ui.A88_tw.clear()
        self.arabalarA88Ui.A88_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA88Ui.A88_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A88"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA88Ui.A88_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a88(self):
        sil_mesaj = QMessageBox.question(self.arabalarA88Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA88Ui.A88_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA88Ui.A88_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a88 = "DELETE FROM A88 WHERE Lot = ?"
               self.islem.execute(sorgu_a88, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA88Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a88()
 
           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA88Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a89(self):
        self.arabalarA89Ui.A89_tw.clear()
        self.arabalarA89Ui.A89_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA89Ui.A89_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A89"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA89Ui.A89_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a89(self):
        sil_mesaj = QMessageBox.question(self.arabalarA89Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA89Ui.A89_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA89Ui.A89_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a89 = "DELETE FROM A89 WHERE Lot = ?"
               self.islem.execute(sorgu_a89, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA89Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a89()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA89Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a90(self):
        self.arabalarA90Ui.A90_tw.clear()
        self.arabalarA90Ui.A90_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA90Ui.A90_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A90"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA90Ui.A90_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a90(self):
        sil_mesaj = QMessageBox.question(self.arabalarA90Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA90Ui.A90_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA90Ui.A90_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a90 = "DELETE FROM A90 WHERE Lot = ?"
               self.islem.execute(sorgu_a90, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA90Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a90()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA90Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a91(self):
        self.arabalarA91Ui.A91_tw.clear()
        self.arabalarA91Ui.A91_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA91Ui.A91_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A91"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA91Ui.A91_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a91(self):
        sil_mesaj = QMessageBox.question(self.arabalarA91Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA91Ui.A91_tw.currentRow()
           if secilen_satir == -1:
               QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
               return

           silinecek_lot = self.arabalarA91Ui.A91_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a91 = "DELETE FROM A91 WHERE Lot = ?"
               self.islem.execute(sorgu_a91, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA91Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a91()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA91Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a92(self):
        self.arabalarA92Ui.A92_tw.clear()
        self.arabalarA92Ui.A92_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA92Ui.A92_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A92"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA92Ui.A92_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a92(self):
        sil_mesaj = QMessageBox.question(self.arabalarA92Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA92Ui.A92_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA92Ui.A92_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a92 = "DELETE FROM A92 WHERE Lot = ?"
               self.islem.execute(sorgu_a92, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA92Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a92()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA92Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a93(self):
        self.arabalarA93Ui.A93_tw.clear()
        self.arabalarA93Ui.A93_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA93Ui.A93_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A93"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA93Ui.A93_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a93(self):
        sil_mesaj = QMessageBox.question(self.arabalarA93Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA93Ui.A93_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA93Ui.A93_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a93 = "DELETE FROM A93 WHERE Lot = ?"
               self.islem.execute(sorgu_a93, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA93Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a93()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA93Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a94(self):
        self.arabalarA94Ui.A94_tw.clear()
        self.arabalarA94Ui.A94_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA94Ui.A94_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A94"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA94Ui.A94_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a94(self):
        sil_mesaj = QMessageBox.question(self.arabalarA94Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA94Ui.A94_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA94Ui.A94_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a94 = "DELETE FROM A94 WHERE Lot = ?"
               self.islem.execute(sorgu_a94, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA94Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a94()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA94Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a95(self):
        self.arabalarA95Ui.A95_tw.clear()
        self.arabalarA95Ui.A95_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA95Ui.A95_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A95"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA95Ui.A95_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a95(self):
        sil_mesaj = QMessageBox.question(self.arabalarA95Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA95Ui.A95_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA95Ui.A95_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a95 = "DELETE FROM A95 WHERE Lot = ?"
               self.islem.execute(sorgu_a95, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA95Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a95()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA95Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a96(self):
        self.arabalarA96Ui.A96_tw.clear()
        self.arabalarA96Ui.A96_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA96Ui.A96_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A96"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA96Ui.A96_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a96(self):
        sil_mesaj = QMessageBox.question(self.arabalarA96Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA96Ui.A96_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA96Ui.A96_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a96 = "DELETE FROM A96 WHERE Lot = ?"
               self.islem.execute(sorgu_a96, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA96Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a96()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA96Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a97(self):
        self.arabalarA97Ui.A97_tw.clear()
        self.arabalarA97Ui.A97_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA97Ui.A97_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A97"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA97Ui.A97_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a97(self):
        sil_mesaj = QMessageBox.question(self.arabalarA97Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA97Ui.A97_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA97Ui.A97_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a97 = "DELETE FROM A97 WHERE Lot = ?"
               self.islem.execute(sorgu_a97, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA97Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a97()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA97Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a98(self):
        self.arabalarA98Ui.A98_tw.clear()
        self.arabalarA98Ui.A98_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA98Ui.A98_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A98"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA98Ui.A98_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a98(self):
        sil_mesaj = QMessageBox.question(self.arabalarA98Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA98Ui.A98_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA98Ui.A98_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a98 = "DELETE FROM A98 WHERE Lot = ?"
               self.islem.execute(sorgu_a98, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA98Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a98()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA98Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a99(self):
        self.arabalarA99Ui.A99_tw.clear()
        self.arabalarA99Ui.A99_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA99Ui.A99_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A99"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA99Ui.A99_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a99(self):
        sil_mesaj = QMessageBox.question(self.arabalarA99Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA99Ui.A99_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA99Ui.A99_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a99 = "DELETE FROM A99 WHERE Lot = ?"
               self.islem.execute(sorgu_a99, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA99Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a99()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA99Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a100(self):
        self.arabalarA100Ui.A100_tw.clear()
        self.arabalarA100Ui.A100_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA100Ui.A100_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A100"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA100Ui.A100_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a100(self):
        sil_mesaj = QMessageBox.question(self.arabalarA100Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA100Ui.A100_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA100Ui.A100_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a100 = "DELETE FROM A100 WHERE Lot = ?"
               self.islem.execute(sorgu_a100, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA100Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a100()
 
           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA100Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a101(self):
        self.arabalarA101Ui.A101_tw.clear()
        self.arabalarA101Ui.A101_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA101Ui.A101_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A101"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA101Ui.A101_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a101(self):
        sil_mesaj = QMessageBox.question(self.arabalarA101Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA101Ui.A101_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA101Ui.A101_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a101 = "DELETE FROM A101 WHERE Lot = ?"
               self.islem.execute(sorgu_a101, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA101Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a101()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA101Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a102(self):
        self.arabalarA102Ui.A102_tw.clear()
        self.arabalarA102Ui.A102_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA102Ui.A102_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A102"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA102Ui.A102_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a102(self):
        sil_mesaj = QMessageBox.question(self.arabalarA102Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA102Ui.A102_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA102Ui.A102_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a102 = "DELETE FROM A102 WHERE Lot = ?"
               self.islem.execute(sorgu_a102, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA102Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a102()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA102Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_a103(self):
        self.arabalarA103Ui.A103_tw.clear()
        self.arabalarA103Ui.A103_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.arabalarA103Ui.A103_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM A103"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.arabalarA103Ui.A103_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_a103(self):
        sil_mesaj = QMessageBox.question(self.arabalarA103Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.arabalarA103Ui.A103_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.arabalarA103Ui.A103_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_a103 = "DELETE FROM A103 WHERE Lot = ?"
               self.islem.execute(sorgu_a103, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.arabalarA103Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_a103()

           except Exception as error:
               self.baglanti.rollback()
               self.arabalarA103Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r1(self):
        self.raflarR1Ui.R1_tw.clear()
        self.raflarR1Ui.R1_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR1Ui.R1_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R1"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR1Ui.R1_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r1(self):
        sil_mesaj = QMessageBox.question(self.raflarR1Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR1Ui.R1_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR1Ui.R1_tw.item(secilen_satir, 0).text()
        
           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r1 = "DELETE FROM R1 WHERE Lot = ?"
               self.islem.execute(sorgu_r1, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR1Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r1()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR1Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r2(self):
        self.raflarR2Ui.R2_tw.clear()
        self.raflarR2Ui.R2_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR2Ui.R2_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R2"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR2Ui.R2_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r2(self):
        sil_mesaj = QMessageBox.question(self.raflarR2Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR2Ui.R2_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR2Ui.R2_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r2 = "DELETE FROM R2 WHERE Lot = ?"
               self.islem.execute(sorgu_r2, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR2Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r2()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR2Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r3(self):
        self.raflarR3Ui.R3_tw.clear()
        self.raflarR3Ui.R3_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR3Ui.R3_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R3"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR3Ui.R3_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r3(self):
        sil_mesaj = QMessageBox.question(self.raflarR3Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR3Ui.R3_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR3Ui.R3_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r3 = "DELETE FROM R3 WHERE Lot = ?"
               self.islem.execute(sorgu_r3, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR3Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r3()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR3Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r4(self):
        self.raflarR4Ui.R4_tw.clear()
        self.raflarR4Ui.R4_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR4Ui.R4_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R4"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR4Ui.R4_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r4(self):
        sil_mesaj = QMessageBox.question(self.raflarR4Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR4Ui.R4_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR4Ui.R4_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r4 = "DELETE FROM R4 WHERE Lot = ?"
               self.islem.execute(sorgu_r4, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR4Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r4()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR4Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
     
    def kayit_listele_r5(self):
        self.raflarR5Ui.R5_tw.clear()
        self.raflarR5Ui.R5_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR5Ui.R5_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R5"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR5Ui.R5_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r5(self):
        sil_mesaj = QMessageBox.question(self.raflarR5Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR5Ui.R5_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR5Ui.R5_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r5 = "DELETE FROM R5 WHERE Lot = ?"
               self.islem.execute(sorgu_r5, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR5Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r5()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR5Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
               
    def kayit_listele_r6(self):
        self.raflarR6Ui.R6_tw.clear()
        self.raflarR6Ui.R6_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR6Ui.R6_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R6"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR6Ui.R6_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r6(self):
        sil_mesaj = QMessageBox.question(self.raflarR6Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR6Ui.R6_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR6Ui.R6_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r6 = "DELETE FROM R6 WHERE Lot = ?"
               self.islem.execute(sorgu_r6, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR6Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r6()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR6Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r7(self):
        self.raflarR7Ui.R7_tw.clear()
        self.raflarR7Ui.R7_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR7Ui.R7_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R7"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR7Ui.R7_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r7(self):
        sil_mesaj = QMessageBox.question(self.raflarR7Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR7Ui.R7_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR7Ui.R7_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r7 = "DELETE FROM R7 WHERE Lot = ?"
               self.islem.execute(sorgu_r7, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR7Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r7()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR7Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r8(self):
        self.raflarR8Ui.R8_tw.clear()
        self.raflarR8Ui.R8_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR8Ui.R8_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R8"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR8Ui.R8_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r8(self):
        sil_mesaj = QMessageBox.question(self.raflarR8Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR8Ui.R8_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR8Ui.R8_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r8 = "DELETE FROM R8 WHERE Lot = ?"
               self.islem.execute(sorgu_r8, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR8Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r8()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR8Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r9(self):
        self.raflarR9Ui.R9_tw.clear()
        self.raflarR9Ui.R9_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR9Ui.R9_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R9"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR9Ui.R9_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r9(self):
        sil_mesaj = QMessageBox.question(self.raflarR9Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR9Ui.R9_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR9Ui.R9_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r9 = "DELETE FROM R9 WHERE Lot = ?"
               self.islem.execute(sorgu_r9, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR9Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r9()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR9Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r10(self):
        self.raflarR10Ui.R10_tw.clear()
        self.raflarR10Ui.R10_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR10Ui.R10_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R10"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR10Ui.R10_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r10(self):
        sil_mesaj = QMessageBox.question(self.raflarR10Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR10Ui.R10_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR10Ui.R10_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r10 = "DELETE FROM R10 WHERE Lot = ?"
               self.islem.execute(sorgu_r10, (silinecek_lot,))
  
               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR10Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r10()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR10Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r11(self):
        self.raflarR11Ui.R11_tw.clear()
        self.raflarR11Ui.R11_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR11Ui.R11_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R11"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR11Ui.R11_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r11(self):
        sil_mesaj = QMessageBox.question(self.raflarR11Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR11Ui.R11_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR11Ui.R11_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r11 = "DELETE FROM R11 WHERE Lot = ?"
               self.islem.execute(sorgu_r11, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR11Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r11()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR11Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r12(self):
        self.raflarR12Ui.R12_tw.clear()
        self.raflarR12Ui.R12_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR12Ui.R12_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R12"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR12Ui.R12_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r12(self):
        sil_mesaj = QMessageBox.question(self.raflarR12Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR12Ui.R12_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR12Ui.R12_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r12 = "DELETE FROM R12 WHERE Lot = ?"
               self.islem.execute(sorgu_r12, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR12Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r12()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR12Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r13(self):
        self.raflarR13Ui.R13_tw.clear()
        self.raflarR13Ui.R13_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR13Ui.R13_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R13"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR13Ui.R13_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r13(self):
        sil_mesaj = QMessageBox.question(self.raflarR13Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR13Ui.R13_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR13Ui.R13_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r13 = "DELETE FROM R13 WHERE Lot = ?"
               self.islem.execute(sorgu_r13, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR13Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r13()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR13Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r14(self):
        self.raflarR14Ui.R14_tw.clear()
        self.raflarR14Ui.R14_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR14Ui.R14_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R14"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR14Ui.R14_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r14(self):
        sil_mesaj = QMessageBox.question(self.raflarR14Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR14Ui.R14_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR14Ui.R14_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r14 = "DELETE FROM R14 WHERE Lot = ?"
               self.islem.execute(sorgu_r14, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR14Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r14()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR14Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r15(self):
        self.raflarR15Ui.R15_tw.clear()
        self.raflarR15Ui.R15_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR15Ui.R15_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R15"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR15Ui.R15_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r15(self):
        sil_mesaj = QMessageBox.question(self.raflarR15Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR15Ui.R15_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR15Ui.R15_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r15 = "DELETE FROM R15 WHERE Lot = ?"
               self.islem.execute(sorgu_r15, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR15Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r15()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR15Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r16(self):
        self.raflarR16Ui.R16_tw.clear()
        self.raflarR16Ui.R16_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR16Ui.R16_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R16"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR16Ui.R16_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r16(self):
        sil_mesaj = QMessageBox.question(self.raflarR16Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR16Ui.R16_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR16Ui.R16_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r16 = "DELETE FROM R16 WHERE Lot = ?"
               self.islem.execute(sorgu_r16, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR16Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r16()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR16Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r17(self):
        self.raflarR17Ui.R17_tw.clear()
        self.raflarR17Ui.R17_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR17Ui.R17_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R17"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR17Ui.R17_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r17(self):
        sil_mesaj = QMessageBox.question(self.raflarR17Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR17Ui.R17_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR17Ui.R17_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r17 = "DELETE FROM R17 WHERE Lot = ?"
               self.islem.execute(sorgu_r17, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR17Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r17()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR17Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r18(self):
        self.raflarR18Ui.R18_tw.clear()
        self.raflarR18Ui.R18_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR18Ui.R18_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R18"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR18Ui.R18_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r18(self):
        sil_mesaj = QMessageBox.question(self.raflarR18Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR18Ui.R18_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR18Ui.R18_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r18 = "DELETE FROM R18 WHERE Lot = ?"
               self.islem.execute(sorgu_r18, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR18Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r18()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR18Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r19(self):
        self.raflarR19Ui.R19_tw.clear()
        self.raflarR19Ui.R19_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR19Ui.R19_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R19"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR19Ui.R19_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r19(self):
        sil_mesaj = QMessageBox.question(self.raflarR19Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR19Ui.R19_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR19Ui.R19_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r19 = "DELETE FROM R19 WHERE Lot = ?"
               self.islem.execute(sorgu_r19, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR19Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r19()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR19Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r20(self):
        self.raflarR20Ui.R20_tw.clear()
        self.raflarR20Ui.R20_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR20Ui.R20_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R20"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR20Ui.R20_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r20(self):
        sil_mesaj = QMessageBox.question(self.raflarR20Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR20Ui.R20_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR20Ui.R20_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r20 = "DELETE FROM R20 WHERE Lot = ?"
               self.islem.execute(sorgu_r20, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR20Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r20()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR20Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r21(self):
        self.raflarR21Ui.R21_tw.clear()
        self.raflarR21Ui.R21_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR21Ui.R21_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R21"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR21Ui.R21_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r21(self):
        sil_mesaj = QMessageBox.question(self.raflarR21Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR21Ui.R21_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR21Ui.R21_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r21 = "DELETE FROM R21 WHERE Lot = ?"
               self.islem.execute(sorgu_r21, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR21Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r21()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR21Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r22(self):
        self.raflarR22Ui.R22_tw.clear()
        self.raflarR22Ui.R22_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR22Ui.R22_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R22"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR22Ui.R22_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r22(self):
        sil_mesaj = QMessageBox.question(self.raflarR22Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR22Ui.R22_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR22Ui.R22_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r22 = "DELETE FROM R22 WHERE Lot = ?"
               self.islem.execute(sorgu_r22, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR22Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r22()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR22Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
        
    def kayit_listele_r23(self):
        self.raflarR23Ui.R23_tw.clear()
        self.raflarR23Ui.R23_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR23Ui.R23_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R23"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR23Ui.R23_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r23(self):
        sil_mesaj = QMessageBox.question(self.raflarR23Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR23Ui.R23_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR23Ui.R23_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r23 = "DELETE FROM R23 WHERE Lot = ?"
               self.islem.execute(sorgu_r23, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR23Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r23()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR23Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r24(self):
        self.raflarR24Ui.R24_tw.clear()
        self.raflarR24Ui.R24_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR24Ui.R24_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R24"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR24Ui.R24_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r24(self):
        sil_mesaj = QMessageBox.question(self.raflarR24Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR24Ui.R24_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR24Ui.R24_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r24 = "DELETE FROM R24 WHERE Lot = ?"
               self.islem.execute(sorgu_r24, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR24Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r24()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR24Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r25(self):
        self.raflarR25Ui.R25_tw.clear()
        self.raflarR25Ui.R25_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR25Ui.R25_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R25"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR25Ui.R25_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r25(self):
        sil_mesaj = QMessageBox.question(self.raflarR25Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR25Ui.R25_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR25Ui.R25_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r25 = "DELETE FROM R25 WHERE Lot = ?"
               self.islem.execute(sorgu_r25, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR25Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r25()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR25Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r26(self):
        self.raflarR26Ui.R26_tw.clear()
        self.raflarR26Ui.R26_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR26Ui.R26_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R26"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR26Ui.R26_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r26(self):
        sil_mesaj = QMessageBox.question(self.raflarR26Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR26Ui.R26_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR26Ui.R26_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r26 = "DELETE FROM R26 WHERE Lot = ?"
               self.islem.execute(sorgu_r26, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR26Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r26()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR26Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r27(self):
        self.raflarR27Ui.R27_tw.clear()
        self.raflarR27Ui.R27_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR27Ui.R27_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R27"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR27Ui.R27_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r27(self):
        sil_mesaj = QMessageBox.question(self.raflarR27Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR27Ui.R27_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR27Ui.R27_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r27 = "DELETE FROM R27 WHERE Lot = ?"
               self.islem.execute(sorgu_r27, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR27Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r27()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR27Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r28(self):
        self.raflarR28Ui.R28_tw.clear()
        self.raflarR28Ui.R28_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR28Ui.R28_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R28"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR28Ui.R28_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r28(self):
        sil_mesaj = QMessageBox.question(self.raflarR28Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR28Ui.R28_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR28Ui.R28_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r28 = "DELETE FROM R28 WHERE Lot = ?"
               self.islem.execute(sorgu_r28, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR28Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r28()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR28Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r29(self):
        self.raflarR29Ui.R29_tw.clear()
        self.raflarR29Ui.R29_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR29Ui.R29_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R29"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR29Ui.R29_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r29(self):
        sil_mesaj = QMessageBox.question(self.raflarR29Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR29Ui.R29_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR29Ui.R29_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r29 = "DELETE FROM R29 WHERE Lot = ?"
               self.islem.execute(sorgu_r29, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR29Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r29()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR29Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r30(self):
        self.raflarR30Ui.R30_tw.clear()
        self.raflarR30Ui.R30_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR30Ui.R30_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R30"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR30Ui.R30_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r30(self):
        sil_mesaj = QMessageBox.question(self.raflarR30Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR30Ui.R30_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR30Ui.R30_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r30 = "DELETE FROM R30 WHERE Lot = ?"
               self.islem.execute(sorgu_r30, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR30Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r30()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR30Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r31(self):
        self.raflarR31Ui.R31_tw.clear()
        self.raflarR31Ui.R31_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR31Ui.R31_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R31"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR31Ui.R31_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r31(self):
        sil_mesaj = QMessageBox.question(self.raflarR31Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR31Ui.R31_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR31Ui.R31_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r31 = "DELETE FROM R31 WHERE Lot = ?"
               self.islem.execute(sorgu_r31, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR31Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r31()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR31Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r32(self):
        self.raflarR32Ui.R32_tw.clear()
        self.raflarR32Ui.R32_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR32Ui.R32_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R32"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR32Ui.R32_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r32(self):
        sil_mesaj = QMessageBox.question(self.raflarR32Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR32Ui.R32_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR32Ui.R32_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r32 = "DELETE FROM R32 WHERE Lot = ?"
               self.islem.execute(sorgu_r32, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR32Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r32()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR32Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r33(self):
        self.raflarR33Ui.R33_tw.clear()
        self.raflarR33Ui.R33_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR33Ui.R33_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R33"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR33Ui.R33_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r33(self):
        sil_mesaj = QMessageBox.question(self.raflarR33Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR33Ui.R33_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR33Ui.R33_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r33 = "DELETE FROM R33 WHERE Lot = ?"
               self.islem.execute(sorgu_r33, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR33Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r33()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR33Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r34(self):
        self.raflarR34Ui.R34_tw.clear()
        self.raflarR34Ui.R34_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR34Ui.R34_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R34"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR34Ui.R34_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r34(self):
        sil_mesaj = QMessageBox.question(self.raflarR34Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR34Ui.R34_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR34Ui.R34_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r34 = "DELETE FROM R34 WHERE Lot = ?"
               self.islem.execute(sorgu_r34, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR34Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r34()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR34Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r35(self):
        self.raflarR35Ui.R35_tw.clear()
        self.raflarR35Ui.R35_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR35Ui.R35_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R35"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR35Ui.R35_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r35(self):
        sil_mesaj = QMessageBox.question(self.raflarR35Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR35Ui.R35_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR35Ui.R35_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r35 = "DELETE FROM R35 WHERE Lot = ?"
               self.islem.execute(sorgu_r35, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR35Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r35()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR35Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r36(self):
        self.raflarR36Ui.R36_tw.clear()
        self.raflarR36Ui.R36_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR36Ui.R36_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R36"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR36Ui.R36_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r36(self):
        sil_mesaj = QMessageBox.question(self.raflarR36Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR36Ui.R36_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR36Ui.R36_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r36 = "DELETE FROM R36 WHERE Lot = ?"
               self.islem.execute(sorgu_r36, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR36Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r36()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR36Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r37(self):
        self.raflarR37Ui.R37_tw.clear()
        self.raflarR37Ui.R37_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR37Ui.R37_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R37"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR37Ui.R37_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r37(self):
        sil_mesaj = QMessageBox.question(self.raflarR37Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR37Ui.R37_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR37Ui.R37_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r37 = "DELETE FROM R37 WHERE Lot = ?"
               self.islem.execute(sorgu_r37, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR37Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r37()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR37Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r38(self):
        self.raflarR38Ui.R38_tw.clear()
        self.raflarR38Ui.R38_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR38Ui.R38_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R38"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR38Ui.R38_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r38(self):
        sil_mesaj = QMessageBox.question(self.raflarR38Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR38Ui.R38_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR38Ui.R38_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r38 = "DELETE FROM R38 WHERE Lot = ?"
               self.islem.execute(sorgu_r38, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR38Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r38()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR38Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r39(self):
        self.raflarR39Ui.R39_tw.clear()
        self.raflarR39Ui.R39_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR39Ui.R39_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R39"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR39Ui.R39_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r39(self):
        sil_mesaj = QMessageBox.question(self.raflarR39Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR39Ui.R39_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR39Ui.R39_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r39 = "DELETE FROM R39 WHERE Lot = ?"
               self.islem.execute(sorgu_r39, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR39Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r39()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR39Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r40(self):
        self.raflarR40Ui.R40_tw.clear()
        self.raflarR40Ui.R40_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR40Ui.R40_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R40"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR40Ui.R40_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r40(self):
        sil_mesaj = QMessageBox.question(self.raflarR40Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR40Ui.R40_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR40Ui.R40_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r40 = "DELETE FROM R40 WHERE Lot = ?"
               self.islem.execute(sorgu_r40, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR40Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r40()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR40Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r41(self):
        self.raflarR41Ui.R41_tw.clear()
        self.raflarR41Ui.R41_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR41Ui.R41_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R41"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR41Ui.R41_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r41(self):
        sil_mesaj = QMessageBox.question(self.raflarR41Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR41Ui.R41_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR41Ui.R41_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r41 = "DELETE FROM R41 WHERE Lot = ?"
               self.islem.execute(sorgu_r41, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR41Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r41()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR41Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r42(self):
        self.raflarR42Ui.R42_tw.clear()
        self.raflarR42Ui.R42_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR42Ui.R42_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R42"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR42Ui.R42_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r42(self):
        sil_mesaj = QMessageBox.question(self.raflarR42Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR42Ui.R42_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR42Ui.R42_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r42 = "DELETE FROM R42 WHERE Lot = ?"
               self.islem.execute(sorgu_r42, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR42Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r42()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR42Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r43(self):
        self.raflarR43Ui.R43_tw.clear()
        self.raflarR43Ui.R43_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR43Ui.R43_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R43"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR43Ui.R43_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r43(self):
        sil_mesaj = QMessageBox.question(self.raflarR43Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR43Ui.R43_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR43Ui.R43_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r43 = "DELETE FROM R43 WHERE Lot = ?"
               self.islem.execute(sorgu_r43, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR43Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r43()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR43Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r44(self):
        self.raflarR44Ui.R44_tw.clear()
        self.raflarR44Ui.R44_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR44Ui.R44_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R44"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR44Ui.R44_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r44(self):
        sil_mesaj = QMessageBox.question(self.raflarR44Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR44Ui.R44_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR44Ui.R44_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r44 = "DELETE FROM R44 WHERE Lot = ?"
               self.islem.execute(sorgu_r44, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR44Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r44()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR44Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r45(self):
        self.raflarR45Ui.R45_tw.clear()
        self.raflarR45Ui.R45_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR45Ui.R45_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R45"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR45Ui.R45_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r45(self):
        sil_mesaj = QMessageBox.question(self.raflarR45Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR45Ui.R45_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR45Ui.R45_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r45 = "DELETE FROM R45 WHERE Lot = ?"
               self.islem.execute(sorgu_r45, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR45Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r45()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR45Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r46(self):
        self.raflarR46Ui.R46_tw.clear()
        self.raflarR46Ui.R46_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR46Ui.R46_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R46"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR46Ui.R46_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r46(self):
        sil_mesaj = QMessageBox.question(self.raflarR46Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR46Ui.R46_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR46Ui.R46_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r46 = "DELETE FROM R46 WHERE Lot = ?"
               self.islem.execute(sorgu_r46, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR46Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r46()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR46Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r47(self):
        self.raflarR47Ui.R47_tw.clear()
        self.raflarR47Ui.R47_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR47Ui.R47_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R47"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR47Ui.R47_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r47(self):
        sil_mesaj = QMessageBox.question(self.raflarR47Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR47Ui.R47_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR47Ui.R47_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r47 = "DELETE FROM R47 WHERE Lot = ?"
               self.islem.execute(sorgu_r47, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR47Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r47()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR47Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r48(self):
        self.raflarR48Ui.R48_tw.clear()
        self.raflarR48Ui.R48_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR48Ui.R48_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R48"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR48Ui.R48_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r48(self):
        sil_mesaj = QMessageBox.question(self.raflarR48Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR48Ui.R48_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR48Ui.R48_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r48 = "DELETE FROM R48 WHERE Lot = ?"
               self.islem.execute(sorgu_r48, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR48Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r48()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR48Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r49(self):
        self.raflarR49Ui.R49_tw.clear()
        self.raflarR49Ui.R49_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR49Ui.R49_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R49"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR49Ui.R49_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r49(self):
        sil_mesaj = QMessageBox.question(self.raflarR49Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR49Ui.R49_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR49Ui.R49_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r49 = "DELETE FROM R49 WHERE Lot = ?"
               self.islem.execute(sorgu_r49, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR49Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r49()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR49Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r50(self):
        self.raflarR50Ui.R50_tw.clear()
        self.raflarR50Ui.R50_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR50Ui.R50_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R50"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR50Ui.R50_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r50(self):
        sil_mesaj = QMessageBox.question(self.raflarR50Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR50Ui.R50_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR50Ui.R50_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r50 = "DELETE FROM R50 WHERE Lot = ?"
               self.islem.execute(sorgu_r50, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR50Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r50()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR50Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r51(self):
        self.raflarR51Ui.R51_tw.clear()
        self.raflarR51Ui.R51_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR51Ui.R51_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R51"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR51Ui.R51_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r51(self):
        sil_mesaj = QMessageBox.question(self.raflarR51Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR51Ui.R51_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR51Ui.R51_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r51 = "DELETE FROM R51 WHERE Lot = ?"
               self.islem.execute(sorgu_r51, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR51Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r51()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR51Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r52(self):
        self.raflarR52Ui.R52_tw.clear()
        self.raflarR52Ui.R52_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR52Ui.R52_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R52"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR52Ui.R52_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r52(self):
        sil_mesaj = QMessageBox.question(self.raflarR52Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR52Ui.R52_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR52Ui.R52_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r52 = "DELETE FROM R52 WHERE Lot = ?"
               self.islem.execute(sorgu_r52, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR52Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r52()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR52Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r53(self):
        self.raflarR53Ui.R53_tw.clear()
        self.raflarR53Ui.R53_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR53Ui.R53_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R53"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR53Ui.R53_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r53(self):
        sil_mesaj = QMessageBox.question(self.raflarR53Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR53Ui.R53_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR53Ui.R53_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r53 = "DELETE FROM R53 WHERE Lot = ?"
               self.islem.execute(sorgu_r53, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR53Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r53()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR53Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r54(self):
        self.raflarR54Ui.R54_tw.clear()
        self.raflarR54Ui.R54_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR54Ui.R54_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R54"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR54Ui.R54_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r54(self):
        sil_mesaj = QMessageBox.question(self.raflarR54Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR54Ui.R54_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR54Ui.R54_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r54 = "DELETE FROM R54 WHERE Lot = ?"
               self.islem.execute(sorgu_r54, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR54Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r54()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR54Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r55(self):
        self.raflarR55Ui.R55_tw.clear()
        self.raflarR55Ui.R55_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR55Ui.R55_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R55"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR55Ui.R55_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r55(self):
        sil_mesaj = QMessageBox.question(self.raflarR55Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR55Ui.R55_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR55Ui.R55_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r55 = "DELETE FROM R55 WHERE Lot = ?"
               self.islem.execute(sorgu_r55, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR55Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r55()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR55Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r56(self):
        self.raflarR56Ui.R56_tw.clear()
        self.raflarR56Ui.R56_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR56Ui.R56_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R56"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR56Ui.R56_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r56(self):
        sil_mesaj = QMessageBox.question(self.raflarR56Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR56Ui.R56_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR56Ui.R56_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r56 = "DELETE FROM R56 WHERE Lot = ?"
               self.islem.execute(sorgu_r56, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR56Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r56()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR56Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")
    
    def kayit_listele_r57(self):
        self.raflarR57Ui.R57_tw.clear()
        self.raflarR57Ui.R57_tw.setHorizontalHeaderLabels(("Lot", "Kalite", "Genişlik"))
        self.raflarR57Ui.R57_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = "SELECT * FROM R57"
        self.islem.execute(sorgu)

        for indexSatir, kayitNumarasi in enumerate(self.islem.fetchall()):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.raflarR57Ui.R57_tw.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil_r57(self):
        sil_mesaj = QMessageBox.question(self.raflarR57Window, "Silme Onayı", "Silmek İstediğinizden Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)

        if sil_mesaj == QMessageBox.Yes:
           secilen_satir = self.raflarR57Ui.R57_tw.currentRow()
           if secilen_satir == -1:
              QMessageBox.warning(self, "Uyarı", "Silinecek bir satır seçilmedi!")
              return

           silinecek_lot = self.raflarR57Ui.R57_tw.item(secilen_satir, 0).text()

           try:
               self.baglanti.execute("BEGIN TRANSACTION")

               sorgu_r57 = "DELETE FROM R57 WHERE Lot = ?"
               self.islem.execute(sorgu_r57, (silinecek_lot,))

               sorgu_kumaslarT = "DELETE FROM kumaslarT WHERE Lot = ?"
               self.islem.execute(sorgu_kumaslarT, (silinecek_lot,))

               self.baglanti.commit()
               QMessageBox.information(self.raflarR57Window, "Silme İşlemi", "Kayıt başarıyla silindi!")
               self.kayit_listele_r57()

           except Exception as error:
               self.baglanti.rollback()
               self.raflarR57Ui.statusbar.showMessage(f"Kayıt Silinemedi! Hata: {error}")

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = LoginApp()
    pencere.show()
    sys.exit(uygulama.exec_())