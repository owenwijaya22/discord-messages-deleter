import aiohttp
import json
import urllib
import asyncio
import math
import requests
from time import sleep
with open('./data/data.json', 'r') as file:
    auth_token = json.load(file)['auth_token']

headers = {'authorization': auth_token}


def get_channel_ids():
    ids = input("Input message link: ").split('/')
    guild_id, channel_id = ids[-2], ids[-1]
    return guild_id, channel_id


def build_search_url(guild_id, channel_id):
    with open('./data/data.json', 'r') as file:
        author_id = json.load(file)['author_id']
    params = {'author_id': author_id, 'offset': 0}
    if guild_id == '@me':
        base_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    else:
        base_url = f'https://discord.com/api/v9/channels/{guild_id}/messages'

    return base_url + '/search?' + urllib.parse.urlencode(params, doseq=True)


def get_messages(search_url):
    response = requests.get(search_url, headers=headers)
    if response.status == 202:
        wait_for_indexing = response.json()['retry_after']
        print(
            f"This channel wasn't indexed yet, waiting {wait_for_indexing}s for discord to index it..."
        )
        sleep(wait_for_indexing)
        return get_messages(search_url)
    elif response.status != 200:
        if response.status == 429:
            wait_for_indexing = response.json()['retry_after']
            print(
                f"Being rate limited by Discord's API for {wait_for_indexing}s"
            )
            asyncio.sleep(wait_for_indexing * 2)
            return get_messages(search_url)
        else:
            print(
                f"Error searching messages, API responded with status {response.status}"
            )
    data = response.json()
    return data


def get_messages_id(message_data):
    return [
        message_info['id'] for message_infos in message_data['messages']
        for message_info in message_infos
    ]


def get_messages_id(message_data):
    return [
        message_info['id'] for message_infos in message_data['messages']
        for message_info in message_infos
    ]


async def delete_message(delete_url, session):
    async with session.delete(delete_url, headers=headers) as response:
        if response.status != 200:
            if response.status == 429:
                wait_for_indexing = (await response.json())['retry_after']
                print(
                    f"Being rate limited by Discord's API for {wait_for_indexing}s"
                )
                asyncio.sleep(wait_for_indexing * 2)
                return await delete_message(delete_url, session)
            else:
                print(
                    f"Error searching messages, API responded with status {response.status}"
                )
        else:
            print(response.status)


async def recurse_delete(channel_id, search_url):
    delete_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    total_data = requests.get('search_url')
    total_messages = total_data['total_results']
    loops = math.ceil(total_messages / 25)
    async with aiohttp.ClientSession() as session:
        for _ in range(0, loops):
            messages_data = get_messages(search_url)
            messages_id = get_messages_id(messages_data)
            delete_urls = []
            for message_id in messages_id:
                delete_urls.append(delete_url + '/' + message_id)
            #delete messages
            delete_tasks = [
                delete_message(delete_url, session)
                for delete_url in delete_urls
            ]
            await asyncio.gather(*delete_tasks)


# def write_data(file_path, data):
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)


def main():
    guild_id, channel_id = get_channel_ids()
    search_url = build_search_url(guild_id, channel_id)
    asyncio.get_event_loop().run_until_complete(recurse_delete(channel_id, search_url))
    # write_data('./data/messages.json', data)


main()