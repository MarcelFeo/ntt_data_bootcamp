from abc import ABC, abstractmethod
from datetime import date

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

class Conta:
    def __init__(self, cliente: Cliente, numero: int, agencia: str):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def sacar(self, valor: float):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(Saque(valor))
        return True

    def depositar(self, valor: float):
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))
        return True

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        conta = cls(cliente, numero, "0001")
        cliente.adicionar_conta(conta)
        return conta

class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, numero: int, agencia: str, limite: float, limite_saques: int):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
