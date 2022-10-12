function testOne() {
  const sn = require("servicenow-rest-api"); // ServiceNow API request

  const ServiceNow = new sn("dev109438", "admin", "LrmsjVJB@8^3"); // Call SNOW client with credentials using the request
  ServiceNow.Authenticate(); // Authentication with provided credentials

  ServiceNow.getSampleData("sys_user", (res) => {}); // Get data from any table/records

  // Specify the fields for the query
  const fields = [
    "first_name",
    "last_name",
    "email",
    "active",
  ];

  // Create filters for specific fields and values
  const filters = [
    "first_name=John",
    "last_name=Doe",
  ];

  // Execute query to the CMDB with the fields and filters created above.
  ServiceNow.getTableData(fields, filters, "sys_user", function (res) {
    // console.log(res[0]);
    let queryResult = res[0];
    console.log(queryResult);
  });
}

testOne();
