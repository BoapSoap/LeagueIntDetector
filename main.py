from lib.api import get_puuid, get_match_ids_from_puuid, get_match_details
from lib.util import calculate_winrate

#######

print('input summoner name: ')
summoner_name = input()
print('input riot id tag')
summoner_tag = input()

#######

puuid = get_puuid(summoner_name, summoner_tag)
match_ids = get_match_ids_from_puuid(puuid)

#######

winCount = 0 

for match_id in match_ids:
    match_details = get_match_details(match_id)

    player_data = None

    for participant in match_details["info"]["participants"]: #get info from participants (aka players)
        if participant["puuid"] == puuid: #checking if the puuid matches the previously stored puuid 
            player_data = participant
            ingame_name = player_data["summonerName"] #player name
            champion = player_data["championName"]
            kills = player_data["kills"]
            deaths = player_data["deaths"]
            assists = player_data["assists"]
            damage = player_data["totalDamageDealtToChampions"]
            gamemode = match_details["info"]["gameMode"] #taken from the skibidi game toilet 
            soloKills = player_data["challenges"]["soloKills"]
            lane = participant.get("lane", "N/A") #using .get() here because if the lane doesnt exist it will fucking EXPLODE!!!!!!!!!!!
            if player_data["win"]:
                winCount += 1 
                win = "Win" 
            else: 
                win = "Loss"
            print(f"Player: {summoner_name}")
            print(f"Gamemode: {gamemode}")
            print(f"Champion: {champion}")
            print(f"Lane: {lane}")
            print(f"KDA: {kills}/{deaths}/{assists}")
            print(f"Solo kills: {soloKills}")
            print(f"Damage: {damage}")
            print(f"Result: {win}")
            print(f"Match ID: {match_id}")
            print("---------------------------------------------------------------------------")
            break

win_rate = calculate_winrate(winCount, len(match_ids)) # OH MY GREAT SKIBIDI IT WORKS
print(f"{summoner_name} has a winrate of {win_rate}% out of {len(match_ids)} games") #im telling it to print the number of games too so when we send it to ai it know what we yappin about more context
