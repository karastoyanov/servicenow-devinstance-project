function testOne() {
  const sn = require("servicenow-rest-api"); // ServiceNow API request

  const ServiceNow = new sn("dev109438", "admin", "LrmsjVJB@8^3"); // Call SNOW client with credentials using the request
  ServiceNow.Authenticate(); // Authentication with provide credentials

  ServiceNow.getSampleData("sys_user", (res) => { // Get data from any table/records
  });

  const fields = [
    "first_name",
    "last_name",
    "email",
    "active",
  ];

  const filters = [
    "first_name=survey",
  ];

  ServiceNow.getTableData(fields, filters, "sys_user", function (res) {
    console.log(res);
  });
}

testOne();
