# SISTEMA BANCÁRIO 2.0

## INTRODUÇÃO
O código permite realizar operações como depósitos, saques, visualização de extratos, cadastro de clientes e criação de contas correntes.

## Conceitos Chave
O sistema é composto por várias funções que gerenciam diferentes aspectos de um banco. Aqui estão alguns conceitos importantes:

* Saldo: O total de dinheiro disponível na conta.
* Extrato: Um registro das transações realizadas (depósitos e saques).
* Limite de Saque: O valor máximo que pode ser sacado em uma única transação.
* Saque Diário: O número máximo de saques permitidos por dia.
* Cadastro de Clientes: Permite registrar novos clientes no sistema.

## Estrutura do Código
O código é organizado em funções que realizam tarefas específicas. Aqui está uma visão geral da estrutura:

* *Variáveis Globais*: Armazenam o saldo, extrato, limite de saque, e informações dos clientes.
Funções:
* *depositar(valor)*: Adiciona um valor ao saldo e registra a transação.
* *sacar(valor)*: Retira um valor do saldo, respeitando limites e condições.
* *visualizar_extrato()*: Mostra todas as transações realizadas.
* *cadastrar_cliente()*: Registra um novo cliente.
* *criar_conta_corrente()*: Cria uma nova conta vinculada a um cliente.
* *listar_contas()*: Exibe todas as contas correntes cadastradas.
* *app()*: Função principal que gerencia o menu e as interações do usuário.

## Conclusão 
Sistema bancário simples desenvolvido em Python. É um ótimo exemplo de como podemos gerenciar contas e transações de forma simples e eficaz.
