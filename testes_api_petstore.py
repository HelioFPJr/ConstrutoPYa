import pytest
import requests
import json

url = 'https://petstore.swagger.io/v2/user'

def testar_incluir_usuario(headers=None):
    #configura
    status_code_esperado = 200      #comunicação
    codigo_esperado = 200           #
    tipo_esperado = 'unknown'       #fixo como desconhecido
    mensagem_esperada = '16614'     #id do usuário
    headers = {'content-Type': 'application/json'}

    #executa
    resposta = requests.post(url,
                             data=open('json/usuario1.json','rb'),
                             headers = headers)
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(),indent=2))

    #valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_consultar_usuario():
    #configura
    headers = {'content-Type': 'application/json'}
    apelido = 'HelioFPJr' #input para consulta
    id_esperado = 16614
    apelido_esperado = 'HelioFPJr'
    email_esperado = 'heliojunior@iterasys.com.br'
    telefone_esperado = '61999999999'
    user_status_esperado = 0
    status_code_esperado = 200

    #executa
    resposta = requests.get(f'{url}/{apelido}',headers=headers)
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(), indent=2))

    #valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == apelido_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado


