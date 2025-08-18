# 🏦 Sistema Bancário em Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white)

Um sistema bancário simples desenvolvido em Python para operações básicas de conta corrente via terminal.

## ✨ Funcionalidades

- [x] **Depósito de valores**
- [x] **Saque com limite diário**
- [x] **Visualização de extrato**
- [x] **Validação de operações**
- [x] **Interface amigável no terminal**

## 🛠️ Como Executar

1. Certifique-se que você tem Python instalado (versão 3.6 ou superior)
2. Clone o repositório ou copie o código
3. Execute o script:

```bash
python sistema_bancario.py
```

## 📋 Regras do Sistema

### 💰 Depósitos
- Apenas valores positivos são aceitos
- Valores são arredondados para 2 casas decimais
- Todos os depósitos são registrados no extrato

### 💸 Saques
- Limite de **R$ 500,00 por saque**
- Máximo de **3 saques diários**
- Saldo suficiente obrigatório
- Cada saque é registrado no extrato

### 📊 Extrato
- Exibe todas as movimentações na sessão atual
- Mostra o saldo atualizado
- Mensagem especial quando não há movimentações

## 🖥️ Demonstração

```plaintext
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 1
Menu [1] Depósito

Digite o valor que deseja depositar: 1000
Deposito de R$ 1000.00 realizado com sucesso
```

## 🧠 Estrutura do Código

### Variáveis Principais
```python
saldo = 0               # Armazena o saldo atual
limite = 500            # Limite por saque
extrato = ""            # Histórico de operações
numero_saques = 0       # Contador de saques
LIMITE_SAQUES = 3       # Máximo de saques diários
```

### Fluxo Principal
1. Exibe menu de opções
2. Processa a escolha do usuário
3. Valida e executa a operação
4. Retorna ao menu até que o usuário saia

## 👨‍💻 Autor

**Fernando Pereira de Oliveira**  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fernando-oliveira-612963245/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/oliveira-fp)
