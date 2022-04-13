import requests
import json
import re

CHAT_ID = 931956812834553978

headers = {
    'authorization': 'mfa.__CFah0NieqcM0Ci90X4m7IBkHQztg0KSc_y5bP57Ez3XTrYizvhZoO5l5-lrluTH3b5fSO1OEldnvN_sFlw'
}

def get_jsonn_from_discord_chat(chat_id, headers: dict):
    url = 'https://discord.com/api/v9/channels/{channel_id}/messages'.format(channel_id=chat_id)
    message = requests.get(url, headers=headers)
    jsonn = json.loads(message.text)
    return jsonn

def parse_jsonn_killfeed_obj(jsonn) -> list:
    kills = []
    for value in jsonn:
        # Find out type of death
        death_type = re.search('(?<=KillFeed: )(.*?)(?=!)', str(value))

        # Find out killer and killed
        killer_name = re.search('(?<=Ник: )(.*?)(?= убил)', str(value))
        killed_name = re.search('(?<=💀)(.*?)(?=💀)', str(value))

        # Finding coords
        coords = re.findall('\<(.*?)\>', str(value))

        if killer_name and killed_name:
            kills.append((death_type[0], killer_name.group(0), killed_name.group(0), coords))
        else:
            kills.append((death_type[0], None, killed_name.group(0), coords))
    return kills


def look_for_new_kill():
    import time
    seed_kills = parse_jsonn_killfeed_obj(get_jsonn_from_discord_chat(CHAT_ID, headers))

    found_kill = True
    while True:
        kills = parse_jsonn_killfeed_obj(get_jsonn_from_discord_chat(CHAT_ID, headers))

        # Kills are collected as reversed list
        if kills[0] == seed_kills[0]:
            if found_kill:
                found_kill = False
                print("Not found new kill")
        else:
            found_kill = True
            print("Found new kill:", kills[0])
            seed_kills = kills

        time.sleep(3)


if __name__ == "__main__":
    look_for_new_kill()
