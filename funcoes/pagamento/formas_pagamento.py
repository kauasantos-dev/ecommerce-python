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