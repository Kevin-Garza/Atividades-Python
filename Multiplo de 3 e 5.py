# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário.

def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

def multiplo_de_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False
    
def multiplo_de_5_e_3(numero):
    if multiplo_de_5 and multiplo_de_3:
        print(f"O número {numero} é múltiplo de 3 e de 5.")
    else:
        print(f"O número {numero} não é multiplo dos dois.")

numero = int(input("Insira um número para saber se ele é múltiplo de 3 e de 5: "))
multiplo_de_5_e_3(numero)