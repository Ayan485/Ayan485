from urllib import response
from wsgiref import headers
import requests

API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = '976809093249527848'
CLIENT_SECRET = '7SiW9F65PzQXZbo28a0bnOsrXdsjVLyz'
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
    url = API_ENDPOINT + "/guilds/976823169228873729/members/" + userID
    botToken = 'OTc2ODA5MDkzMjQ5NTI3ODQ4.GtHEYQ.DpDULpD_KCDxpLmo8XmXws8R87YSimyeEpebD0'

    data = {
       "acces_token": access_token 
    }
    headers = {
        'authorization': "Bot" + botToken,
        'Content-Type': 'application/json'
    }
    response = requests.post(url = url, headers=headers, json=data)
    print(response.text)

code = exchange_code('AxS8rpS7RT8kaJFBwd5YnO8nHWIAZj')['access_token']
print(code)
add_to_guild(code, '731761525005615155')