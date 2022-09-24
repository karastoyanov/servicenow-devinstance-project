from pysnc import ServiceNowClient, ServiceNowOAuth2
from PyQt5.QtWidgets import QApplication
from pysnc import exceptions
import sys, os
from login_screen import LoginForm

instance = LoginForm().instance_url_line_edit.text()
user = LoginForm().user_name_line_edit.text()
password = LoginForm().password_line_edit.text()

# instance = "dev109438"
# user = "admin"
# password = "LrmsjVJB@8^3"

client = ServiceNowClient(instance, (user, password))

def check_conn():
    try:
        query = client.GlideRecord('sys_user')
        query.get('does not matter') # Really does not matter here
        print("Login Success")
        return True
        
    except exceptions.AuthenticationException as e:
        print("Login Failure")
        return False
    
    
app = QApplication([])   
k = LoginForm()

check_conn()