from random import randint
import numpy as np


def generate_array(length):
    arr = np.random.randint(length, size=length)
    return arr
