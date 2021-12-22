import requests


def choose_url():
    subject = input('Math (m) or Physics (p): ')
    if subject == 'm':
        url = "https://discord.com/api/v9/channels/641351291343208448/messages"
    elif subject == 'p':
        url = "https://discord.com/api/v9/channels/536995799859724309/messages"
    return url


def main():
    url = choose_url()
    payload = "{\"content\":\"<@!300506208832585728> thank you\",\"nonce\":\"923027088506617856\",\"tts\":false}"
    headers = {
        'user-agent': "vscode-restclient",
        'authorization':
        "ODEzNzAyMDg1NTA5Nzc1Mzcw.YcAm7w.ie_QO2nhvWi5i5R6XqLq164JKZo",
        'content-type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


main()