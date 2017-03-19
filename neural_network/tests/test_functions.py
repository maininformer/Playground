import numpy as np  # noqa

from ..functions import (
    activation,
    linear_combination
)


def test_linear_combination():  # noqa
    weights = np.array([1, 2, 3, 4])
    variables = np.array([5, 5, 5, 5])
    assert linear_combination(weights, variables) == 50

def test_activation():  # noqa
    pass