# 🏦 Sistema Bancário em Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white)
![OOP](https://img.shields.io/badge/POO-999999?style=for-the-badge&logo=python&logoColor=white)

Sistema bancário completo desenvolvido em Python com funcionalidades de gerenciamento de contas e usuários via terminal.

## ✨ Funcionalidades

### 👥 Gestão de Usuários
- [x] **Cadastro de usuários** com CPF único
- [x] **Validação de dados** completos (nome, data nascimento, endereço)
- [x] **Prevenção de duplicatas** por CPF

### 🏦 Gestão de Contas Correntes
- [x] **Criação de contas** vinculadas a usuários
- [x] **Sistema de agência** (0001 como padrão)
- [x] **Números de conta sequenciais** automáticos
- [x] **Listagem completa** de contas cadastradas

### 💰 Operações Financeiras
- [x] **Depósitos** com validação de valores positivos
- [x] **Saques** com limite diário e por operação
- [x] **Extrato detalhado** com histórico de transações
- [x] **Saldo atualizado** em tempo real

## 🛠️ Arquitetura do Sistema

### 🔄 Fluxo Principal
```python
# Estrutura modularizada com funções específicas
def main() → menu() → operações bancárias
              │
              ├── depositar()
              ├── sacar()
              ├── exibir_extrato()
              ├── criar_usuario()
              ├── criar_conta()
              └── listar_contas()
```

### 📦 Estrutura de Dados
```python
# Usuários: Lista de dicionários
usuarios = [
    {
        "nome": "João Silva",
        "data_nascimento": "01-01-1990",
        "cpf": "12345678900",
        "endereço": "Rua A, 123 - Centro - SP"
    }
]

# Contas: Lista de dicionários vinculados
contas = [
    {
        "agencia": "0001",
        "numero_conta": 1,
        "usuario": {usuário}
    }
]
```

## 🚀 Como Executar

1. **Pré-requisitos**: Python 3.6+ instalado
2. **Clone o repositório** ou copie o código
3. **Execute o script**:

```bash
python3 sistema_bancario.py
```

## 📋 Regras do Sistema

### 💳 Cadastro de Usuários
- CPF como identificador único (somente números)
- Dados completos obrigatórios
- Impedimento de cadastro duplicado

### 🏦 Criação de Contas
- Vinculação obrigatória a usuário existente
- Agência fixa "0001"
- Número de conta sequencial automático

### 💰 Operações Financeiras
**Depósitos:**
- Apenas valores positivos
- Arredondamento para 2 casas decimais
- Registro no extrato

**Saques:**
- Limite de **R$ 500,00 por operação**
- Máximo de **3 saques diários**
- Saldo suficiente obrigatório
- Registro no extrato

**Extrato:**
- Histórico completo de transações
- Saldo atualizado
- Mensagem especial para sem movimentações

## 🖥️ Demonstração

```plaintext
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar conta
[0] Sair

=> 4
Menu [4] Criação de novo usuário

Informe o CPF (somente números): 12345678900
Informe o nome completo: Maria Silva
Informe a data e nascimento (dd-mm-aaaa): 15-05-1985
Informe o endereço (logradouro, n° - bairro - cidade/sigla estado): Av. Principal, 456 - Centro - SP
Usuário cadastrado com sucesso!
```

## 👨‍💻 Autor

**Fernando Pereira de Oliveira**  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fernando-oliveira-612963245/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/oliveira-fp)
