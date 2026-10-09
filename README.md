# python-basico

Exercício:
- Resolver problemas de lógica usando Python
- Criar funções reutilizáveis para validação e cálculo

## Sobre o projeto

Um gerenciador simples de contas a pagar: você cadastra contas (título + valor),
pode remover, editar, listar o total e verificar se o seu dinheiro cobre ou não
todas as despesas.

## Funcionalidades

- Adicionar conta (título e valor)
- Remover conta pelo título
- Editar o valor de uma conta
- Listar as contas e o total
- Verificar o saldo: mostra quanto **falta** ou quanto **sobra**
- Validação de entrada (não aceita texto no lugar de número)

## Estrutura do projeto

```
python-basico/
├── main.py                      # ponto de entrada
├── README.md
└── controle_despesas/
    ├── __init__.py
    └── contas.py                # lógica do menu e funções
```

## Como rodar

Precisa apenas do Python 3 instalado.

```bash
python3 main.py
```

Depois é só escolher uma opção no menu:

```
(1)-adicionar conta
(2)-remover conta
(3)-editar conta
(4)-ver contas
(5)-verificar_saldo
(6)-sair
```

## Conceitos praticados

- Funções reutilizáveis (`pedir_valor`, `calcular_total`, `verificar_saldo`)
- Dicionários (`{titulo: valor}`)
- Tratamento de erro com `try/except`
- Organização do código em módulos/pacote
