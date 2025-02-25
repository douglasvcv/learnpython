#Criando mini jogo

import random

print("Bem vindo ao jogo 'advinhando número'")

while True:

    numero_secreto = random.randint(1,10)
    print(numero_secreto)

    print("Pensei em um número entre 1 a 10")
    print("Você tem 5 tentativas!")

    tentativas = 5
    
    while tentativas > 0:
        numero_digitado= int(input("Digite um número: "))
        if numero_digitado > 10 or numero_digitado < 1:
            print("O número deve ser entre 1 a 10")
            continue
        if numero_digitado != numero_secreto:
            tentativas-=1
            print("Número errado, tente novamente!")
            print("Tentativas restantes:", tentativas)
            if numero_digitado > numero_secreto:
                print("Número secreto é menor que o inserido")
            if numero_digitado < numero_secreto:
                print("Número secreto é maior que o inserido")
            
        if numero_digitado == numero_secreto:
            print("Você acertou", numero_secreto)
            break
        elif tentativas == 0:
            print("Número correto:", numero_secreto)
    break