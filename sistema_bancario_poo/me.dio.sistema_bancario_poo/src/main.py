import textwrap
from controllers.cliente_controller import ClienteController
from controllers.conta_controller import ContaController
from views.menu_view import MenuView
from models.conta_iterador import ContaIterador


def criar_cliente(cliente_controller, menu_view):
    nome, cpf, data_nascimento, endereco = menu_view.obter_dados_cliente()
    cliente_controller.criar_cliente(nome, cpf, data_nascimento, endereco)
    print("Cliente criado com sucesso!")

def criar_conta(cliente_controller, conta_controller, menu_view):
    cpf = menu_view.obter_cpf()
    cliente = cliente_controller.buscar_cliente_por_cpf(cpf)
    if cliente:
        valor_deposito = menu_view.obter_valor("deposito")
        conta_controller.criar_conta(cliente, valor_deposito)
        print("Conta criada com sucesso!")
    else:
        print("Cliente não encontrado!")

def listar_contas(cliente_controller):  # Corrigido para listar todas as contas
    clientes = cliente_controller.clientes
    contas_encontradas = False
    for cliente in clientes:
        for conta in cliente.contas:  # Itera diretamente nas contas do cliente
            contas_encontradas = True
            print(f"Conta: {conta.numero_conta}, Agência: {conta.agencia}, Saldo: {conta.saldo}, Titular: {cliente.nome}")
    if not contas_encontradas:
        print("Nenhuma conta cadastrada.")

def gerar_relatorio(cliente_controller, conta_controller, menu_view, tipo_relatorio="completo"):
    cpf = menu_view.obter_cpf()
    cliente = cliente_controller.buscar_cliente_por_cpf(cpf)
    if cliente:
        numero_conta = menu_view.obter_numero_conta()
        conta = conta_controller.buscar_conta_por_numero(cliente, numero_conta)
        if conta:
            if tipo_relatorio == "completo":
                tipo_transacao = None
            else:
                tipo_transacao = tipo_relatorio  # Não precisa mais capitalizar

            for transacao in conta.historico.gerar_relatorio(tipo_transacao):
                print(transacao)
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")


def listar_clientes(cliente_controller):
    clientes = cliente_controller.clientes
    if not clientes:
        print("Nenhum cliente cadastrado.")
    for cliente in clientes:
        print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}")

def realizar_deposito(cliente_controller, conta_controller, menu_view):
    cpf = menu_view.obter_cpf()
    cliente = cliente_controller.buscar_cliente_por_cpf(cpf)
    if cliente:
        numero_conta = menu_view.obter_numero_conta()
        conta = conta_controller.buscar_conta_por_numero(cliente, numero_conta)
        if conta:
            valor = menu_view.obter_valor("deposito")
            conta_controller.realizar_deposito(conta, valor)
            print("Depósito realizado com sucesso!")
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")

def realizar_saque(cliente_controller, conta_controller, menu_view):
    cpf = menu_view.obter_cpf()
    cliente = cliente_controller.buscar_cliente_por_cpf(cpf)
    if cliente:
        numero_conta = menu_view.obter_numero_conta()
        conta = conta_controller.buscar_conta_por_numero(cliente, numero_conta)
        if conta:
            valor = menu_view.obter_valor("saque")
            if conta_controller.realizar_saque(conta, valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")

def ver_saldo(cliente_controller, conta_controller, menu_view):
    cpf = menu_view.obter_cpf()
    cliente = cliente_controller.buscar_cliente_por_cpf(cpf)
    if cliente:
        numero_conta = menu_view.obter_numero_conta()
        conta = conta_controller.buscar_conta_por_numero(cliente, numero_conta)
        if conta:
            saldo = conta_controller.ver_saldo(conta)
            menu_view.exibir_saldo(saldo)
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")

def ver_extrato(cliente_controller, conta_controller, menu_view):
    cpf = menu_view.obter_cpf()
    cliente = cliente_controller.buscar_cliente_por_cpf(cpf)
    if cliente:
        numero_conta = menu_view.obter_numero_conta()
        conta = conta_controller.buscar_conta_por_numero(cliente, numero_conta)
        if conta:
            extrato = conta_controller.ver_extrato(conta)
            menu_view.exibir_extrato(extrato)
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")

def listar_contas_cliente(cliente_controller, menu_view):  
    cpf = menu_view.obter_cpf()
    cliente = cliente_controller.buscar_cliente_por_cpf(cpf)
    if cliente:
        for info_conta in ContaIterador(cliente):
            print(f"Conta: {info_conta['numero']}, Agência: {info_conta['agencia']}, Saldo: {info_conta['saldo']}")
    else:
        print("Cliente não encontrado!")

def main():
    cliente_controller = ClienteController()
    conta_controller = ContaController()
    menu_view = MenuView()

    while True:
        escolha = menu_view.mostrar_menu()

        if escolha == "1":
            criar_cliente(cliente_controller, menu_view)
        elif escolha == "2":
            criar_conta(cliente_controller, conta_controller, menu_view)
        elif escolha == "3":
            listar_contas(cliente_controller)
        elif escolha == "4":
            listar_clientes(cliente_controller)
        elif escolha == "5":
            realizar_saque(cliente_controller, conta_controller, menu_view)
        elif escolha == "6":
            ver_extrato(cliente_controller, conta_controller, menu_view)
        elif escolha == "7":
            ver_saldo(cliente_controller, conta_controller, menu_view)
        
        elif escolha == "8":
            realizar_deposito(cliente_controller, conta_controller, menu_view)
        elif escolha == "9":
            listar_contas_cliente(cliente_controller, menu_view)
        elif escolha == "10":
            gerar_relatorio(cliente_controller, conta_controller, menu_view)
        elif escolha == "11":
            gerar_relatorio(cliente_controller, conta_controller, menu_view, tipo_relatorio="deposito")
        elif escolha == "12":
            gerar_relatorio(cliente_controller, conta_controller, menu_view, tipo_relatorio="saque")
        elif escolha == "13":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
