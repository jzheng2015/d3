# miniproject-ZHENG-JAMES
This mini project is conducted by Stelligent as part of the interview process.
## Quick Overview: 
The project deliverable is a software product, hosted on AWS, which provides a service to other applications or users via an URL request. The service provides a message with current time. 

To use the service, type the URL in a web browser's url input box, or program the URL into your application to request the service, like this below:
```
https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini
```
The request above yields a result that looks like this:
```
{"message": "Automation for the People", "timestamp": "1545375371"}
```
The time displayed in the result above is in a format of UNIX timestamp.

Simply, this service in URL is so called Web Services or little more technical, a RESTful API.

The service URL specified above, is also referred to as the HTTP endpoint.

### Quick Test in Automation
For a quick test of the service, click <a href="https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini" target="_blank" title="A quick view to the project deliverable at AWS">here</a>.

Notice the difference of the timestamps on the message; it captures the moment when the request received by the service.

### Further Information
Further information in this document, README.md, will be more technology oriented; it will provide instructional information of the project deployment, testing, and how some software artifacts help to run the service. It also includes instructions to cleanup the service from AWS' running environment, or uninstall the service from AWS.

The document divides its further content into following sections:
* <b>Deploy Service to AWS</b>
* <b>Test and Run Service</b>
* <b>Cleanup Service from AWS</b>
 
The project is designed and implemented in Python scripting language.

## Deploy Service to AWS
The service deployment is in a single command line execution, like this below:
```
serverless deploy
```
The deployment command above will launch the environment on AWS with all the necessary infrastructures provisioned automatically.

<b>* DO NOT</b> execute the deployment command now, until all the deployment prerequsites satisfied on your local computer - the deployment platform.

The prerequisites include a framework named <b>serverless</b> that automates the deployment process by packaging the source code and uploads it to AWS that further provisions service infrastructure and sets up the HTTP endpoint, automatically.

Follow steps below to prepare the prerequisites and the source code on your deployment platform before executing the deployment command:
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
The service runs in AWS environment, and all its running infrastructures will be created or provisioned through the use of <b>AWS Command-line Interface</b> (aws cli) during the deployment process, handled by <b>serverless</b> framework. We work with <b>serverless</b> functions directly, and the functions transparently interact with <i>aws cli</i> APIs to create and provision the running infrastructures. So, make sure that your deployment platform has <i>aws cli</i> installed, and if not, follow general instructions found from the AWS documentation for the installation. 

Also, and more important, make sure that your user profile, created in AWS IAM service, allowing you to deploy software packages to AWS environment.

#### Prepare Source Code
The source code is stored in a remote repository at <i>github</i>. The simplest way to prepare source code is to clone the respository to your deployment platform. Or, you may manually copy files of the source code form <i>github</i> repository to your deployment platform.

To clone the source code, make sure that you have <i>git</i> installed; if not, follow the general instructions to have it installed. Then, execute a command below to clone the source code:
```
git clone https://github.com/stelligent/miniproject-ZHENG-JAMES
```
To manually prepare the source code instead of the cloning, copy the files of the source code from the respository and make sure that all the files fall into a file structure exactly as it listed below, same as that in <i>github</i>:
```
README.md
mini
  |__ .gitignore
      handler.py
      serverless.yml
```

Now, it comes the final step to deploy the source code to AWS.

#### Execute Single Deployment Command
First, change the directory at the command line to the repository, a file directory named <b>mini</b>:
```
cd mini
```
and then, execute the deployment command as mentioned before:
```
serverless deploy
```
The deployment command depends on your AWS user profile, configured by <i>aws cli</i>. If the defult profile used by <i>aws cli</i> is not allowed to deploy packages to AWS, you need to specify one that is allowed to do that. For example, if my profile name is <b>jz-aws-user</b>, execute the command by appending the profile name as one of the optinal command-line input parameters, like this below:
```
serverless deploy --aws-profile jz-aws-user
```
Upon the success, the deployment returns some information on your screen; a part of the information looks like this below:
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
Notice the URL, listed under <b>endpoints</b>; that is the service URL - the RESTful API which is the HTTP endpoint the serve is going to send users' requests to for the message along with a timestamp.

## Test and Run Service
To test and run the service on LINUX operating systems, <b>serverless</b> provides a easy way to test it, immediately after the successful deployment. Also, executing a LINUX command in <b>curl</b> does the same.

The easy way to test the service in <b>serverless</b>, execute a command:
```
serverless invoke -f mini
```
Attaching an optinal command-line input parameter, we can have some additional information obtained, like this:
```
serverless invoke -f mini --log
```
The LINUX command to test the service in <b>curl</b>, execute a command:
```
curl -i -X GET https://17j9kelj04.execute-api.us-east-1.amazonaws.com/dev/mini
```
<b>NOTE:</b>
The first part of the URL, observed, <i>17j9kelj04</i>, is the identification for any given of the RESTful API. Your deployment should have a one that is different from the URL above. 

### How Service Runs
The service runs when its HTTP endpoint hosted by AWS API Gateway receives the service request by the URL, and then, the host forwards the request to an AWS Lambda function that captures the current time and creates the message as the service result back for the user.

The service running infrastructure includes the followins:
* AWS API Gateway, pointing the service HTTP endpoint
* Lambada function, executing the logics capturing the time and creating the message
* AWS S3, housing the actual URL and the code-base of the logics

All those AWS services as the service running infrastructure are considered as the software artifacts or building blocks in design, which constructe the service. Or simply, the AWS running environment.

The AWS running environment is created and provisioned by <i>aws cli</i> in an AWS <b>CloudFormation</b> template. The template is created when <b>serverless</b> runs the deployment process and interacts with <i>aws cli</i>.

The code-base of the logics, that captures the current time and creates the message in Python:
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


