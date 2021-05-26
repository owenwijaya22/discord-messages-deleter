import urllib
import requests
import json
import re
from time import sleep as s
import math

headers = {
    'authorization':
    'mfa.sjimlBXGnW8xr8YHWEtQGp8shrY2oI_yhD_a0FGQn8DyCEf-Eob8Kh8w99VDx9tLm591cN8fQMZCrQVzgw49'
}


def get_channel_id():
    #parsing the channel id
    guild_channel = input('Input the url here: ')
    return guild_channel.split('/')[4:6]


def build_search_url(guild_channel_ids):
    guild_id = guild_channel_ids[-2]
    channel_id = guild_channel_ids[-1]
    max_id = input('Before messages with Id: ')
    min_id = input('After messages with Id: ')
    has_link = input('Has link?: ')
    has_file = input('Has file?: ')
    has_params = [x for x in (has_link, has_file) if len(x) != 0]
    base_url = f'https://discord.com/api/v6/guilds/{guild_id}/messages' if guild_id != '@me' else f'https://discord.com/api/v6/channels/{channel_id}/messages'

    params = {
        'sort_by': 'timestamp',
        'sort_order': 'asc',
        'include_nsfw': True
    }

    if guild_id != '@me':
        params['channel_id'] = channel_id
    if max_id:
        params['max_id'] = max_id
    if min_id:
        params['min_id'] = min_id
    if has_link and has_file:
        params['has'] = has_params

    return base_url + '/search?' + urllib.parse.urlencode(params, doseq=True)


def get_total_messages(search_url):
    #get total messages of the channel
    while True:
        r = requests.get(search_url, headers=headers)
        if r.status_code == 200:
            #channel indexed
            data = r.json()
            return data['total_results']
        elif r.status_code == 202:
            #channel not yet indexed, waiting for 2 second
            print('Channel not yet indexed, please wait for 2000 ms')
            s(2.1)
        elif r.status_code == 404:
            print("Error not found")
            break


def recurse_get_messages(total_messages, search_url):
    all_links = []
    for offset in range(0, total_messages, 25):
        new_param = {
            "offset" : offset
        }
        r = requests.get(search_url, params=new_param ,headers=headers)
        if r.status_code == 429:
            r = requests.get(search_url, params=new_param ,headers=headers)
        else:
            print(r.status_code)
        s(5)
        data = r.json()
        links = get_message_link(data)
        all_links.append(links)
    return all_links

def get_message_link(messages):
    links = []
    try:
        for x in messages['messages']:
            links.append(x[0]["content"])
        return links
    except Exception as e:
        print(e)
        pass
def write_json(all_links, filename='./data/messages.json'):
    with open(filename, 'w') as file:
        json.dump(all_links, file)

def main():
    channel_ids = get_channel_id()
    search_url = build_search_url(channel_ids)
    total_messages = get_total_messages(search_url)
    all_links = recurse_get_messages(total_messages, search_url)
    write_json(all_links)

if __name__ == "__main__":
    main()