import requests
import json
import random

def filmeInfo():
    
    name = input('Digite o nome do filme: ')
    req = None 
    try:
        req = requests.get(f'http://www.omdbapi.com/={name}')
        info = json.loads(req.text)
    except:
        print('Erro na requisição')
        exit()

    if info['Response'] == 'False':
        print('Filme não encontrado!!')
        return None
    else:
        return info.get('Title'), info.get('Year'), info.get('Director'), info.get('Actors')

def addFilme(dictFilmes):
    info = filmeInfo()
    if info:
        dictFilmes[info[0]] = [f"Ano: {info[1]}",  f"Diretor: {info[2]}", f"Cast: {info[3]}"]
        print('Filme adicionado com sucesso')
    else:
        print('Erro ao adicionar filme')

infos = {'La la land': ['2016','Damien Chazelle','emma stone, ryan gosling'], 'The handmaiden': ['2016', 'Park Chan-wook', 'Kim Min-hee, Ha Jung-woo, Cho Jin-woong'], 'Scream': ['1996', 'Wes Craven', 'Neve Campbell, Courteney Cox, David Arquette'], 'Poor things': ['2023', 'Yorgos Lanthimos', 'Emma Stone, Mark Ruffalo, Willem Dafoe']}
palavra = random.choice(list(infos.keys()))
dicas = infos[palavra]
print(dicas)
