from config import Paths
import unicodedata
import json

class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def mostrar_produtos(self):
        produtos = AbrirArquivo.arquivo_r(Paths.save_produtos)
        if not produtos:
            return False
        else:
            return produtos

    def buscar_produto(self, nome):
        produto_encontrado = self.verificar_produto(nome)
        if produto_encontrado:
            lista_produtos = AbrirArquivo.arquivo_r(Paths.save_produtos)
            for produto in lista_produtos:
                if nome.lower() == produto['Nome'].lower():
                    return produto
        else:
            return False

    def verificar_produto(self, nome):
        lista_produtos = AbrirArquivo.arquivo_r(Paths.save_produtos)
        if not lista_produtos:
            return None
        else:
            for produto in lista_produtos:
                if nome.lower() == produto['Nome'].lower():
                    return True
        return False

class Validador:
    @staticmethod
    def validar_nome(nome):
        if nome.replace(" ", "").isalnum():
            return nome.replace(" ", "")
        else:
            raise ValueError("O nome de usuário deve conter apenas letras e números.")
    
    @staticmethod
    def validar_senha(senha):
        if len(senha) < 6:
            raise ValueError("A senha deve conter no mínimo seis caracteres.")
        
        elif " " in senha:
            raise ValueError("A senha não pode conter espaços.")
        
        elif senha.isalnum():
            raise ValueError("A senha deve conter pelo menos um caractere especial.")
        return senha
    
    @staticmethod
    def validar_email(email):
        #validação 1
        if email.count('@') != 1:
            raise ValueError("O e-mail deve conter somente um domínio '@'.")
        else:
            dividir_email = email.split('@') #isso divide o local port e o domínio do e-mail
            local_part = dividir_email[0] #antes do '@'
            domain = dividir_email[1] #depois do '@'

        #validação 2
        for letra in email:
            if letra.isalpha():
                acentucao = unicodedata.normalize('NFD', letra)
                if any(unicodedata.combining(c) for c in acentucao):
                    raise ValueError("O e-mail não pode conter acentuação.")
        
        #validação 3
        if " " in email:
            raise ValueError("O e-mail não pode conter espaços.")
        
        #validação 4
        for i in range(1, len(email)):
            if not email[i].isalnum() and not email[i-1].isalnum():
                raise ValueError("O e-mail não pode conter caracteres especiais em sequência.")
        
        #validação 5
        if not local_part[0].isalnum() or not local_part[-1].isalnum():
            raise ValueError("O e-mail não pode começar ou terminar com caracteres especiais.")
        
        #validação 6
        elif not domain[0].isalnum() or not domain[-1].isalnum():
            raise ValueError("O domínio do e-mail não pode começar ou terminar com caracteres especiais.")
        return email
    
    @staticmethod
    def validar_preco(preco):
        try:
            preco = float(preco)
        except ValueError:
            raise ValueError("O preço deve conter somente números.")
        
        if preco <= 0:
            raise ValueError("O preço não pode ser menor ou igual a zero.")
        return preco
    
    @staticmethod
    def validar_nome_produto(nome_produto):
        if nome_produto.replace(" ", "").isalnum():
            return nome_produto.strip()
        else:
            raise ValueError("O nome do produto deve conter apenas letras e números.")
    
    @staticmethod
    def validar_estoque(estoque):
        try:
            estoque = int(estoque)
        except ValueError:
            raise ValueError("O estoque deve conter apenas números.")
        
        if estoque < 0:
            raise ValueError("O estoque não pode ser menor que zero.")
        return estoque
    
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
        
class Cliente(Usuario):
    def __init__(self, email, senha):
        super().__init__(email, senha)

    @staticmethod
    def verificar_email_senha(email, senha):
        lista_de_clientes = AbrirArquivo.arquivo_r(Paths.save_clientes)
        if not lista_de_clientes:
            return False
        else:
            for cliente in lista_de_clientes:
                if email == cliente['E-mail'] and senha == cliente['Senha']:
                    return True
        return False
        
    def mostrar_produtos(self):
       return super().mostrar_produtos()
    
    def buscar_produto(self, nome):
        return super().buscar_produto(nome)

    def salvar_produtos(self, nome):
        procurar_id = False
        achar_produto = super().verificar_produto(nome)
        if not achar_produto:
            return None
        else:
            carrinho = AbrirArquivo.arquivo_r(Paths.save_carrinho)
            lista_clientes = AbrirArquivo.arquivo_r(Paths.save_clientes)
            for cliente in lista_clientes:
                if self.email == cliente['E-mail']:
                    id_cliente = cliente['ID'] #precisa achar o id do cliente para identificar o carrinho dele
                    break
        if carrinho:
            for i in range(len(carrinho)):
                if id_cliente == carrinho[i]['ID']:
                    indice = i
                    procurar_id = True
                    produtos_salvos = carrinho[i]['Carrinho']
                    break
            if procurar_id:
                for produto in produtos_salvos:
                    if nome.replace(" ", "").lower() == produto.replace(" ", "").lower(): #verifica se o produto informado pelo cliente já está salvo no carrinho dele
                        return False            
                produtos_salvos.append(nome)
                carrinho[indice] = {'ID': id_cliente, 'Carrinho': produtos_salvos}
            else:
                carrinho.append({'ID': id_cliente, 'Carrinho': [nome]}) 
            AbrirArquivo.arquivo_w(Paths.save_carrinho, carrinho)
            return True
        else:
            carrinho = [{'ID': id_cliente, 'Carrinho': [nome]}]
            AbrirArquivo.arquivo_w(Paths.save_carrinho, carrinho)
            return True
            
    def ver_carrinho(self):
        verificar_id = False
        lista_clientes = AbrirArquivo.arquivo_r(Paths.save_clientes)
        for cliente in lista_clientes:
            if self.email == cliente['E-mail']:
                id_cliente = cliente['ID']
                break
        carrinho = AbrirArquivo.arquivo_r(Paths.save_carrinho)
        if carrinho:
            for i in range(len(carrinho)):
                if id_cliente == carrinho[i]['ID']:
                    verificar_id = True
                    produtos_carrinho = carrinho[i]['Carrinho']
                    break
            if verificar_id:
                return produtos_carrinho
            else:
                return False
        else:
            return False

