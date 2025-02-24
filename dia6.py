#listas e tuplas
#interligados com loops

#listas/array: podem ser modificadas

carros=["fiat", "ford", "bmw"]

print(carros[0])

carros.append("vw")

print(carros[3])

if "fordd" in carros:
    print("Achei")
else:
    print("Não achei")

#tuplas: não podem ser modificadas

cores = ("vermelho", "laranja", "azul")

print(cores)
print(cores[2])

cores[1]= "Verde"

print(cores[1])