from ecommerce.usuarios import validadores
from login import fazer_login
import uuid

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

def dados_para_abrir_conta():
    """
    Solicita e valida dados necessários para criar uma nova conta.

    Utiliza a função `solicitar_dados` para receber:
        - Nome de usuário
        - E-mail
        - Senha
    
        Gera automaticamente um ID único para o usuário.

    Returns:
        False: Caso o e-mail informado já esteja cadastrado em uma conta.
        dict: Dicionário contendo os dados informados pelo o usuário:
            - 'Nome': nome de usuário.
            - 'E-mail': e-mail do usuário.
            - 'Senha': senha do usuário.
            - 'ID': identificação exclusiva do usuário.
    """
    nome = solicitar_dados("Crie seu nome de usuário: ", validadores.ValidarUsuario.validar_nome)
    email = solicitar_dados("Digite seu e-mail: ", validadores.ValidarUsuario.validar_email)
    senha = solicitar_dados("Digite sua senha: ", validadores.ValidarUsuario.validar_senha)
    id_usuario = str(uuid.uuid4())
    verificar_existencia_email = fazer_login.emails_cadastrados(email)
    if verificar_existencia_email:
        return False
    else:
        return {'Nome': nome, 'E-mail': email, 'Senha': senha, 'ID': id_usuario}