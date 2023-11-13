lista_livro = []
id_global = 0

def cadastrar_livro(id):
    nome = input('Nome do livro: ')
    autor = input('Autor do livro: ')
    editora = input('Editora do livro: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro.copy()) # inserindo na lista o dicionário


def consultar_livro():
    opcao = input('Escolha uma opção (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu): ')
    if opcao == '1':
        for livro in lista_livro:
            for key, value in livro.items(): # varrer todos os itens de chave e valor do dicionario
              print('{}:{}'.format(key, value))



    elif opcao == '2':
        id_busca = int(input('Digite o ID do livro: '))
        for livro in lista_livro:
            if livro['id'] == id_busca:
                for key, value in livro.items(): # varrer todos os itens de chave e valor do dicionario
                  print('{}:{}'.format(key, value))

    elif opcao == '3':
        autor_busca = input('Digite o nome do autor: ')
        for livro in lista_livro:
            if livro['autor'] == autor_busca:
                for key, value in livro.items(): # varrer todos os itens de chave e valor do dicionario
                  print('{}:{}'.format(key, value))

# Função para remover um livro
def remover_livro():
    id_remover = int(input('Digite o ID do livro a ser removido: '))
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            for key, value in livro.items(): # varrer todos os itens de chave e valor do dicionario
                  print('{}:{}'.format(key, value))

# mensagem de boas-vindas com identificação
print('Bem-vindo a Loja da Carolina Vitória Linck Lopes')

# menu principal
while True:
    print('********************************************')
    print('---------------MENU PRINCIPAL--------------')
    print('1. Cadastrar Livro')
    print('2. Consultar Livro')
    print('3. Remover Livro')
    print('4. Encerrar Programa')
    opcao_menu = input('Escolha a opção desejada: ')


    if opcao_menu == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_menu == '2':
        consultar_livro()
    elif opcao_menu == '3':
        remover_livro()
    elif opcao_menu == '4':
        break
    else:
        print('Opção inválida')
        continue # volta para o início do laço
