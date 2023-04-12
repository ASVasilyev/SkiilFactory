price_all = 0
while True:
    try:
        count_ticket = int(input('\nСколько билетов желаете приобрести?\n'))
        if count_ticket <= 0:
            print('\nКоличество билетов не может быть меньше или равно 0')
        else:
            break
    except ValueError:
        print('\nВведите целое число')
for i in range(count_ticket):
    i += 1
    while True:
        try:
            age = int(input(f'\nВведите возвраст посетителя для билета №{i}: '))
            if age < 0:
                print('\nВам не может быть столько лет')
            elif age < 18:
                print('Билет бесплатный')
                print(f'Общая стоимость: {price_all} руб.')
                break
            elif 18 <= age < 25:
                price_all += 990
                print('Стоимость билета: 990 руб.')
                print(f'Общая стоимость: {price_all} руб.')
                break
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
                print(f'Общая стоимость: {price_all} руб.')
                break
        except ValueError:
            print('\nВведите целое число')
if count_ticket > 3:
    price_all = price_all*0.9
    print('\n*****')
    print(f'Сумма к оплате {price_all} руб. (с учётом 10% скидки за приобретение больше 3х билетов)')
else:
    print('\n*****')
    print(f'Сумма к оплате {price_all} руб.')