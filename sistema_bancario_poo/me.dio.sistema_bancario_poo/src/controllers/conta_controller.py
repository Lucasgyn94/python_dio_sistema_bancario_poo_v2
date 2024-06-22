from models.conta import Conta
from datetime import datetime

def decorador_log(tipo_transacao):
    def decorator(funcao):
        def empacotador(*args, **kwargs):
            data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"Transação: {tipo_transacao} - Data: {data_hora}")
            return funcao(*args, **kwargs)
        return empacotador
    return decorator


class ContaController:
    def __init__(self):
        self.numero_conta = 0

    @decorador_log(tipo_transacao="Criação de Conta")
    def criar_conta(self, cliente, valor_deposito):
        self.numero_conta += 1
        numero_conta = str(self.numero_conta).zfill(4)  
        agencia = "2408" 
        conta = Conta(cliente, numero_conta, agencia)
        conta.depositar(valor_deposito)
        cliente.adicionar_conta(conta)
        return conta

    def buscar_conta_por_numero(self, cliente, numero):
        for conta in cliente.contas:
            if conta.numero_conta == numero:
                return conta
        return None

    def realizar_deposito(self, conta, valor):
        return conta.depositar(valor)

    def realizar_saque(self, conta, valor):
        return conta.sacar(valor)

    def ver_saldo(self, conta):
        return conta.saldo
    
    def ver_extrato(self, conta):
        return conta.historico.transacoes


