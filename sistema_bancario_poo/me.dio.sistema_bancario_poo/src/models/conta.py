from models.historico import Historico
from datetime import datetime

def decorador_log(tipo_transacao):
    def decorator(funcao):
        def empacotador(*args, **kwargs):
            data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"Transação: {tipo_transacao} - Data: {data_hora}")
            return funcao(*args, **kwargs)
        return empacotador
    return decorator


class Conta:
    def __init__(self, cliente, numero_conta, agencia):
        self.__saldo = 0
        self.__numero_conta = numero_conta
        self.__agencia = agencia
        self.__historico = Historico()
        self.cliente = cliente

    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls(cliente, numero_conta)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def agencia(self):
        return self.__agencia

    @property
    def historico(self):
        return self.__historico

    @decorador_log(tipo_transacao="Saque")
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Limite insuficiente.")
        elif valor > 0:
            self.__saldo -= valor
            self.historico.adicionar_transacao("Saque", valor)  # Passa "Saque" e o valor
            return True
        else:
            print("Operação falhou! Valor inválido.")

        return False

    @decorador_log(tipo_transacao="Deposito")
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.historico.adicionar_transacao("Deposito", valor)  # Passa "Depósito" e o valor
            return True
        else:
            print("Operação falhou! Valor inválido.")

        return False
