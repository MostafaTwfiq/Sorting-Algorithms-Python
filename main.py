# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sorting as s

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [10, 4, 2, 3, 6, 7, 9, 8, 1, 5]
    sort = s.Sorting()
    sort.quick_sort(arr)
    print(arr)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
