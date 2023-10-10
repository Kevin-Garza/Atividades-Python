# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

def palindromo(palavra):
    if palavra.lower() == palavra[::-1].lower():
        print(f"A palavra {palavra} é um palindromo.")
    else:
        print(f"A palavra {palavra} não é um palindromo.")

palavra = input("Digite uma palavra para saber se ela é um palindromo: ")
palindromo(palavra)