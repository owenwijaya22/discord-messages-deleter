import requests
import json
import re
from time import sleep as s
payload = {}

headers = {
        'authorization': 'Nzc4NTM1ODEzNDM2MTQ1Njk2.YDC2ww.vrHd-dDQX1XDweKz48_3IRVzdvg'
    }

def get_ids():
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
        return f'https://discord.com/api/v6/channels/{channel_id}/messages/search?'

def get_author_id():
    author_id = input('Specify the author id? (press enter to skip): ')
    return author_id

def get_author_search_url(author_id, search_url):
    if author_id == None:
        return f"{search_url}author_id=778535813436145696&sort_by=timestamp&sort_order=desc&offset=0"

def get_total_messages(author_search_url):
    r = requests.get(author_search_url, headers=headers)
    data = r.json()
    return data['total_results']

def get_messages_id(total_messages, author_search_url):
    for x in range(0, total_messages, 25):
        r = requests.get(author_search_url, headers = headers)
        print(r.json())
        with open('raw.json', 'r+', encoding='utf-8') as file:
            file.write(json.dumps(r.json()))

def main():
    ids = get_ids()
    search_url = get_search_url(ids)
    author_id = get_author_id()
    author_search_url = get_author_search_url(author_id, search_url)
    # total_messages = get_total_messages(author_search_url)
    # messages_id = get_messages_id(total_messages, author_search_url)
    # print(messages_id)

if __name__ == '__main__':
    main()