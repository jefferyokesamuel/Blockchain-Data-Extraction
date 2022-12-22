import requests
import csv

cookies = {
    '_ga': 'GA1.2.542201702.1657320687',
}

headers = {
    'authority': 'api.etherscan.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.2.542201702.1657320687',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

params = {
    'module': 'account',
    'action': 'txlist',
    'address': '0xd9ba1Dbe38eB76307ec275F11CEd907033961bA1',
    'startblock': '0',
    'endblock': '99999999',
    'page': '1',
    'offset': '10',
    'sort': 'asc',
    'apikey': 'QXB9ZZ76YPKPPQ7GFS3GI4346R39GNEWPY',
}

response = requests.get('https://api.etherscan.io/api', params=params, cookies=cookies, headers=headers)
myjson = response.json()
ourdata = []

csvheader = ["Hash", "From Address", "To Address", "Value", "Gas Price"]

for x in myjson['result']:
    listing = [x['hash'], x['to'], x['from'], x['value']]
    ourdata.append(listing)

with open('erc20.csv', 'w',encoding="UTF8", newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

print(ourdata)

