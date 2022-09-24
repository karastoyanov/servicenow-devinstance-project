import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import main_menu

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ServiceNow Dev Instance Task Verifier")
        self.setWindowIcon(QIcon(r'images\now-mobile-icon.png'))
        self.setFixedSize(500, 320)
        
        self.url_label = QLabel("ServiceNow Instance URL address", self)
        self.url_label.setText("ServiceNow Instance URL address")
        self.url_label.setGeometry(10, 1, 260, 40)
        self.url_label.show()
        
        self.instance_url_line_edit = QLineEdit(self)
        self.instance_url_line_edit.setGeometry(220, 5, 258, 30)
        self.instance_url_line_edit.show()
        
        self.user_name_label = QLabel("User Name", self)
        self.user_name_label.setText("ServiceNow Instance User Name")
        self.user_name_label.setGeometry(10, 70, 200, 40)
        self.user_name_label.show()
        
        self.user_name_line_edit = QLineEdit(self)
        self.user_name_line_edit.setGeometry(220, 75, 258, 30)
        self.user_name_line_edit.show()
        
        self.password_line_edit = QLineEdit(self)
        self.password_line_edit.setGeometry(220, 152, 258, 30)
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line_edit.show()
        
        self.user_password_label = QLabel("User Password", self)
        self.user_password_label.setText("ServiceNow Instance Password")
        self.user_password_label.setGeometry(10, 150, 200, 40)
        self.user_password_label.show()
        
        self.login_button = QPushButton(self, clicked = lambda : self.open_app())
        self.login_button.setText("Login")
        self.login_button.setGeometry(200, 240, 100, 50)
        self.login_button.show()
        
        self.license = QLabel(self)
        self.license.setText("GNU General Public License v3.0")
        self.license.setGeometry(300, 290, 300, 40)
        self.license.show()

        self.get_instance = self.instance_url_line_edit.text()
        self.get_user = self.user_name_line_edit.text()
        self.get_pass = self.password_line_edit.text()
    
    def open_app(self):
        import snow_connection
        if snow_connection.check_conn(self.instance_url_line_edit.text(), self.user_name_line_edit.text(), self.password_line_edit.text()) == True:
            print('Login Successfull')
            win2 = main_menu.MainMenu()
            win2.show()
            win.hide()
        else:
            fail_conn = QMessageBox()
            fail_conn.setIcon(QMessageBox.Warning)
            fail_conn.setText('Error connecting to ServiceNow Instance. Please check the credentials.\nIMPORTANT: ServiceNow Instance'\
                ' should be UP and RUNNING')
            fail_conn.setWindowTitle('Authentication Failure')
            fail_conn.setStandardButtons(QMessageBox.Ok)
            fail_conn.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginForm()
    win.show()
    app.exec_()
    
application_path = os.path.dirname(sys.executable)