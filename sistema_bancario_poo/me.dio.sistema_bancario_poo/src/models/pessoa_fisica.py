from models.cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_de_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
