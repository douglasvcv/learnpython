#Manipulação de string

name= "Douglas"

print(f"Olá {name}")

traco = "-" *5

print(f"{traco} Olá {traco}")

#indexação

nome2 = "python"

print(nome2[2])

#fatiamento slicing

frase = "Aprender python é legal"

print(frase[9:16])#começa do indice que eu indiquei e termina no indece a menos do que indiquei

#comprimento

print(len(nome2))

#mudar a case

print(frase.upper()) #ASD
print(frase.lower()) #asd
print(frase.title()) #Alternar As Frases

#limpeza de espaços em branco

msg_em_branco = "                  Olá teste"

print(msg_em_branco)
print(msg_em_branco.strip())

#substituição

frasee = "Eu vou ficar pobre"
novFrase = frasee.replace("pobre", "rico")
print(novFrase)

#encontrar uma string

nomesla = "Tamo junto natalina ui wifi"
encontrei = nomesla.find("natalina")

print(f"O indice da palavra é {encontrei}")