import sys
import snow_connection
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QDateEdit)
from PyQt5.QtGui import (QIcon, QFont, QFontDatabase)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt, QTimer, QSize)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ServiceNow Dev Instance Task Verifier")
        self.setWindowIcon(QIcon(r'images\now-mobile-icon.png'))
        self.setFixedSize(500, 320)
        self.instance_url()
        self.instance_url_textbox()
        self.user_name()
        self.user_name_textbox()
        self.user_password()
        self.password_textbox()
        self.login_button()
        self.license()
        self.show()

    def instance_url(self):
        url_label = QLabel("ServiceNow Instance URL address", self)
        url_label.setText("ServiceNow Instance URL address")
        url_label.setGeometry(10, 1, 260, 40)      
    
    def user_name(self):
        user_name_label = QLabel("User Name", self)
        user_name_label.setText("ServiceNow Instance User Name")
        user_name_label.setGeometry(10, 70, 200, 40)
    
    def user_password(self):
        user_password_label = QLabel("User Password", self)
        user_password_label.setText("ServiceNow Instance Password")
        user_password_label.setGeometry(10, 150, 200, 40)

    def instance_url_textbox(self):
        instance_url_line_edit = QLineEdit(self)
        instance_url_line_edit.setGeometry(220, 5, 258, 30)
        return instance_url_line_edit.text()
    
    def user_name_textbox(self):
        user_name_line_edit = QLineEdit(self)
        user_name_line_edit.setGeometry(220, 75, 258, 30)

    def password_textbox(self):
        password_line_edit = QLineEdit(self)
        password_line_edit.setGeometry(220, 152, 258, 30)
        
    def login_button(self):
        login_button = QPushButton(self, clicked = lambda : self.open_app())
        login_button.setText("Login")
        login_button.setGeometry(200, 240, 100, 50)
        
    def license(self):
        license = QLabel(self)
        license.setText("GNU General Public License v3.0")
        license.setGeometry(300, 290, 300, 40)
        
    def open_app(self):
        if snow_connection.check_conn() == True:
            pass
        else:
            fail_conn = QMessageBox()
            fail_conn.setIcon(QMessageBox.critical)
            fail_conn.setText('Error during connection. Check SNOW credentials')
            fail_conn.setWindowTitle('Authentication Failure')
            fail_conn.setStandardButtons(QMessageBox.Ok, QMessageBox.Cancel)
            fail_conn.buttonClicked.connect()
            return_value = fail_conn.exec_()
            if return_value == QMessageBox.Cancel:
                print('Cancel')
            else:
                print('OK')





app = QApplication(sys.argv)
win = LoginForm()
win.show()
sys.exit(app.exec_())
                           