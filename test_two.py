import snow_connection

def verify_task():
    gr = snow_connection.client.GlideRecord("sys_user")
    
    gr.get("first_name")
    gr.query()
    is_found_f_name = False
    while gr.next():
        if gr.get_display_value("first_name") == 'John':
            print(f'Task 2: First name is found - {gr.get_display_value("first_name")}')
            is_found_f_name = True
            break
        else:
            continue
    
    gr.get("last_name")
    gr.query()
    is_found_l_name = False
    while gr.next():
        if gr.get_display_value("last_name") == "Doe":
            print(f'Task 2: Last name is found - {gr.get_display_value("last_name")}')
            is_found_l_name = True
            break
        else:
            continue

    gr.get("email")
    gr.query()
    is_found_email = False
    while gr.next():
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
    is_found_user = False
    while gr_two.next():
        if "Test Group" in gr_two.get_display_value("name"):
            print(f'Task 2: Table {gr_two.get_display_value("name")} is found')
            # Table sys_user_grmember stores the mapping of user and group. New GlideRecord client should be created
            gr_three = snow_connection.client.GlideRecord("sys_user_grmember")
            gr_three.fields = 'group, user'
            gr_three.query()
            while gr_three.next():
                gr_three.serialize()
                if gr_three.get_display_value("user") == "John Doe" and gr_three.get_display_value("group") == "Test Group":
                    is_found_user = True
                    print(f'Task 2: User <{gr_three.get_display_value("user")}> is member of Group <{gr_three.get_display_value("group")}>')
                    break
        
    
    if is_found_f_name and is_found_l_name and is_found_email and is_found_user:
        print("Task 2: All found\n")
        return True
    else:
        return False


# Uncomment for debugging purposes only
# verify_task()

