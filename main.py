import snow_connection
import test_one
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QFont, QFontDatabase, QPixmap)
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
            print('Login Successfull')
            MainMenu.main_menu(self)
        elif snow_connection.check_conn is False:
            fail_conn = QMessageBox()
            # fail_conn.setIcon(QMessageBox.information)
            fail_conn.setText('Error during connection. Check SNOW credentials')
            fail_conn.setWindowTitle('Authentication Failure')
            fail_conn.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # fail_conn.buttonClicked.connect()
            return_value = fail_conn.exec_()
            if return_value == QMessageBox.Cancel:
                print('Cancel')
            else:
                print('OK')

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ServiceNow Dev Instance Task Verifier")
        self.setWindowIcon(QIcon(r'images\now-mobile-icon.png'))
        self.setFixedSize(800, 900)
        self.task_one()
        self.review_task_one()
        self.task_two()
        self.review_task_two()
        self.task_three()
        self.review_task_three()
        self.task_one_feedback()
        self.task_two_feedback()
        self.task_three_feedback()
        self.show()
        self.contribuite()
       
        

    def task_one(self):
        task_one_button = QPushButton(self,  clicked = lambda : self.task_one_verify())
        task_one_button.setText("Verify Task N1")
        task_one_button.setGeometry(10, 10, 150, 40)
    
    def review_task_one(self):
        task_one_review_button = QPushButton(self, clicked = lambda : self.task_one_description())
        task_one_review_button.setText("Check Task N1")
        task_one_review_button.setGeometry(10, 50, 150, 40)

    def task_two(self):
        task_two_button = QPushButton(self)
        task_two_button.setText("Verify Task N2")
        task_two_button.setGeometry(10, 150, 150, 40)

    def review_task_two(self):
        task_two_review_button = QPushButton(self)
        task_two_review_button.setText("Check Task N2")
        task_two_review_button.setGeometry(10, 190, 150, 40)

    def task_three(self):
        task_three_button = QPushButton(self)
        task_three_button.setText("Verify Task N3")
        task_three_button.setGeometry(10, 290, 150, 40)

    def review_task_three(self):
        task_three_review_button = QPushButton(self)
        task_three_review_button.setText("Check Task N3")
        task_three_review_button.setGeometry(10, 330, 150, 40)
        
    def task_one_feedback(self):
        task_one_feedback_label = QLabel(self)
        task_one_feedback_label.setGeometry(200, 10, 40, 40)
        waiting = QPixmap(r'images\waiting.png')
        task_one_feedback_label.setPixmap(waiting)
        task_one_feedback_label.resize(waiting.width(), waiting.height())
        
    def task_two_feedback(self):
        task_two_feedback_label = QLabel(self)
        task_two_feedback_label.setGeometry(200, 150, 40, 40)
        waiting = QPixmap(r'images\waiting.png')
        task_two_feedback_label.setPixmap(waiting)
        task_two_feedback_label.resize(waiting.width(), waiting.height())

    def task_three_feedback(self):
        task_three_feedback_label = QLabel(self)
        task_three_feedback_label.setGeometry(200, 290, 40, 40)
        waiting = QPixmap(r'images\waiting.png')
        task_three_feedback_label.setPixmap(waiting)
        task_three_feedback_label.resize(waiting.width(), waiting.height())
    
    def task_one_description(self):
        task_one_description_label = QPlainTextEdit(self)
        text = open(r'tasks_description\task_one.txt').read()
        task_one_description_label.setPlainText(text)
        task_one_description_label.setGeometry(10, 400, 780, 400)
        task_one_description_label.show()
        
    def contribuite(self):
        contribute = QLabel(self)
        github_image = QPixmap(r'images\github.png')
        contribute.setPixmap(github_image) 
        contribute.setGeometry(750, 850, 50, 50)
        url_link = "<a href =\"https://github.com/karastoyanov/servicenow-devinstance-project\"</a>"
        contribute.setOpenExternalLinks(self, True)
        contribute.show()
        
        
    
    def task_one_verify(self):
        if test_one.verify_task() == True:
            print("Task 1 OK")
            task_one_feedback_label = QLabel(self)
            task_one_feedback_label.setGeometry(200, 10, 40, 40)
            check = QPixmap(r'images\check.png')
            task_one_feedback_label.setPixmap(check)
            task_one_feedback_label.resize(check.width(), check.height())
            task_one_feedback_label.show()
        else:
            print("Task 1 FAILED")
            task_one_feedback_label = QLabel(self)
            task_one_feedback_label.setGeometry(200, 10, 40, 40)
            fail = QPixmap(r'images\failure.png')
            task_one_feedback_label.setPixmap(fail)
            task_one_feedback_label.resize(fail.width(), fail.height())
            task_one_feedback_label.show()

   
    def main_menu(self):
        self.w = MainMenu()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginForm()
    win.show()
    app.exec_()
