# servicenow-devinstance-project
## ServiceNow Task Verifier

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

### About The Project :information_source:
ServiceNow Task Verifier gives the opportunity to verify premade tasks on ServiceNow Instance. Different assigments can be coded using PySNC API, which connects to the SNOW Instance and sends queries to the CMDB. Queries can be made to check for specific tables, fields and records and their values. 

### Built With :hammer:
* [PySNC](https://github.com/ServiceNow/PySNC)
* [PySNC Documentation](https://servicenow.github.io/PySNC/)
* [PyQt5 Python Library for Qt Framework](https://doc.qt.io/qtforpython/)
</br>
:warning: To install all the required python libraries you can run 

```
pip install -r REQUIREMENTS
```

### Usage :question:
* After you open the apllication, the first screen you will see is the login form. You should provide the credentials for your ServiceNow instance. To get the credentials open the [Developer Portal](https://developer.servicenow.com/) and login with your account. Then, go to the upper right corner, open your profile and click on "Manage instance password". You should be seeing a similar window
<p align="center">
  <img src="https://github.com/karastoyanov/servicenow-devinstance-project/blob/main/images/ServiceNow%20Instance/Credentials.png" width="500" title="ServiceNow Task Verifier Main Page">
  </p>
* - ServiceNow Instance Name: Only the instance name in format devXXXXXX
* - ServiceNow User Name: Your instance user name
* - ServiceNow Password: Your instance user password
* After you introduce the credentials press the "Login" button. If the credentials are correct, you will sign in the application succsefully. In case that credentials are incorrect, a prompt message will appeat. Keep in mind that to be able to log in, your ServiceNow instance should be running(awake). 
* On the main application window you will find buttons for each of the tasks. Each task have two separate buttons, one to verify the task and the second one to review the task assigment. The user DOESN'T have the possibility to change any of the CMDB values or objects through the application. The ServiceNow Task Verifier would give only the chance to verify if specific table or records is existing.

  <p align="center">
  <img src="https://github.com/karastoyanov/servicenow-devinstance-project/blob/main/images/ServiceNow%20Instance/ServiceNow%20Task%20Verifier.png" width="500" title="ServiceNow Task Verifier Main Page">
  </p>

* If all the assigments for the specific tasks are done correctly on the SNOW Instance, green check mark incon will apear next to the Verify button, in case that the assigment is not done properly, a red X mark icon will appear.

 ### Contributing :computer:
 
 * If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with tags "BUG" for fixing a issue or "REQ" for improving the code. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
 
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


 ### License :scroll:
  * Distributed under the GPL-3.0 license. See `LICENSE` for more information.
  
 ### Contact :mailbox:
  * Aleksandar Karastoyanov - [LinkedIn](https://www.linkedin.com/in/aleksandar-karastoyanov/) - karastoqnov.alexandar@gmail.com
