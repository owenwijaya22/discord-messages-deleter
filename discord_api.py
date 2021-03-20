import requests
headers = {
    'authority': 'discord.com',
    'method': 'GET',
    'path': '/api/v6/channels/819189198933458964/messages/search?author_id=778535813436145696&sort_by=timestamp&sort_order=desc&offset=0',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'authorization': 'Nzc4NTM1ODEzNDM2MTQ1Njk2.YDTfkw.jbSYmVAVE95-lz62Gmlq0vGkv84',
    'content-length': '58',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/channels/@me/819189198933458964',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'User-Agent': 'Edg/89.0.774.54',
}
response = requests.get('https://discord.com/api/v6/channels/819189198933458964/messages/search?author_id=778535813436145696&sort_by=timestamp&sort_order=desc&offset=0', headers = headers)
print(response.status_code)
print(response.text)

