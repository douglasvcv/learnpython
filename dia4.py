#Condicionais /Estruturas => if, else

idade = 15

if idade >= 18: 
    print("Você é maior de idade!")
else: 
    print("Você é menor de idade!")

#meia entrada = tem que ser menor de idade e estar estudando em escola pública

menor_de_idade = True
Estuda = not True

if menor_de_idade == True and Estuda == True:
    print("Você tem direito a meia entrada!")
else:
    print("Você terá direito a uma entrada inteira!")


#outro exemplo
nota=10

if nota >= 9:
    print("Sua nota é a A")
elif nota >= 8:
    print("Sua nota é B")

#exemplo clima

clima = "chuvoso"

if clima == "ensolarado":
    print("Clima está ensolarado")
elif clima == "chuvoso":
    print("Clima está chuvoso")
elif clima == "nublado":
    print("Clima está nublado")

#comisão
#>1000 = 5%
#>500 = 2%
#<500 = 1%

comisao=1200

if comisao > 1000:
    valor = comisao * .05
    print("Comissão foi de:", valor)
elif comisao > 500:
    valor = comisao * .02
    print("Comissão foi de:", valor)
elif comisao < 500:
    valor = comisao * .01
    print("Comissão foi de:", valor)
