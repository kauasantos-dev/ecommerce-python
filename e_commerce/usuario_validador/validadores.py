import unicodedata

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