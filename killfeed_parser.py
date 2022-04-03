import requests
import json
import re

CHAT_ID = 931956812834553978

headers = {
    'authorization': 'mfa.__CFah0NieqcM0Ci90X4m7IBkHQztg0KSc_y5bP57Ez3XTrYizvhZoO5l5-lrluTH3b5fSO1OEldnvN_sFlw'
}

url = 'https://discord.com/api/v9/channels/{channel_id}/messages'.format(channel_id=CHAT_ID)
message = requests.get(url, headers=headers)
jsonn = json.loads(message.text)

counter = 0
for value in jsonn:
    print(value)
    # Find out type of death
    death_type = re.findall('(?<=KillFeed: )(.*?)(?=!)', str(value))
    print(death_type[0])

    # Find out killer and killed
    killer_name = re.findall('(?<=Ник: )(.*?)(?= убил)', str(value))
    print("Killer: {}".format(killer_name))

    #killed_name = re.findall('(?<=убил )(.*?)(?= STEAM)', str(value))
    killed_name = re.findall('(?<=💀)(.*?)(?=💀)', str(value))
    print("Killed: {}".format(killed_name))

    # Finding coords
    coords = re.findall('\<(.*?)\>', str(value))
    print(coords)
    print('\n')
