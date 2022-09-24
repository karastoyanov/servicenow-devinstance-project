from pysnc import ServiceNowClient, ServiceNowOAuth2
from pysnc import exceptions
import sys, os


# instance = 'dev109438'
# user = 'admin'
# password = 'LrmsjVJB@8^3'

instance = LoginForm.snow_connection().instance()
user = LoginForm.snow_connection().user
password = LoginForm.snow_connection().password

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

check_conn()