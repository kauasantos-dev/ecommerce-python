from ecommerce.gerenciamento import gerenciar_arquivos as arquivo
from funcoes.produtos import ver_produtos
from funcoes.pagamento import formas_pagamento
from ecommerce.usuarios import validadores

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
        lista_produtos = arquivo.AbrirArquivo.arquivo_r(arquivo.Paths.save_produtos)
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
                fazer_pagamento = formas_pagamento.pix(produto_encontrado)
                if fazer_pagamento:
                    print("Pagamento realizado com sucesso! Seu pedido estará a caminho em breve.\n")
                    break
                else:
                    print(f"O preço do produto é R${produto['Preço']:.2f}. Tente novamente.\n")
                                
            elif pagamento == '2':
                print("INSIRA OS DADOS DO SEU CARTÃO\n")
                fazer_pagamento = formas_pagamento.cartao()
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

def endereco():
    while True:
        try:
            estado = input("Informe o nome do estado: ")
            cidade = input("Informe o nome da cidade: ")
            rua = input("Informe o nome da rua: ")
            numero = input("Informe o número da residência: ")
            bairro = input("Informe o nome do bairro: ")
            validadores.ValidarEnderecoECartao.validar_endereço(estado, cidade, rua, numero, bairro)
            return
        except ValueError as erro:
            print("Erro: ", erro, " Tente novamente.\n")
            continue

def opcao_selecionada_cliente(instancia_cliente, opcao_cliente):
    if opcao_cliente == '1' or opcao_cliente == '2':
        ver_produtos.ver_ou_buscar_produtos(instancia_cliente, opcao_cliente)
                
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