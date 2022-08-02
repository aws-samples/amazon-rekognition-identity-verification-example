import requests
from base64 import b64encode
from json import dumps

SOURCE = 'angela_orth.png'
TARGET = 'NY_Drivers_License_Angela_Orth.png'
URL = " https://3lpjx20498.execute-api.us-east-1.amazonaws.com/prod/ips"
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



