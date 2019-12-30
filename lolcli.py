import click
import requests
import os

@click.group()
def lolcli():
    """A CLI for League of Legends."""

api_key = os.environ['LOLCLI_APIKEY']
lol_endpoint = "https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations"
champions_endpoint = "http://ddragon.leagueoflegends.com/cdn/9.24.2/data/en_US/champion.json"

@lolcli.command()
def freechamp():
    """Getting free-to-play champion rotation"""
    # Get all champions
    champions = list(requests.get(url = champions_endpoint).json()["data"].values())

    params = {'api_key': api_key}
    free_champ_ids = requests.get(url = lol_endpoint, params = params).json()['freeChampionIds']
    free_champs = [ champ['id'] for champ in champions if int(champ['key']) in free_champ_ids]
    print(free_champs)
    
if __name__ == '__main__':
    lolcli(prog_name='lolcli')