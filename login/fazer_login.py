from ecommerce.usuarios import config_usuarios as usuario
from ecommerce.gerenciamento import gerenciar_arquivos as arquivo
from funcoes.dados import solicitar_dados

def fazer_login():
    """
    Pede ao usuário e-mail e senha para fazer login.

    Returns:
        Cliente:
            Instância da classe `Cliente`, caso o e-mail informado esteja cadastrado em uma conta de cliente.

        Administrador:
            Instância da classe `Administrador`, caso o e-mail informado esteja cadastrado em uma conta de administrador.

        bool:
            Retorna `False` se o e-mail informado não estiver cadastrado em nenhuma conta. 
    """
    email = input("Digite seu e-mail: ").strip()
    senha = input("Digite sua senha: ").strip()
    conta_clientes = usuario.Cliente.verificar_email_senha(email, senha)
    conta_adms = usuario.Administrador.verificar_email_senha(email, senha)
    if conta_clientes:
        return usuario.Cliente(email, senha)
    elif conta_adms:
        return usuario.Administrador(email, senha)
    else:
        return False

verificar_existencia_adm = arquivo.AbrirArquivo.arquivo_r(arquivo.Paths.save_adms)
if not verificar_existencia_adm:
    print("CRIE SUA CONTA DE ADMINISTRADOR(A)\n")
    dados_adm = [solicitar_dados.dados_para_abrir_conta()]
    arquivo.AbrirArquivo.arquivo_w(arquivo.Paths.save_adms, dados_adm)
    print("CONTA CRIADA COM SUCESSO!\n")

def emails_cadastrados(email):
    lista_clientes = arquivo.AbrirArquivo.arquivo_r(arquivo.Paths.save_clientes)
    lista_adms = arquivo.AbrirArquivo.arquivo_r(arquivo.Paths.save_adms)
    for administrador in lista_adms:
        if email == administrador['E-mail']:
            return True
    if lista_clientes:
        for cliente in lista_clientes:
            if email == cliente['E-mail']:
                return True
    return False