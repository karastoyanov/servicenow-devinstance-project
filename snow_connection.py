from pysnc import ServiceNowClient, ServiceNowOAuth2
from pysnc import exceptions


instance = 'dev109438'
user = 'admin'
password = 'LrmsjVJB@8^3'

client = ServiceNowClient(instance, (user, password))

def check_conn():
    try:
        query = client.GlideRecord('sys_user')
        query.get('does not matter') # Really does not matter here
        # print("Success")
        return True
    except exceptions.AuthenticationException as e:
        # print("Failure")
        return False

check_conn()
# def check_conn():
#     instance = 'dev109438'
#     user = 'admin'
#     password = 'LrmsjVJB@8^3'
#     client = ServiceNowClient(instance, (user, password), verify = True)
#     gr = client.GlideRecord('sys_user')
#     gr.get('does not matter') # Really does not matter here
#     if gr.get == True:
#         print("True")
#     print("False")

# try:
#     gr = client.GlideRecord('sys_user')
#     gr.get('does not matter') # Really does not matter here
#     print("Login Successfull")
# except exceptions.AuthenticationException as e:
#     print("Error during authentication")
    
    
# gr = client.GlideRecord('u_project_verify')
# # gr.initialize()

# # gr.get('u_description', 'Example Description 1')
# gr.query()
# while True:
#     gr.next()
#     gr.u_description
#     gr.get_value('u_description')
#     gr.get_display_value('u_description')
#     if gr.get_display_value('u_description') == 'Test':
#         break
#     else:
#         continue

# print(gr.u_description)
# # gr.u_short_description = "Example Problem 3"
# # gr.u_description = "Example Discription"

# # gr.insert()
