import sqlite3

def criar_banco_dados():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            ano_publicacao INTEGER
        )
    ''')

    conexao.commit()
    conexao.close()

def inserir_livro(titulo, autor, ano_publicacao):
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao)
        VALUES (?, ?, ?)
    ''', (titulo, autor, ano_publicacao))

    conexao.commit()
    conexao.close()

def consultar_livros():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    for livro in livros:
        print(livro)

    conexao.close()

def remover_livro(livro_id):
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM livros WHERE id = ?', (livro_id,))

    conexao.commit()
    conexao.close()

criar_banco_dados()

while True:
    print("\nMenu:")
    print("1. Inserir livro")
    print("2. Consultar todos os livros")
    print("3. Remover livro")
    print("4. Sair")

    escolha = input("Escolha a opção desejada: ")

    if escolha == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")
        inserir_livro(titulo, autor, ano_publicacao)

    elif escolha == "2":
        consultar_livros()

    elif escolha == "3":
        livro_id = input("Digite o ID do livro que deseja remover: ")
        remover_livro(livro_id)

    elif escolha == "4":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")