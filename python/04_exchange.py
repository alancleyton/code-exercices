'''
Currency Exchange

https://exercism.org/tracks/python/exercises/currency-exchange
'''

def exchange_money(budget: float, exchange_rate: float) -> float:
    return budget / exchange_rate

print(exchange_money(127.5, 1.2))

def get_change(budget: float, exchanging_value: float) -> float:
    return budget - exchanging_value

print(get_change(127.5, 120))

def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    return denomination * number_of_bills

print(get_value_of_bills(5, 128))

def get_number_of_bills(amount: float, denomination: int) -> int:
    return int(amount) // denomination

print(get_number_of_bills(127.5, 5))

def get_leftover_of_bills(amount: float, denomination: int) -> float:
    return amount % denomination

print(get_leftover_of_bills(127.5, 20))

def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    exchange_rate_fee = (spread * exchange_rate) / 100
    exchange_money_value = exchange_money(budget, exchange_rate + exchange_rate_fee)
    number_of_bills = get_number_of_bills(exchange_money_value, denomination)
    value_of_bills = get_value_of_bills(denomination, number_of_bills)
    return value_of_bills

print(exchangeable_value(127.25, 1.20, 10, 20))