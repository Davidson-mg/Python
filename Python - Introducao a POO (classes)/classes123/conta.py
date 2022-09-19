



from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numeroConta, saldo):
        self._agencia = agencia
        self._numeroConta = numeroConta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def digito (self, agencia):
        self._agencia = agencia

    @property
    def numeroConta(self):
        return self._numeroConta

    @numeroConta.setter
    def numeroConta(self, numeroConta):
        self._numeroConta = numeroConta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def detalhes(self):
        print()
        print(f'Agencia: {self._agencia} \n Conta: {self._numeroConta}\n Saldo: {self._saldo}')
        print()

    def depositar(self, valor):
        self._saldo = self._saldo + valor
        print('Deposito efetuado com sucesso')
        self.detalhes()
        return self._saldo

    @abstractmethod
    def sacar(self):
        pass



class ContaCorrente(Conta):
    def __init__(self, agencia, numeroConta, saldo, limite=1000):
        super().__init__(agencia, numeroConta, saldo)
        self._limite = limite

    def sacar(self, valor):

        if valor > self._limite:
            print('Não é possivel sacar mais de R$1000,00.')
            self.detalhes()
            return

        self._saldo = self._saldo - valor
        print('Saque efetuado com sucesso')
        self.detalhes()
        return self._saldo


class ContaPoupanca(Conta):
    def __init__(self, agencia, numeroConta, saldo):
        super().__init__(agencia, numeroConta, saldo)
        self._saldo = saldo

    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')
            return

        self._saldo = self._saldo - valor
        print('Saque efetuado com sucesso')
        self.detalhes()
        return self._saldo





