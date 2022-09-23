from pysnc import ServiceNowClient, ServiceNowOAuth2
from pysnc import exceptions
import sys, os
import main

# instance = 'dev109438'
# user = 'admin'
# password = 'LrmsjVJB@8^3'

instance = main.LoginForm.instance_url_textbox()
user = main.LoginForm.user_name_textbox()
password = main.LoginForm.password_textbox()

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

if __name__ == "__snow_connection__":
    app = main.QApplication(sys.argv)
    win = main.LoginForm()
    win.show()
    app.exec_()