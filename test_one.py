import snow_connection
from pysnc import exceptions

def verify_task():
    gr = snow_connection.client.GlideRecord('u_project_verify')
    
    gr.get('u_description')
    gr.query()
    gr.next()
    gr.state
    gr.get_value('u_description')
    gr.get_display_value('u_description')
    if gr.get_display_value('u_description') == 'Test Task 1':
        pass
    else:
        return False
    
    gr.get('u_short_description')
    gr.query()
    gr.next()
    gr.state
    gr.get_value('u_short_description')
    gr.get_display_value('u_short_description')
    if gr.get_display_value('u_short_description') == 'Test 1':
        pass
    else:
        return False
    
    gr.get('u_assigned_to')
    gr.query()
    gr.next()
    gr.state
    gr.get_value('u_assigned_to')
    gr.get_display_value('u_assigned_to')
    if gr.get_display_value('u_assigned_to') == 'Jason Roy':
        pass
    else:
        return False
    # gr.get('sys_created_on')
    # print("Success")
    return True


verify_task()