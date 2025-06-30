from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon, QFont
from variables import *
import sys
import os
import sqlite3
import Register_Window, Main_Window

font_10 = QFont("Vazir", 10)
app = QApplication(sys.argv)

# set connection to database
conn = sqlite3.connect("data-test.db")
cursor = conn.cursor()

def login_wnd():

    global wnd_l
    wnd_l = QWidget()
    wnd_l.setFixedSize(350, 200)
    wnd_l.setWindowTitle("Money Saver | Login")
    icon_path = os.path.join(os.path.dirname(__file__), "ico.png")
    wnd_l.setWindowIcon(QIcon(icon_path))

    label_l_1 = QLabel(wnd_l)
    label_l_1.setText("نام کاربری")
    label_l_1.setFont(font_10)
    label_l_1.move(280, 40)

    label_l_2 = QLabel(wnd_l)
    label_l_2.setText("رمز عبور")
    label_l_2.setFont(font_10)
    label_l_2.move(285, 100)
    
    txt_l_1 = QLineEdit(wnd_l)
    txt_l_1.setFont(font_10)
    txt_l_1.resize(230, 25)
    txt_l_1.move(30, 38)

    txt_l_2 = QLineEdit(wnd_l)
    txt_l_2.setFont(font_10)
    txt_l_2.resize(230, 25)
    txt_l_2.move(30, 100)


    btn_l_1 = QPushButton(wnd_l)
    btn_l_1.setText("ورود")
    btn_l_1.setFont(font_10)
    btn_l_1.move(175, 150)
    btn_l_1.clicked.connect(Login_Action)

    btn_l_2 = QPushButton(wnd_l)
    btn_l_2.setText("ثبت نام")
    btn_l_2.setFont(font_10)
    btn_l_2.move(40, 150)
    btn_l_2.clicked.connect(Register_Window.register_wnd)

    wnd_l.show()
    sys.exit(app.exec())
    
#----------------- Event defs -----------------
def Login_Action():
    Main_Window.main_wnd()
    wnd_l.close()
    
