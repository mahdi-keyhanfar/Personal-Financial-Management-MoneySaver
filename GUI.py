from PyQt6.QtWidgets import QApplication
import sys
import  Login_Window
from variables import *
import sqlite3 

# set connection to database
conn = sqlite3.connect("data-test.db")
cursor = conn.cursor()

# write a execute command to create a table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50),
        password VARCHAR(50),
        email VARCHAR(100),
        phone VARCHAR(11)
    )"""
)
conn.commit()
conn.close()

app = QApplication(sys.argv)

Login_Window.login_wnd()

app.exit(exec())