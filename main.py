# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sorting as s
import generator as g

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generator = g.GenerateArray()
    arr = generator.generate_array(10, 0, 10)
    print(arr)


def check_if_sorted(array):
    for i in range(0, len(array) - 1, 1):
        if array[i] > array[i + 1]:
            return False

    return True

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
