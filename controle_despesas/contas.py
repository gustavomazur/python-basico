def pedir_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um número válido!')

def calcular_total(conta):
    return sum(conta.values())

def verificar_saldo(conta):
    dinheiro = pedir_valor('Quantos você tem para pagar as contas? ')
    saldo = dinheiro - calcular_total(conta)
    if saldo < 0 :
        print(f'Falta {saldo}')
    elif saldo > 0:
        print(f'Sobra {saldo}')
    else:
        print('Pagou tudo certinho, saldo zero! ')

def menu():
    conta = dict()

    valido = False
    while not valido:
        n = pedir_valor('''Escolha uma opção
        (1)-adicionar conta
        (2)-remover conta
        (3)-editar conta
        (4)-ver contas
        (5)-verificar_saldo
        (6)-sair
        Digite a opção desejada: ''')

        if n == 1:
            titulo = str(input('Titulo: '))
            conta[titulo] = pedir_valor('valor: ')

        if n == 2:
            remover = input('Qual conta deseja remover? ')
            if remover in conta:
                del conta[remover]
                print('Conta removida')
            else:
                print('conta não encontrada')

        if n == 3:
            editar = input('Qual conta deseja editar? ')
            if editar in conta:
                conta[editar] = pedir_valor('Novo valor: ')
                print('Conta editada')
            else:
                print('conta não encontrada')

        if n == 4:
            for t, v in conta.items():
                print(f'titulo:, {t}, valor, {v}')
            total = calcular_total(conta)
            print(f'Total: {total}')

        if n == 5:
            verificar_saldo(conta)

        if n == 6:
            print('conta fechada... volte sempre')
            break

