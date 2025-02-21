#Operadores
a = 5
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# ** Exponenciação
# // Divisão inteira

print(a//b)
print(a/b)
print(a%b)

#Operadores de comparação

print(a>b)
print(a<b)
print(a==b)
print(a!=b)

#Operadores lógicos
#AND, OR e NOT

for_verdadeiro = True
print(a>b and for_verdadeiro==False)

#revisão
nota=8
frequencia=90

passou = nota>7 and frequencia>80
print("Aluno passou:",passou)
#AND vai ser true se ambas as condicionais forem verdadeiras

sal = True
bem_passado = not True

carne = sal and bem_passado
print("Carne gostosa:", carne)

#OR vai ser true se uma das condições forem verdadeira

carne2 = sal or bem_passado

print("Segunda carne gostosa:", carne2)

#NOT vai inverter um valor booleano

carne_gostosa = True
carne_crua = not carne_gostosa

print("A carne original:", carne_gostosa)
print("A carne crua:", carne_crua)