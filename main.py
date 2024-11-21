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
all_match_data = []  # list to store each match's data
print("hol up yn ts processing...")

for match_id in match_ids:
    match_details = get_match_details(match_id)

    player_data = None

    for participant in match_details["info"]["participants"]:  # get info from participants (aka players)
        if participant["puuid"] == puuid:  # checking if the puuid matches the previously stored puuid
            player_data = participant
            ingame_name = player_data["summonerName"]  # player name
            champion = player_data["championName"]
            kills = player_data["kills"]
            deaths = player_data["deaths"]
            assists = player_data["assists"]
            damage = player_data["totalDamageDealtToChampions"]
            gamemode = match_details["info"]["gameMode"]  # taken from the skibidi game toilet
            soloKills = player_data["challenges"]["soloKills"]
            lane = participant.get("lane",
                                   "N/A")  # using .get() here because if the lane doesnt exist it will fucking EXPLODE!!!!!!!!!!!
            if player_data["win"]:
                winCount += 1
                win = "Win"
            else:
                win = "Loss"

            # Store the information in a dictionary and append to the list
            match_data = {
                "summoner_name": summoner_name,
                "gamemode": gamemode,
                "champion": champion,
                "lane": lane,
                "kills": kills,
                "deaths": deaths,
                "assists": assists,
                "solo_kills": soloKills,
                "damage": damage,
                "result": win,
                "match_id": match_id
            }
            all_match_data.append(match_data)
            break  # exit the inner loop after finding the player

# prints match info after collecting ts
for match in all_match_data:
    print(f"Player: {match['summoner_name']}")
    print(f"Gamemode: {match['gamemode']}")
    print(f"Champion: {match['champion']}")
    print(f"Lane: {match['lane']}")
    print(f"KDA: {match['kills']}/{match['deaths']}/{match['assists']}")
    print(f"Solo kills: {match['solo_kills']}")
    print(f"Damage: {match['damage']}")
    print(f"Result: {match['result']}")
    print(f"Match ID: {match['match_id']}")
    print("---------------------------------------------------------------------------")


win_rate = calculate_winrate(winCount, len(match_ids))  # OH MY GREAT SKIBIDI IT WORKS
print(
    f"{summoner_name} has a winrate of {win_rate}% out of {len(match_ids)} games")  # im telling it to print the number of games too so when we send it to ai it know what we yappin about more context

