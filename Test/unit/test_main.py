import csv
import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, \
    area_do_triangulo, area_do_quadrado, area_do_retangulo, area_do_circulo, elevar_um_numero_pelo_outro, \
    calcular_volume_do_paralelograma


def testar_somar_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    # Dados / Valores
    # Entradas / Inputs
    num1 = 8
    num2 = 9
    # Saida / Output
    resultado_esperado = 17
    # 2ª Etapa - Executar
    resultado_atual = somar_dois_numeros(num1, num2)
    # 3ª Etapa - Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


def testar_subtrair_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    # Dados / Valores
    # Entradas / Inputs
    num1 = 9
    num2 = 8
    # Saida / Output
    resultado_esperado = 1

    # 2ª Etapa - Executar
    resultado_atual = subtrair_dois_numeros(num1, num2)

    # 3ª Etapa - Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


def testar_multiplicar_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    # Dados / Valores
    # Entradas / Inputs
    num1 = 8
    num2 = 2
    # Saida / Output
    resultado_esperado = 16

    # 2ª Etapa - Executar
    resultado_atual = multiplicar_dois_numeros(num1, num2)

    # 3ª Etapa - Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


def testar_dividir_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    # Dados / Valores
    # Entradas / Inputs
    num1 = 16
    num2 = 8
    # Saida / Output
    resultado_esperado = 2

    # 2ª Etapa - Executar
    resultado_atual = dividir_dois_numeros(num1, num2)

    # 3ª Etapa - Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


# Divisao por ZERO
'''
def testar_dividir_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    # Dados / Valores
    # Entradas / Inputs
    num1 = 16
    num2 = 0
    # Saida / Output
    resultado_esperado = ZeroDivisionError

    # 2ª Etapa - Executar
    resultado_atual = dividir_dois_numeros(num1, num2)

    # 3ª Etapa - Confirma / Check / Valida
    assert resultado_atual == resultado_esperado
'''


def testar_elevar_um_numero_pelo_outro():
    # 1ª Etapa - Configura / Prepara
    # Dados / Valores
    # Entradas / Inputs
    num1 = 2
    num2 = 2
    # Saida / Output
    resultado_esperado = 4

    # 2ª Etapa - Executar
    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)

    # 3ª Etapa - Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


def testar_area_do_quadrado():
    lado = 4
    resultado_esperado = 16
    resultado_atual = area_do_quadrado(lado)
    assert resultado_esperado == resultado_atual


def testar_area_do_retangulo():
    largura = 3
    comprimento = 4
    resultado_esperado = 12
    resultado_atual = area_do_retangulo(largura, comprimento)
    assert resultado_esperado == resultado_atual


def testar_area_do_triangulo():
    lado1 = 6
    lado2 = 6
    resultado_esperado = 18
    resultado_atual = area_do_triangulo(lado1, lado2)
    assert resultado_esperado == resultado_atual


# Anotação para utilizar como massa de teste:
@pytest.mark.parametrize('raio,resultado_esperado', [
    # valores
    (1, 3.14),  # teste nº1
    (2, 12.56),  # teste nº2
    (3, 28.26),  # teste nº3
    (4, 50.24),  # teste nº4
    ('a', 'Falha no calculo - Raio não é um número'),  # teste nº5 --> Teste negativo usando str no lugar de int
    (' ', 'Falha no calculo - Raio não é um número'),  # teste nº6 --> Teste negativo usando espaço no lugar de int
])
# Calcular a área de um circulo
def testar_area_do_circulo(raio, resultado_esperado):
    # 1-Configura
    # raio = 1   Comentamos parametros manuais para que os parametros sejam lidos
    # resultado_esperado = 3.14
    # 2-Executa
    resultado_atual = area_do_circulo(raio)
    # 3-Valida
    assert resultado_atual == resultado_esperado


# Ler dados de um arquivo csv para usar no teste seguinte
def ler_dados_csv():
    dados_csv = []  # criação de uma lista vazia
    nome_arquivo = 'C:\\Users\\aless\\PycharmProjects\\Cursos_Iterasys\\FTS132\\Test\\db\\massa_caixa.csv'  # local e nome do arquivo de massa
    try:
        with open(nome_arquivo,
                  newline='') as csvfile:  # repetir a leitura das linhas até o fim do arquivo (linha vazia)
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print('Arquivo não encontrado: ', nome_arquivo)
    except Exception as fail:
        print(f'falha não prevista: {fail}')


@pytest.mark.parametrize('id,largura,comprimento,altura,resultado_esperado', ler_dados_csv())

def testar_calcular_volume_do_paralelograma(id, largura, comprimento, altura, resultado_esperado):
    # 1 - Configura
    '''
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    '''

    # 2 - Executa
    resultado_atual = calcular_volume_do_paralelograma(int(largura), int(comprimento), int(altura))

    # 3 - Valida
    assert resultado_atual == int(resultado_esperado)
