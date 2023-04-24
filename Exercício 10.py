"""
Escreva um programa em python para armazenar dois valores inteiros informados pelo
usuário, por exemplo, nas variáveis x e y. Deve-se realizar a troca dos valores das variáveis e, por
fim, deve-se imprimir os valores finais das variáveis.

Repita o exercício da questão anterior sem utilizar variável auxiliar.
"""

x = int(input("Intorme o valor inteiro: "))
y = int(input("Intorme outro valor inteiro: "))

#aux = x
#x = y
#y = aux

x, y = y, x

print("O valor final é: - x: ", x, "- y: ", y)