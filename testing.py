import requests
import json
import pandas as pd


urls = 'https://websummit.com/startups/featured-startups'
def request():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://websummit.com',
        'Referer': 'https://websummit.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '{"requests":[{"indexName":"Avenger_Appearance_production","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=48&tagFilters=%5B%22ws23%22%5D&page=0&query=&maxValuesPerFacet=100&facets=%5B%22country%22%2C%22industry%22%5D"}]}'

    response = requests.post(
        'https://x0o1h31a99-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.4.0)%3B%20Browser%20(lite)%3B%20JS%20Helper%20(3.5.5)%3B%20react%20(17.0.2)%3B%20react-instantsearch%20(6.12.1)&x-algolia-api-key=ZGRjYzdjYmNmMGJiNjFhNmYwNzQ5YjdhOWUwYWQ0OTJkNDIyOTI1NzIyMmUwYzQzMzgwMWIxM2E1NDg5YjFiYWZpbHRlcnM9X3RhZ3MlM0F3czIzK0FORCslMjh0cmFjayUzQUdST1dUSCtPUit0cmFjayUzQUJFVEErT1IrdHJhY2slM0FBTFBIQSUyOSZyZXN0cmljdEluZGljZXM9JTVCJTIyQXZlbmdlcl9BcHBlYXJhbmNlX3Byb2R1Y3Rpb24lMjIlNUQ%3D&x-algolia-application-id=X0O1H31A99',
        headers=headers,
        data=data,
    )
    data_respon = response.text
    return data_respon

def parsing_data():
    html = request()
    with open("HTML/websummit.html", "+w", encoding="utf-8") as f:
        f.write(html)

if __name__ == '__main__':
    parsing_data()
