import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7b7ffc328e838f769fdfcdd27c2bc495'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create ={
    "name": "Dgin",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

response_name = requests.patch(url = f'{URL}/pokemons', headers= HEADER, json= body_name)
print(response_name.text)

body_pokeball ={
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_pokeball)
print(response_pokeball.text)