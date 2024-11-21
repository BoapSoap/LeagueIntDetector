import requests
from dotenv import load_dotenv
import os



load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

HEADERS = {
    "X-Riot-Token": API_KEY,
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com"
}

# API Actions here

def get_puuid(summoner_name, summoner_tag):
    response = requests.get(f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{summoner_tag}", headers=HEADERS)
    if response.status_code == 200:
        summoner_data = response.json()
        return summoner_data["puuid"]
    else:
        raise RuntimeError("Failed to get puuid for", summoner_name, summoner_tag)

def get_match_ids_from_puuid(puuid):
    response = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids", headers=HEADERS)
    if response.status_code == 200:
        match_ids = response.json()
        return match_ids
    else:
        raise RuntimeError("Failed to get match ids for", puuid)
    
def get_match_details(match_id):
    response = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}", headers=HEADERS)
    if response.status_code == 200:
        match_details = response.json()
        return match_details
    else:
        raise RuntimeError("Failed to get match details for", match_id)

