from fastapi import FastAPI, Query
import requests
import json

app =FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    endpoint para ver a mensagem hello world
    '''

    return {'Hello':' world'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    endpoint para ver cardapio dos restaurantes
    '''
    url='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company']== restaurante:         
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante,'Cardapio': dados_restaurante}
    else: 
            return {'Erro': f'{response.status_code} - {response.text}'}

    for nome_do_restaurante, dados in dados_restaurante.items():
        nome_do_arquivo = f'{nome_do_restaurante}. json'
        with open(nome_do_arquivo,'w') as arquivo_restaurante:
            json.dump(dados,arquivo_restaurante, indent=4)