import requests

URL = 'http://www.daum.net'

respose = requests.get(URL)
respose.status_code
respose.text

print(respose.text)