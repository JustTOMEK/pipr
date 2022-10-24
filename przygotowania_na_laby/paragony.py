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


def get_product():
    product = input('Give product name: ')
    price = int(input('Give product price in gr: '))
    return (product, price)


def get_total_price(receipt):
    total_price = 0
    for product in receipt:
        total_price += product[1]
    return total_price


def print_receipt(receipt):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    product_count = 1
    for name, price in receipt:
        price = format_price(price)
        print(f' {product_count:2}. {name:19}{price:>6}')
        product_count += 1
    print('-' * 30)
    total_price = get_total_price(receipt)
    formatted_value = format_price(total_price)
    print(f'TOTAL:{formatted_value:>24}')


my_receipt = [
    ('Stanik', 9283),
    ('Majtki', 432),
    ('Mleko', 321)]

print_receipt(my_receipt)
