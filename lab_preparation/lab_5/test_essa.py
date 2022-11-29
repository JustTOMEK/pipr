import essa
import pytest


def test_diversion_b_0():
    with pytest.raises(ZeroDivisionError):
        assert essa.diversion(7, 0) == 0
