import os
import time

from funcionalidades import pedir_letra, jogar_novamente,escrever_resultado, historico_de_partidas

os.system("cls")

def jogar():

    nome_desafiante = input("Digite o nome do desafiante: ")
    nome_competidor = input("Digite o nome do competidor: ")
    digitadas = []
    chances = 5
    dica = 0

    os.system("cls")

    secreto = input("Digite a palavra secreta: ")

    os.system("cls")

    dica1 = input("Digite a primeira dica: ")
    dica2 = input("Digite a segunda dica: ")
    dica3 = input("Digite a terceira dica: ")  

    print(f"A palavra secreta tem {len(secreto)} caracteres")

    time.sleep(2)
    os.system("cls")

    def escolher():
        lista = [dica1 , dica2 , dica3]
        while dica < 3:
            try:
                escolha = int(input("Digite (0) para jogar ou (1) para uma dica: "))
                if escolha == 1:
                    print(f"A dica é: {lista[dica]}")
                    return dica + 1
                elif escolha == 0:
                    return dica
            except:
                print("Digite apenas os números 0 ou 1: ")
        return dica
    dica = escolher()

    time.sleep(2)
    os.system("cls")

    print("Vamos começar o jogo!")

    time.sleep(2)
    os.system("cls")

    while True:
        if chances <= 0:
            print('Você perdeu!!!')
            time.sleep(2)
            escrever_resultado((f"Palavra: {secreto} | Perdedor: Competidor {nome_competidor} | Ganhador: Desafiante {nome_desafiante} \n"))
            break

        if dica >= 3:
            print("Você não tem mais dicas.")
            time.sleep(2)
            os.system("cls")

        letra = pedir_letra()

        time.sleep(3)
        os.system("cls")    

        digitadas.append(letra)

        if letra in secreto:
            print(f'O caractere "{letra}" existe na palavra secreta.')
            
        else:
            print(f'O caractere "{letra}" NÃO EXISTE na palavra secreta.')
            digitadas.pop()
        
        secreto_temporario = ''
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'

        if secreto_temporario == secreto:
            print(f'VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
            time.sleep(3)
            escrever_resultado((f"Palavra: {secreto} | Perdedor: Desafiante {nome_desafiante} | Ganhador: Competidor {nome_competidor} \n"))
            break
        else:
            print(f'A palavra secreta está assim: {secreto_temporario}')

        if letra not in secreto:
            chances -= 1

        print(f'Você ainda tem {chances} chances.')
        print()
        dica = escolher()
    
    jogar_novamente(jogar)
    os.system("cls")

jogar()