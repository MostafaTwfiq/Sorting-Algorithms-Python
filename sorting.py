class Sorting:
    def __init__(self):
        return

    def quick_sort(self, arr):
        self.quick_sort_helper(arr, 0, len(arr) - 1)

    def quick_sort_helper(self, arr, s, e):

        if e - s <= 0:
            return

        piv = s
        bound = e + 1
        for i in range(e, s, -1):
            if arr[piv] - arr[i] < 0:
                bound -= 1
                arr[bound], arr[i] = arr[i], arr[bound]

        bound -= 1
        arr[bound], arr[piv] = arr[piv], arr[bound]
        f_half_s = s
        f_half_e = bound - 1
        s_half_s = bound + 1
        s_half_e = e
        self.quick_sort_helper(arr, f_half_s, f_half_e)
        self.quick_sort_helper(arr, s_half_s, s_half_e)

    def selection_sort(self, arr):

        for i in range(0, len(arr), 1):
            min_element = i
            for j in range(i, len(arr), 1):
                if arr[min_element] > arr[j]:
                    min_element = j

            arr[i], arr[min_element] = arr[min_element], arr[i]
