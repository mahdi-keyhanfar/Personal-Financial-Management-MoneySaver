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
    
    def login_click_event():
        V_DPM_Username = txt_l_1.text()
        V_DPM_Password = txt_l_2.text()
        
        if check_credentials(V_DPM_Username, V_DPM_Username):
            Login_Action()
        else:
            QMessageBox.warning(wnd_l, "خطا", "نام کاربری یا رمز عبور اشتباه است")

            
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
    btn_l_1.clicked.connect(login_click_event)

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
    
def check_credentials(username: str, password: str) -> bool:
    try:
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user_data = cursor.fetchone()

        conn.close()
        return user_data is not None

    except Exception as e:
        print(f"Error checking credentials: {e}")
        return False

    
