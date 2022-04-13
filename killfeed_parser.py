import requests
import json
import re
from pprint import pprint

CHAT_ID = 931956812834553978

headers = {
    'authorization': 'mfa.__CFah0NieqcM0Ci90X4m7IBkHQztg0KSc_y5bP57Ez3XTrYizvhZoO5l5-lrluTH3b5fSO1OEldnvN_sFlw'
}

def get_jsonn_from_discord_chat(chat_id, headers: dict):
    url = 'https://discord.com/api/v9/channels/{channel_id}/messages'.format(channel_id=CHAT_ID)
    message = requests.get(url, headers=headers)
    jsonn = json.loads(message.text)
    return jsonn

def parse_jsonn_killfeed_obj(jsonn) -> list:
    kills = []
    for value in jsonn:
        # Collect timestamp of kill
        timestamp = value['timestamp']

        # Find out type of death
        death_type = re.search('(?<=KillFeed: )(.*?)(?=!)', str(value))

        # Find out killer and killed
        killer_name = re.search('(?<=Ник: )(.*?)(?= убил)', str(value))

        #killed_name = re.findall('(?<=убил )(.*?)(?= STEAM)', str(value))
        killed_name = re.search('(?<=💀)(.*?)(?=💀)', str(value))

        # Finding coords
        coords = re.findall('\<(.*?)\>', str(value))

        if killer_name and killed_name:
            kills.append((timestamp, death_type[0], killer_name.group(0), killed_name.group(0), coords))
        else: 
            kills.append((timestamp, death_type[0], None, killed_name.group(0), coords))
    return kills


def update():
    import time
    jsonn = get_jsonn_from_discord_chat(CHAT_ID, headers)
    seed_kills = parse_jsonn_killfeed_obj(jsonn)
    seed_timestamps = [] 
    for kill in seed_kills:
        seed_timestamps.append(kill[0]) # timestamp from tuple 

    print(seed_timestamps)

    time.sleep(3)
    tick_no = 0
    while True:
        kills = parse_jsonn_killfeed_obj(get_jsonn_from_discord_chat(CHAT_ID, headers))
        diff = set(seed_timestamps) ^ set(timestamps)
        seed_kills = kills
        seed_timestamps = timestamps
        print("Tick #{no}:".format(no=tick_no), diff)
        time.sleep(5)
        tick_no += 1

if __name__ == "__main__":
    update()

