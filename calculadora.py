# Recebe o primeiro número, qual operação ele deve fazer e
# em seguida o segundo número.
# Executa a operação:
# + - * /

numero1 = float(input("Insira o primeiro número: "))
operacao = input("Insira a operação a ser executada: ")
numero2 = float(input("Insira o segundo número: "))

if (operacao == "+"):
    print(f"Soma: {numero1 + numero2}")
elif (operacao == "-"):
    print(f"Subtração: {numero1 - numero2}")
elif (operacao == "*"):
    print(f"Multiplicação: {numero1 * numero2}")
elif (operacao == "/"):
    print(f"Divisão: {numero1 / numero2}")
else:
    print("Operação inválida.")
