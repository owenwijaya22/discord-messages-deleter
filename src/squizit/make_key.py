import requests
import time
from config import headers

def start_make_key():
    url = "https://discord.com/api/v9/channels/844332631876567081/messages"
    payload = "{\"content\": \"keygen\", \"tts\": false}"
    headers['content-type'] = 'application/json'
    print(headers)
    for _ in range(10):
        response = requests.post(url, data=payload, headers=headers)
        print(response.text, response.status_code)
        time.sleep(61)

if __name__ == "__main__":
    start_make_key()()