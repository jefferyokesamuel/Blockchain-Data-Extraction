import requests
import csv
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'https://github.com/tronscan/tronscan-frontend/blob/dev2019/document/api.md',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'sort': '-timestamp',
    'count': 'true',
    'limit': '20',
    'start': '0',
    'address': 'TR9octGKwGi8EaBhphP8d8D6dTkSyMJKXW',
}

response = requests.get('https://apilist.tronscan.org/api/transaction', params=params, headers=headers)

myjson = response.json()
ourdata = []
csvheader = ["OwnerAddress", "ToAddress", "Result", "Amount"]

for x in myjson['data']:
    listing = [x['ownerAddress'], x['toAddress'], x['result'], x['amount']]
    ourdata.append(listing)

with open('crypto.csv', 'w',encoding="UTF8", newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

print('done')
