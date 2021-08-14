import numpy as np


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidType(Error):
    """Raised when the input is invalid"""

    def __init__(self, name, type):
        print(f"Invalid Type: {name}, {type} expected!")


def unit_sequence_1d(length, random=False):
    if not isinstance(length, int) or length <= 0:
        raise InvalidType("length", int)
    if not isinstance(random, bool):
        raise InvalidType("random", bool)
    seq = np.arange(0, 1+1.0/(length-1), 1.0/(length-1))
    if random:
        return np.random.shuffle(seq)
    return seq
