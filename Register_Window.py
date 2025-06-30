from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon, QFont
from variables import *
import sys
import os
import sqlite3

font_10 = QFont("Vazir", 10)
app = QApplication(sys.argv)

# set connection to database
conn = sqlite3.connect("data-test.db")
cursor = conn.cursor()

def register_wnd():
    
    global wnd_r
    global txt_r_2, txt_r_3
    wnd_r = QWidget()
    wnd_r.setFixedSize(350, 300)
    wnd_r.setWindowTitle("Money Saver | Sign in")
    icon_path = os.path.join(os.path.dirname(__file__), "ico.png")
    wnd_r.setWindowIcon(QIcon(icon_path))
    
    def click_btn_signup():
        V_DPM_Username = txt_r_1.text()
        V_DPM_Password = txt_r_2.text()
        V_DPM_RepPassword = txt_r_3.text()
        V_DPM_Email = txt_r_4.text()
        V_DPM_PhoneNum = txt_r_5.text()

        if not all([V_DPM_Username, V_DPM_Password, V_DPM_RepPassword, V_DPM_Email, V_DPM_PhoneNum]):
            QMessageBox.warning(wnd_r, "خطا", "لطفا تمام فیلدها را پر کنید")
            return
        
        if len(V_DPM_Username) <= 8:
            QMessageBox.warning(wnd_r, "خطا", "نام کاربری باید بیشتر از 8 کاراکتر باشد")
            return
        
        if V_DPM_Password != V_DPM_RepPassword:
            QMessageBox.warning(wnd_r, "خطا", "رمزهای عبور مطابقت ندارند")
            return
        
        try:
            cursor.execute(
                """INSERT INTO users(username, password, email, phone) VALUES (?, ?, ?, ?)""",
                (V_DPM_Username, V_DPM_Password, V_DPM_Email, V_DPM_PhoneNum)
            )
            conn.commit()
            QMessageBox.information(wnd_r, "موفق", "ثبت نام با موفقیت انجام شد")
            wnd_r.close()
        except Exception as e:
            QMessageBox.critical(wnd_r, "خطا", f"خطا در ثبت اطلاعات: {str(e)}")        
        

    label_r_1 = QLabel(wnd_r)
    label_r_1.move(270, 20)
    label_r_1.setText("نام کاربری")

    label_r_2 = QLabel(wnd_r)
    label_r_2.move(275, 60)
    label_r_2.setText("رمز عبور")

    label_r_3 = QLabel(wnd_r)
    label_r_3.move(250, 100)
    label_r_3.setText("تایید رمز عبور")

    label_r_4 = QLabel(wnd_r)
    label_r_4.move(290, 140)
    label_r_4.setText("ایمیل")

    label_r_5 = QLabel(wnd_r)
    label_r_5.move(250, 180)
    label_r_5.setText("شماره موبایل")
    
    txt_r_1 = QLineEdit(wnd_r)
    txt_r_1.setFont(font_10)
    txt_r_1.resize(230, 25)
    txt_r_1.move(30, 20)
    
    txt_r_2 = QLineEdit(wnd_r)
    txt_r_2.setFont(font_10)
    txt_r_2.resize(230, 25)
    txt_r_2.move(30, 58)
    
    txt_r_3 = QLineEdit(wnd_r)
    txt_r_3.setFont(font_10)
    txt_r_3.resize(215, 25)
    txt_r_3.move(30, 97)
    
    txt_r_4 = QLineEdit(wnd_r)
    txt_r_4.setFont(font_10)
    txt_r_4.resize(250, 25)
    txt_r_4.move(30, 138)
    
    txt_r_5 = QLineEdit(wnd_r)
    txt_r_5.setFont(font_10)
    txt_r_5.resize(215, 25)
    txt_r_5.move(30, 178)
                         
    btn_r_1 = QPushButton(wnd_r)
    btn_r_1.move(70, 240)
    btn_r_1.setFont(font_10)
    btn_r_1.setText("ثبت نام")
    btn_r_1.clicked.connect(click_btn_signup)

    btn_r_2 = QPushButton(wnd_r)
    btn_r_2.move(210, 240)
    btn_r_2.setFont(font_10)
    btn_r_2.setText("بازگشت")
    
    wnd_r.show()
    
#----------------- Event defs -----------------
