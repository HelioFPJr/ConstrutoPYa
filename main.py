# 1 - imports = Bibliotecas
import pytest
# 2 - class = Classes

# 3 - definitions = métodos e funções
def print_hi(name):
        print (f'Oi, {name}')

def somar(num1,num2):
    return num1 + num2

def substrair(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

# exemplo de demonstração
def dividir(num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'NÃO DIVIDIRAS POR ZERO'

def dividir_try_except(num1,num2):
    try:
        return num1 / num2
    except TypeError:
        #return 'NÃO DIVIDIRAS POR ZERO'
        return TypeError

if __name__ == '__main__':
    print_hi('Helio')
resultado = somar(2,3)
print(f' O resultado da soma é {resultado}')

resultado = substrair(5,3)
print(f' O resultado da subtração é {resultado}')

resultado = multiplicar(2,4)
print(f' O resultado da multiplicação é {resultado}')

resultado = dividir(3,0)
print(f' O resultado da divisão é {resultado}')

# Testes Unitarios


# Teste da função somar

@pytest.mark.parametrize('num1,num2,resultado',[
    #valores
    (5,4,9), #teste 1
    (3,5,8), #teste 2
    (10,6,16), #teste 3
])
def test_somar(num1,num2,resultado):
    #1- preparo
    #num1 = 8 #input
    #num2 = 5 #input
    #resultado_esperado = 15 #output

    #2- exectuta
    #resultado_atual = somar(num1,num2)

    #3- valida
    assert num1+num2 == resultado

@pytest.mark.parametrize('num1,num2,resultado',[
    #valores
    (5,4,9), #teste 1
    (3,5,8), #teste 2
    (10,6,16), #teste 3
])
def test_somar_compacto(num1,num2,resultado):
    assert somar(8,5) == 13

def test_somar_resultado_negativo():
    assert somar(-1000,-2000) == -3000

def test_subtrair():
    assert substrair(4,5) == -1

def test_multiplicar():
    assert multiplicar(5,5) == 25

def test_dividir():
    assert dividir(20,5) == 25

def test_dividir_0():
    assert dividir(6,0) == 'NÃO DIVIDIRAS POR ZERO'

@pytest.mark.parametrize('num1,num2,resultado',[
    #valores
    (8,2,4), #teste 1
    (25,5,5), #teste 2
    (30,0,'NÃO DIVIDIRAS POR ZERO'), #teste 3
    (4,0,'NÃO DIVIDIRAS POR ZERO'), #teste 4
])
def test_dividir_try_except(num1,num2,resultado):
    assert dividir_try_except(num1,num2) == resultado

#TDD : Desenvolvimento Direcionado pelo Testes
# - Criar o esqueleto de classes, funções e métodos logo no início da Sprint
# - Criar pelo 1 teste (feliz) para todas as funções e métodos
# - Executar todos os testes unitários diariamente para medir o progresso