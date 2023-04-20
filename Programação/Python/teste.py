
#limite_superior = input("Digite o limite superior: ")
#limite_inferior = input("Digite o limite inferior: ")
#termo_geral = input("Digite o termo geral (n como variavel): ")

import os
import ast

##avisos
wdt = "Tipo de dados incorreto!"
#
#
##

def clear():
        print("\n" * 130)


def validar_limite_superior(limite_superior):
    try:
        limite_superior = int(limite_superior)
        return True, limite_superior
    except ValueError:
        return False

def validar_limite_inferior(limite_inferior, limite_superior):
    try:
        limite_inferior = int(limite_inferior)
        if limite_inferior >= limite_superior:
            return False, None
        else:
            return True, limite_inferior
    except ValueError:
        return False, None

def validar_termo_geral(termo):
    try:
        # Tenta avaliar a expressão para um valor de n qualquer
        ast.parse(termo, mode='eval')
        return_type = type(eval(termo, {'n': 1}))
    except:
        # Se a avaliação da expressão gerar um erro, informa ao usuário que o termo é inválido
        print("Termo inválido! Digite novamente.")
        return False, None
    
    if 'n' not in termo:
        # Se a expressão não contiver a variável "n", informa ao usuário que o termo é inválido
        print("O termo deve conter a variável 'n'! Digite novamente.")
        return False, None
    
    # Se a expressão for válida e conter a variável "n", retorna o tipo da variável resultante da avaliação da expressão
    return return_type


def obter_inputs():
    while True:
        limite_superior = input("Digite o limite superior: ")
        valido, limite_superior = validar_limite_superior(limite_superior)
        if valido:
            break
        else:
            clear()
            print("Limite superior inválido. Tente novamente.")

    while True:
        limite_inferior = input("Digite o limite inferior: ")
        valido, limite_inferior = validar_limite_inferior(limite_inferior, limite_superior)
        if valido:
            break
        else:
            clear()
            print("Limite inferior inválido. Tente novamente.")

    while True:
        termo_geral = input("Digite o termo geral (n como variável): ")
        valido = validar_termo_geral(termo_geral)
        if valido:
            break
        else:
            clear()
            print("Termo geral inválido. Tente novamente.")

    return limite_superior, limite_inferior, termo_geral


    termo_geral = input("Digite o termo geral (n como variável): ")
    tipo_variavel = None

    while not tipo_variavel:
        tipo_variavel = validar_termo_geral(termo_geral)
        termo_geral = input("Digite o termo geral (n como variável): ")

    print(f"O termo geral '{termo_geral}' é válido e retorna uma variável do tipo {tipo_variavel}.")
obter_inputs()