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
            novo_preco = Validador.validar_preco(input("Informe o novo preço do produto: "))
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
            novo_estoque = Validador.validar_estoque(input("Informe o novo estoque do produto: "))
        except ValueError as erro:
            print("Erro: ", erro)
            return
        estoque_atualizado = adm.atualizar_estoque(nome_produto, novo_estoque)
        if estoque_atualizado:
            print("Estoque atualizado com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

def opcao_selecionada_cliente(instancia_cliente, opcao_cliente):
    if opcao_cliente == '1' or opcao_cliente == '2':
        ver_ou_buscar_produtos(instancia_cliente, opcao_cliente)
                
    elif opcao_cliente == '3':
        ver_carrinho()
                
    elif opcao_cliente == '4':
        nome_produto = input("Informe o nome do produto: ")
        novo_produto_carrinho(nome_produto)
                
    elif opcao_cliente == '5':
        nome_produto = input("Informe o nome do produto: ")
        fazer_pedido(instancia_cliente, nome_produto)
                
    else:
        print("Opção inválida. Por favor, selecione uma das opções disponíveis.\n")

def opcao_selecionada_adm(instancia_adm, opcao_adm):
    if opcao_adm == '1' or opcao_adm == '2':
        ver_ou_buscar_produtos(instancia_adm, opcao_adm)
                
    elif opcao_adm == '3':
        while True:
            try:
                nome_produto = Validador.validar_nome(input("Digite o nome do produto: "))
                preco = Validador.validar_preco(input("Informe o preço do produto: "))
                estoque = Validador.validar_estoque(input("Informe o estoque do produto: "))
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