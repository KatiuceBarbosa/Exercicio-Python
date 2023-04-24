"""
Faça um programa em python que imprima a média aritmética de 4 números informados pelo
usuário. Atente-se para a existência de números nos formatos inteiro e float. Faça o tratamento
apropriado.
"""
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))
numero4 = float(input("Informe o quarto número: "))

mediaAritimetica = (numero1 + numero2 + numero3 + numero4)/4
print("\n")
print("Cálculo da média aritimética: ", mediaAritimetica)