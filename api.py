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

response = requests.get(url,headers=headers) #get from the url using said headers 

if response.status_code == 200:
    summoner_data = response.json() #configure the data into a dictionary 
    print("puuid: ", summoner_data["puuid"]) #parse data because python is godly at that i guess 
    puuid = summoner_data["puuid"] #when you see this anmol just know after this is going to be skibidi ahh code 💀

else: 
    print('shi dont work')  #so basically if you get this that means it didnt work 


matchesUrl = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids" #this is for getting MATCH IDS!
matchResponse = requests.get(matchesUrl, headers=headers) #SKIBIDI TOILETTTTTTTTTTTTTTTTT

if matchResponse.status_code == 200:
    match_data = matchResponse.json() #parse match ids
    print("match ids: ", str(match_data)) #pring that shit 
else:
    print("yo match data broke too lowkey") #this should never happen but if u fuck it up lmk anmol

