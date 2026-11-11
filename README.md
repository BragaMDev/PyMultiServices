# PyMultiServices

Um sistema centralizado desenvolvido em **Python** que reúne múltiplos utilitários e simulações de sistemas do mundo real através de um menu interativo baseado em terminal (`CLI`).

---

## Funcionalidades do Sistema

O projeto é dividido em **8 serviços principais**:

1. **Controle de Consumo de Água:** Calcula o valor da conta de água com base em faixas progressivas de consumo por metro cúbico.
2. **Sistema de Avaliação Acadêmica:** Coleta notas, calcula a média aritmética e classifica o aluno entre **Aprovado**, **Recuperação** ou **Reprovado**.
3. **Controle de Estoque:** Cadastra produtos e quantidades, organiza o estoque de forma ordenada e identifica qual item possui a maior quantidade armazenada.
4. **Simulador de Caixa Eletrônico:** Processa saques bancários calculando a distribuição exata de notas de R$ 100, R$ 50, R$ 20 e R$ 10 (validando múltiplos de 10).
5. **Sistema de Controle de Vendas:** Registra vendas diárias, separa os totais por forma de pagamento (Dinheiro ou Cartão) e calcula métricas como ticket médio e quantidade total de transações.
6. **Sistema de Monitoramento de Temperatura:** Analisa um conjunto de leituras térmicas, exibindo a temperatura máxima, mínima, média e contando quantas vezes o limite de 80°C foi ultrapassado.
7. **Sistema de Login com Tentativas Limitadas:** Autentica o usuário (`admin` / `1234`) com restrição de até 3 tentativas antes de bloquear o acesso por segurança.
8. **Encerramento:** Sai do programa de forma segura.

---

## Pré-requisitos

Para executar este projeto, você precisará ter instalado em sua máquina:
* **Python** (versão 3.6 ou superior recomendada)

---

## Como Executar

1. Clone este repositório ou baixe o arquivo com o código-fonte (ex: `main.py`).
2. Abra o terminal (Prompt de Comando, PowerShell ou seu terminal de preferência).
3. Navegue até a pasta onde o arquivo está salvo.
4. Execute o comando:

```bash
python main.py
