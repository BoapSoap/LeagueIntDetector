import requests 
import json 
from dotenv import load_dotenv 
import os 

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

print('input summoner name: ')
summoner_name = input()
print('input riot id tag')
tag_line = input() 


url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"

headers = { 
    "X-Riot-Token": API_KEY,
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com"
}

response = requests.get(url,headers=headers)

if response.status_code == 200:
    summoner_data = response.json()
    print("puuid: ", summoner_data["puuid"])
    puuid = summoner_data["puuid"]
else: 
    print('shi dont work')


