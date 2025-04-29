print("Calculadora")
continua = "sim"
while (continua == "sim"):
    continua = input("Deseja continuar? sim ou não\n")
    if continua == "não":
        print("Obrigada!! Até depois *-*")
        break
    elif continua != ("sim" or "nâo"):
        print("Não foi possivel entender sua resposta!!")
        break
    valor_1 = float(input("Digite um numero: \n"))
    valor_2 = float(input("Digite um numero: \n"))
    calculo = input("Escolha uma operação: \n + \n - \n x \n / \n")
    if calculo == "+":
        calculo = valor_1 + valor_2
        print(calculo)
    elif calculo == "-":
        calculo = valor_1 - valor_2
        print(calculo)
    elif calculo == "x":
        calculo = valor_1 * valor_2
        print(calculo)
    elif calculo == "/":
        calculo = valor_1 / valor_2
        print(calculo)
    else:
        print("Não é possivel realisar esse calculo")
