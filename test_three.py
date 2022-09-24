# import snow_connection
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
        
    
    if is_found_name and is_found_discover and is_found_run_type and is_found_day:
        print("Task 3: All found\n")
        return True
    else:
        return False

# Uncomment for debugging purposes only
# verify_task()