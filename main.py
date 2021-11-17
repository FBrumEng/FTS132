import pytest

    # Cozinheiro / Definição
def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except:
        return ZeroDivisionError
        #return ' --> Não é possível dividir por zero'

def elevar_um_numero_pelo_outro(num1,num2):
    return num1 ** num2

#Calcular a área de um quadrado
def area_do_quadrado(lado):
    return lado**2

#Calcular a área de um retangulo
def area_do_retangulo(largura,comprimento):
    return largura*comprimento

#Calcular a área de um triangulo
def area_do_triangulo(lado1,lado2):
    return lado1*lado2/2

#Calcular a área de um circulo
def area_do_circulo(raio):
    return 3.14 * raio ** 2

if __name__ == '__main__':
    # Garçon - Requisições / Chamadas
    resultado = somar_dois_numeros(5, 7)
    print(f'A soma é {resultado}')  # <---prato

    resultado = subtrair_dois_numeros(7, 5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(3, 5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(8, 4)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2,2)
    print(f'A exponenciação é {resultado}')

    resultado = area_do_quadrado(3)
    print(f'A área do quadrado é {resultado}')

    resultado = area_do_retangulo(2,5)
    print(f'A área do retangulo é {resultado}')

    resultado = area_do_triangulo(4,4)
    print(f'A área do triangulo é {resultado}')

    resultado = area_do_circulo(2)
    print(f'A área do circulo é {resultado}')


    # Degustador / Teste
'''
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

#Divisao por ZERO:
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

def testar_elevar_um_numero_pelo_outro():
    # 1ª Etapa - Configura / Prepara
    # Dados / Valores
    # Entradas / Inputs
    num1 = 2
    num2 = 2
    # Saida / Output
    resultado_esperado = 4

    # 2ª Etapa - Executar
    resultado_atual = elevar_um_numero_pelo_outro(num1,num2)

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
    resultado_atual = area_do_retangulo(largura,comprimento)
    assert resultado_esperado == resultado_atual

def testar_area_do_triangulo():
    lado1 = 6
    lado2 = 6
    resultado_esperado = 18
    resultado_atual = area_do_triangulo(lado1,lado2)
    assert resultado_esperado == resultado_atual

def testar_area_do_circulo():
    #1-Configura
    raio = 1
    resultado_esperado = 3.14
    #2-Executa
    resultado_atual = area_do_circulo(raio)
    assert resultado_esperado == resultado_atual
'''