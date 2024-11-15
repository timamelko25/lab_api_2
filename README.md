# API Mini lab Melko Timofey 5030102/20201

This API is designed to provide information about the most popular cryptocurrencies, NFTs and exchange platforms.

# Application deployment and configuration

## Requirements
    Python 3
    Postman

## Installation
1. Clone the repository:
```
git clone https://github.com/timamelko25/lab_api_2.git
```
2. Install requirements
```
pip install -r requirements.txt
```

## Run application

To run the application:

``` uvicorn main:app ```

# Endpoints

## NFT
- **Endpoint**: ```/pages/nft```
- **Description**: Get supported NFTs with id, contract address, name, asset platform id and symbol.

## Exchanges
- **Endpoint**: ```/pages/exchanges```
-  **Description**: Get the supported exchanges with exchanges’ data.

## Coins
- **Endpoint**: ```/pages/coins```
- **Description**: Get the most popular crypto with name, price and market cap.
# Postman

Postman workplace: [click](https://www.postman.com/lunar-module-administrator-67308313/minilabapi224/collection/o9fxbq8/get-requests)