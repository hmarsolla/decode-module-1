# Um professor passa 4 notas de prova por ano por aluno
# Quer a média dessas 4 notas 
# Media for menor que 6 => O aluno está Reprovado
# Caso contrário => O aluno está Aprovado

p1 = float(input("Insira a P1: "))
p2 = float(input("Insira a P2: "))
p3 = float(input("Insira a P3: "))
p4 = float(input("Insira a P4: "))

media = (p1 + p2 + p3 + p4) / 4
print(f"Média = {media}")

if (media >= 6):
    print("Aprovado")
else:
    print("Reprovado")