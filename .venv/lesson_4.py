purchase_amount = input('Введите сумму покупки: ')
vip_check = input('Клиент вип(ДА или НЕТ)? ').lower()

if int(purchase_amount) > 1000 and vip_check == 'да':
    discount = int(purchase_amount) * 0.25
elif int(purchase_amount) > 1000 and vip_check == 'нет':
    discount = int(purchase_amount) * 0.2
elif  500 < int(purchase_amount) < 1000:
    discount = int(purchase_amount) * 0.1
elif int(purchase_amount) < 500:
    discount = 0
else:
    print('Что-то пошло не так, попробойти всё повторить!')

print(f'К оплате: {round(int(purchase_amount) - discount, 3)} рублёв.\n'
      f'Размер скидки составил: {round(discount, 3)} рублёв.')


