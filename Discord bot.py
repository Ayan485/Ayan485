from urllib import response
from wsgiref import headers
import requests

API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = 'Enter Id'
CLIENT_SECRET = 'Enter Secret Id'
REDIRECT_URI = "https://google.com"

def exchange_code(code):
    data = {
        'client_id' : CLIENT_ID,
        'client_secret' : CLIENT_SECRET,
        'grant_type' : 'authorization_code',
        'code' : code,
        'redirect_uri' : REDIRECT_URI
    }
    headers = {
        'Content_Type' : 'application/x-www-form-urlencoded'
    }
    r= requests.post(API_ENDPOINT + '/oauth2/token', data=data, headers=headers)
    return r.json

def add_to_guild(access_token, userID):
    url = API_ENDPOINT + "enter guild id" + userID
    botToken = 'Enter Token'

    data = {
       "acces_token": access_token 
    }
    headers = {
        'authorization': "Bot" + botToken,
        'Content-Type': 'application/json'
    }
    response = requests.post(url = url, headers=headers, json=data)
    print(response.text)

code = exchange_code('enter token')['access_token']
print(code)
add_to_guild(code, 'enter id')
