import requests
from pprint import pprint

def smartest(hero1, hero2, hero3):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url) 
    dict_hero = {}
    for num in range(len(response.json())):
        name_hero = response.json()[num]['name']
        if hero1 == name_hero:
            dict_hero[hero1] = response.json()[num]['powerstats']['intelligence']
        elif hero2 == name_hero:
            dict_hero[hero2] = response.json()[num]['powerstats']['intelligence']
        elif hero3 == name_hero:
            dict_hero[hero3] = response.json()[num]['powerstats']['intelligence']  
    return max(dict_hero, key = lambda x: dict_hero[x])

if __name__ == '__main__':
    smartest_hero = smartest('Hulk', 'Captain America', 'Thanos')
    print('Самый умный из трех персонажей:', smartest_hero)

