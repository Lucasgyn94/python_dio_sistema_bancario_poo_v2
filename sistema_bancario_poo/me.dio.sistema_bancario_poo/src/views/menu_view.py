import textwrap

class MenuView:
    def mostrar_menu(self):
        menu = """\n
        ================ MENU ================
        [1] Novo usuário
        [2] Nova conta
        [3] Listar contas
        [4] Listar clientes
        [5] Sacar
        [6] Extrato
        [7] Ver saldo
        [8] Depositar
        [9] Listar contas de um cliente (Iterador)
        [10] Gerar relatório completo
        [11] Gerar relatório de depósitos
        [12] Gerar relatório de saques
        [13] Sair
        => """
        return input(textwrap.dedent(menu))

    def obter_dados_cliente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
        endereco = input("Endereço: ")
        return nome, cpf, data_nascimento, endereco

    def obter_dados_conta(self):
        numero = input("Número da Conta: ")
        agencia = input("Agência: ")
        return numero, agencia

    def obter_valor(self, tipo):
        return float(input(f"Valor do {tipo}: "))

    def obter_cpf(self):
        return input("CPF do Cliente: ")

    def obter_numero_conta(self):
        return input("Número da Conta: ")

    def exibir_extrato(self, extrato):
        if extrato:
            for transacao in extrato:
                print(f"{transacao['data']}: {transacao['tipo']} de R${transacao['valor']:.2f}")
        else:
            print("Nenhuma transação encontrada.")

    def exibir_saldo(self, saldo):
        print(f"Saldo atual: R${saldo:.2f}")

    def obter_tipo_relatorio(self):
        while True:
            tipo = input("Tipo de relatório (completo, deposito, saque): ")
            if tipo in ["completo", "deposito", "saque"]:
                return tipo
            else:
                print("Opção inválida. Escolha entre 'completo', 'deposito' ou 'saque'.")