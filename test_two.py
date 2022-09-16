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
    
    if is_found_f_name and is_found_l_name and is_found_email:
        print("Task 2: All found")
        return True
    else:
        return False
    # gr.get('sys_user_group')
    # gr.query()
    # gr.next()
    # gr.state
    # gr.get_value('name')
    # gr.get_display_value('name')
    # if gr.get_display_value('name') == 'Service Desk':
    #     gr.get('sys_user_group.sys_user_grmember.group_list')
    #     gr.query()
    #     gr.next()
    #     gr.state
    #     gr.get_value('sys_user_grmember.group_list')
    #     gr.get_display_value('sys_user_grmember.group_list')
    #     if gr.get_display_value('sys_user_grmember.group_list') == 'John Doe':
    #         pass
    #     else:
    #         return False
    
verify_task()

