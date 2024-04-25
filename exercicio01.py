#Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:• não-eleitor (abaixo de 16 anos)• eleitor obrigatório (entre 18 e 65 anos)• eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)

eleitor = int(input("Digite sua Idade: "))

if eleitor <16:
    print("não é possivel votar.")
if eleitor > 18 and eleitor  <=65:
    print("eleitor obrigatorio.")
elif (16 < eleitor < 18) or (eleitor > 65):
    print("eleitor facultativo")
    