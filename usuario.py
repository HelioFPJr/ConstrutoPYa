# 1- imports
import json
import pytest
import csv
import requests
from requests import HTTPError

teste_dados_novos_usuarios = [
    (1, 'Juca', 'Pirama', 'juca@iterasys.com.br'),  # 1-usuario
    (2, 'Agatha', 'Christie', 'agatha@iretasys.com.br')  # 2-usuario
]
teste_dados_usuarios_atuais = [
    (1, 'George', 'Bluth', 'george.bluth@reqres.in'),  # 1-usuario
    (2, 'Janet', 'Weaver', 'janet.weaver@reqres.in')  # 2-usuario
]


# CRUD / ICAE
# Aplicações             APIs            Português
# Create                 Post            Incluir / Publicar
# Reach / Research       Get             Consultar / Pegar
# Update                 Put             Atualizar
# Delete                 Delete          Excluir

@pytest.mark.parametrize('id,nome,sobrenome,email', teste_dados_usuarios_atuais)
def testar_dados_usuarios(id, nome, sobrenome, email):  # função testa o algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        print(f'\nId: {id_obtido} - Nome: {nome_obtido} - Sobrenome: {sobrenome_obtido} - E-mail: {email_obtido}')
        print(f'\nId: {id_obtido}\nNome: {nome_obtido}\nSobrenome: {sobrenome_obtido}\nE-mail: {email_obtido}')
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email
    except HTTPError as http_fail:
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:  # Qualquer exceção sera tratada a seguir
        print(f'Falha inesperada: {fail}')


# função que faz algo --> fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users/{id}

# Leitor do arquivo CSV
def ler_dados_do_csv():
    teste_dados_csv = []
    nome_arquivo = 'usuarios.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            next(dados)
            for linha in dados:
                teste_dados_csv.append(linha)
        return teste_dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id,nome,sobrenome,email',ler_dados_do_csv())
def testar_dados_usuarios_csv(id, nome, sobrenome, email):  # função testa o algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        print(f'\nId: {id_obtido} - Nome: {nome_obtido} - Sobrenome: {sobrenome_obtido} - E-mail: {email_obtido}')
        print(f'\nId: {id_obtido}\nNome: {nome_obtido}\nSobrenome: {sobrenome_obtido}\nE-mail: {email_obtido}')
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == int(id)
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email
    except HTTPError as http_fail:
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:  # Qualquer exceção sera tratada a seguir
        print(f'Falha inesperada: {fail}')


def testar_consultar_usuarioi():