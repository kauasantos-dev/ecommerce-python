import projeto.caminho_arquivos.abrir_arquivos as arquivo
import projeto.caminho_arquivos.caminhos as caminhos

class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def mostrar_produtos(self):
        produtos = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_produtos)
        if not produtos:
            return False
        else:
            return produtos

    def buscar_produto(self, nome):
        produto_encontrado = self.verificar_produto(nome)
        if produto_encontrado:
            lista_produtos = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_produtos)
            for produto in lista_produtos:
                if nome.lower() == produto['Nome'].lower():
                    return produto
        else:
            return False

    def verificar_produto(self, nome):
        lista_produtos = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_produtos)
        if not lista_produtos:
            return None
        else:
            for produto in lista_produtos:
                if nome.lower() == produto['Nome'].lower():
                    return True
        return False
        
class Cliente(Usuario):
    def __init__(self, email, senha):
        super().__init__(email, senha)

    @staticmethod
    def verificar_email_senha(email, senha):
        lista_de_clientes = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_clientes)
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
            carrinho = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_carrinho)
            lista_clientes = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_clientes)
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
            arquivo.AbrirArquivo.arquivo_w(caminhos.Paths.save_carrinho, carrinho)
            return True
        else:
            carrinho = [{'ID': id_cliente, 'Carrinho': [nome]}]
            arquivo.AbrirArquivo.arquivo_w(caminhos.Paths.save_carrinho, carrinho)
            return True
            
    def ver_carrinho(self):
        verificar_id = False
        lista_clientes = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_clientes)
        for cliente in lista_clientes:
            if self.email == cliente['E-mail']:
                id_cliente = cliente['ID']
                break
        carrinho = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_carrinho)
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

class Administrador(Usuario):
    def __init__(self, email, senha):
        super().__init__(email, senha)

    @staticmethod
    def verificar_email_senha(email, senha):
        lista_adms = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_adms)
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
            lista_produtos = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_produtos)
            lista_produtos.append({'Nome': nome, 'Preço': preco, 'Estoque': estoque})
        arquivo.AbrirArquivo.arquivo_w(caminhos.Paths.save_produtos, lista_produtos)
        return True
    
    def remover_produto(self, nome):
        achar_produto = super().verificar_produto(nome)
        if achar_produto:
            lista_produtos = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_produtos)
            for i in range(len(lista_produtos)):
                if nome.lower() == lista_produtos[i]['Nome'].lower():
                    indice = i
                    break
            del lista_produtos[indice]
            arquivo.AbrirArquivo.arquivo_w(caminhos.Paths.save_produtos, lista_produtos)
            return True
        else:
            return False
    
    def atualizar_estoque(self, nome, estoque):
        achar_produto = super().verificar_produto(nome)
        if achar_produto:
            lista_produtos = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_produtos)
            for i in range(len(lista_produtos)):
                if nome.lower() == lista_produtos[i]['Nome'].lower():
                    lista_produtos[i]['Estoque'] = estoque
                    break
            arquivo.AbrirArquivo.arquivo_w(caminhos.Paths.save_produtos, lista_produtos)
            return True
        else:
            return False
    
    def atualizar_preco(self, nome, preco):
        achar_produto = super().verificar_produto(nome)
        if achar_produto:
            lista_produtos = arquivo.AbrirArquivo.arquivo_r(caminhos.Paths.save_produtos)
            for i in range(len(lista_produtos)):
                if nome.lower() == lista_produtos[i]['Nome'].lower():
                    lista_produtos[i]['Preço'] = preco
                    break
            arquivo.AbrirArquivo.arquivo_w(caminhos.Paths.save_produtos, lista_produtos)
            return True
        else:
            return False