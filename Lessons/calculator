EXCHANGE_RATES = {
    'USD': 1,
    'EUR': 1.3,
    'RUB': 0.01425,
    'BTC': 6000,
}


def get_exchange_rates():  # TODO: реализовать получение курсов по API
    return EXCHANGE_RATES


def main():  # TODO: сделать, чтобы программа работала, пока пользователь не введет команду (например, exit)
    exchange_rates = get_exchange_rates()
    currencies = list(exchange_rates)  # TODO: сделать красивый вывод списка валют

    base_currency = input(f'Введите валюту, которую хотите поменять {currencies}: ').upper()
    if base_currency not in currencies:  # TODO: сделать возможность повторного ввода
        print('Такой валюты нет')
        return

    target_currency = input(f'Введите валюту, на которую хотите поменять {currencies}: ').upper()  # TODO: сделать возможность повторного ввода
    if target_currency not in currencies:
        print('Такой валюты нет')
        return  # TODO: выделить схожие блоки кода в функцию

    currency_amount = int(input('Введите количество валюты: '))  # TODO: обработать случай, когда пользователь вводит не целое число

    base_currency_rate = exchange_rates[base_currency]
    target_currency_rate = exchange_rates[target_currency]
    cross_course = base_currency_rate / target_currency_rate
    result = cross_course * currency_amount  # TODO: сделать красивый вывод (округлять)
    print(result)


main()
