# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.

frutas = []

while True:
    fruta = input("Digite as frutas que deseje comprar, quando terminar, digite 'sair' para finalizar: ")
    if fruta.lower() == 'sair':
        break
    frutas.append(fruta)

print("Lista de futas que deseja comprar: ")
for fruta in frutas:
    print(fruta)