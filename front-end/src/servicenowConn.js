function snowConnection() {
  const sn = require("servicenow-rest-api");

  const ServiceNow = new sn("dev109438", "admin", "LrmsjVJB@8^3");

  ServiceNow.Authenticate();
  ServiceNow.getSampleData("u_project_verify", (res) => {
    console.log(res);
  });
}

snowConnection();
