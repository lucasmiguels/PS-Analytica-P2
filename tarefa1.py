# Função que retorna o menor ângulo entre os 
# ponteiros de um relógio até receber 'f'

# Optei por considerar as pequenas variações no ponteiro das horas a cada minuto (diferente do exemplo)

def min_angle():
    hour = input('Escolha um horario (formato: "hh:mm"): ')

    while hour != 'f':
        try:
            hour = str(hour)
            hour = hour.split(':')
            hour_time = int(hour[0])
            min_time = int(hour[1])

            if len(hour[0]) != 2 or len(hour[1]) != 2 or hour_time < 0 or hour_time >= 24 or min_time < 0 or min_time >=60:
                raise Exception('Input inválido')
        except:
            if hour != 'f':
                print("Input inválido")
        else:
            # o relógio reinicia a cada 12 horas
            # 12:00 é a "referência"
            if hour_time > 12:
                hour_time = hour_time - 12
            total_minutes = hour_time * 60 + min_time
            # 360 graus a cada 12 horas = 0.5 grau por minuto no ponteiro das horas
            h_angle = 0.5 * total_minutes
            # 360 graus a cada 60 minutos = 6 graus por minuto no ponteiro dos minutos
            m_angle = 6 * min_time
            if (h_angle - m_angle) >= 0:
                angle = h_angle - m_angle
            else:
                angle = m_angle - h_angle
            angle = min(angle, 360-angle)
            print(f'O menor ângulo é de {angle} graus')
        finally:
            if hour != 'f':
                hour = input('Escolha um horario (formato: "hh:mm"): ')
    print('Fim...')

min_angle()
                

