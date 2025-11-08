def menu_cliente():
    print("1- Ver produtos da loja\n2- Buscar um produto\n3- Ver meu carrinho\n4- Adicionar produto ao carrinho\n5- Fazer pedido\n6- Sair\n")

def ver_carrinho():
    carrinho = cliente.ver_carrinho()
    if carrinho:
        print("LISTA DE PRODUTOS EM SEU CARRINHO:\n")
        for posicao, produto in enumerate(carrinho, start=1):
            print(f"{posicao}. {produto}")
    else:
        print("Não há produtos em seu carrinho.\n")

def novo_produto_carrinho(nome_produto):
    adicionar_produto = cliente.salvar_produtos(nome_produto)
    if adicionar_produto:
        print("O produto foi adicionado em seu carrinho.\n")
    
    elif adicionar_produto is None:
        print("Nenhum produto encontrado.\n")
        
    else:
        print("Esse produto já está presente em seu carrinho.\n")

def fazer_pedido(usuario, nome_produto):
    verificar = cliente.verificar_produto(nome_produto)
    if not verificar:
        print("Nenhum produto encontrado.\n")
        return
    else:
        lista_produtos = AbrirArquivo.arquivo_r(Paths.save_produtos)
        for produto in lista_produtos:
            if produto['Nome'].lower() == nome_produto.lower():
                produto_encontrado = produto
                break 
        
        print("INFORME O ENDEREÇO DE ENTREGA\n")
        endereco()
        while True:
            print("\nSelecione a forma de pagamento:\n1- Pix\n2- Cartão de crédito\n3- Cancelar pagamento\n")
            pagamento = input()
            if pagamento == '1':
                fazer_pagamento = pix(produto_encontrado)
                if fazer_pagamento:
                    print("Pagamento realizado com sucesso! Seu pedido estará a caminho em breve.\n")
                    break
                else:
                    print(f"O preço do produto é R${produto['Preço']:.2f}. Tente novamente.\n")
                                
            elif pagamento == '2':
                print("INSIRA OS DADOS DO SEU CARTÃO\n")
                fazer_pagamento = cartao()
                if fazer_pagamento:
                    print("Pagamento realizado com sucesso! Seu pedido estará a caminho em breve.\n")
                    break
                else:
                    print("Erro ao realizar o pagamento. Tente novamente.\n")
                            
            elif pagamento == '3':
                print("Pagamento cancelado.\n")
                break
            
            else:
                print("Opção inválida. Por favor, selecione uma das opções disponíveis.\n")