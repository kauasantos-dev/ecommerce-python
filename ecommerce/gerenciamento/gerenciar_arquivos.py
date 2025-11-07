import os
import json

class Paths:
    base_dir = os.path.dirname(__file__)
    save_clientes = os.path.join(base_dir, 'clientes.json')
    save_adms = os.path.join(base_dir, 'adms.json')
    save_produtos = os.path.join(base_dir, 'produtos.json')
    save_carrinho = os.path.join(base_dir, 'carrinho.json')

class AbrirArquivo:
    @staticmethod
    def arquivo_w(caminho, conteudo):
        with open(caminho, "w", encoding='utf-8') as file:
            json.dump(conteudo, file, indent=2, ensure_ascii=False)

    @staticmethod
    def arquivo_r(caminho):
        try:
            with open(caminho, "r", encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return False