# servicenow-devinstance-project
### ServiceNow Task Verifier

<details>
  <summary>Table of Contents</summary>
  <ol>
	<li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project
ServiceNow Task Verifier gives the opportunity to verify premade tasks on ServiceNow Instance. Different assigments can be coded using PySNC API, which connects to the SNOW Instance and sends queries to the CMDB. Queries can be made to check for specific tables, fields and records and their values. 

### Built With
* [PySNC](https://github.com/ServiceNow/PySNC)
* [PySNC Documentation](https://servicenow.github.io/PySNC/)
* [PyQt5 Python Library for Qt Framework](https://doc.qt.io/qtforpython/)

### Usage

* On the main application window you will find buttons for each of the tasks. Each task have two separate buttons, one to verify the task and the second one to review the task assigment. The user DOESN'T have the possibility to change any of the CMDB values or objects through the application. The ServiceNow Task Verifier would give only the chance to verify if specific table or records is existing.

  <p align="center">
  <img src="https://github.com/karastoyanov/servicenow-devinstance-project/blob/main/images/ServiceNow%20Instance/ServiceNow%20Task%20Verifier.png" width="500" title="ServiceNow Task Verifier Main Page">
  </p>

* If all the assigments for the specific tasks are done correctly on the SNOW Instance, green check mark incon will apear next to the Verify button, in case that the assigment is not done properly, a red X mark icon will appear.

 ### Contributing
 * Using PySNC API you could easly create queries to the CMDB and check for specific table, field or record. For more information check <a href="#built-with">Built With</a> section of this file. Simple example of running CMDB query to find "Billie Cowley" user in sys_user table
```python
from pysnc import ServiceNowClient

client = ServiceNowClient('snow instance url address', ('user', 'password'))

gr = client.GlideRecord('sys_user')
gr.get('user_name')
gr.query()
for r in gr:
 if r == 'billie.cowley':
 print(r)
 break
  ```
  
  * For easy of use you can get a specific table field lable from accessing the XML file describing the form. To do that, right click on the Form header and choose 'Show XML'
<p align="center">
  <img src="https://github.com/karastoyanov/servicenow-devinstance-project/blob/main/images/ServiceNow%20Instance/user_name_SNOW_XML.png" width="500" title="XML from sys_user table record">
</p>
