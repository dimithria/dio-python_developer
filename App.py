import datetime

saldo = 0.0
extrato = []
limite_saque = 500.00
saque_diario = 5
saque_realizado = 0
data_atual = datetime.date.today()
clientes = {}
contas = []
numero_conta = 1

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:,.2f}")
        print(f"\nDepósito de R$ {valor:,.2f} realizado com sucesso!")
        print("\n-----------------------------------")
    else:
        print("Valor inválido para depósito. Por favor, deposite apenas valores positivos.")
        print("\n-----------------------------------")

def sacar(*, valor):
    global saldo, extrato, saque_realizado, data_atual
    if datetime.date.today() != data_atual:
        saque_realizado = 0
        data_atual = datetime.date.today()

    if saque_realizado >= saque_diario:
        print("\nLimite de saques diários atingido.")
        print("-----------------------------------\n")
        return saldo, extrato
    
    elif valor > limite_saque:
        print(f"\nO limite máximo por saque é de R$ {limite_saque:,.2f}.")
        print("-----------------------------------\n")
        return saldo, extrato
    
    elif valor > saldo:
        print("\nSaldo insuficiente para saque.")
        print("-----------------------------------\n")   
        return saldo, extrato   
    
    if valor > 0:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:,.2f}")
        saque_realizado += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        print("-----------------------------------\n")
        return saldo, extrato
    
    else:
        print("Valor inválido para saque. Por favor, insira um valor positivo.")
        return saldo, extrato
    print("-----------------------------------\n")

def visualizar_extrato():
    print("\n======= EXTRATO BANCÁRIO =======\n")
    if not extrato:
        print("Nenhuma movimentação realizada.\n")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo atual: R$ {saldo:,.2f}")
    print("-----------------------------------")

def cadastrar_cliente():
    global clientes
    print("===== Cadastro de Cliente ======")
    
    while True:
        cpf = input("\nDigite o CPF: ")
        if not cpf.isdigit():
            print("\nCPF Inválido")
            print("----------------------------------------")
            continue
            
        if cpf in clientes:
            print("Cliente com esse CPF já existe.")
            print("----------------------------------------")
            return   
        break
            
    nome = input("Digite o nome: ")
    data_nascimento = input("Data de Nascimento: ")
    endereco = input("Enderço: ")
    
    # armazenando
    clientes[cpf] = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'endereço': endereco
    }
    print("===============================================")
    
    print("\n----------------------------------------")   
    print(f"Cliente {nome} cadastrado com sucesso!\n")
    
    print("===== Dados do Cliente =====")
    print(f"CPF: {cpf}")
    print(f"Nome: {nome}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Endereço: {endereco}")
    print("---------------------------------------\n")
    
def criar_conta_corrente():
    global numero_conta, contas
    
    while True:
        print("\n==== CRIAR CONTA CORRENTE ====")
        cpf = input("Digite o CPF: ")
        if not cpf.isdigit():
            print("CPF Inválido!")
            continue
        
        if cpf not in clientes:
            print("\nCPF não encontrado. Cadastre o cliente.")
            print("-----------------------------------\n")
            return
        break
    
    #conta vinculada ao usuario
    conta = {
        'agencia': '0001', 
        'numero_conta': numero_conta,
        'cpf': cpf
    }
    contas.append(conta)
    
    print("-----------------------------------\n")
    print(f"Conta criada com sucesso!\n",
        f"Agência: {conta['agencia']}\n", 
        f"Conta: {conta['numero_conta']}\n", 
        f"Cliente: {clientes[cpf]['nome']}\n",
        )
    print("-----------------------------------\n")
    
    numero_conta += 1
    
def listar_contas():
    print("\n==== LISTA DE CONTA CORRENTE ====\n")
    
    if not contas:
        print("Nenhuma Conta Corrente foi cadastrada!\n")
        print("-----------------------------------\n")
        return
    
    for conta in contas:
        cpf = conta['cpf']

        nome_cliente = clientes[cpf]['nome']
        
        print("-----------------------------------\n")
        print(f"Agência: {conta['agencia']}\n",
              f"Conta: {conta['numero_conta']}\n",
              f"Cliente: {nome_cliente}\n"
              f"CPF: {cpf}\n"
            )    
    print("-----------------------------------\n")
        
def app():
    while True:
        print("\n///////////////////////////////////")
        print("\n$$ Sistema Bancário $$")
        print("========== MENU ==========")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato Bancário")
        print("4 - Cadastrar Cliente")
        print("5 - Criar Conta Corrente")
        print("6 - Listar Contas Correntes")        
        print("7 - Sair.")
        print("//////////////////////////////////")
    
        opcao = input("\nDigite a opção desejada: ")
        
        if opcao == '1':
            print("-----------------------------------")
            while True:
                try:
                    valor = float(input("\nQual o valor do depósito? "))
                    depositar(valor)
                    break
                except ValueError:
                    print("\nPor favor, insira um valor numérico válido.")
                    print("-----------------------------------")
        
        elif opcao == '2':
            while True:
                print("-----------------------------------")
                try:
                    valor = float(input("\nQual valor deseja sacar? "))               
                    saldo, extrato = sacar(valor=valor)
                    break
                except ValueError:
                    print("\nPor favor, insira um valor numérico válido.")
                    print("-----------------------------------")
                       
        elif opcao == '3':
            visualizar_extrato()
            
        elif opcao == '4':
            cadastrar_cliente()
            
        elif opcao == '5':
            criar_conta_corrente()
        
        elif opcao == '6':
            listar_contas()
        
        elif opcao == '7':
            print("Saindo do Sistema Bancário. Até logo!")
            break
        
        else:
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    app()
