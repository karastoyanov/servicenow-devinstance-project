function verifyTask() {
  const { ServiceNow } = require("./servicenowConn.js"); // Import "ServiceNow" variable from servicenowConn.js

  // Get data from table
  ServiceNow.getSampleData('u_project_verify', (res) => {
    for (let i = 0; i < res.length; i++) {
      const object = res[i];
      for (const key in object) {
        // TO DO if-conditions
      }
    }  
  });
}
verifyTask();
