# API Mini lab Melko Timofey 5030102/20201

This API is designed to provide information about the most popular cryptocurrencies, NFTs and exchange platforms.

# Application deployment and configuration

## Requirements
    Pyhton 3
    Postman

## Instalation
1. Clone the repository:
```
git clone asdasd
```
2. Install requierments
```
pip install -r requirments.txt
```

## Run application

To run the application:

```
uvicorn main:app
```

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