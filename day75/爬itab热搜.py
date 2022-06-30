import requests
import json


url = 'https://api.codelife.cc/api/top/list'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',

}
data = {
    id: "mproPpoq6O"
}
resp = requests.post(url, data=data, headers=headers)

json_data = resp.json()
print(json_data)