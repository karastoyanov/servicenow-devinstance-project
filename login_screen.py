import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QDateEdit)
from PyQt5.QtGui import (QIcon, QFont, QFontDatabase)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt, QTimer, QSize)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ServiceNow Dev Instance Task Verifier")
        self.setWindowIcon(QIcon(r'images\now-mobile-icon.png'))
        self.resize(500, 320)
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
        font = QFontDatabase.addApplicationFont(r'fonts\Helvetica Neue.otf')
        font_families = QFontDatabase.applicationFontFamilies(font)
        url_label.setFont(QFont(font_families[0], 8))
        url_label.setGeometry(110, 1, 260, 40)      
    
    def user_name(self):
        user_name_label = QLabel("User Name", self)
        user_name_label.setText("User Name")
        font = QFontDatabase.addApplicationFont(r'fonts\Helvetica Neue.otf')
        font_families = QFontDatabase.applicationFontFamilies(font)
        user_name_label.setFont(QFont(font_families[0], 8))
        user_name_label.setGeometry(200, 70, 100, 40)
    
    def user_password(self):
        user_password_label = QLabel("User Password", self)
        user_password_label.setText("User Password")
        font = QFontDatabase.addApplicationFont(r'fonts\Helvetica Neue.otf')
        font_families = QFontDatabase.applicationFontFamilies(font)
        user_password_label.setFont(QFont(font_families[0], 8))
        user_password_label.setGeometry(190, 150, 120, 40)

    def instance_url_textbox(self):
        instance_url_line_edit = QLineEdit(self)
        font = QFontDatabase.addApplicationFont(r'fonts\Helvetica Neue.otf')
        font_families = QFontDatabase.applicationFontFamilies(font)
        instance_url_line_edit.setFont(QFont(font_families[0], 8))
        instance_url_line_edit.setGeometry(109, 30, 258, 30)
        return instance_url_line_edit.text()
    
    def user_name_textbox(self):
        user_name_line_edit = QLineEdit(self)
        font = QFontDatabase.addApplicationFont(r'fonts\Helvetica Neue.otf')
        font_families = QFontDatabase.applicationFontFamilies(font)
        user_name_line_edit.setFont(QFont(font_families[0], 8))
        user_name_line_edit.setGeometry(155, 100, 180, 40)

    def password_textbox(self):
        password_line_edit = QLineEdit(self)
        font = QFontDatabase.addApplicationFont(r'fonts\Helvetica Neue.otf')
        font_families = QFontDatabase.applicationFontFamilies(font)
        password_line_edit.setFont(QFont(font_families[0], 8))
        password_line_edit.setGeometry(155, 180, 180, 40)
        
    def login_button(self):
        login_button = QPushButton(self)
        login_button.setText("Login")
        # login_button.clicked.connect(check_conn())
        login_button.setGeometry(200, 240, 100, 50)
        
    def license(self):
        license = QLabel(self)
        license.setText("GNU General Public License v3.0")
        font = QFontDatabase.addApplicationFont(r'fonts\Helvetica Neue.otf')
        font_families = QFontDatabase.applicationFontFamilies(font)
        license.setFont(QFont(font_families[0], 8))
        license.setGeometry(250, 290, 300, 40)
        







app = QApplication(sys.argv)
win = LoginForm()
win.show()
sys.exit(app.exec_())
                           