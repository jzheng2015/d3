# miniproject-ZHENG-JAMES
This mini project is conducted by Stelligent as part of the interview process.<br />
### Quick Project Introduction: 
The project deliverable is a software product that provides a service to other applications or users via an URL, and displays a message with current time. The applications and users will use a simple URL to query the message, like this below:
```
https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini
```
And the result will be:
```
{"message": "Automation for the People", "timestamp": "1545375371"}
```
The service mention above from the deliverable is so called Web Services or RESTful API, and the time displayed is in a format of UNIX timestmap.<br /><br />
For a quick view of the project deliverable and try the service, click <a href="https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini" target="_blank" title="A quick view to the project deliverable at AWS">here</a>. Or, copy and paste the url displayed above to your browser's URL input box.<br />
The rest of this document, README.md, will be more technology oriented; it provides further information on the project deployment, testing, and some software artifacts in the project design and implementation that make the service available, including instructions to cleanup the running platform on AWS.<br />
The document divides its content into following sections:
* How to deploy the service to AWS
* How to run the service
* How to cleanup the service
## Deploy to AWS
