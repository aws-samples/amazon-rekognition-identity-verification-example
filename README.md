
# ID Plus Selfie Identity Verification with Amazon Rekognition

A solution to digitally verfiy a users identity using Amazon Rekognition.

Source                     | Target
:-------------------------:|:-------------------------:
![Source](../amazon-rekognition-identity-verification-example/Documentation/readme_images/idplusselfie_dl.jpg) | ![Target](../amazon-rekognition-identity-verification-example/Documentation/readme_images/idplusselfie_selfie.png)
## Flow
A user submits an POST call to a REST api with the source and target. Source being the selfie and target
the users drivers license.  Identity matching occurs on the backend and a confidence percentage is returned.

![Diagram](../amazon-rekognition-identity-verification-example/Documentation/readme_images/idplusselfie_diagram.jpg)

## Deploy the project
This project is available to deploy through AWS CDK <repo link>.  You can clone the repository and use the following CDK process to deploy to your local AWS account.
1. Setup a user who has permissions to programmatically deploy the resources listed above through AWS CDK
2. Setup your AWS CLI configuration - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
3. If this is your first time using CDK go to the following link and follow the prerequisites https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html   
4. Clone the repository <git hub link>
5. Create the virtual environment
   1. If using Windows run the following command in your terminal window from the source of the cloned repository
   .venv\Scripts\activate
   2. If using Mac or Linux run the following command in your terminal window from the source of the cloned repository source
   .venv/bin/activate
6. After activating the virtual environment install the app’s standard dependencies:
python -m pip install -r requirements.txt
7. Now that the environment is setup and the requirements are met we can issue the AWS CDK deployment command to deploy this project to AWS
```
CDK Deploy
```

## Making API Calls
We need to send the payload in base64 format to the rest endpoint.  We use a python file main.py located in the idplusselfie_api directory to make the api call which allows us to open the source and target files, convert them to base64 and send the payload to the api gateway.  

NOTE: The SOURCE and TARGET file locations will be on your local file system and the URL is the Amazon API Gateway url generated during the creation of the project.



Clean Up
We used the AWS CDK to build this project, therefore we can open our project locally and issue the AWS CDK command to clean up the resources.
```
CDK Destroy
```
## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License
This library is licensed under the MIT-0 License. See the LICENSE file.
