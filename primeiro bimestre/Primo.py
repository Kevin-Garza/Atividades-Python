# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i  == 0:
            return False
    return True

numero = int(input("Digite o número que deseja saber se é primo: "))
if eh_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")