
# ID Plus Selfie Identity Verification with Amazon Rekognition

The “ID + Selfie” design pattern is the comparison of the face in the selfie to the face(s) on the identification document. For this, we use the Amazon Rekognition CompareFaces API. The API compares a face in the source input image with a face or faces detected in the target input image.
In the example below, we compare a selfie with a sample South Carolina Real ID driver’s license.

Source                     | Target
:-------------------------:|:-------------------------:
![Source](../../../Users/donnoah/Downloads/selfieplusid/Documentation/readme_images/idplusselfie_selfie.png) | ![Target](../../../Users/donnoah/Downloads/selfieplusid/Documentation/readme_images/idplusselfie_dl.jpg)
## Flow
A user submits an POST call to a REST api with the source and target. Source being the selfie and target
the users drivers license.  Identity matching occurs on the backend and a confidence percentage is returned.

![Diagram](../../../Users/donnoah/Downloads/selfieplusid/Documentation/readme_images/idplusselfie_diagram.jpg)

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
CDK Deploy

## Making API Calls
We need to send the payload in base64 format to the rest endpoint.  We use a python file to make the api call which allows us to open the source and target files, convert them to base64 and send the payload to the api gateway.  This code is available in the repository.  

NOTE: The SOURCE and TARGET file locations will be on your local file system and the URL is the Amazon API Gateway url generated during the creation of the project.

```
import requests
from base64 import b64encode
from json import dumps

SOURCE = '<Selfie>.png'
TARGET = <ID Image>.png'
URL = "https://<your api gateway>.execute-api.<region>.amazonaws.com/<deployment slot>/spi"
ENCODING = 'utf-8'
JSON_NAME = 'output.json'

# first: reading the binary stuff
with open(SOURCE, 'rb') as source_file:
    s_byte_content = source_file.read()
with open(TARGET, 'rb') as target_file:
    t_byte_content = target_file.read()

# second: base64 encode read data
s_base64_bytes = b64encode(s_byte_content)
t_base64_bytes = b64encode(t_byte_content)

# third: decode these bytes to text
s_base64_string = s_base64_bytes.decode(ENCODING)
t_base64_string = t_base64_bytes.decode(ENCODING)

# make raw data for json
raw_data = {
    "selfie": s_base64_string,
    "dl": t_base64_string
}

# now: encoding the data to json
json_data = dumps(raw_data, indent=2)

response = requests.post(url=URL, json=json_data)
response.raise_for_status()

print("Status Code", response.status_code)
print("Body ", response.json())

```

Clean Up
We used the AWS CDK to build this project, therefore we can open our project locally and issue the AWS CDK command to clean up the resources.
```
CDK Destroy
```
## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License
This library is licensed under the MIT-0 License. See the LICENSE file.
