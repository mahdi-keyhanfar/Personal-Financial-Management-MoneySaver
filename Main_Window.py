from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon, QFont
from variables import *
import sys
import os
import Register_Window

font_10 = QFont("Vazir", 10)
font_12 = QFont("Vazir", 12)
font_14 = QFont("Vazir", 14)
font_16 = QFont("Vazir", 16)
font_18 = QFont("Vazir", 18)
font_20 = QFont("Vazir", 20)

app = QApplication(sys.argv)

def main_wnd():
    
    global wnd_m
    wnd_m = QWidget()
    wnd_m.setFixedSize(1300, 700)
    wnd_m.setWindowTitle("Money Saver | Dashboard")
    icon_path = os.path.join(os.path.dirname(__file__), "ico.png")
    wnd_m.setWindowIcon(QIcon(icon_path))

    tab_m = QTabWidget(wnd_m)
    tab_m.setGeometry(10, 10, 1280, 680)

    tab_home = QWidget()
    
    # Home Tab
    tab_m.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    tab_m.setTabPosition(QTabWidget.TabPosition.North)

    # Label
    lbl_h_SelectAccount = QLabel("انتخاب حساب بانکی 💳", tab_home)
    lbl_h_SelectAccount.setFont(font_16)
    lbl_h_SelectAccount.move(1030, 30)

    lbl_h_NumberAccount = QLabel("شماره ی حساب انتخاب شده", tab_home)
    lbl_h_NumberAccount.setFont(font_16)
    lbl_h_NumberAccount.move(1000, 260)

    lbl_h_NumberAccount_Show = QLabel("2222 3333 4444 6666", tab_home)
    lbl_h_NumberAccount_Show.setFont(font_14)
    lbl_h_NumberAccount_Show.move(1050, 300)

    lbl_h_AddAccount = QLabel("افزودن حساب جدید ➕", tab_home)
    lbl_h_AddAccount.setFont(font_16)
    lbl_h_AddAccount.move(1040, 420)

    lbl_h_Inventory = QLabel("موجودی 💲", tab_home)
    lbl_h_Inventory.setFont(font_20)
    lbl_h_Inventory.move(550, 70)

    lbl_h_Inventory_Show = QLabel("2,393,000 T", tab_home)
    lbl_h_Inventory_Show.setFont(font_20)
    lbl_h_Inventory_Show.move(390, 70)

    lbl_h_Payment = QLabel("پرداختی 🟥", tab_home)
    lbl_h_Payment.setFont(font_18)
    lbl_h_Payment.move(800, 240)

    lbl_h_Payment_Show = QLabel("1,500,000 T", tab_home)
    lbl_h_Payment_Show.setFont(font_18)
    lbl_h_Payment_Show.move(645, 240)

    lbl_h_Received = QLabel("دریافتی 🟩", tab_home)
    lbl_h_Received.setFont(font_18)
    lbl_h_Received.move(800, 320)

    lbl_h_Received_Show = QLabel("500,000 T", tab_home)
    lbl_h_Received_Show.setFont(font_18)
    lbl_h_Received_Show.move(645, 320)

    lbl_h_FundTransfer = QLabel("انتقال وجه 📨", tab_home)
    lbl_h_FundTransfer.setFont(font_18)
    lbl_h_FundTransfer.move(30, 350)

    lbl_h_FundTransfer_Show = QLabel("1,560,000 T", tab_home)
    lbl_h_FundTransfer_Show.setFont(font_18)
    lbl_h_FundTransfer_Show.move(30, 390)

    lbl_h_Installments = QLabel("قسط ها 📇", tab_home)
    lbl_h_Installments.setFont(font_18)
    lbl_h_Installments.move(30, 430)

    lbl_h_Installments_Show = QLabel("20,200,000 T", tab_home)
    lbl_h_Installments_Show.setFont(font_18)
    lbl_h_Installments_Show.move(30, 430)

    # ComboBox
    combo_h_SelectAcc = QComboBox(tab_home)
    combo_h_SelectAcc.addItems(["گزینه ۱", "گزینه ۲", "گزینه ۳"])
    combo_h_SelectAcc.setFont(font_10)
    combo_h_SelectAcc.resize(210, 30)
    combo_h_SelectAcc.move(1030, 80)

    # Button
    btn_h_ConfAcc = QPushButton("تأیید انتخاب", tab_home)
    btn_h_ConfAcc.setFont(font_10)
    btn_h_ConfAcc.resize(150, 30)
    btn_h_ConfAcc.move(1090, 130)
    
    btn_h_AddAcc = QPushButton("➕", tab_home)
    btn_h_AddAcc.setFont(font_12)
    btn_h_AddAcc.resize(120, 40)
    btn_h_AddAcc.move(1120, 460)

    # تب‌های دیگر ساده
    tab2 = QLabel("پرداختی")
    tab3 = QLabel("دریافتی")
    tab4 = QLabel("انتقال وجه")
    tab5 = QLabel("اقساط")
    tab6 = QLabel("جست‌وجو")

    # Add Tabs
    tab_m.addTab(tab_home, "خانه")
    tab_m.addTab(tab2, "پرداختی")
    tab_m.addTab(tab3, "دریافتی")
    tab_m.addTab(tab4, "انتقال وجه")
    tab_m.addTab(tab5, "اقساط")
    tab_m.addTab(tab6, "جست و جو")

    wnd_m.show()