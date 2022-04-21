import sys
import os
import random
#from deep_translator import GoogleTranslator
#import gtts

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Translator (QWidget):
    def __init__ (self):
        super().__init__()
        self.init_ui()

    def init_ui (self):
        vb=QVBoxLayout()
        self.setLayout(vb)

        self.insert_text= QTextEdit()
        vb.addWidget (self.insert_text)

        self.show_translation=QTextEdit()
        vb.addWidget (self.show_translation)

        self.translatebtn= QPushButton("Translate")
        vb.addWidget (self.translatebtn)

        self.playsoundbtn= QPushButton ("Play Sound")
        vb.addWidget(self.playsoundbtn)

        self.combo= QComboBox()
        vb.addWidget (self.combo)

def main():
    app = QApplication (sys.argv)
    gui = Translator()
    gui.setGeometry(100, 100, 700, 500)
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
