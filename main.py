from e_commerce import *
import uuid
import sys

print("\n===== LOJA ONLINE =====\n")

def solicitar_dados(mensagem_input, validador):
    """
    Solicita um dado ao usuário e valida o valor informado.

    Args:
        mensagem_input (str):
            Texto exibido ao solicitar o dado via input().
        
        validador (callable):
            Função ou método de validação pertencente à classe `Validador`.
            Deve lançar um `ValueError` caso o valor informado seja inválido.

    Returns:
        Any:
            Dado validado e aprovado pelo método de validação utilizado.
    
    Observações:
        O dado só é retornado se atender a todas as validações do método.
        Caso contrário, o loop continuará até que o usuário informe um valor válido.
    """
    while True:
        try:
            dado_informado = validador(input(mensagem_input).strip())
            return dado_informado
        except ValueError as erro:
            print(f"Erro: {erro}. Tente novamente.\n")
            continue

def validar_dados():
    while True:
        try:
            nome = Validador.validar_nome(input("Crie seu nome de usuário: "))
            email = Validador.validar_email(input("Digite seu e-mail: "))
            senha = Validador.validar_senha(input("Crie sua senha: "))
            id_usuario = str(uuid.uuid4())
            return {'Nome': nome, 'E-mail': email, 'Senha': senha, 'ID': id_usuario}
        except ValueError as erro:
            print("Erro:", erro, "Tente novamente.\n")

verificar_conta = AbrirArquivo.arquivo_r(Paths.save_adms)
if not verificar_conta:
    print("CRIE SUA CONTA DE ADMINISTRADOR(A)\n")
    dados_adm = [validar_dados()]
    AbrirArquivo.arquivo_w(Paths.save_adms, dados_adm)
    print("Conta criada com sucesso!\n")

def criar_conta(email):
    lista_clientes = AbrirArquivo.arquivo_r(Paths.save_clientes)
    lista_adms = AbrirArquivo.arquivo_r(Paths.save_adms)
    for administrador in lista_adms:
        if email == administrador['E-mail']:
            return True
    if lista_clientes:
        for cliente in lista_clientes:
            if email == cliente['E-mail']:
                return True
    return False

def login(email, senha):
    conta_cliente = Cliente.verificar_email_senha(email, senha)
    conta_adm = Administrador.verificar_email_senha(email, senha)
    if conta_cliente:
        return 'cliente'
    elif conta_adm:
        return 'adm'
    else:
        return False
    
def menu_cliente():
    print("1- Ver produtos da loja\n2- Buscar um produto\n3- Ver meu carrinho\n4- Adicionar produto ao carrinho\n5- Fazer pedido\n6- Sair\n")

def menu_adm():
    print("1- Ver produtos da loja\n2- Buscar produto\n3- Adicionar novo produto\n4- Remover produto\n5- Atualizar preço\n6- Atualizar estoque\n7- Sair\n")

def ver_ou_buscar_produtos(instancia, opcao_selecionada):
    """
    Verifica a opção do menu selecionada pelo o usuário e chama a função `exibir_produtos`.

    Args:
        instancia (Cliente | Administrador):
            Objeto criado a partir da classe `Cliente` ou `Administrador`.
            Ambas possuem dois métodos em comum:
                - mostrar_produtos_loja(): retorna uma lista com todos os produtos disponíveis na loja.
                - buscar_produto(nome_produto): retorna um produto específico informado pelo o usuário.
        
        opcao_selecionada (str):
            Opção do menu selecionada pelo usuário.
            Pode ser:
                - '1': Ver todos os produtos da loja.
                - '2': Buscar um produto específico.
    """
    produtos_loja = instancia.mostrar_produtos_loja()
    if not produtos_loja:
        print("Não há produtos disponíveis na loja.\n")
    else:
        if opcao_selecionada == '1':
            print("PRODUTOS DA LOJA:\n")
            exibir_produto(produtos_loja)
        
        elif opcao_selecionada == '2':
            nome_produto = input("Informe o nome do produto: ").strip()
            produto_encontrado = instancia.buscar_produto(nome_produto)
            if produto_encontrado:
                print("PRODUTO ENCONTRADO:\n")
                exibir_produto(produto_encontrado)
            else:
                print("Nenhum produto encontrado.\n")
                
