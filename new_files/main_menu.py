import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ServiceNow Dev Instance Task Verifier")
        self.setWindowIcon(QIcon(r'images\now-mobile-icon.png'))
        self.setFixedSize(800, 900)
        self.show()
        
        
        # Creates button to verify Task One
        self.task_one_button = QPushButton(self,  clicked = lambda : self.task_one_verify())
        self.task_one_button.setText("Verify Task N1")
        self.task_one_button.setGeometry(10, 10, 150, 40)
        self.task_one_button.show()
   
        # Creates button to check Task One assignments
        self.task_one_review_button = QPushButton(self, clicked = lambda : self.task_one_description_label.show())
        self.task_one_review_button.setText("Check Task N1")
        self.task_one_review_button.setGeometry(10, 50, 150, 40)
        self.task_one_review_button.show()
        
        # Creates button to verify Task Two
        self.task_two_button = QPushButton(self, clicked = lambda : self.task_two_verify())
        self.task_two_button.setText("Verify Task N2")
        self.task_two_button.setGeometry(10, 150, 150, 40)
        self.task_two_button.show()
        
        # Creates button to check Task Two assignments
        self.task_two_review_button = QPushButton(self, clicked = lambda : self.task_two_description_label.show())
        self.task_two_review_button.setText("Check Task N2")
        self.task_two_review_button.setGeometry(10, 190, 150, 40)
        self.task_two_review_button.show()
        
        # Creates button to check Task Three
        self.task_three_button = QPushButton(self, clicked = lambda : self.task_three_verify())
        self.task_three_button.setText("Verify Task N3")
        self.task_three_button.setGeometry(10, 290, 150, 40)
        self.task_three_button.show()
        
        # Creates button to check Three
        self.task_three_review_button = QPushButton(self, clicked = lambda : self.task_three_description_label.show())
        self.task_three_review_button.setText("Check Task N3")
        self.task_three_review_button.setGeometry(10, 330, 150, 40)
        self.task_three_review_button.show()
        
        # Default icon to display Task One Status    
        self.task_one_feedback_label = QLabel(self)
        self.task_one_feedback_label.setGeometry(200, 10, 40, 40)
        waiting = QPixmap(r'images\waiting.png')
        self.task_one_feedback_label.setPixmap(waiting)
        self.task_one_feedback_label.resize(waiting.width(), waiting.height())
        self.task_one_feedback_label.show()
        
        # Default icon to display Task Two Status    
        self.task_two_feedback_label = QLabel(self)
        self.task_two_feedback_label.setGeometry(200, 150, 40, 40)
        waiting = QPixmap(r'images\waiting.png')
        self.task_two_feedback_label.setPixmap(waiting)
        self.task_two_feedback_label.resize(waiting.width(), waiting.height())
        self.task_two_feedback_label.show()
        
        # Default icon to display Task Three Status
        self.task_three_feedback_label = QLabel(self)
        self.task_three_feedback_label.setGeometry(200, 290, 40, 40)
        waiting = QPixmap(r'images\waiting.png')
        self.task_three_feedback_label.setPixmap(waiting)
        self.task_three_feedback_label.resize(waiting.width(), waiting.height())
        self.task_three_feedback_label.show()
        
        # Creates separate label to display Task One assignments
        self.task_one_description_label = QPlainTextEdit(self)
        self.text_task_one = open(r'tasks_description\task_one.txt').read()
        self.task_one_description_label.setPlainText(self.text_task_one)
        self.task_one_description_label.setGeometry(10, 400, 780, 400)
        # self.self.task_one_description_label.show()
    
        # Creates separate label to display Task Two assignments
        self.task_two_description_label = QPlainTextEdit(self)
        self.text_task_two = open(r'tasks_description\task_two.txt').read()
        self.task_two_description_label.setPlainText(self.text_task_two)
        self.task_two_description_label.setGeometry(10, 400, 780, 400)
        # self.task_two_description_label.show()
    
        # Creates separate label to display Task Three assignments
        self.task_three_description_label = QPlainTextEdit(self)
        self.text_task_three = open(r'tasks_description\task_three.txt').read()
        self.task_three_description_label.setPlainText(self.text_task_three)
        self.task_three_description_label.setGeometry(10, 400, 780, 400)
        # self.task_three_description_label.show()
         
    # Function that verifies Task One
    def task_one_verify(self):
        from test_one import verify_task
        if verify_task == True:
            print("Task 1 OK\n")
            task_one_feedback_label = QLabel(self)
            task_one_feedback_label.setGeometry(200, 10, 40, 40)
            check = QPixmap(r'images\check.png')
            task_one_feedback_label.setPixmap(check)
            task_one_feedback_label.resize(check.width(), check.height())
            task_one_feedback_label.show()
        else:
            print("Task 1 FAILED\n")
            task_one_feedback_label = QLabel(self)
            task_one_feedback_label.setGeometry(200, 10, 40, 40)
            fail = QPixmap(r'images\failure.png')
            task_one_feedback_label.setPixmap(fail)
            task_one_feedback_label.resize(fail.width(), fail.height())
            task_one_feedback_label.show()
    
    # Function that verifies Task Two
    def task_two_verify(self):
        from test_two import verify_task
        if verify_task() == True:
            print("Task 2 OK\n")
            task_two_feedback_label = QLabel(self)
            task_two_feedback_label.setGeometry(200, 150, 40, 40)
            check = QPixmap(r'images\check.png')
            task_two_feedback_label.setPixmap(check)
            task_two_feedback_label.resize(check.width(), check.height())
            task_two_feedback_label.show()
        else:
            print("Task 2 FAILED\n")
            task_two_feedback_label = QLabel(self)
            task_two_feedback_label.setGeometry(200, 150, 40, 40)
            fail = QPixmap(r'images\fail.png')
            task_two_feedback_label.setPixmap(fail)
            task_two_feedback_label.resize(fail.width(), fail.height())
            task_two_feedback_label.show()
            
    # Function that verifies Task Three
    def task_three_verify(self):
        from test_three import verify_task
        if verify_task() == True:
            print("Task 3 OK\n")
            task_three_feedback_label = QLabel(self)
            task_three_feedback_label.setGeometry(200, 290, 40, 40)
            check = QPixmap(r'images\check.png')
            task_three_feedback_label.setPixmap(check)
            task_three_feedback_label.resize(check.width(), check.height())
            task_three_feedback_label.show()
        else:
            print("Task 2 FAILED\n")
            task_three_feedback_label = QLabel(self)
            task_three_feedback_label.setGeometry(200, 290, 40, 40)
            fail = QPixmap(r'images\fail.png')
            task_three_feedback_label.setPixmap(fail)
            task_three_feedback_label.resize(fail.width(), fail.height())
            task_three_feedback_label.show()

if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = MainMenu()
    win.show()
    app.exec_()
    