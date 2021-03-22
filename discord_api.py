import requests
import json
import re
from time import sleep as s
payload = {}

def search_guild_all_messages():
    #Getting the infos needed
    global channel_id, search_url
    guild, channel_id = ' '.join(re.findall('(\d+)',input('Guild url: '))).split()
    search_url = f'https://discord.com/api/v6/guilds/{guild}/messages/search?channel_id={channel_id}'

def search_dm_all_messages():
    #Getting the infos needed
    global channel_id, search_url
    channel_id = ''.join(re.findall('/?(\d+)', input('Dm url: ')))
    search_url = f"https://discord.com/api/v6/channels/{channel_id}/messages/search?author_id="

def download_all_messages():
    response = requests.get(search_url, headers=headers, data=payload)
    data = json.loads(response.text)
    with open('./raw.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))
        # file.write(json.dumps([x[0]['content'] for x in data['messages']][::-1]))

def get_messages_id():
    response = requests.get(search_url, headers=headers, data=payload)
    data = json.loads(response.text)
    return [x[0]['id'] for x in data['messages']]

def _delete():
    messages_url = f"https://discord.com/api/v6/channels/{channel_id}/messages/"
    while True:
        for x in get_messages_id():
            message_url = messages_url + x
            s(1)
            responses = requests.delete(message_url, headers=headers, data=payload)
            print(responses.status_code)
        get_messages_id()

def send_message():
    response = requests.post('https://discord.com/api/v8/channels/783304248476565524/messages', headers=headers, data={'content': "since you are offline, i'll just send the goodbye from your discord app", 'tts': 'false'})

a = input('Guild or dm?: ')
if a.lower() == 'g':
    search_guild_all_messages()

else:
    search_dm_all_messages()

#Listing all the messages sent by the author

headers = {
    'authorization': 'Mjc0NjM5NDA1MjM3NjY1Nzky.YFcbSA.uNrWdQfqrHV9wvGGT5Ltggo5OJ0',
}

download_all_messages()