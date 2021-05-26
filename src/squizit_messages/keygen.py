import requests
import time

url = "https://discord.com/api/v9/channels/844332631876567081/messages"

payload = "{\"content\": \"keygen\", \"tts\": false}"
headers = {
    'user-agent': "vscode-restclient",
    'authorization':
    "mfa.sjimlBXGnW8xr8YHWEtQGp8shrY2oI_yhD_a0FGQn8DyCEf-Eob8Kh8w99VDx9tLm591cN8fQMZCrQVzgw49",
    'content-type': "application/json"
}
for x in range(100):
    response = requests.post(url, data=payload, headers=headers)
    print(response.text, response.status_code)
    time.sleep(61)
