# 🏦 Sistema Bancário em Python (Orientado a Objetos)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge\&logo=windows-terminal\&logoColor=white)
![OOP](https://img.shields.io/badge/POO-999999?style=for-the-badge\&logo=python\&logoColor=white)

Sistema bancário orientado a objetos em Python, desenvolvido para rodar via **terminal**.
O projeto utiliza **classes abstratas, herança e encapsulamento** para modelar clientes, contas e transações financeiras.

---

## ✨ Funcionalidades

### 👥 Gestão de Usuários

* [x] Cadastro de usuários (CPF único, nome, data de nascimento e endereço).
* [x] Associação de um usuário a múltiplas contas.
* [x] Prevenção de duplicidade de CPF.

### 🏦 Gestão de Contas

* [x] Criação de **contas correntes** vinculadas a clientes existentes.
* [x] Agência fixa `0001`.
* [x] Números de contas gerados automaticamente.
* [x] Impressão formatada de dados da conta com `__str__`.

### 💰 Operações Financeiras

* [x] **Depósitos** (valores positivos, saldo atualizado e registro no histórico).
* [x] **Saques** com:

  * Limite de **R\$ 500,00 por operação**.
  * Máximo de **3 saques diários**.
  * Saldo obrigatório.
* [x] **Histórico de transações** persistido por conta.
* [x] **Extrato detalhado** (mostra conta, operações e saldo final).

---

## 🛠️ Arquitetura do Sistema

### 🔄 Fluxo Principal

```python
main() → menu() → operações bancárias
              │
              ├── depositar()
              ├── sacar()
              ├── exibir_extrato()
              ├── criar_cliente()
              ├── criar_conta()
              └── listar_contas()
```

### 📦 Estrutura de Classes

```plaintext
Cliente (superclasse)
 └── PessoaFisica
      └── possui várias → ContaCorrente

Conta (superclasse)
 └── ContaCorrente
       ├── sacar()
       └── depositar()

Transacao (abstrata)
 ├── Saque
 └── Deposito

Historico
 └── Armazena transações (tipo, valor, data/hora)
```

---

## 🚀 Como Executar

1. **Pré-requisitos**: Python 3.8+ instalado.
2. **Clone o repositório** ou copie o código.
3. Execute no terminal:

```bash
python3 sistema_bancario.py
```

---

## 📋 Regras do Sistema

### 💳 Cadastro de Usuários

* CPF é identificador único.
* Dados completos obrigatórios.
* Usuários podem ter múltiplas contas.

### 🏦 Criação de Contas

* Vinculação obrigatória a um usuário.
* Agência padrão `0001`.
* Numeração sequencial automática.

### 💰 Operações

**Depósitos:**

* Apenas valores positivos.
* Registro automático no extrato.

**Saques:**

* Limite de **R\$ 500,00 por saque**.
* Máximo de **3 saques diários**.
* Verificação de saldo antes da operação.

**Extrato:**

* Mostra titular, agência e número da conta.
* Lista de transações (tipo, valor).
* Saldo atualizado.
* Mensagem quando não há movimentações.

---

## 🖥️ Demonstração

```plaintext
######### MENU ##########

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar conta
[0] Sair

=> 1
Informe o CPF do cliente: 12345678900
Informe o valor do depósito: 200

Depósito realizado com sucesso!
Valor depositado R$ 200.00
```

---

## 👨‍💻 Autor

**Fernando Pereira de Oliveira**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/fernando-oliveira-612963245/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/oliveira-fp)

---

👉 Você gostaria que eu também acrescentasse no README uma **seção de melhorias futuras** (ex.: suporte a contas poupança, persistência em banco de dados, interface gráfica)? Isso deixaria o projeto com mais cara de roadmap evolutivo.
