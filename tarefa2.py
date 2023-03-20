# Função que recebe duas posições de xadrez e verifica
# se é um movimento válido para um cavalo
# Encerra ao receber 'f'

def knight_moves():

    vertical1 = {'a':['c'], 'b':['d'], 'c':['a','e'], 'd':['b','f'], 'e':['c','g'], 'f':['d','h'], 'g':['e'], 'h':['f']}
    vertical2 = {'a':['b'], 'b':['a','c'], 'c':['b','d'], 'd':['c','e'], 'e':['d','f'], 'f':['e','g'], 'g':['f','h'], 'h':['f']}
    moves = input('Escolha duas posições(formato: "posicao1 posicao2"): ')

    while moves != 'f':
        try:
            moves = str(moves)
            moves = moves.split()
            prev_letter = str(moves[0][0])
            prev_num = int(moves[0][1])
            post_letter = str(moves[1][0])
            post_num = int(moves[1][1])

            if len(moves[0])!= 2 or len(moves[1])!= 2 or len(moves)!= 2 or prev_letter not in vertical1.keys() or post_letter not in vertical1.keys() or prev_num < 1 or prev_num > 8 or post_num < 1 or post_num > 8:
                raise Exception('Input inválido')
        except:
            if moves != 'f':
                print('Input inválido')
        else:
            if abs(post_num - prev_num) ==  1:
                # nesse caso, sabemos que andou 1 casa na vertical e precisamos
                # andar duas na horizontal para movimento válido
                if post_letter in vertical1[prev_letter]:
                    print('MOVIMENTO VÁLIDO')
                else:
                    print('MOVIMENTO INVÁLIDO')
            elif abs(post_num - prev_num) == 2:
                # nesse caso, sabemos que andou 2 casas na vertical e precisamos
                # andar uma na horizontal para movimento válido
                if post_letter in vertical2[prev_letter]:
                    print('MOVIMENTO VÁLIDO')
                else:
                    print('MOVIMENTO INVÁLIDO')
            else:
                print("MOVIMENTO INVÁLIDO")
        finally:
            if moves != 'f':
               moves = input('Escolha duas posições(formato: "posicao1 posicao2"): ')
    print('Fim...')

knight_moves()