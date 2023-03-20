from decimal import Decimal
# Calculadora de troco que retorna quantas notas/moedas
# de cada valor são necessárias (em sua menor quantidade)

def change_calc():
    notes = {100:0,50:0,20:0,10:0,5:0,2:0}
    coins = {1.00:0,0.50:0,0.25:0,0.10:0,0.05:0,0.01:0}
    value = input('Qual o valor do troco? ')

    try:
        split_value = str(value).split('.')
        if len(split_value[1]) != 2:
            raise Exception('Input inválido')
        else:
            int_part = int(split_value[0])
            value = float(value)
            dec_part = round(value - int_part,2)
    except:
        print('Input inválido')
    else:
        # para minimizar o número de notas, começamos utilizando
        # as maiores possíveis primeiro
        for k in notes:
            notes[k] += (int_part // k)
            int_part = int_part % k
        # Caso o valor inteiro não seja atingido pelas notas, deverá ser atingido com as moedas
        dec_part = dec_part + int_part
        for k in coins:
            coins[k] += (Decimal(str(dec_part)) // Decimal(str(k)))
            dec_part = round(Decimal(str(dec_part)) % Decimal(str(k)),2)
        # Utilizamos Decimal para tratar a imprecisão da operação com números quebrados

        print('NOTAS:')
        for n,v in notes.items():
            print(f'{v} nota(s) de R$ {n:.2f} ')
        print('')
        print('MOEDAS:')
        for c,v in coins.items():
            print(f'{int(v)} moeda(s) de R$ {c:.2f} ')

        num_notes = 0
        num_coins = 0
        for v in notes.values():
            num_notes += v
        for v in coins.values():
            num_coins += int(v)
        return (num_notes,num_coins)
        # retorna o menor número de notas e moedas possíveis para representar o valor

change_calc()