import os

def pedir_letra():
    letra = input("Digite uma letra ou caractere: ")

    if len(letra) > 1:
        print("Digite apenas um caractere.")
        pedir_letra()
    return letra

def jogar_novamente(function_game):
    historico_de_partidas()
    resposta = input("Deseja jogar novamente? Digite (s) para sim ou (n) para não: ")

    if (resposta == "s"):
        function_game()
        os.system("cls")
    elif resposta == "n":
        quit()
    else:
        print("Operação inválida")
        jogar_novamente(function_game)


def escrever_resultado(resultado):
    doc = open("resultados.txt", "a")
    doc.writelines(resultado)


def historico_de_partidas():
    try:
        doc = open('resultados.txt', 'r')
        text = doc.read()
        print(f'{""*50} Histórico de partidas {""*50} \n')
        print(text)
        print("*"*50)
    except:
        print("*"*50)
        print("Não há resultados no momento")
        print("*"*50)