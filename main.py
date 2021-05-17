# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import matplotlib.pyplot as plt
import sorting as s

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max_power = 1000
    base = 10
    sortingMethods = [s.quick_sort, s.merge_sort, s.heap_sort, s.selection_sort, s.bubble_sort, s.insertion_sort]
    sortingNames = ['Quick Sort', 'Merge Sort', 'Heap Sort', 'Selection Sort', 'Bubble Sort', 'Insertion Sort']
    numOfSortingMethods = len(sortingMethods)
    timeArr = np.zeros((numOfSortingMethods, max_power), float)
    for i in range(numOfSortingMethods):
        for j in range(max_power):
            timeArr[i, j] = s.benchmark(sortingMethods[i], base * (j + 1))
            if j%100 ==0:
                print("Currently in {} iteration number {}".format(sortingNames[i], j))


    for i in range(numOfSortingMethods):
        print('{} : '.format(sortingNames[i]))
        for j in range(max_power):
            print('{}'.format(timeArr[i, j]), end=' ')
        print("")
    X = np.array([base * i for i in range(1, max_power + 1)])
    for i in range(numOfSortingMethods):
        plt.plot(X, timeArr[i], label=sortingNames[i])
    plt.xlabel('Number Of Elements')
    plt.ylabel('Time Taken In Seconds')
    plt.title("Sorting Methods Complexities")
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0.)
    plt.yscale('log')
    plt.show()


def check_if_sorted(array):
    for k in range(0, len(array) - 1, 1):
        if array[k] > array[k + 1]:
            return False

    return True

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
