while True:

    number = input('введите число от 1 до 10')

    if number.isdigit() == False:

        print(f'{number} -  не является числом')
        continue
    elif 1 > int(number) > 10 :

        print(f'Вы ввели - {number}. Число не может быть меньше 0 и больше 10')
        continue

    else:

        break

    


print(int(number)+10)
