import random

class Conta():
    def __init__(self, numConta):
        self.numero=numConta
        self.saldo=0

    def deposite(self,valor):
        self.saldo= self.saldo+ (valor-valor*0.1)
            

    def sacar(self,valor):
        if self.saldo>= valor:
            self.saldo= self.saldo - valor
            return True
        else:
            return False

class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo* (0.01*self.percentual)
           

    def __init__(self, numConta, percentual):
        self.percentual=percentual
        super().__init__(numConta)

   

class ContaBonificada(Conta):

    def __init__(self, numConta, bonus):
        self.bonus=bonus
        super().__init__(numConta)
    
    def depositar(self, numConta, bonus):
        for conta in self.contas:
            if conta.numero==numConta: 
                conta.deposite(valor+bonus)
        super().depositar()

        
class Banco():
    def __init__(self,nome):
        self.nome=nome
        self.contas=[]

    def getNome(self):
        return self.nome

    def criarConta(self):
        num=random.randint(0,1000)
        c=Conta(num)
        self.contas.append(c)
        return num
    
    def criarPoupanca(self,percentual):
        num=random.randint(0,1000)
        p=Poupanca(num,percentual)
        self.contas.append(p)
        return num

    def criarContaBonificada(self,bonus):
        num=random.randint(0,1000)
        cb=ContaBonificada(num,bonus)
        self.contas.append(cb)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero==numConta:
                return conta.saldo
        return -1
        
    def depositar(self, numConta):
        for conta in self.contas:
            if conta.numero==numConta: 
                conta.deposite(valor)

    def sacar(self, numConta,valor):
        for conta in self.contas:
            if conta.numero==numConta:
                return conta.sacar(valor)
            
    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero==numConta and isinstance(i,Poupanca):
                    i.render()
                    return True
        return False

