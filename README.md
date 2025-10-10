<h1 align="center">Loja Online — E-commerce em Python</h1>
<p align="center">Aplicação de terminal com contas de usuários, carrinho e pedidos com pagamento simulado</p>


## Sobre o Projeto

Um sistema completo de **loja virtual em terminal**, desenvolvido em **Python**, com suporte a **contas de administradores e clientes**, gerenciamento de **produtos**, **carrinho de compras** e **processo de pedido com pagamento simulado**.

---

## Requisitos

- Python **3.10** ou superior
- Nenhuma biblioteca externa é necessária (usa apenas módulos padrão do Python)

---

## Funcionalidades Principais

### Administrador
- Criar conta de administrador (obrigatória na primeira execução)
- Fazer login
- Adicionar novos produtos à loja
- Remover produtos
- Atualizar preço e estoque
- Visualizar e buscar produtos disponíveis

### Cliente
- Criar conta de cliente
- Fazer login
- Visualizar todos os produtos
- Buscar um produto específico
- Adicionar produtos ao carrinho
- Visualizar carrinho
- Fazer pedido (com validação de endereço e simulação de pagamento via Pix ou cartão)

---

## Tecnologias Utilizadas

- **Python 3.10+**
- **JSON** para armazenamento de dados locais
- **Programação orientada a objetos (POO)**
- **Tratamento de exceções**
- **Validação de dados de entrada**

---

## Estrutura do Projeto

ecommerce-python/
│
├── e_commerce.py    # Lógica POO do projeto
├── main.py          # Arquivo principal com menus e fluxo da aplicação
├── config.py        # Classe Paths: caminhos dos arquivos salvos
└── README.md        # Este arquivo

---

## Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/kauasantos-dev/ecommerce-python.git
cd ecommerce-python
```

### 2. Executar o programa
```bash
python main.py
```

### 3. Criar conta de administrador

Na primeira execução, será solicitado o cadastro de um administrador.
Sem isso, o sistema não permitirá a criação de contas de clientes.

---

## Armazenamento de Dados

Os dados são salvos localmente em arquivos .json dentro da pasta do projeto:

| **Arquivo**             | **Conteúdo**                                  |
|-------------------------|-----------------------------------------------|
| `clientes.json`         | Dados dos clientes                            |
| `adms.json`             | Dados dos administradores                     |
| `produtos.json`         | Lista de produtos da loja                     |
| `carrinho.json`         | Itens adicionados ao carrinho de cada cliente |

---

## Principais Classes e Responsabilidades

| **Classe**                     | **Responsabilidade**                                              |
|--------------------------------|-------------------------------------------------------------------|                
| `Paths`                        | Gerencia os caminhos dos arquivos JSON                            |
| `AbrirArquivo`                 | Faz a leitura e escrita dos arquivos JSON                         |
| `Validador`                    | Valida entradas (nome, email, senha,     preço, estoque etc.)     |
| `ValidarEnderecoECartao`       | Valida endereço e dados de pagamento                              |
| `Usuario`                      | Classe base com funcionalidades comuns                            |
| `Cliente`                      | Representa o cliente e seus métodos (ver produtos, carrinho etc.) |
| `Administrador`                | Representa o administrador e seus métodos (gerenciar produtos)    |

---

## Validações Incluídas

- Nome com apenas letras
- E-mail em formato válido
- Senha com mínimo de caracteres e mistura de tipos
- Preço e estoque com valores positivos
- Endereço completo (estado, cidade, rua, número e bairro)
- Cartão com número, nome, validade e CVV válidos

---

## Simulação de Pagamento

Durante o pedido, o cliente pode escolher entre:

- **Pix:** Confirmação do valor digitado igual ao do produto
- **Cartão de crédito:** Simulação de validação dos dados do cartão

Se o pagamento for aprovado, o sistema exibe a mensagem:
    “Pagamento realizado com sucesso! Seu pedido estará a caminho em breve.”

---

## Exemplo de Uso (Terminal)

```bash
===== LOJA ONLINE =====

1- Fazer login
2- Criar uma nova conta
3- Sair

Digite sua opção: 1

E-mail: cliente@email.com
Senha: 1234

Login efetuado com sucesso!

MENU DE OPÇÕES:
1- Ver produtos da loja
2- Buscar um produto
3- Ver meu carrinho
4- Adicionar produto ao carrinho
5- Fazer pedido
6- Sair
```

---

## Contribuição

Contribuições são bem-vindas!
Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorar o projeto.

---

## Licença

Este programa está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**Kavilly Kauã**

Estudante de **Análise e Desenvolvimento de Sistemas (ADS) - IFRN**

💼 Projeto acadêmico / estudo de lógica e POO com Python

📧 Contato: kavillykaua@gmail.com

🌐 GitHub: github.com/kauasantos-dev
