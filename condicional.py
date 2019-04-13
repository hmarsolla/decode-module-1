idade = int(input("Insira a sua idade: "))

if (idade >= 18 and idade < 65):
    print("Você é obrigado a votar.")
elif ((idade >= 16 and idade < 18) or idade >= 65):
    print("Votar é opcional.")
else:
    print("Você não pode votar.")
