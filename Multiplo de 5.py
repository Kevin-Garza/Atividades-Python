# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário.

def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número: "))
if multiplo_de_5(numero):
    print("Este número é múltiplo de 5.")
else:
    print("Este número não é múltiplo de 5.")