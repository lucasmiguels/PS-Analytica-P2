# Função que conta o número de vezes que cada inteiro  
# apareceu e termina ao receber 'f'

def frequency():  
    num_dict = {}
    number = input('Escolha um inteiro: ')
    while number != 'f': 
        try:
            number = int(number)
        except:
            # o input recebido não pôde ser convertido em inteiro
            pass
        else: 
            if number in num_dict:
                # num_dict[number] já está definido e podemos somar 1 ao número de ocorrências
                num_dict[number] = num_dict[number] + 1
            else:
                # nesse caso temos a primeira ocorrência do inteiro em questão
                num_dict[number] = 1
        finally:
            if number != 'f':
                number = input('Escolha um inteiro: ')

    
    for k,v in num_dict.items():
        if v == 1:
            print(f'O número {k} apareceu {v} vez')
        else:
            print(f'O número {k} apareceu {v} vezes')
    print("Fim...")
    return num_dict

frequency()