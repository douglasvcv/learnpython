
#Variáveis
nome="Douglas"
idade=22
altura=1.74
estudante = True

#Printando ela na tela
print("Nome: " + nome)
print("Idade:", idade)
print("Altura:", altura)
print("Estudante:", estudante)

#Ano de nascimento

ano_nascimento = 2025 - idade
print("Ano de nascimento:",ano_nascimento)

#Verificar se é maior de idade
maior_de_idade=idade>=18
print("É maior de idade:", maior_de_idade)

#Manipulação de string

texto= "! Tudo bem?"

print("Olá, "+nome+ texto)

#Operações matemáticas
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1+numero2
sub = numero1-numero2
mult = numero1*numero2
div = numero1/numero2

print("A soma é:",soma)
print("A subtração é:",sub)
print("A multiplicação",mult)
print("A divisão é:",div)

#Conversor de temperatura
celsius= float(input("Digite o grau em celsiu: "))
fahrenheit=celsius*9/5+32
print("Graus em fahrenheit:", fahrenheit)

#Cálculo do circulo
raio = float(input("Digite o raio do círculo: "))
area_circulo = 3.14159 * raio**2
print("A área do círculo é:", area_circulo)