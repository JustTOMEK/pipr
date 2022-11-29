from math import sqrt


class Planet:
    """
    Class Planet. Contains attributes:
    :param name: planet's name, defaults to (empty)
    :type name: str

    :param x: planet' x coordinate
    :type x: int

    :param y: planet' y coordinate
    :type y: int

    :param z: planet' z coordinate
    :type z: int
    """
    def __init__(self, x, y, z, name=''):
        """
        Creates instance of planet.
        Gives Valuerror if x or y or z are not int type.
        """
        if int(x) != x or int(y) != y or int(z) != z:
            raise ValueError('Coordinates must be int')
        self._x = x
        self._y = y
        self._z = z
        self._name = str(name).title()

    def __str__(self):
        """
        Returns information about planet.
        """
        return f'Planet {self.name()} coordinates are: x:{self.x()}, y:{self.y()}, z:{self.z()}.'

    def set_x(self, new_x):
        """
        Changes value of x attribute.
        Raises Valuerror, if empty or not int.
        """
        if not new_x:
            raise ValueError('No x value given')
        if int(new_x) != new_x:
            raise ValueError('X must be int')
        self._x = new_x

    def x(self):
        """
        Returns value of x attribute.
        """
        return self._x

    def set_y(self, new_y):
        """
        Changes value of y attribute.
        Raises Valuerror, if empty or not int.
        """
        if not new_y:
            raise ValueError('No y value given')
        if int(new_y) != new_y:
            raise ValueError('Y must be int')
        self._y = new_y

    def y(self):
        """
        Returns value of y attribute.
        """
        return self._y

    def set_z(self, new_z):
        """
        Changes value of z attribute.
        Raises Valuerror, if empty or not int.
        """
        if not new_z:
            raise ValueError('No z value given')
        if int(new_z) != new_z:
            raise ValueError('Z must be int')
        self._z = new_z

    def z(self):
        """
        Returns value of z attribute.
        """
        return self._z

    def set_name(self, new_name):
        """
        Changes value of name attribute.
        """
        self._name = str(new_name).title()

    def name(self):
        """
        Returns value of name attribute.
        """
        return self._name


def distance(planet_1, planet_2):
    """
    Returns distance of two Planet objects.
    Distances is a float rounded to 2.
    """
    return round(sqrt(pow(planet_2.x() - planet_1.x(), 2) + pow(planet_2.y()
                 - planet_1.y(), 2) + pow(planet_2.z() - planet_1.z(), 2)), 2)
