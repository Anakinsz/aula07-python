#valor < R$10,00 lucro de 70% R$ 10,00 <= valor < R$ 30,00 lucro de 50%R$ 30,00 <= valor < R$ 50,00 lucro de 40%valor >= R$50,00 lucro de 30%

produto = input("Digite o Nome do Produto: ")
valor_compra = int(input("Valor da Compra: "))

if valor_compra <10:
    print("Lucro de 70% ")
elif valor_compra <=30:
    print("lucro de 50%")
elif valor_compra <50:
    print("Lucro de 40%")
elif valor_compra >=50:
    print("lucro de 30% na venda")