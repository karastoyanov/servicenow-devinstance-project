from random import randint
import sys
import test_one
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QDateEdit)
from PyQt5.QtGui import (QIcon, QFont, QFontDatabase, QPainter, QPen)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt, QTimer, QSize)


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ServiceNow Dev Instance Task Verifier")
        self.setWindowIcon(QIcon(r'images\now-mobile-icon.png'))
        self.resize(800, 900)
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
        

    def task_one(self):
        task_one_button = QPushButton(self)
        task_one_button.setText("Verify Task N1")
        task_one_button.setGeometry(10, 10, 150, 40)
    
    def review_task_one(self):
        task_one_review_button = QPushButton(self)
        task_one_review_button.setText("Check Task N1")
        task_one_review_button.setGeometry(10, 50, 150, 40)
        # task_one_review_button.clicked.connect(test_one.verify_task())

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
        task_one_feedback_label = QPushButton(self)
        task_one_feedback_label.setGeometry(200, 10, 40, 40)
    
    def task_two_feedback(self):
        task_two_feedback_label = QPushButton(self)
        task_two_feedback_label.setGeometry(200, 150, 40, 40)
    
    def task_three_feedback(self):
        task_three_feedback_label = QPushButton(self)
        task_three_feedback_label.setGeometry(200, 290, 40, 40)
        

app = QApplication(sys.argv)
win = MainForm()
win.show()
sys.exit(app.exec_())
                           