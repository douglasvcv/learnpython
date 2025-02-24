#Estruturas de repetição

#Repetir N vezes, onde a gente pode decidir se esse N é uma quantidade ou uma condição

frutas= ["maçã", "banana", "pera"]
print(frutas[2])

for fruta in frutas:
    print("Fruta:", fruta)


#definir um número de N

for i in range(7):
    print("Número:", i)

contador=0

while contador < 6:
    print("Contando:", contador)
    contador+=1


#Break para o loop
for j in range(10):
    if j == 6:
        break
    print("Contandoo for break:", j)    

#Continue pula uma execução

for j in range(10):
    if j == 6:
        continue
    print("Contandoo for continue:", j)    


N = input("Digite um número")

multiplicaçao=0

for i in range(1+N*2):
    N = i
    print(multiplicaçao=i)

