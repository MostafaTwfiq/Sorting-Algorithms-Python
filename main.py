# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sorting as s
import generator as g


class GraphPoint:
    array_size = 0
    time = 0

    def __init__(self, size: int, running_time):
        self.array_size = size
        self.time = running_time

    def __str__(self):
        return "size:" + str(self.array_size) + "\n" \
               + "time: " + str(self.time) + "\n"

    def __repr__(self):
        return "size:" + str(self.array_size) + "\n" \
               + "time: " + str(self.time) + "\n"


def generate_x_axes_points(graph_points):
    x = []
    for graph_point in graph_points:
        x.append(graph_point.array_size)

    return x


def generate_y_axes_points(graph_points):
    y = []
    for graph_point in graph_points:
        y.append(graph_point.time)

    return y


def plot_graph(graph_points, sorintg_types, types_colors):

    for k in range(0, len(graph_points)):
        plot_second_order_curve(graph_points[k], sorintg_types[k], types_colors[k])

    plt.title('Sorts')
    plt.xlabel('Size')
    plt.ylabel('Time in micro')

    plt.show()


def plot_second_order_curve(graph_points, name, color):
    x_points = generate_x_axes_points(graph_points)
    y_points = generate_y_axes_points(graph_points)
    x_points = np.array(x_points)
    x_points = x_points.reshape(len(x_points), 1)
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(x_points)
    poly.fit(X_poly, y_points)
    lin2 = LinearRegression()
    lin2.fit(X_poly, y_points)

    plt.scatter(x_points, y_points, color=color, label=name)
    plt.plot(x_points, lin2.predict(poly.fit_transform(x_points)), color=color, label=name)

    plt.grid(True)
    plt.legend(loc='upper left', borderaxespad=0.)


def write_data(sorting_fun, types):
    file = open('dataSet.txt', 'w')

    count = 0
    for s_fun in sorting_fun:
        x = generate_x_axes_points(s_fun)
        y = generate_y_axes_points(s_fun)
        file.write(types[count] + ":\n")
        for j in range(0, len(x)):
            file.write("(" + str(x[j]) + ", " + str(y[j]) + ")" + "\n")

        count += 1

    file.close()


if __name__ == '__main__':

    arr = []

    for i in range(10, 1000, 10):
        arr.append(g.generate_array(i))

    plot_functions = [[],
                      [],
                      [],
                      [],
                      [],
                      []]

    sorting_functions = [s.quick_sort, s.merge_sort, s.heap_sort, s.insertion_sort, s.selection_sort, s.bubble_sort]
    colors = ['red', 'blue', 'black', 'orange', 'yellow', 'green']
    names = ['Quick sort', 'Merge sort', 'Heap sort', 'Insertion sort', 'Selection sort', 'Bubble sort']

    counter = 0
    for fun in sorting_functions:
        for cur_arr in arr:
            length = len(cur_arr)
            time = s.benchmark(fun, cur_arr.copy()) * 10 ** 6
            gp = GraphPoint(length, time)
            plot_functions[counter].append(gp)

        counter += 1

    write_data(plot_functions, names)
    plot_graph(plot_functions, names, colors)


def check_if_sorted(array):
    for k in range(0, len(array) - 1, 1):
        if array[k] > array[k + 1]:
            return False

    return True
