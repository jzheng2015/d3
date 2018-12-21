# miniproject-ZHENG-JAMES
This mini project is conducted by Stelligent as part of the interview process.
## Project Quick Introduction: 
The project deliverable is a software product, hosted on AWS, which provides a service to other applications or users via an URL. The service provides a message with current time. 

To use the service, send the URL below in a web browser or your applications like this below:
```
https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini
```
And the request above yields a result that looks like this below:
```
{"message": "Automation for the People", "timestamp": "1545375371"}
```
The time displayed above is in a format of UNIX timestamp.

Simply, this service in URL is so called Web Services or little more technical, a RESTful API.

### Quick Test
For a quick test for the service created by the mini project, click <a href="https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini" target="_blank" title="A quick view to the project deliverable at AWS">here</a>, or copy and paste the URL displayed above to your browser's URL input box.

### Further Information
Further information in this document, README.md, will be more technology oriented; it will provide instructional information of the project deployment, testing, and how some software artifacts help to run the service. It also includes instructions to cleanup the service from AWS' running environment, or uninstall the service from AWS.

The document divides its further content into following sections:
* <b>Deploy Service to AWS</b>
* <b>Test and Run Service</b>
* <b>Cleanup Service from AWS</b>
 
The project is designed and implemented in Python scripting language.

## Deploy Service to AWS
The service deployment is in a single command line execution. The command will launch the environment on AWS with all the necessary infrastructures provisioned automatically.

After all prerequisites installed on your deployment platform, executing a single deployment command below to kick off the deployment process:
```
serverless deploy
```
<b>* DO NOT</b> execute the deployment command above now until all prerequsites satisfied on your local computer - the deployment platform.

The prerequisites include a framework named <b>serverless</b> that automates the deployment process by packaging the source code and uploads it to AWS for further provisioning the infrastructures and the service.

Follow steps below to install the prerequisites of the frameworks and the source code before executing the deployment command:
#### Install Frameworks
Install the latest version of <b>nodejs</b> and <b>serverless</b> frameworks; first, install <b>nodejs</b> by executing a command below:
```
sudo yum install nodejs
```
and then, using the package manager to install <b>serverless</b>:
```
npm install -g serverless
```
#### Install AWS Command-Line Interface
The service runs in AWS environment, and <b>serverless</b> interacts with functions facilitated by AWS Command-Line Interface (aws cli) to deploy the service. Make sure you have <i>aws cli</i> installed, and if not, follow general instructions found from the AWS documentation for the installation. 

Also, and more important, make sure that your user profile allowing you to deploy software packages to AWS environment.

#### Prepare Source Code
The source code is stored in a remote repository at <i>github</i>, and the simplest way to prepare the source code on your deployment platform is to use <i>git</i> to clone the source code and its file structure. Or you may manually copy files of the source code form <i>github</i> to your deployment platform.

To clone the source code, making sure that you have <i>git</i> installed; if not, following the general instructions found on the internet for the installtion; and then, execute a command below to clone the source code:
```
git clone https://github.com/stelligent/miniproject-ZHENG-JAMES
```
To manually prepare the source code instead of the clone, copy the files of the source code from the respository and make sure that all the files fall into a file structure below listed below, same as that in <i>github</i>:
```
README.md
mini
  |__ .gitignore
      handler.py
      serverless.yml
```

Now, it comes the final step to deploy the source code to AWS.

Execute a command below to have the command prompt contained within the directory <i>mini</i>:
```
cd mini
```
and then execute the deployment command mentioned before, to start the deployment process if your <i>aws cli</i> user profile is the default in the deployment platform:
```
serverless deploy
```
If your deployment platform has multiple profiles defined in <i>aws cli</i>, append your profile name to the command. For example, if my profile name is <b>jz-aws-user</b>, execute the command by appending the profile name:
```
serverless deploy --aws-profile jz-aws-user
```
The command above uses the <b>serverless</b> framework to kick off the deployment process that automatically promptes AWS to have everything setup the service needs to run.

Upon the successful deployment, you screen should have some information displayed like this below:
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
To test and run the service on LINUX operating system, there are 2 basic types of test methods we can use immediately after the deployment: testing in <b>serverless</b> and testing in <b>curl</b>.

Testing in <b>serverless</b>, execute a command:
```
serverless invoke -f mini
```
In this method, we can have some additional information obtained about the running process by appending a log option like this below:
```
serverless invoke -f mini --log
```
Testing in <b>curl</b>, execute a command:
```
curl -i -X GET https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini
```
<b>NOTE:</b>
The first part of the URL as displayed above, <i>17j9kelj04</i>, is the API identification. Your deployment should have that part different than the one displayed above. 

To get the URL containing the corrent API identification, referrer to the entry listed under <i><b>endpoints</b></i> from the information displayed on your screen after the successful deployment, described in section <b>Deploy Service to AWS</b>.

To run the service in a URL as the RESTful API, a user sends the URL to the AWS host; and then it points to a function that further triggers off a logic process capturing the current time and creating the message as the result back for the user.

In order to have the above running mechanism work, the deployment process packages the source code, including an AWS CloudFormation template and uploads the package to AWS, and the CloudFormation will be further executed by AWS to complete the tasks below:
* Creating an entry at AWS API Gateway
* Creating a Lambada function that registers itself to AWS API gateway
* Creating a bucket in AWS S3 to expose the API in URL

The AWS services created and provisioned above become the primary building blocks or software artifacts that make the service possible.

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


