from datetime import datetime


def split_price(price):
    price_zl = price // 100
    price_gr = price % 100
    return (price_zl, price_gr)


def format_price(price):
    zl, gr = price // 100, price % 100
    return f'{zl}.{gr:02}'


def get_description(name, price):
    price_parts = split_price(price)
    return f'{name}\t{price_parts[0]}.{price_parts[1]:02}'


def print_description(name, price):
    description = get_description(name, price)
    print(description)


def get_total_price(receipt):
    total_price = 0
    for product in receipt:
        total_price += product[1]
    return total_price


def print_receipt(receipt):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")
    print(dt_string)
    product_count = 1
    tax_value = 0
    for name, price in receipt:
        tax_value += price * get_tax_value(get_tax_group(name))
        price = format_price(price)
        print(f'{product_count}. {name:10} {price:>13} {get_tax_group(name)}')
        product_count += 1
    print('-' * 30)
    total_price = get_total_price(receipt)
    formatted_value = format_price(total_price)
    print(f'TAX:{format_price(tax_value//100):>23}')
    print(f'TOTAL:{formatted_value:>21}')
    print(f'TOTAL+TAX:{format_price(tax_value//100+total_price):>17}')


def get_tax_group(product):
    tax_group_A = ['Stanik', 'Majtki', 'Figi']
    tax_group_B = ['Cars', 'Planes', 'Jets']
    if product in tax_group_A:
        return 'A'
    elif product in tax_group_B:
        return 'B'
    else:
        return 'E'


def get_tax_value(tax_group):
    slownik = {'A': 12, 'B': 8, 'E': 22}
    return slownik[tax_group]


def get_product():
    product_prices = {
        'Stanik': 92883,
        'Majtki': 4382,
        'Mleko': 3281
    }
    name = input('Give a product name: ')
    quantity = int(input('Give a product quantity: '))
    return (name, quantity*product_prices[name])


my_receipt = [
    ('Stanik', 97283),
    ('Majtki', 4732),
    ('Mleko', 3271)]

print_receipt(my_receipt)