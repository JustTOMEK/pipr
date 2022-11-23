import paragony
import pytest


def test_split_price():
    price_zl, price_gr = paragony.split_price(123)
    assert price_zl == 1
    assert price_gr == 23


def test_split_price_gr_less_than_10():
    price_zl, price_gr = paragony.split_price(101)
    assert price_zl == 1
    assert price_gr == 1


def test_split_price_zl_less_than_1():
    price_zl, price_gr = paragony.split_price(15)
    assert price_zl == 0
    assert price_gr == 15


def test_split_price_negative():
    price_zl, price_gr = paragony.split_price(-990)
    assert price_zl == -9
    assert price_gr == 90


def test_split_price_float():
    price_zl, price_gr = paragony.split_price(10.15)
    assert price_zl == 0
    assert price_gr == 10


def test_split_price_str_invalid():
    # spodziewam się, że zostanie rzucony wyjątek Valueerror
    with pytest.raises(ValueError):
        price_zl, price_gr = paragony.split_price(str(10.15))


def test_split_price_str_convertible():
    price_zl, price_gr = paragony.split_price(str(10))
    assert price_zl == 0
    assert price_gr == 10


def test_get_description_typical():
    description = paragony.get_description('Bananas', 499)
    assert description == 'Price of Bananas is 4.99'


def test_get_description_gr_less_than_10():
    description = paragony.get_description('Oranges', 801)
    assert description == 'Price of Oranges is 8.01'


def test_get_description_zl_less_than_1():
    description = paragony.get_description('Lollipop', 95)
    assert description == 'Price of Lollipop is 0.95'


def test_get_description_empty_name():
    # spodziewam się, że zostanie rzucony wyjątek Valueerror
    with pytest.raises(ValueError):
        paragony.get_description('', 999)


def test_get_description_zero_price():
    description = paragony.get_description('Apples', 0)
    assert description == 'Price of Apples is 0.00'


def test_get_description_negative_price():
    description = paragony.get_description('Apples', -990)
    assert description == 'Price of Apples is -9.90'


def test_format_price_typical():
    formatted_price = paragony.format_price(134)
    assert formatted_price == '1.34'


def test_format_price_gr_less_than_10():
    formatted_price = paragony.format_price(101)
    assert formatted_price == '1.01'


def test_format_price_zl_less_than_1():
    formatted_price = paragony.format_price(56)
    assert formatted_price == '0.56'


def test_format_price_zero_price():
    formatted_price = paragony.format_price(0)
    assert formatted_price == '0.00'


def test_format_price_negative_price():
    formatted_price = paragony.format_price(-134)
    assert formatted_price == '-1.34'
