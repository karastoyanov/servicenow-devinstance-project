 export async function snowConnection(credentials) {
  const sn = require("servicenow-rest-api");
  const ServiceNow = new sn(credentials.instName, credentials.instUserName,credentials.instPassword);
//   const ServiceNow = new sn("dev109438", "admin", "LrmsjVJB@8^3");
  module.exports = { ServiceNow };
  //ServiceNow.Authenticate();
  const connection = ServiceNow.Authenticate();
}
// snowConnection();

// const sn = require("servicenow-rest-api"); // Call the API
// // const ServiceNow = new sn(); // Create SN client with credentials
// const ServiceNow = new sn("dev109438", "admin", "LrmsjVJB@8^3"); // Create SN client with credentials
// module.exports = { ServiceNow }; // Exports the "ServiceNow" variable for later use 
// ServiceNow.Authenticate(); // Authenticate with SNOW instance
