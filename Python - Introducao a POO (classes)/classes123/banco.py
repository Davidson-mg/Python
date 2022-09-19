
class Banco ():
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.conta = []


    def inserirCliente(self, cliente):
        self.clientes.append(cliente)

    def inserirConta(self, conta):
        self.conta.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.conta:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True
