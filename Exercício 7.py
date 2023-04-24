# Faça um programa em python para ler um número inteiro informado pelo usuário. Ao final o
# programa deve informar na tela o resto da divisão deste número por 2, por 3 e por 5.


a = int(input("Digite o valor da variável: "))

divisao2 = a%2
divisao3 = a%3
divisao5 = a%5

print("O resto divido por 2: ", divisao2)
print("O resto divido por 3: ", divisao3)
print("O resto divido por 5: ", divisao5)
