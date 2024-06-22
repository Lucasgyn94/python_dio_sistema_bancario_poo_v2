from models.pessoa_fisica import PessoaFisica

class ClienteController:
    def __init__(self):
        self.clientes = []

    def criar_cliente(self, nome, cpf, data_de_nascimento, endereco):
        cliente = PessoaFisica(nome, cpf, data_de_nascimento, endereco)
        self.clientes.append(cliente)
        return cliente

    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
