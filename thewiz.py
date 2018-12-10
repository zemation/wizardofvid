#!/usr/local/bin/python3.7

from headers import *
import json
import requests

# Basic example GET https://api-endpoint.igdb.com/games/

def get_games(games):
    data = requests.get('https://api-endpoint.igdb.com/games/?search={}&fields=*'.format(games), headers=HEADERS).json()
    for i in data:
        print(i['name'])

def get_characters(games):
    data = requests.get('https://api-endpoint.igdb.com/characters/?search={}&fields=*'.format(games), headers=HEADERS).json()
    for i in data:
        print(i['name'])


running = True

while running:
    selection = input("What would you like to search for? - [C]haracters, [G]ames, [Q]uit: ")
    if selection.lower() == 'c':
        games = input("Enter a character: ")
        get_characters(games)
    elif selection.lower() == 'g':
        games = input("Enter part of a game: ")
        get_games(games)
    elif selection.lower() == 'q':
        print("Exiting")
        running = False
    else:
        print("Please select a valid option")
