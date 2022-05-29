import sys
import os
import random
#mengimport modul yang sudah di download
from deep_translator import GoogleTranslator
#mengubah teks menjadi suara manusia
import gtts

#mengimport modul PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

#membuat class dengan nama Translator
class Translator (QWidget):
    #membuat konstruktor
    def __init__ (self):
        super().__init__()
        self.init_ui()

    #membuat tampilan layout
    def init_ui (self):
        vb=QVBoxLayout()
        self.setLayout(vb)
        
        #mengatur jenis font dan ukuran font
        font = QFont ("Times", 14 )

        #membuat text box untuk memasukkan text yang akan di translate
        self.insert_text = QTextEdit()
        self.insert_text.setFont(font)
        vb.addWidget (self.insert_text)

        #membuat tampilan untuk melihat hasil translate  
        self.show_translation = QTextEdit()
        self.show_translation.setFont(font)
        vb.addWidget (self.show_translation)

        #membuat tombol translate
        self.translatebtn = QPushButton ("Translate")
        self.translatebtn.setFont(font) 
        vb.addWidget (self.translatebtn)

        #membuat tombol play sound untuk memperjelas pengucapan kosa kata yang benar
        self.playsoundbtn = QPushButton ("Play Sound")
        self.playsoundbtn.setFont(font)
        vb.addWidget(self.playsoundbtn)

        #membuat tampilan untuk memilih bahasa yang akan di translate
        self.combo = QComboBox()
        self.combo.setFont(font)
        bahasa = ["Arabic", "English", "French", "Indonesian", "Japanese", "Spanish", "Thailand"]
        self.combo.addItems(bahasa)
        
        #mengatur line pada widget pilihan bahasa
        self.combo.setEditable(True)
        self.combo.lineEdit().setAlignment(Qt.AlignCenter)
        vb.addWidget (self.combo)
        
        #membuat kamus bahasa
        self.target = {"Arabic":"ar", "English":"en", "French":"fr", "Indonesian":"id", "Japanese":"ja", "Spanish":"es", "Thailand":"th"}
        
        #membuat variabel qmediaplayer
        self.player = QMediaPlayer()
        #mengaktifkan dan menghubungkan tombol translate ke fungsi translate
        self.translatebtn.clicked.connect(self.translate_text)
        self.playsoundbtn.clicked.connect(self.play_sound)

    #membuat fungsi translate
    def translate_text(self):
        global mp3
        mp3 = random.randint(10000, 1000000)
        target = self.target[self.combo.currentText()]
        text = self.insert_text.toPlainText()
        
        #hasil translate menggunakan library google translator yang sudah di import diatas
        translated = GoogleTranslator(source="auto", target=target).translate(text)
        self.show_translation.setText(translated)
        
        #mengubah hasil translate ke dalam suara manusia menggunakan library gtts
        tts = gtts.gTTS(translated, lang=target)
        #menyimpan file
        tts.save(str(mp3)+'.mp3')

    #membuat fungsi pada tombol play sound
    def play_sound(self):
        #membuat link untuk membuka file yang sudah disimpan
        path = os.path.join(os.getcwd(), str(mp3)+".mp3")
        url = QUrl.fromLocalFile(path)
        #membuat content
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

#fungsi untuk menjalankan aplikasi translate
def main():
    app = QApplication (sys.argv)
    gui = Translator()
    #mengatur posisi dan panjang tinggi gui
    gui.setGeometry(100, 100, 700, 500)
    #mengatur nama judul pada windows
    gui.setWindowTitle("Translator Sederhana")
    gui.show()
    sys.exit(app.exec_())
    
#menjalankan fungsi main
if __name__ == '__main__':
    main()
