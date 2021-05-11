class GenerateArray:

    def __init__(self):
        return

    def generate_array(self, length, s_range, e_range):
        from random import randint
        arr = [1] * length
        for i in range(0, length, 1):
            arr[i] *= randint(s_range, e_range)

        return arr
