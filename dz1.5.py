proceeds = float(input('Выручка- '))
if proceeds >= 0:
    costs = float(input('Издержки - '))
    if costs >= 0:
        if proceeds < costs:
            print('Фирма работает с убытком')
        elif proceeds > costs:
            print('Фирма работает с прибылью')
            if proceeds - costs / proceeds * 0.01 > costs:
                print ('Фирма рентабельна')
                workers = int(input('Количество человек в фирме - '))
                print( 'Прибыль в расчете на одного сотрудника - ', (proceeds - costs) / workers)




