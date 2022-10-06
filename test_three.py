import sys, os
import snow_connection

def verify_task():
    gr = snow_connection.client.GlideRecord("discovery_schedule")
    gr.get("sys_name")
    gr.query()
    is_found_name = False
    while gr.next():
        if gr.get_display_value("sys_name") == "Test Schedule":
            # Intentionally gr.get_display_value("sys_name") is set to "Test Schedule_ERR". In SNOW Instance sys_name \
                #value is "Test Schedule"
            is_found_name = True
            print(f'Task 3: Discovery Schedule <{gr.get_display_value("sys_name")}> found.')
            break
        
    gr = snow_connection.client.GlideRecord("discovery_schedule")
    gr.get("discover")
    gr.query()
    is_found_discover = False
    while gr.next():
        if gr.get_display_value("discover") == "Configuration items":
            is_found_discover = True
            print(f'Task 3: Discovery schedule is set to discover CIs')
            break
    
    gr = snow_connection.client.GlideRecord("discovery_schedule")
    gr.get("disco_run_type")
    gr.query()
    is_found_run_type = False
    while gr.next():
        if gr.get_display_value("disco_run_type") == "Weekly":
            print(f'Task 3: Discovery is set to <Weekly>')
            is_found_run_type = True
            break
            

    gr = snow_connection.client.GlideRecord("discovery_schedule")       
    gr.get("run_dayofweek")
    gr.query()
    is_found_day = False
    while gr.next():
        if gr.get_display_value("run_dayofweek") == "Monday":
            print(f'Task 3: Discovery set to run every Monday')
            is_found_day = True
            break
    
    gr = snow_connection.client.GlideRecord("discovery_range_item")
    gr.get("name")
    gr.query()
    is_range_found = False
    for range in gr:
        if gr.get_display_value("name") =="Test IP Range":
            gr.get("start_ip_address")
            gr.query()
            for start_ip in gr:
                if gr.get_display_value("start_ip_address") == "192.168.0.1":
                    gr.get("end_ip_address")
                    gr.query()
                    for end_ip in gr:
                        if gr.get_display_value("end_ip_address") =="192.168.0.100":
                            gr.get("schedule")
                            for schedule in gr:
                                if gr.get_display_value("schedule") == "Test Schedule":
                                    is_range_found = True
                                    print(f'Task 4: IP range <{gr.get_display_value("name")} found')
                                    break
                            break
                    break
            break

    
    if is_found_name and is_found_discover and is_found_run_type and is_found_day and is_range_found:
        print("Task 3: All found\n")
        return True
    else:
        return False

# Uncomment for debugging purposes only
# verify_task()

application_path = os.path.dirname(sys.executable)