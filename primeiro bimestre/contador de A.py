# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.

def contador_de_a():
    texto = input("Digite o texto que deseja contar quantos 'a' possui: ")
    return f"A letra 'a' aparece {texto.count('a') + texto.count('ã') + texto.count('á') + texto.count('à') + texto.count('A') + texto.count('Á') + texto.count('À')} vezes."

print(contador_de_a())