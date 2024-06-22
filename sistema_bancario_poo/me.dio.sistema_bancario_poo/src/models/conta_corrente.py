from models.conta import Conta
from models.saque import Saque


class ContaCorrente(Conta):
    def __init__ (self, numero_conta, cliente, limite, limite_saques  = 3):
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite_saques
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Você atingiu o limite de saques.")

        else:
            super().sacar(valor)

        return False
    
    def __str__(self):
        return f"Agência:\t {self.agencia}\nC/C:\t\t{self.numero_conta}\nTitular:\t{self.cliente.nome}"
    