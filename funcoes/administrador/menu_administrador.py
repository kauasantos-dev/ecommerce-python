from ecommerce.usuarios import validadores
from funcoes.produtos import ver_produtos as produtos

def menu_adm():
    print("1- Ver produtos da loja\n2- Buscar produto\n3- Adicionar novo produto\n4- Remover produto\n5- Atualizar preço\n6- Atualizar estoque\n7- Sair\n")

def adicionar_produto_loja(nome, preco, estoque):
    adicionar = adm.adicionar_produto(nome, preco, estoque)
    if adicionar:
        print("O produto foi adicionado a sua loja!\n")
    else:
        print("Esse produto já está presente na loja.\n")

def remover_produto_loja(nome_produto):
    produto_removido = adm.remover_produto(nome_produto)
    if produto_removido:
        print("Produto removido com sucesso!\n")
    else:
        print("Nenhum produto encontrado.\n")

def atualizar_preco_estoque(opcao_adm):
    nome_produto = input("Digite o nome do produto: ")
    if opcao_adm == '5':
        try:
            novo_preco = validadores.ValidarProduto.validar_preco(input("Informe o novo preço do produto: "))
        except ValueError as erro:
            print("Erro: ", erro)
            return
        preco_atualizado = adm.atualizar_preco(nome_produto, novo_preco)
        if preco_atualizado:
            print("Preço atualizado com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

    elif opcao_adm == '6':
        try:
            novo_estoque = validadores.ValidarProduto.validar_estoque(input("Informe o novo estoque do produto: "))
        except ValueError as erro:
            print("Erro: ", erro)
            return
        estoque_atualizado = adm.atualizar_estoque(nome_produto, novo_estoque)
        if estoque_atualizado:
            print("Estoque atualizado com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

def opcao_selecionada_adm(instancia_adm, opcao_adm):
    if opcao_adm == '1' or opcao_adm == '2':
        produtos.ver_ou_buscar_produtos(instancia_adm, opcao_adm)
                
    elif opcao_adm == '3':
        while True:
            try:
                nome_produto = validadores.ValidarProduto.validar_nome(input("Digite o nome do produto: "))
                preco = validadores.ValidarProduto.validar_preco(input("Informe o preço do produto: "))
                estoque = validadores.ValidarProduto.validar_estoque(input("Informe o estoque do produto: "))
                break
            except ValueError as erro:
                print("Erro: ", erro, " Tente novamente.\n")
                continue
        adicionar_produto_loja(nome_produto, preco, estoque)
                
    elif opcao_adm == '4':
        nome_produto = input("Digite o nome do produto: ")
        remover_produto_loja(nome_produto)
                
    elif opcao_adm == '5':
        atualizar_preco_estoque(opcao_adm)
                
    elif opcao_adm == '6':
        atualizar_preco_estoque(opcao_adm)
                
    else:
        print("Opção inválida. Por favor, selecione uma das opções disponíveis.\n")