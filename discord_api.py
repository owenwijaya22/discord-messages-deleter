import urllib
from requests.models import PreparedRequest
import requests
import json
import re
from time import sleep as s
import math

headers = {
    'authorization':
    'mfa.ey0chPPIEj7A8czpIo4-CarSbWVP-o2jWeeJAg0IjwrAJbGQjTertifrMrdabCrRi_iWRZq0k7jqDEaaSUzs'
}

def get_channel_id():
    #parsing the channel id
    guild_channel = input('Input the url here: ')
    return guild_channel.split('/')[4:6]


def build_search_url(guild_channel_ids):
    guild_id = guild_channel_ids[-2]
    channel_id = guild_channel_ids[-1]
    author_id = input('Insert author id: ')
    has_link = input('Has link?: ')
    has_file = input('Has file?: ')
    has_params = [x for x in (has_link, has_file) if len(x) != 0]
    base_url = f'https://discord.com/api/v6/guilds/{guild_id}/messages' if guild_id != '@me' else f'https://discord.com/api/v6/channels/{channel_id}/messages'

    params = {
        'channel_id': channel_id,
        'author_id': author_id,
        'sort_by': 'timestamp',
        'sort_order': 'desc',
        'offset': 0,
        'has': has_params
    }

    if guild_id == '@me':
        params.pop('channel_id')
    if len(has_link) == 0 and len(has_file) == 0:
        params.pop('has')
    return base_url + '/search?' + urllib.parse.urlencode(params, doseq=True), channel_id

def build_delete_url(channel_id):
    return f'https://discord.com/api/v6/channels/{channel_id}/messages'

def get_total_messages(search_url):
    #get total messages of the channel
    r = requests.get(search_url, headers=headers)
    data = r.json()
    return data['total_results']

def get_message_id(message_data):
    return [
        message_info['id'] for message_infos in message_data['messages']
        for message_info in message_infos
    ]

def delete(message_id, delete_url):
    for x in message_id:
        r = requests.delete(delete_url + '/' + x, headers=headers)
        s(3)
        if r.status_code == 204:
            print('message found, nice!')
        elif r.status_code == 404:
            print('message not found, check the requirements')
        elif r.status_code == 401:
            print('unauthorized, check the author token')

def recurse_delete(total_messages, delete_url, search_url):
    loop = math.ceil(total_messages/25)
    for x in range(0, loop):
        r = requests.get(search_url, headers=headers)
        data = r.json()
        message_id = get_message_id(data)
        delete(message_id, delete_url)


def main():
    channel_ids = get_channel_id()
    search_url,channel_id = build_search_url(channel_ids)
    print(search_url)
    total_messages = get_total_messages(search_url)
    delete_url = build_delete_url(channel_id)
    recurse_delete(total_messages, delete_url, search_url)

if __name__ == '__main__':
    attempts = int(input('How many time are you going to run the code?: '))
    for x in range(attempts):
        main()