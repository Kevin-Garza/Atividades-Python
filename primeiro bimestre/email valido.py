# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

def email_valido(email):
    if "@" in email:
        print("Email válido.")
    else:
        print("Email inválido.")

email = input("Insira seu email: ")
email_valido(email)