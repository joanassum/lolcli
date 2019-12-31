import click
import requests
import os
import runes_storage

from pprint import pprint
from PyInquirer import prompt

@click.group()
def lolcli():
    """A CLI for League of Legends."""

api_key = os.environ['LOLCLI_APIKEY']
lol_endpoints = {
    "ru": "https://ru.api.riotgames.com",
    "kr": "https://kr.api.riotgames.com",
    "br": "https://br1.api.riotgames.com",
    "oc": "https://oc1.api.riotgames.com",
    "jp": "https://jp1.api.riotgames.com",
    "na": "https://na1.api.riotgames.com",
    "eun": "https://eun1.api.riotgames.com",
    "euw": "https://euw1.api.riotgames.com", 
    "tr": "https://tr1.api.riotgames.com",
    "la": "https://la1.api.riotgames.com",
    "la1": "https://la1.api.riotgames.com",
    "la2": "https://la2.api.riotgames.com",
}
champions_endpoint = "http://ddragon.leagueoflegends.com/cdn/9.24.2/data/en_US/champion.json"

@lolcli.command()
@click.option('-r', '--region', type=click.STRING, default="euw", help="region of the server. (default to euw)")
def freechamp(region):
    """Getting free-to-play champion rotation"""
    # Get all champions
    champions = list(requests.get(url = champions_endpoint).json()["data"].values())

    params = {'api_key': api_key}
    if region not in lol_endpoints:
        print(region + " is nos a valid region")
        print("List or supported regions: " + str(list(lol_endpoints.keys())))
        return
    url = lol_endpoints[region] + "/lol/platform/v3/champion-rotations"
    free_champ_ids = requests.get(url = url, params = params).json()['freeChampionIds']
    free_champs = [ champ['id'] for champ in champions if int(champ['key']) in free_champ_ids]
    print(free_champs)

paths = ['Precision','Domination','Sorcery','Resolve','Inspiration']

slot1 = {
    "Precision": ["Overheal", "Triumph", "Presence of Mind"],
    "Domination": ["Cheap Shot", "Taste of Blood", "Sudden Impact"],
    "Sorcery": ["Nullifying Orb", "Manaflow Band", "Nimbus Cloak"],
    "Resolve": ["Demolish", "Font of Life", "Shield Bash"],
    "Inspiration": ["Hextech Flashtraption", "Magical Footware", "Perfect Timing"],
}
slot2 = {
    "Precision": ["Legend: Alacrity", "Legend: Tenacity", "Legend: Bloodline"],
    "Domination": ["Zombie Ward", "Ghost Poro", "Eyeball Collection"],
    "Sorcery": ["Transcendence", "Celerity", "Absolute Focus"],
    "Resolve": ["Conditioning", "Second Wind", "Bone Plating"],
    "Inspiration": ["Future's Market", "Minion Dematerializer", "Biscuit Delivery"],
}
slot3 = {
    "Precision": ["Coup de Grace", "Cut Down", "Last Stand"],
    "Domination": ["Ravenous Hunter", "Ingenious Hunter", "Relentless Hunter", "Ultimate Hunter"],
    "Sorcery": ["Scorch", "Waterwalking", "Gathering Storm"],
    "Resolve": ["Overgrowth", "Revitalize", "Unflinching"],
    "Inspiration": ["Cosmic Insight", "Approach Velocity", "Time Warp Tonic"],
}

def get_keystones(answers):
    keystones = {
        "Precision": ["Press the Attack", "Lethal Tempo", "Fleet Footwork", "Conqueror"],
        "Domination": ["Electrocute", "Predator", "Dark Harvest", "Hall of Blades"],
        "Sorcery": ["Summon Aery", "Arcane Comet", "Phase Rush"],
        "Resolve": ["Grasp of the Undying", "Aftershock", "Guardian"],
        "Inspiration": ["Glacial Augment", "Unsealed Spellbook", "Prototype: Omnistone"],
    }
    return keystones[answers['primarypath']]

def get_primary_slot1(answers):
    return slot1[answers['primarypath']]

def get_primary_slot2(answers):
    return slot2[answers['primarypath']]

def get_primary_slot3(answers):
    return slot3[answers['primarypath']]

def get_secondary_path(answers):
    return [x for x in paths if x != answers['primarypath']]

def get_secondary_slot1(answers):
    return slot1[answers['secondarypath']] + slot2[answers['secondarypath']] + slot3[answers['secondarypath']]

def get_secondary_slot2(answers):
    all_slots = slot1[answers['secondarypath']] + slot2[answers['secondarypath']] + slot3[answers['secondarypath']]
    return [x for x in all_slots if x != answers['secondaryslot1']]

@lolcli.command()
@click.argument('name', type=click.STRING)
def addrunes(name):
    questions = [
        {
            'type': 'list',
            'name': 'primarypath',
            'message': 'Primary Path?',
            'choices': paths
        },
        {
            'type': 'list',
            'name': 'keystone',
            'message': 'Keystone?',
            'choices': get_keystones
        },
        {
            'type': 'list',
            'name': 'primaryslot1',
            'message': 'Primary slot 1?',
            'choices': get_primary_slot1
        },
        {
            'type': 'list',
            'name': 'primaryslot2',
            'message': 'Primary slot 2?',
            'choices': get_primary_slot2
        },
        {
            'type': 'list',
            'name': 'primaryslot3',
            'message': 'Primary slot 3?',
            'choices': get_primary_slot3
        },
        {
            'type': 'list',
            'name': 'secondarypath',
            'message': 'Secondary Path?',
            'choices': get_secondary_path
        },
        {
            'type': 'list',
            'name': 'secondaryslot1',
            'message': 'Secondary slot 1?',
            'choices': get_secondary_slot1
        },
        {
            'type': 'list',
            'name': 'secondaryslot2',
            'message': 'Secondary slot 2?',
            'choices': get_secondary_slot2
        },
        {
            'type': 'list',
            'name': 'offensive',
            'message': 'Shard -- Offensive?',
            'choices': [
                "1. +9 Adaptive Force",
                "2. +10%% Attack Speed",
                "3. +1%%-10%% (based on level) Cooldown Reduction"
            ]
        },
        {
            'type': 'list',
            'name': 'flex',
            'message': 'Shard -- Flex?',
            'choices': [
                "1. +9 Adaptive Force",
                "2. +6 Armor",
                "3. +8 Aagic Resistance"
            ]
        },
        {
            'type': 'list',
            'name': 'defence',
            'message': 'Shard -- Defence?',
            'choices': [
                "1. +15-90 (based on level) Health",
                "2. +6 Armor",
                "3. +8 Aagic Resistance"
            ]
        },
    ]
    answers = prompt(questions)
    pprint(answers)

    runes_storage.addrunes(name, answers)
    
if __name__ == '__main__':
    lolcli(prog_name='lolcli')