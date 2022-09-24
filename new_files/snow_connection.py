from pysnc import ServiceNowClient, ServiceNowOAuth2
from PyQt5.QtWidgets import QApplication
from pysnc import exceptions
import sys, os



# instance = "dev109438"
# user = "admin"
# password = "LrmsjVJB@8^3"



def check_conn(ins, uss, passw):
    instance = ins
    user = uss
    password = passw
    client = ServiceNowClient(instance, (user, password))
    try:
        query = client.GlideRecord('sys_user')
        query.get('does not matter') # Really does not matter here
        print("Connection Function Login Success")
        return True
        
    except:
        print("Connection Function Login Failure")
        return False
    
# app = QApplication([])
# k = LoginForm()
# k.get_credentials()
# instance = k.get_instance
# user = k.get_user
# password = k.get_pass
# client = ServiceNowClient(instance, (user, password))
# check_conn()