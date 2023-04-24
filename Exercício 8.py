"""
Faça um programa em python para ler dois números inteiros informados pelo usuário.
Ao final o programa deve imprimir um relatório com o seguinte formato:
- dividendo:
- divisor:
- quociente:
- resto:
"""

dividendo = int(input("Digite o número dividendo: "))
divisor = int(input("Digite o número divisor: "))
print("\n")
quociente = dividendo//divisor
resto = dividendo%divisor
print("O dividendo é: ", dividendo)
print("O divisor é: ", divisor)
print("O quociente é: ", quociente)
print("O resto é: ", resto)