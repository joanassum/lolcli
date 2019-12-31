import click
import requests
import os

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
    
if __name__ == '__main__':
    lolcli(prog_name='lolcli')