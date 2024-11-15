from fastapi import APIRouter, Request
import requests

router = APIRouter(prefix = '/pages' , tags = ['frontend'])

@router.get('/coins')

async def get_home(request: Request):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    params = {
        "vs_currency": "usd",
        "per_page": "50",
        "page": "1",
        "price_change_percentage": "24h",
        "locale": "ru"
    }
    
    response = requests.get(url, params=params)
    dict = {}
    if response.status_code == 200:
        data = response.json()
        for item in data:
            id = item['id']
            name = item['name']
            current_price = item['current_price']
            market_cap = item['market_cap']
            dict[id] = {'name': name, 'current_price': current_price, 'market_cap': market_cap}
        return dict
    else:
        print("Error:", response.status_code)



@router.get('/exchanges')

async def get_exchanges(request: Request):
    url = "https://api.coingecko.com/api/v3/exchanges"
    
    params = {
        "per_page": "50",
        "page": "1",
    }
    
    response = requests.get(url, params=params)
    
    dict = {}
    if response.status_code == 200:
        data = response.json()
        for item in data:
            id = item['id']
            name = item['name']
            description = item['description']
            trust_score = item['trust_score']
            url = item['url']
            dict[id] = {'name': name, 'description': description, 'trust_score': trust_score, 'url': url}
        return dict
    else:
        print("Error:", response.status_code)

@router.get('/nft')

async def get_volume_tradings(request: Request):
    url = "https://api.coingecko.com/api/v3/nfts/list"
    
    params = {
        "per_page": "50",
        "page": "1",
    }
    
    response = requests.get(url, params=params)
    
    dict = {}
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)