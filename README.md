# Sistema Bancário POO com Decoradores, Iteradores e Geradores
Implementação de um sistema bancário simples em Python, utilizando conceitos de Programação Orientada a Objetos (POO), decoradores, iteradores e geradores. 
O sistema permite criar clientes, contas bancárias, realizar depósitos e saques, visualizar extratos e saldos, além de gerar relatórios de transações.

## Funcionalidades
Criação de Clientes: Cadastro de clientes com nome, CPF, data de nascimento e endereço.
Criação de Contas: Abertura de contas bancárias para clientes, com depósito inicial.
Depósitos e Saques: Realização de depósitos e saques em contas, com validação de saldo e limite de saques.
Extrato e Saldo: Visualização do extrato completo e do saldo atual de uma conta.
Listagem de Clientes e Contas: Exibição de todos os clientes e contas cadastrados no sistema.
Iterador de Contas: Iteração sobre as contas de um cliente específico, retornando informações básicas de cada conta.
Gerador de Relatórios: Geração de relatórios de transações, com filtros por tipo (depósito, saque ou completo).
Decorador de Log: Registro automático de cada transação realizada, incluindo tipo, data e hora.

## Estrutura do Projeto
O projeto está organizado em módulos e classes, seguindo os princípios da POO:

controllers: Contém as classes ClienteController e ContaController, responsáveis pela lógica de negócio do sistema.
models: Contém as classes que representam os objetos do sistema, como Cliente, Conta, PessoaFisica, Transacao, Deposito, Saque, Historico e ContaIterador.
views: Contém a classe MenuView, responsável pela interação com o usuário através de um menu de opções.
main.py: Arquivo principal que executa o programa, inicializa os controladores e a interface de menu, e gerencia o fluxo de execução.

## Tecnologias Utilizadas
Python: Linguagem de programação utilizada para desenvolver o sistema.
Programação Orientada a Objetos (POO): Paradigma de programação que organiza o código em objetos com propriedades e métodos, facilitando a modularidade e reutilização.
Decoradores: Funções que modificam o comportamento de outras funções, utilizadas aqui para registrar automaticamente as transações.
Iteradores: Objetos que permitem percorrer elementos de uma coleção sequencialmente, utilizados para listar as contas de um cliente.
Geradores: Funções especiais que produzem uma sequência de valores sob demanda, utilizados para gerar os relatórios de transações.

## Como Executar o Projeto
Clone o repositório do projeto.
Certifique-se de ter o Python 3 instalado em seu sistema.
Execute o arquivo main.py no terminal:
Bash
python3 main.py

## Siga as instruções do menu para interagir com o sistema bancário.