def exibir_produto(produtos_loja):
    """
    Exibe as informações de um ou mais produtos da loja.

    Args:
        produtos_loja (list | dict):
            Produtos que serão exibidos ao usuário.
            Pode ser uma lista de dicionários (todos os produtos da loja).
            Ou um único dicionário (produto específico).
    """
    def imprimir(produto):
        """
        Imprime as informações do produto (nome, preço, estoque).

        Args:
            produto (dict): 
                Dicionário contendo os dados do produto, com as chaves:
                - 'Nome': Nome do produto.
                - 'Preço': Preço do produto.
                - 'Estoque': Estoque do produto.
        """
        for chave, valor in produto.items():
            if chave == 'Preço':
                print(f"{chave}: R${valor:.2f}")
            elif chave == 'Estoque':
                print(f"{chave}: {valor}\n")
            else:
                print(f"{chave}: {valor}")
                print("-" * 30)
    
    if isinstance(produtos_loja, list):
        for produto in produtos_loja:
            imprimir(produto)

    elif isinstance(produtos_loja, dict):
        imprimir(produtos_loja)

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

def pix(produto):
    while True:
        try:
            preco_digitado = Validador.validar_preco(input("Digite o preço do produto: "))
            break
        except ValueError as erro:
            print("Erro", erro, "Tente novamente.\n")
            continue
    if preco_digitado != produto['Preço']:
        return False
    else:
        return True
            
def cartao():
    while True:
        try:
            numero = input("Número: ")
            nome = input("Nome no cartão (exatamente como consta no cartão): ")
            validade = input("Validade: ")
            cvv = input("Código de segurança: ")
            ValidarEnderecoECartao.validar_cartao(numero, nome, validade, cvv)
            break
        except ValueError as erro:
            print("Erro: ", erro, " Tente novamente.\n")
            continue
    return True

def endereco():
    while True:
        try:
            estado = input("Informe o nome do estado: ")
            cidade = input("Informe o nome da cidade: ")
            rua = input("Informe o nome da rua: ")
            numero = input("Informe o número da residência: ")
            bairro = input("Informe o nome do bairro: ")
            ValidarEnderecoECartao.validar_endereço(estado, cidade, rua, numero, bairro)
            return
        except ValueError as erro:
            print("Erro: ", erro, " Tente novamente.\n")
            continue
    
def adicionar_produto(nome, preco, estoque):
    adicionar = adm.adicionar_produto(nome, preco, estoque)
    if adicionar:
        print("O produto foi adicionado a sua loja!\n")
    else:
        print("Esse produto já está presente na loja.\n")

def remover_produto(nome_produto):
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
        adicionar_produto(nome_produto, preco, estoque)
                
    elif opcao_adm == '4':
        nome_produto = input("Digite o nome do produto: ")
        remover_produto(nome_produto)
                
    elif opcao_adm == '5':
        atualizar_preco_estoque(opcao_adm)
                
    elif opcao_adm == '6':
        atualizar_preco_estoque(opcao_adm)
                
    else:
        print("Opção inválida. Por favor, selecione uma das opções disponíveis.\n")

while True:
    print("Selecione uma opção abaixo (digite o número da opção):\n")
    print("1- Fazer login\n2- Criar uma nova conta\n3- Sair\n")
    opcao = input()

    if opcao == '1':
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        fazer_login = login(email, senha)

        if fazer_login == 'cliente':
            cliente = Cliente(email, senha)
            print("Login efetuado com sucesso!\n")
            while True:
                print("\nMENU DE OPÇÕES (DIGITE O NÚMERO DA OPÇÃO):\n")
                menu_cliente()
                opcao_cliente = input()
                if opcao_cliente == '6':
                    break
                else:
                    opcao_selecionada_cliente(cliente, opcao_cliente)
        
        elif fazer_login == 'adm':
            adm = Administrador(email, senha)
            print("Login efetuado com sucesso!\n")
            while True:
                print("\nMENU DE OPÇÕES (DIGITE O NÚMERO DA OPÇÃO):\n")
                menu_adm()
                opcao_adm = input()
                if opcao_adm == '7':
                    break
                else:
                    opcao_selecionada_adm(adm, opcao_adm)
        else:
            print("E-mail ou senha incorreta. Tente novamente.\n")    

    elif opcao == '2':
        novo_cliente = validar_dados()
        criar = criar_conta(novo_cliente['E-mail'])
        if not criar:
            lista_clientes = AbrirArquivo.arquivo_r(Paths.save_clientes)
            if lista_clientes:
                lista_clientes.append(novo_cliente)
            else:
                lista_clientes = [novo_cliente]
            AbrirArquivo.arquivo_w(Paths.save_clientes, lista_clientes)
            print("Conta criada com sucesso!\n")
        else:
            print("Já existe uma conta com esse e-mail.\n")
    
    elif opcao == '3':
        print("Programa encerrado.")
        sys.exit(0)
    
    else:
        print("Opção inválida. Por favor, selecione uma das opções disponíveis.\n")