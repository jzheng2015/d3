# miniproject-ZHENG-JAMES
This mini project is conducted by Stelligent as part of the interview process.
## Quick Project Introduction: 
The project deliverable is a software product, hosted on AWS, which provides a service to other applications or users via an URL, and displays a message with current time. The applications and users will use a simple URL to query the message, like this below:
```
https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini
```
And the result displayed on your screen will be:
```
{"message": "Automation for the People", "timestamp": "1545375371"}
```
The time displayed is in a format of UNIX timestamp.

Simply, a URL that provides a given service is so called Web Services, or a little more technical, RESTful API.

### Quick Test
For a quick test for the service, click <a href="https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini" target="_blank" title="A quick view to the project deliverable at AWS">here</a>, or copy and paste the URL displayed above to your browser's URL input box.

### Further Information
Further information in this document, README.md, will be more technology oriented; it will provide instructional information of the project deployment, testing, and how some software artifacts help to run the service, including instructions to cleanup the service from AWS' running environment in terms of uninstalling the service.

The document divides its content into following sections:
* <b>Deploy Service to AWS</b>
* <b>Test and Run Service</b>
* <b>Cleanup Service from AWS</b>
 
The project is designed and implemented in Python scripting language.

## Deploy Service to AWS
The service deployment is in a single command line execution to launch the environment deployed on AWS; execute a command listed below to start the deployment after all prerequisites installed on your deployment platform:
```
serverless deploy
```
The prerequisites include a framework named <b>serverless</b> that automates the whole deployment process including packaging the source code and provisioning the necessary infrastructures on AWS.

Follow steps below to install the prerequisites of the frameworks and the source code:
#### Install Frameworks
Install the current <b>nodejs</b> and <b>serverless</b> frameworks; first, install <b>nodejs</b> by executing a command below:
```
sudo yum install nodejs
```
and then, using the package manager to install <b>serverless</b>:
```
npm install -g serverless
```
#### Install AWS Command-Line Interface
The service runs in AWS environment, and using AWS Command-Line Interface - aws cli to deploy the service to AWS. Make sure you have aws cli installed, and if not, follow general instructions found from the AWS documentation to have it installed. Ensure your user profile allowing you to deploy software packages to the AWS environment.

#### Prepare Source Code
The source is stored in a remote repository in <i>github</i>. The simplest way to prepare the source code on your deployment platform is to use <i>git</i> to clone the source code on your local computer - the deployment platform, or you may manually copy files of the source code form <i>github</i> to your local computer.

To clone the source code, making sure that you have <i>git</i> installed; if not, following the general instructions found on the internet to have it installed. Execute a command below to clone the source code:
```
git clone https://github.com/stelligent/miniproject-ZHENG-JAMES
```
To manually copy the files of the source code, make sure that you follow the same file structure, found in <i>github</i>:
```
mini README.md
  |__ .gitignore
      handler.py
      serverless.yml
```

Now, it comes the final step to deploy the source code to AWS.

Execute a command below to have the command prompt within the directory <i>mini</i>:
```
cd mini
```
and then execute a command to start the deployment process if the deployment platform has your user profile setup in aws cli:
```
serverless deploy
```
If your deployment platform has multiple profiles defined in aws cli, append your profile name to the command above. For example, if my profile name is <b>jz-aws-user</b>, execute the command:
```
serverless deploy --aws-profile jz-aws-user
```
After the command above executed, the <b>serverless</b> framework will automatically kick off the deployment process.

Upon success, you screen should have some information like this below:
```
..............................
Serverless: Stack update finished...
Service Information
service: stelligent
stage: dev
region: use-east-1
stack: stelligent-dev
api keys:
   None
endpoints:
   GET - https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini
functions:
   mini
layers:
   None
```
## Test and Run Service
The instruction on testing and running the service is limited on LINUX operating system only.

Basically, there are 2 types of test methods we use to test the service immediately after the deployment; testing in <b>serverless</b> and testing in <b>curl</b>.

Testing in <b>serverless</b>, execute a command:
```
serverless invoke -f mini
```
To have some process information included by the testing result, execute a command:
```
serverless invoke -f mini --log
```
Testing in <b>curl</b>, execute a command:
```
curl -i -X GET https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini
```
<b>NOTE:</b>
The first part of the URL in the command <i>17j9kelj04</i> is the API identification. Your deployment will generate a different API identification. Referrer to the API URL listed under <i><b>endpoints</b></i>, described in section <b>Deploy Service to AWS</b>.

To run the service, a user sends the URL that pointing to the service hosted by AWS API gateway, which further triggers off a function that captures the current time and creates the message back to the user.

In order to have the running mechanisms work as described above, the deployment process packages the source code, including AWS CloudFormation and then uploads the package to AWS that automatically completes the tasks below:
* Creating an entry at AWS API Gateway
* Creating a Lambada function that registers itself to AWS API gateway
* Creating a bucket in AWS S3 to expose the API in URL

The function that captures the current time and creates the message in Python:
```python
import json
import time
def mini( event, context ):
   ct = round( time.time() )
   body = {
      "message": "Automation for the People",
      "timestamp": str( ct )
   }
   
   response = {
      "body": json.dumps( body )
   }
   
   return response
```
## Cleanup Service
To cleanup or uninstall the service from the AWS environment, execute a command below:
```
serverless remove
```
You may log on to AWS Console to ensure everyting being cleaned up by observing AWS services listed below:
* S3
* API Gateway
* Lambada
* CloudFormation

## License
[MIT](https://choosealicense.com/licenses/mit/)


