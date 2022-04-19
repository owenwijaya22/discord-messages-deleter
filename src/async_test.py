import aiohttp
import asyncio
import json
with open('./data/data.json', 'r') as file:
    auth_token = json.load(file)['auth_token']

headers = {'authorization': auth_token}


async def delete_now(delete_url, session):
    print(delete_url)
    async with session.delete(delete_url) as response:
        print(response.status)


async def delete_all(delete_urls, session):
    print(delete_urls)
    tasks = [delete_now(delete_url, session) for delete_url in delete_urls]
    return await asyncio.gather(*tasks)

async def main():
    message_ids = [
        '886129407444545557', '886129074840404030', '886129007492493332',
        '886128971308228648', '886128942120062977', '886128553261940786',
        '886128543925436416', '886128520185655317', '886128435498463264',
        '886128424295489576', '886128420734505000', '886128375142420522',
        '886128335615303731', '886128298713837618', '886128283635290132',
        '886128264412799016', '886128234507403305', '886128206325899275',
        '886128152122912818', '886128145693016115', '886128139883917372',
        '886127828674945024', '886127635225255957', '886127622952718396',
        '886127604783018015'
    ]
    delete_urls = []
    for message_id in message_ids:
        delete_urls.append(
            f"https://discord.com/channels/773916240544137298/messages/{message_id}"
        )
    async with aiohttp.ClientSession() as session:
        statuses = await delete_all(delete_urls, session)

    

asyncio.get_event_loop().run_until_complete(main())