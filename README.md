# Build and Validate an Uptime Monitoring Alert System

### Objective

Create an uptime monitoring solution that detects website or application issues before customers report them. This SOP guides a team member through the setup, validation, and alerting workflow so outages, incorrect content, or performance issues can be identified quickly.

### Link to Loom

<https://loom.com/share/03f651c7f1504aaab6060f3650119269>

## Key Steps

**1. Define the business problem and monitoring goal** [0:00](https://loom.com/share/03f651c7f1504aaab6060f3650119269?t=0)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a7ec1169-f035-4afa-80ac-e1a75bc24ef4" />

- Confirm the purpose of the uptime monitor: detect when a site is down, slow, or serving incorrect information.
- Frame the solution as a **blind spot detection** tool that alerts the team before customers notice an issue.
- Identify the main outcomes: 
  - Faster issue detection
  - Reduced customer complaints
  - Better visibility into website health

 

**2. Identify what the monitor should check** [0:46](https://loom.com/share/03f651c7f1504aaab6060f3650119269?t=46)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8b989bee-9c14-431a-b107-03f3b08cb4fc" />

- Determine the key checks the system must perform: 
  - Website availability
  - Page load speed
  - Correct content rendering
  - General system health indicators
- Define what counts as a failure or abnormal condition.
- Decide which metrics will be used to confirm the site is functioning properly.

 

**3. Review the infrastructure and code components** [1:24](https://loom.com/share/03f651c7f1504aaab6060f3650119269?t=84)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3a9c4448-0daa-4ee3-b1ce-c1ab58899363" />

- Inspect the Terraform variables to confirm all required values are defined.
- Review the main Terraform configuration to verify the resources are created correctly.
- Check the Terraform outputs to ensure the deployment exposes the needed values.
- Review the Python logic used in the Logic App to understand how the monitoring workflow executes.

 

**4. Verify the monitoring function app is enabled and running** [1:48](https://loom.com/share/03f651c7f1504aaab6060f3650119269?t=108)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/71e41684-adf9-4c7e-9de5-b3b0ab21f69e" />

- Open the function app or monitoring service used by the solution.
- Confirm the app is enabled.
- Verify the function app is currently running without errors.
- Use this step to ensure the monitoring logic can execute successfully before testing alerts.

 

**5. Validate uptime and health metrics in the monitoring dashboard** [2:17](https://loom.com/share/03f651c7f1504aaab6060f3650119269?t=137)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f5398f51-598e-4b9e-89b2-e315e8f09a73" />

- Open the Application Uptime or monitoring dashboard.
- Review the available health indicators, including: 
  - Overall health
  - Exception rate
  - CPU total
  - Dependency calls
  - Incoming requests
  - Trace activity
- Confirm the dashboard is receiving data and displaying the expected monitoring signals.

 

**6. Confirm the environment is collecting data correctly** [2:42](https://loom.com/share/03f651c7f1504aaab6060f3650119269?t=162)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/042537a8-1a30-40cb-b2be-9c6b2f2df936" />

- Check whether the resource group or monitored environment contains active data.
- If the environment is empty, verify that the monitoring configuration is still correctly deployed.
- Ensure the code is set up to capture and transmit the expected telemetry and health information.

 

**7. Configure and test alert rules** [3:13](https://loom.com/share/03f651c7f1504aaab6060f3650119269?t=193)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/689b2b75-9859-4d2f-8e84-d7e31b37799d" />

- Review the alert rule configuration.
- Set the alert condition to trigger when the server fails or the site crashes.
- Confirm the alert will notify the appropriate person or team when a failure occurs.
- Test the rule to ensure alerts are generated under the correct failure conditions.

 

**8. Confirm the alerting workflow supports proactive response** [3:47](https://loom.com/share/03f651c7f1504aaab6060f3650119269?t=227)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0878bd50-1701-4db5-b15e-0a9c905d2e56" />

- Verify that alerts provide enough information to identify the issue quickly.
- Ensure the notification process helps the team respond before customers report the problem.
- Validate that the monitoring system functions as a proactive blind-spot checker for the business.

### Cautionary Notes

- Do not rely on customer complaints as the first sign of failure; the purpose of this system is early detection.
- Make sure alert thresholds are not too sensitive, or the team may receive unnecessary notifications.
- Confirm all Terraform and application components are deployed consistently; missing configuration can prevent monitoring from working.
- If the dashboard appears empty, verify data collection and telemetry settings before assuming the system is broken.

### Tips for Efficiency

- Start by validating the function app before troubleshooting dashboards or alerts.
- Use the dashboard metrics as a quick health check instead of manually inspecting the site every time.
- Keep alert rules focused on high-impact failures first, then expand to performance and content checks.
- Document the expected behavior for each metric so team members can quickly recognize abnormal patterns.
