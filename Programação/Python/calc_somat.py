import ast

def checar_somatorio(limite_superior, limite_inferior, termo_geral):
    while True:
        try:
            # verifica se o limite superior e inferior são números inteiros
            limite_superior = int(limite_superior)
            limite_inferior = int(limite_inferior)

            # verifica se a expressão do termo geral contém a variável "n"
            if "n" not in termo_geral:
                raise ValueError("A expressão do termo geral não contém a variável 'n'.")

            # tenta avaliar a expressão do termo geral com n = 1 para verificar se é uma expressão matemática válida
            eval(termo_geral.replace("n", "1"))

            # tenta analisar a expressão do termo geral como uma expressão Python usando o módulo ast
            ast.parse(termo_geral.replace("n", "1"))

            # todas as verificações foram bem sucedidas, retorna True
            return True

        except ValueError as e:
            # a entrada é inválida, pede para o usuário digitar novamente
            print("Entrada inválida:", e)
            limite_superior = input("Digite o limite superior novamente: ")
            limite_inferior = input("Digite o limite inferior novamente: ")
            termo_geral = input("Digite o termo geral novamente (usando 'n' como a variável): ")

        except:
            # a entrada é inválida, pede para o usuário digitar novamente
            print("Entrada inválida. Tente novamente.")
            limite_superior = input("Digite o limite superior novamente: ")
            limite_inferior = input("Digite o limite inferior novamente: ")
            termo_geral = input("Digite o termo geral novamente (usando 'n' como a variável): ")

while True:
    limite_superior = input("Digite o limite superior: ")
    limite_inferior = input("Digite o limite inferior: ")
    termo_geral = input("Digite o termo geral (usando 'n' como a variável): ")

    # verifica se a entrada é válida usando a função checar_somatorio
    entrada_valida = checar_somatorio(limite_superior, limite_inferior, termo_geral)

    if entrada_valida:
        # converte os limites para inteiros
        limite_superior = int(limite_superior)
        limite_inferior = int(limite_inferior)

        # cria uma lista com os valores da sequência
        sequencia = [eval(termo_geral.replace("n", str(n))) for n in range(limite_inferior, limite_superior+1)]

        # calcula o resultado da somatória usando a função sum
        resultado = sum(sequencia)

        # exibe os valores da sequência e o resultado da somatória
        print("Sequência: ", sequencia)
        print("Resultado: ", resultado)

    # pergunta se o usuário deseja fazer outro cálculo
    resposta = input("Deseja fazer outro cálculo? (S/N): ")
    if resposta.lower() != "s":
        break
