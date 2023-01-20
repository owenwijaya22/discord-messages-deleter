import aiohttp
import json
import asyncio
import requests
import urllib

with open("./data/data.json", "r") as file:
    data = json.load(file)
    auth_token = data["auth_token"]
    author_id = data["author_id"]


headers = {
    "authorization": auth_token,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
}


def get_id():
    ids = input("Input message link: ").split("/")
    guild_id, channel_id = ids[-3], ids[-2]
    return guild_id, channel_id


def build_search_url(guild_id, channel_id):
    author_id = input("Insert author id: ")
    has_link = input("Has link? (any key for yes/empty for no): ")
    has_file = input("Has file? (any key for yes/empty for no): ")
    params = {
        "channel_id": channel_id or None,
        "author_id": author_id or None,
        "sort_by": "timestamp",
        "sort_order": "desc",
        "offset": 0,
        "has": [x for x in (has_file, has_link) if x],
    }
    base_url = f"https://discord.com/api/v9/guilds/{guild_id}/messages" if guild_id != "@me" else f"https://discord.com/api/v9/channels/{channel_id}/messages"

    params = {k: v for k, v in params.items() if v}
    return base_url + "/search?" + urllib.parse.urlencode(params, doseq=True)

