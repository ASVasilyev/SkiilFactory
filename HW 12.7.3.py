money = int(input('Введите сумму, которую планируете положить под проценты:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# tkb = money * per_cent.get('ТКБ')/100
# skb = money * per_cent.get('СКБ')/100
# vtb = money * per_cent.get('ВТБ')/100
# sber = money * per_cent.get('СБЕР')/100
# deposit = [tkb, skb, vtb, sber]

deposit = []
for key in per_cent:
    deposit.append(round(per_cent[key]*money/100))

print(deposit)
print('Максимальная сумма, которую вы можете заработать - ' + str(max(deposit)))

