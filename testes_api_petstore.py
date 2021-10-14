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

def testar_alterar_usuario():
    headers = {'content-Type': 'application/json'}
    apelido = 'HelioFPJr'
    status_code_esperado = 200 #comunicação
    codigo_esperado = 200 #funcional
    tipo_esperado = 'unknown'
    mensagem_esperado = '16614'

    resposta=requests.put(f'{url}/{apelido}',
                         data=open('json/usuario2.json','rb'),
                         headers=headers)
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code_esperado
    assert  corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperado

def testar_excluir_usuario():
    # Configura
    headers = {'Content-Type': 'application/json'}
    apelido = 'HelioFPJr'
    tipo_esperado = 'unknown'
    status_code_esperado = 200  # comunicação

    # Executa
    resposta = requests.delete(f'{url}/{apelido}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == apelido

def testar_incluir_usuario_extrair_apelido():
    def testar_incluir_usuario(headers=None):
        # configura
        status_code_esperado = 200  # comunicação
        codigo_esperado = 200  #
        tipo_esperado = 'unknown'  # fixo como desconhecido
        mensagem_esperada = '16614'  # id do usuário
        headers = {'content-Type': 'application/json'}

        # executa
        resposta = requests.post(url,
                                 data=open('json/usuario1.json', 'rb'),
                                 headers=headers)
        corpo_da_resposta = resposta.json()
        print(resposta)
        print(resposta.status_code)
        print(json.dumps(resposta.json(), indent=2))

        # valida
        assert resposta.status_code == status_code_esperado
        assert corpo_da_resposta['code'] == codigo_esperado
        assert corpo_da_resposta['type'] == tipo_esperado
        assert corpo_da_resposta['message'] == mensagem_esperada

def testar_consultar_usuario_e_extrair_senha():
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

    return corpo_da_resposta['password']

def testar_login(apelido, password):
    headers = {'content-Type': 'application/json'}
    status_code_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session'

    # executa
    resposta = requests.get(f'{url}/login?username={apelido}&password={password}', headers=headers)
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(), indent=2))

    # valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert mensagem_esperada in corpo_da_resposta['message']
    token = corpo_da_resposta['message'][-13:]# capturando os treze ultimos caracteres da string
    #token = corpo_da_resposta['message'].rpartition(':')[-1]# capturando final da string a partir do ':'
    print(f'token: {token}')

    return token

def testar_orquestracao_consultar_senha_e_realizar_login():
    apelido = 'HelioFPJr'

    senha = testar_consultar_usuario_e_extrair_senha()
    token = testar_login(apelido,senha)
    print(f'Token no maestro: {token}')