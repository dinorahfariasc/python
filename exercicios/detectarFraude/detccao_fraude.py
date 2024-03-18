from datetime import datetime as dt
from datetime import timedelta
import pandas as pd

transacoes = [
    (0,  1000.00, "00:00:00"),  # Registro inicial com limite de R$ 1000.00
    (1,  100.00,  "12:00:00"),
    (2,  1500.00, "12:05:00"),
    (3,  200.00,  "13:10:00"),
    (4,  300.00,  "13:40:00"),
    (5,  400.00,  "14:20:00"),
    (6,  1200.00, "15:00:00"),
    (7,  3000.00, "15:40:00"),
    (8,  1200.00, "16:20:00"),
    (9,  500.00,  "17:00:00"),
    (10, 600.00,  "17:40:00"),
    (11, 800.00,  "19:30:00"),
    (12, 700.00,  "19:40:00")
]

# alertas 
# 1. valor 20% que a media das ultimas 5 transacoes normais
# 2. se nao tiver 5 anteriores ela se torna suspeita caso esteja acima do limite inicial 
# 3. sse alguma for fraudulenta, todas num intervalo de 60 tbm serao consideradas

# transacoes(numero,valor,hora)
def detectar_fraude(transacoes):

    #converter a coluna das horas para Date Time
    df = pd.DataFrame(transacoes,columns=["Id","Valor","Hora"])
    df['Hora'] = pd.to_datetime(df['Hora'], format='%H:%M:%S')

    lista = df.values.tolist()

    fraudes = []
    normais =[]
   
    lim_ini = lista[0][1]

    for tran in lista[1:]:
        ultima = lista[-1]
        dif_hora = ultima[2] - tran[2]

        if len(normais) < 5:
            if tran[1] > lim_ini*1.2:
                fraudes.append(tran)
            else:
                normais.append(tran)

        elif len(normais) >= 5:
            saldo_ok = [valor[1] for valor in normais[-5:]]
            media = sum(saldo_ok)/5
            media_final = (media*0.2) + media

            if dif_hora <= timedelta(minutes=60):
                fraudes.append(tran)
            elif tran[1] > media_final :
                fraudes.append(tran)
            else:
                normais.append(tran)
               
    trans_fraude = [fraude[0] for fraude in fraudes]
    return(trans_fraude)


print(detectar_fraude(transacoes))

        
