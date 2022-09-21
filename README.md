# servicenow-devinstance-project
ServiceNow training and testing environment


### What: ###
  ##### ServiceNow Task Verifier gives the opportunity to verify premade tasks on ServiceNow Instance. Different assigments can be coded using PySNC API, which connects to the SNOW Instance and sends queries to the CMDB. Queries can be made to check for specific tables, fields and records and their values. 
  ##### A brief example of running CMDB query to find "Billie Cowley" user in sys_user table 
  
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
 
  ##### For easy of use you can get a specific table field lable from accessing the XML file describing the form. To do that, right click on the Form header and choose 'Show XML'
