// function snowConnection() {
//   const sn = require("servicenow-rest-api");
//   const ServiceNow = new sn("dev109438", "admin", "LrmsjVJB@8^3");
//   module.exports = { ServiceNow };
//   //ServiceNow.Authenticate();
//   const connection = ServiceNow.Authenticate();
// }
// snowConnection();

const sn = require("servicenow-rest-api"); // Call the API
const ServiceNow = new sn("dev109438", "admin", "LrmsjVJB@8^3"); // Create SN client with credentials
module.exports = { ServiceNow }; // Exports the "ServiceNow" variable for later use 
ServiceNow.Authenticate(); // Authenticate with SNOW instance
