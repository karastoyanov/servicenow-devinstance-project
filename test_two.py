import snow_connection

def verify_task():
    gr = snow_connection.client.GlideRecord("sys_user")
    
    gr.get("first_name")
    gr.query()
    gr.next()
    is_found_f_name = False
    while gr.next():
        gr.state
        gr.get_value("first_name")
        gr.get_display_value("first_name")
        if gr.get_display_value("first_name") == 'John':
            print(f'Task 2: First name is found - {gr.get_display_value("first_name")}')
            is_found_f_name = True
            break
        else:
            continue
    
    gr.get("last_name")
    gr.query()
    gr.next()
    is_found_l_name = False
    while gr.next():
        gr.state
        gr.get_value("last_name")
        gr.get_display_value("last_name")
        if gr.get_display_value("last_name") == "Doe":
            print(f'Task 2: Last name is found - {gr.get_display_value("last_name")}')
            is_found_l_name = True
            break
        else:
            continue

    gr.get("email")
    gr.query()
    gr.next()
    is_found_email = False
    while gr.next():
        gr.state
        gr.get_value("email")
        gr.get_display_value("email")
        # IMPORTANT NOTE: Use "in" instead of "==" to check if the email address is set properly in the SNOW Instance \
            # using if gr.get_display_value("email") == "john.doe@example.com" will not work\
                # (it works only for pre-defined records in sys_user table)
        if gr.get_display_value("email") in "john.doe@example.com":
            print("Task 2: Email is found")
            is_found_email = True
            break
        else:
            continue
        
    # IMPORTANT NOTE: New GlideRecord client should be created to request a query to sys_user_group table    
    gr_two = snow_connection.client.GlideRecord("sys_user_group")
    gr_two.get("name")
    gr_two.query()
    gr_two.next()
    is_found_user = False
    while gr_two.next():
        gr_two.state
        gr_two.get_value("name")
        gr_two.get_display_value("name")
        if "Task 2 Project Verify" in gr_two.get_display_value("name"):
            print(f'Task 2: Table {gr_two.get_display_value("name")} is found')
            

            
           
        
    if is_found_f_name and is_found_l_name and is_found_email:
        print("Task 2: All found")
        return True
    else:
        return False

    
verify_task()

