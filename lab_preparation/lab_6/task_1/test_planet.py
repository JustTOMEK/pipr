from planet import Planet, distance
from pytest import raises


def test_introduce_planet():
    planet = Planet(3, 4, 5, 'Saturn')
    assert planet.x() == 3
    assert planet.y() == 4
    assert planet.z() == 5
    assert planet.name() == 'Saturn'


def test_introduce_planet_no_name():
    planet = Planet(3, 4, 5,)
    assert planet.x() == 3
    assert planet.y() == 4
    assert planet.z() == 5
    assert planet.name() == ''


def test_set_name():
    planet = Planet(1, 2, 3, 'Essa')
    assert planet.name() == 'Essa'
    planet.set_name('NoWiSz')
    assert planet.name() == 'Nowisz'


def test_set_name_empty():
    planet = Planet(1, 2, 3, 'Essa')
    assert planet.name() == 'Essa'
    planet.set_name('')
    assert planet.name() == ''


def test_set_x():
    planet = Planet(1, 2, 3, 'Essa')
    assert planet.x() == 1
    planet.set_x(3)
    assert planet.x() == 3


def test_set_x_not_int():
    planet = Planet(1, 2, 3, 'Essa')
    assert planet.x() == 1
    with raises(ValueError):
        planet.set_x(2.5)


def test_set_y():
    planet = Planet(1, 2, 3, 'Essa')
    assert planet.y() == 2
    planet.set_y(3)
    assert planet.y() == 3


def test_set_y_not_int():
    planet = Planet(1, 2, 3, 'Essa')
    assert planet.y() == 2
    with raises(ValueError):
        planet.set_y(2.5)


def test_set_z():
    planet = Planet(1, 2, 3, 'Essa')
    assert planet.z() == 3
    planet.set_z(4)
    assert planet.z() == 4


def test_set_z_not_int():
    planet = Planet(1, 2, 3, 'Essa')
    assert planet.z() == 3
    with raises(ValueError):
        planet.set_z(2.5)


def test__str__():
    planet = Planet(1, 2, 3, 'Saturn')
    assert str(planet) == 'Planet Saturn coordinates are: x:1, y:2, z:3.'


def test__str___no_name():
    planet = Planet(1, 2, 3)
    assert str(planet) == 'Planet  coordinates are: x:1, y:2, z:3.'


def test_distance():
    planet_1 = Planet(1, 1, 0)
    planet_2 = Planet(2, 1, 2)
    assert distance(planet_1, planet_2) == 2.24


def test_distance_zero():
    planet_1 = Planet(1, 1, 0)
    planet_2 = Planet(1, 1, 0)
    assert distance(planet_1, planet_2) == 0
