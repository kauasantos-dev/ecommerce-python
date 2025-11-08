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