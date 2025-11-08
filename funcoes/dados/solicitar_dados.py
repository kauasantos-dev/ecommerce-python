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
    nome = Validador.validar_nome(input("Crie seu nome de usuário: "))
    email = Validador.validar_email(input("Digite seu e-mail: "))
    senha = Validador.validar_senha(input("Crie sua senha: "))
    id_usuario = str(uuid.uuid4())
    verificar_existencia_email = emails_cadastrados(email)
    if verificar_existencia_email:
        return False
    else:
        return {'Nome': nome, 'E-mail': email, 'Senha': senha, 'ID': id_usuario}