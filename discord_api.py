import requests
import json
import re

a = input('Guild or dm?: ')
if a.lower() == 'g':
    guild = input('Guild url: ')
    guild, channel_id = ' '.join(re.findall('(\d+)', guild)).split()
    search_url = f'https://discord.com/api/v6/guilds/{guild}/messages/search?author_id=778535813436145696&channel_id={channel_id}&sort_by=timestamp&sort_order=desc&offset=0'
elif a.lower() == 'd':
    channel_id = input('Url: ')
    channel_id = ''.join(re.findall('(\d+)', channel_id))
    search_url = f"https://discord.com/api/v6/channels/{channel_id}/messages/search?author_id=778535813436145696&sort_by=timestamp&sort_order=desc&offset=0"
url = f"https://discord.com/api/v6/channels/{channel_id}/messages/"
payload = {}
headers = {
    'authorization':
    'Nzc4NTM1ODEzNDM2MTQ1Njk2.YDTfkw.jbSYmVAVE95-lz62Gmlq0vGkv84',
}


def _delete():
    for x in messages:
        message_url = url + x
        print(message_url)
        responses = requests.delete(message_url, headers=headers, data=payload)
        print(response.status_code)


response = requests.get(search_url, headers=headers, data=payload)
data = json.loads(response.text)
messages = [x[0]['id'] for x in data['messages']]
_delete()