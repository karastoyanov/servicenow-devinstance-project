import snow_connection
import sys, os

def verify_task():
    gr = snow_connection.client.GlideRecord("u_project_verify")
    gr.get("u_description")
    gr.query()
    is_description_found = False
    for r in gr:
        gr.get_display_value("u_description")
        if "Test Task 1" in gr.get_display_value("u_description"):
            print(f'Task 1: Field <Description> with value {gr.get_value("u_description")} found')
            is_description_found = True
            break
        else:
            continue

    gr = snow_connection.client.GlideRecord("u_project_verify")
    gr.get("u_short_description")
    gr.query()
    is_short_description_found = False
    for r in gr:
        gr.get_display_value("u_short_description")
        if gr.get_display_value("u_short_description") == 'Test 1':
            print(f'Task 1: Field <Short description> with value {gr.get_display_value("u_short_description")} found')
            is_short_description_found = True
            break
        else:
            continue
        
    gr = snow_connection.client.GlideRecord("u_project_verify")
    gr.get('u_assigned_to')
    gr.query()
    is_assigned_to_found = False
    for r in gr:
        gr.get_display_value('u_assigned_to')
        if gr.get_display_value('u_assigned_to') == 'Jason Roy':
            print(f'Task 1: Field <Assigned to> with value' \
                f' {gr.get_display_value("u_assigned_to")} found')
            is_assigned_to_found = True
            break
        else:
            continue

    if is_description_found and is_short_description_found and is_assigned_to_found:
        print("Task 1: All found\n")
        return True
    else:
        return False
        

# Uncomment for debugging purposes only
# verify_task()
application_path = os.path.dirname(sys.executable)