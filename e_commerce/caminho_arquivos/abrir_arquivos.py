import json

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