import os

class Paths:
    base_dir = os.path.dirname(__file__)
    save_clientes = os.path.join(base_dir, 'clientes.json')
    save_adms = os.path.join(base_dir, 'adms.json')
    save_produtos = os.path.join(base_dir, 'produtos.json')
    save_carrinho = os.path.join(base_dir, 'carrinho.json')