import requests
import json
import re
from time import sleep as s
import math
payload = {}

headers = {
        'authorization': 'Nzc4NTM1ODEzNDM2MTQ1Njk2.YDC2ww.vrHd-dDQX1XDweKz48_3IRVzdvg',
    }

def get_channel_id():
    #parsing the channel id
    guild_channel = input('Input the url here: ')
    return re.findall('\d+', guild_channel)

def get_search_url(guild_channel_ids):
    #it's a guild
    if len(guild_channel_ids) > 1:
        guild_id = guild_channel_ids[-2]
        channel_id = guild_channel_ids[-1]
        return f'https://discord.com/api/v6/guilds/{guild_id}/messages/search?channel_id={channel_id}'
    elif len(guild_channel_ids) == 1:
        #it's a dm message
        channel_id = ''.join(guild_channel_ids)
        return f'https://discord.com/api/v6/channels/{channel_id}/messages'

def get_author_id():
    #get author id, returning none if not specified
    author_id = input('Specify the author id? (press enter to skip): ')
    return author_id

def get_author_search_url(author_id, search_url):
    #get the search url combined with the id of the author
    return f"{search_url}/search?author_id={author_id}&sort_by=timestamp&sort_order=desc&offset=0" if len(author_id) > 0 else f'{search_url}/search?sort_by=timestamp&sort_order=desc&offset=0'

def get_total_messages(author_search_url):
    #get total messages of the channel
    r = requests.get(author_search_url, headers=headers)
    data = r.json()
    return data['total_results']

def get_message_id(message_data):
    return [message_info['id'] for message_infos in message_data['messages'] for message_info in message_infos]

def delete(message_id, search_url):
    for x in message_id:
        r = requests.delete(search_url + '/' + x, headers=headers)
        s(1)
        print(r.status_code)

def recurse_delete(total_messages, author_search_url, search_url):
    loop = math.ceil(total_messages/25)
    for x in range(0, loop):
        r = requests.get(author_search_url, headers=headers)
        data = r.json()
        message_id = get_message_id(data)
        delete(message_id, search_url)

def main():
    channel_ids = get_channel_id()
    search_url = get_search_url(channel_ids)
    author_id = get_author_id()
    author_search_url = get_author_search_url(author_id, search_url)
    total_messages = get_total_messages(author_search_url)
    recurse_delete(total_messages, author_search_url, search_url)

if __name__ == '__main__':
    main()