class ValidarEnderecoECartao:
    @staticmethod
    def validar_cartao(numero, nome, validade, cvv):
        if not numero.replace(" ", "").isdigit():
            raise ValueError("O número do cartão não pode conter letras ou caracteres especiais.")

        elif not nome.replace(" ", "").isalpha():
            raise ValueError("O nome deve conter apenas letras e espaços como consta no cartão.")
        
        elif validade.count("/") != 1 or not validade.replace("/", "").isdigit():
            raise ValueError("A data de validade deve estar como consta no cartão.")   

        elif not cvv.isdigit():
            raise ValueError("O código de segurança deve conter apenas números.")
        
        elif len(cvv) != 3:
            raise ValueError("O código de segurança deve conter apenas três números como consta no cartão.")
        
    @staticmethod
    def validar_endereço(estado, cidade, rua, numero, bairro):
        if not estado.replace(" ", "").isalpha():
            raise ValueError("O nome do estado deve conter apenas letras e espaços.")

        elif not cidade.replace(" ", "").isalpha():
            raise ValueError("O nome da cidade deve conter apenas letras e espaços.")
        
        elif not rua.replace(" ", "").isalnum():
            raise ValueError("O nome da rua não pode conter caracteres especiais.")
        
        elif not numero.isdigit():
            raise ValueError("O número residencial não pode conter letras, espaços ou caracteres especiais.")
        
        elif not bairro.replace(" ", "").isalnum():
            raise ValueError("O nome do bairro não pode conter caracteres especiais.")

class Administrador(Usuario):
    def __init__(self, email, senha):
        super().__init__(email, senha)

    @staticmethod
    def verificar_email_senha(email, senha):
        lista_adms = AbrirArquivo.arquivo_r(Paths.save_adms)
        if not lista_adms:
            return False
        else:
            for adm in lista_adms:
                if email == adm['E-mail'] and senha == adm['Senha']:
                    return True
        return False
    
    def mostrar_produtos(self):
        return super().mostrar_produtos()
    
    def buscar_produto(self, nome):
        return super().buscar_produto(nome)
    
    def adicionar_produto(self, nome, preco, estoque):
        achar_produto = super().verificar_produto(nome)
        if achar_produto:
            return False
        
        elif achar_produto is None:
            lista_produtos = [{'Nome': nome, 'Preço': preco, 'Estoque': estoque}]

        else:
            lista_produtos = AbrirArquivo.arquivo_r(Paths.save_produtos)
            lista_produtos.append({'Nome': nome, 'Preço': preco, 'Estoque': estoque})
        AbrirArquivo.arquivo_w(Paths.save_produtos, lista_produtos)
        return True
    
    def remover_produto(self, nome):
        achar_produto = super().verificar_produto(nome)
        if achar_produto:
            lista_produtos = AbrirArquivo.arquivo_r(Paths.save_produtos)
            for i in range(len(lista_produtos)):
                if nome.lower() == lista_produtos[i]['Nome'].lower():
                    indice = i
                    break
            del lista_produtos[indice]
            AbrirArquivo.arquivo_w(Paths.save_produtos, lista_produtos)
            return True
        else:
            return False
    
    def atualizar_estoque(self, nome, estoque):
        achar_produto = super().verificar_produto(nome)
        if achar_produto:
            lista_produtos = AbrirArquivo.arquivo_r(Paths.save_produtos)
            for i in range(len(lista_produtos)):
                if nome.lower() == lista_produtos[i]['Nome'].lower():
                    lista_produtos[i]['Estoque'] = estoque
                    break
            AbrirArquivo.arquivo_w(Paths.save_produtos, lista_produtos)
            return True
        else:
            return False
    
    def atualizar_preco(self, nome, preco):
        achar_produto = super().verificar_produto(nome)
        if achar_produto:
            lista_produtos = AbrirArquivo.arquivo_r(Paths.save_produtos)
            for i in range(len(lista_produtos)):
                if nome.lower() == lista_produtos[i]['Nome'].lower():
                    lista_produtos[i]['Preço'] = preco
                    break
            AbrirArquivo.arquivo_w(Paths.save_produtos, lista_produtos)
            return True
        else:
            return False