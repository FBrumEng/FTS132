# Biblioteca
import pytest       # Framework de Teste Unitário - Engine (Motor do Teste)
import requests     # Framework de Teste de API - Requests / Responses

# Endereço da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # Define qual o formato dos dados que serao transmitidos, no caso JSON.
                                                # O proprio documento da API descreve qual o formato está sendo utilizado.
                                                # Nas apis mais antigas asmx seria 'text/xml'
# O teste de CRIAR USUARIOS (POST):
def testar_criar_usuario():
    # 1 - Configurar
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '1001'

    # 2 - Executar
    resposta = requests.post(                   # Faz a requisição para fazer uma INCLUSÃO (POST), informando:
        url=base_url,                           # O endpoint da API (endereço)
        data=open('C:\\Users\\aless\\PycharmProjects\\Cursos_Iterasys\\FTS132\\Test\\db\\user1.json', 'rb'),  # O body da mensagem que vem do json
        headers=headers,                        # O header com o Content-Type
    )

    # 3 - Formatar
    corpo_da_resposta = resposta.json()         # Formata como Json (pois inicialmente ele vem numa linha unica)
    print(resposta)                             # Resposta Bruta
    print(resposta.status_code)                 # Resposta Code
    print(corpo_da_resposta)                    # Resposta Formatada

    # 4 - Validar
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

# O teste de CRIAR CONSULTAS (GET):
def testar_consultar_usuario():
    #1- Configurar
    status_code = 200
    id = 1001
    username = 'minduim'
    firstName = 'charlie'
    lastName = 'brown'
    email = 'charlie.brown@teste.com.br'
    password = '123456'
    phone = '11999999999'
    userStatus = 0

    #2- Executar
    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )

    #3- Formatar
    corpo_da_resposta = resposta.json()         # Formata como Json (pois inicialmente ele vem numa linha unica)
    print(resposta)                             # Resposta Bruta
    print(resposta.status_code)                 # Resposta Code
    print(corpo_da_resposta)                    # Resposta Formatada

    #4- Validar
    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone

# O teste de ALTERAR INFORMAÇÕES (PUT):
def testar_alterar_usuario():
    #1- Configurar
    username = 'minduim'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '1001'

    #2- Executar
    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('C:\\Users\\aless\\PycharmProjects\\Cursos_Iterasys\\FTS132\\Test\\db\\user2.json', 'rb'),   # O body da mensagem que vem do json
        headers=headers,                                                                                       # O header com o Content-Type
        )

    #3- Formatar
    corpo_da_resposta = resposta.json()         # Formata como Json (pois inicialmente ele vem numa linha unica)
    print(resposta)                             # Resposta Bruta
    print(resposta.status_code)                 # Resposta Code
    print(corpo_da_resposta)                    # Resposta Formatada

    #4- Validar
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

# O teste de ALTERAR INFORMAÇÕES (PUT):
def testar_excluir_usuario():
    #1- Configurar
    username = 'minduim'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = 'minduim'

    #2- Executar
    resposta = requests.delete(
        url=f'{base_url}/{username}',
        data=open('C:\\Users\\aless\\PycharmProjects\\Cursos_Iterasys\\FTS132\\Test\\db\\user1.json', 'rb'),   # O body da mensagem que vem do json
        headers=headers,                                                                                       # O header com o Content-Type
        )

    #3- Formatar
    corpo_da_resposta = resposta.json()         # Formata como Json (pois inicialmente ele vem numa linha unica)
    print(resposta)                             # Resposta Bruta
    print(resposta.status_code)                 # Resposta Code
    print(corpo_da_resposta)                    # Resposta Formatada

    #4- Validar
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada