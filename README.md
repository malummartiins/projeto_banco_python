# 🏦Criando um Sistema Bancário

Desafio proposto pela plataforma DIO no bootcamp Potência Tech com parceria com o Ifood.

``` Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. ```

- Criar um Sistema Bancário com 3 operações iniciais:
    - depositar
    - sacar
    - extrato

## Operação deposito:
Deve ser possivel depositar valores positivos. A v1 do projeto trabalha apenas com 1 usuário. Todos os depositos devem ser armazenados em uma variável e exibidos na Operação extrato.

## Operação saque:
O Sistema deve perimir 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha salfo em conta, o sistema deve exibir mensagem informando. Todos os saques devem ser armazenados em uma variável e exibidos em extrato.

## Operação extrato:
Deve listar todos os depositos e saques realizados na conta. No fim da lsitagem deve ser exibido o sado atual.

# Versão 2.0
## Atualização do código
O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo.

* Saque = deve receber argumentos apenas por keyword only
* Depósito = apenas positional only
* Extrato = recebe argumentos por posição e nome

* Criar usuário: armazenados em uma lista: nome, data nascimento, cpf, endereço (ultimo string). CPF apenas números.
* Criar CC: armazenar contas em uma lista: agência, número da conta e usuário.
O  número da conta é sequencial, iniciando em 1. É fixo "0001". Usuário pode ter mais de uma conta.
