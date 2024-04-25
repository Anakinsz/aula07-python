#Elabore um programa em Python que implemente uma calculadora com as funções desomar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os doisvalores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular emostrar o resultado

print("Calculadora")
num = (input("Digite a sua opçãp, +, - , *, /: "))

if (num == '+'):
    n1 = int(input("Digite o primeiro Número: "))
    n2 = int(input("Digite o segundo Número: "))
    resultado = (n1+n2)
    print ("o resultado entre", n1,"+", n2,"=", resultado)
if (num == '-'):
    n1 = int(input("Digite o primeiro Número: "))
    n2 = int(input("Digite o segundo Número: "))
    resultado = (n1-n2)
    print ("o resultado entre", n1,"-", n2,"=", resultado)
if (num == '*'):
    n1 = int(input("Digite o primeiro Número: "))
    n2 = int(input("Digite o segundo Número: "))
    resultado = (n1*n2)
    print ("o resultado entre", n1,"*", n2,"=", resultado)
if (num == '/'):
    n1 = int(input("Digite o primeiro Número: "))
    n2 = int(input("Digite o segundo Número: "))
    resultado = (n1/n2)
    print ("o resultado entre", n1,"/", n2,"=", resultado)