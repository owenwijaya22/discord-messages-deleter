import requests
import random


def choose_token():
    token = random.choice([
        "ODEzNzAyMDg1NTA5Nzc1Mzcw.YcAm7w.ie_QO2nhvWi5i5R6XqLq164JKZo",
        "Nzc4NTM1ODEzNDM2MTQ1Njk2.YcgVlw.6Rr0qHMUHWdI0CjedkvdVA9Dbu4"
    ])
    return token


def choose_url():
    subject = input('Math (m) or Physics (p): ')
    if subject == 'm':
        url = "https://discord.com/api/v9/channels/641351235215294486/messages"
    elif subject == 'p':
        url = "https://discord.com/api/v9/channels/536995799859724309/messages"
    return url


def main():
    url = choose_url()
    token = choose_token()
    payload = "{\"content\":\"<@!300506208832585728> thank you\",\"nonce\":\"923027088506617856\",\"tts\":false}"
    headers = {'authorization': token, 'content-type': "application/json"}
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


main()