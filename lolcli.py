import click
import requests
import os
import runes_storage
import runes_utils

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
    # If region is not valid, show list of valid regions and abort
    if region not in lol_endpoints:
        print(region + " is nos a valid region")
        print("List or supported regions: " + str(list(lol_endpoints.keys())))
        return
    
    # Get the list of IDs of the free champions
    url = lol_endpoints[region] + "/lol/platform/v3/champion-rotations"
    free_champ_ids = requests.get(url = url, params = params).json()['freeChampionIds']

    # Get the free champion names using the ID and full champion list
    free_champs = [ champ['id'] for champ in champions if int(champ['key']) in free_champ_ids]

    # Print the free champions
    print(free_champs)

@lolcli.command()
@click.argument('name', type=click.STRING)
def addrunes(name):
    """Store your runes set!"""
    # Get the question set from utils for setting runes
    questions = runes_utils.get_questions()
    
    # Prompt the questions
    answers = prompt(questions)

    # Store the runes
    runes_storage.add_runes(name, answers)

@lolcli.command()
@click.argument('name', type=click.STRING)
def getrunes(name):
    """Get runes set by name"""
    # Get the runes from storage
    runes = runes_storage.get_runes(name)

    # If runes set not found, print error message and return
    if runes == None:
        print("Runes set not found.")
        return
    
    # Print the runes
    print("")
    print(runes['primarypath'] + ", " +  runes['keystone'] + ", " + runes['primaryslot1'] + ", " + runes['primaryslot2'] + ", " + runes['primaryslot3'])
    print(runes['secondarypath'] + ", " + runes['secondaryslot1'] + ", " + runes['secondaryslot2'] )
    print("Offensive: " + runes['offensive'])
    print("Flex: " + runes['flex'])
    print("Defence: " + runes['defence'])
    print("")

    # Print a simplified version for setting the runes easily
    print(runes_utils.simplify_output(runes))
    
if __name__ == '__main__':
    lolcli(prog_name='lolcli')