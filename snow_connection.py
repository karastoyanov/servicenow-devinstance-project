from pysnc import ServiceNowClient


# instance = "dev109438"
# user = "admin"
# password = "LrmsjVJB@8^3"

with open(r'credentials.txt') as f:
    contents = f.readlines()
    for line in contents:
        instance = contents[0][0:-1]
        user = contents[1][0:-1]
        password = contents[2]
        break
client = ServiceNowClient(instance, (user, password))    

def check_conn():
    try:
        query = client.GlideRecord('sys_user')
        query.get('does not matter') # Really does not matter here
        print("Connection Function Login Success")
        return True
        
    except:
        print("Connection Function Login Failure")
        return False

# check_conn("dev109438", "admin", "LrmsjVJB@8^3")
# check_conn()