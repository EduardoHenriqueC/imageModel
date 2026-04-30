# Projeto Test Assistent Programing

Este projeto contém exemplos de código Python voltados para:
- verificação de número primo,
- refatoração de código com cálculo de estatísticas,
- análise e depuração de um programa de cálculo de compras.

## Estrutura do projeto

- `num_primo.py`
  - Implementa a função `is_prime(number: int) -> bool`.
  - Verifica se um número inteiro é primo usando a raiz quadrada inteira (`math.isqrt`) e eliminando divisores pares.
  - Inclui `run_tests()` para execução interativa no terminal.

- `refatoracao.py`
  - Contém a função `calcular_estatisticas(numeros: list[int]) -> tuple[int, float, int, int]`.
  - Calcula total, média, maior e menor valores de uma lista de inteiros.
  - Demonstra o uso de built-ins `sum()`, `max()` e `min()`.

- `Debug.py`
  - Exemplo de programa que lê dados de compras, calcula o subtotal, aplica imposto de 10% e desconto opcional.
  - Exibe um recibo formatado com valores monetários.

- `explicacao_num_primo.md`
  - Explicação linha a linha do arquivo `num_primo.py`.

- `explicacao_refatoracao.md`
  - Explicação da refatoração aplicada em `refatoracao.py`.

- `debug.md`
  - Análise detalhada do código `Debug.py`, explicando cada seção do programa.

## Como executar

Abra um terminal na pasta `test-assistent-programing` e execute os scripts conforme necessário.

### Executar o verificador de número primo

```bash
python num_primo.py
```

O programa solicita um número inteiro e informa se ele é primo ou não.

### Executar o exemplo de estatísticas

```bash
python refatoracao.py
```

O script mostra o total, a média, o maior e o menor valor para uma lista fixa de números.

### Executar o programa de compras

```bash
python Debug.py
```

O programa pede informações sobre o cliente, quantidade e preço dos itens e calcula o total final.

## Descrição dos objetivos

- `num_primo.py` demonstra uma função de verificação de primalidade eficiente.
- `refatoracao.py` mostra como melhorar a legibilidade e a clareza de um código original pouco expressivo.
- `Debug.py` serve como exemplo de lógica de entrada, cálculo e formatação de saída.

## Observações

- Os arquivos `.md` de explicação documentam a lógica e as escolhas de implementação.
- A organização do projeto é simples e adequada para estudo e pequenas demonstrações de Python.
