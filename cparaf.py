# Recebe em C => F
#   C          F - 32
#-------  =  ---------
#   5            9
#
#  F = [(C / 5) * 9] + 32
#100 C = 212 F


C = float(input("Insira Graus Celsius: "))

F = ((C / 5) * 9) + 32

print(f"Graus Celsius: {C}º")
print(f"Graus Farenheit: {F}º")