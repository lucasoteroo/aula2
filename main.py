from BancoLib import Banco

bancoUfrpe=Banco("UABJ")
print("Bem vindo")
print("Menu")
print("0 - sair")
print("1- Criar uma conta")
print("2- consulta saldo da conta")
print("3- depositar na conta")
print("4 - Sacar da conta")

escolha=int(input("digite a opção desejada: "))

while escolha>0:
    if escolha==1:
        #criar uma conta
        c=Conta(1)
        numConta=bancoUfrpe.criarConta()
        print("Conta criada ", numConta)
    elif escolha ==2:
       
        numConta=int(input("digite o numero da conta"))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        print("Seu saldo é: ",saldo)
    elif escolha ==3:
       
        numConta=int(input("digite o numero da conta"))
        valor=int(input("digite o valor que gostaria de depositar na conta"))
        saldo = bancoUfrpe.depositar(numConta)

    elif escolha ==4:
       
        numConta=int(input("digite o numero da conta"))
        valor=int(input("digite o valor que gostaria de sacar na conta"))
        resp = bancoUfrpe.sacar(numConta,valor)
        if resp :
            print("valor sacado")
        else:
            print("valor insuficiente")
    escolha=int(input("digite a opção desejada: "))