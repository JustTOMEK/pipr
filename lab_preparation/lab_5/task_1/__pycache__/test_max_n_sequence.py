from max_n_sequence import max_n_sequence
import pytest


def test_max_n_sequence_wrong_input():
    with pytest.raises(ValueError):
        max_n_sequence('dsada', 10)
    with pytest.raises(ValueError):
        max_n_sequence([1, 2, 3, 4, 5], '10')
    with pytest.raises(ValueError):
        max_n_sequence('dsada', 10)


def test_max_n_sequence_length_to_big():
    result = max_n_sequence([1, 2, 3, 4, 5, 6], 7)
    assert not result
