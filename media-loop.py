# Um professor passa quantas notas ele quiser
# Quer a média de todas as notas
# Media for menor que 6 => O aluno está Reprovado
# Caso contrário => O aluno está Aprovado

notas = []

while(True):
    nota = float(input("Insira a próxima nota: "))
    notas.append(nota)
    resposta = input("Quer inserir mais uma nota? (s/n)")
    if (resposta == "n"):
        break

soma = 0

for valor in notas:
    soma += valor

media = soma / len(notas)
print(f"Média = {media}")

if (media < 6):
    print("Reprovado")
else:
    print("Aprovado")