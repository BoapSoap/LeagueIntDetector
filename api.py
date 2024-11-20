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

headers = { #USE THIS HEADER FOR ALL THINGS PLEASEPLEASEPLEASPEPLEASEPLEASEPLEASE 🥺🙏
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
    matchIDList = matchResponse.json() #parse match ids
    print(json.dumps(matchIDList, indent=4)) #prints the last 30 matches i think 
else:
    print("yo match data broke too lowkey") #this should never happen but if u fuck it up lmk anmol

print("input the match id you want to view: ")
matchID = input() 
matchIDurl = f"https://americas.api.riotgames.com/lol/match/v5/matches/{matchID}" #same shi diff url type shi 
matchIDresponse = requests.get(matchIDurl, headers=headers) #u know how it is

if matchIDresponse.status_code == 200:
    matchIDdata = matchIDresponse.json()
    #uhhhhh get the player's uuid and parse its data
    #dictionary parsing and some other stuff idk u got it anmol william 🤲🙏📿📿
    player_data = None

    for participant in matchIDdata["info"]["participants"]: #get info from participants (aka players)
        if participant["puuid"] == puuid: #checking if the puuid matches the previously stored puuid 
            player_data = participant
            break

    if player_data:
        ingame_name = player_data["summonerName"] #list of usual stats from a player in a game 
        champion = player_data["championName"]
        kills = player_data["kills"]
        deaths = player_data["deaths"]
        assists = player_data["assists"]
        damage = player_data["totalDamageDealtToChampions"]
        if player_data["win"]:
            win = "Win" 
        else: 
            "Loss"
        print(f"Player: {summoner_name}")
        print(f"Champion: {champion}")
        print(f"KDA: {kills}/{deaths}/{assists}")
        print(f"Damage: {damage}")
        print(f"Result: {win}")
else:
    print("broooooooooooooooo idk how this happened ngl")
