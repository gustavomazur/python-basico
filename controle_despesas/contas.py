def pedir_valor(mensagem):
    tentativas = 0
    while tentativas < 3:
        try:
            return float(input(mensagem))
        except ValueError:
            tentativas += 1
            print('Entrada invalida! Digite apenas numeros.')
    print('Muitas tentativas invalidas.')
    return None    
    
def calcular_total(conta):
    return sum(conta.values())

def formatar_valor(valor):
    return f'R$ {valor:.2f}'

def verificar_saldo(conta):
    dinheiro = pedir_valor('Quanto você tem para pagar as contas? ')
    if dinheiro is None:
        return
    saldo = dinheiro - calcular_total(conta)
    if saldo < 0 :
        print(f'Falta: {formatar_valor(-saldo)}')
    elif saldo > 0:
        print(f'Sobra: {formatar_valor(saldo)}')
    else:
        print('Pagou tudo certinho, saldo zero! ')

def menu():
    conta = dict()

    while True:
        n = pedir_valor('''Escolha uma opção
        (1)-adicionar conta
        (2)-remover conta
        (3)-editar conta
        (4)-ver contas
        (5)-verificar_saldo
        (6)-sair
        Digite a opção desejada: ''')
        if n is None:
            break

        if n == 1:
            titulo = str(input('Titulo: '))
            valor = pedir_valor('Valor: ')
            if valor is not None:
                conta[titulo] = valor
                print('Conta adicionada')

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
                valor = pedir_valor('Novo valor: ')
                if valor is not None:
                    conta[editar] = valor
                    print('Conta editada')
            else:
                print('conta não encontrada')

        if n == 4:
            for t, v in conta.items():
                print(f'titulo: {t}, valor: {formatar_valor(v)}')
            total = calcular_total(conta)
            print(f'Total: {formatar_valor(total)}')

        if n == 5:
            verificar_saldo(conta)

        if n == 6:
            print('conta fechada... volte sempre')
            break

