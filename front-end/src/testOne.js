function testOne() {
  const sn = require("servicenow-rest-api"); // ServiceNow API request

  const ServiceNow = new sn("dev109438", "admin", "LrmsjVJB@8^3"); // Call SNOW client with credentials using the request
  ServiceNow.Authenticate(); // Authentication with provide credentials

  ServiceNow.getSampleData("u_project_verify", (res) => { // Get data from any table/record
    console.log(res);
    //for (const [key, value] of Object.entries(res)) {
    //console.log(key + ":" + value);
    //}
  });
}

testOne();
