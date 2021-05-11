class Sorting:
    def __init__(self):
        return

    def quick_sort(self, arr):
        self.quick_sort_helper(arr, 0, len(arr) - 1)

    def quick_sort_helper(self, arr, s, e):
        if e - s <= 0:
            return

        bound = e + 1
        for i in range(e, s, -1):
            if arr[s] - arr[i] < 0:
                bound -= 1
                arr[bound], arr[i] = arr[i], arr[bound]

        bound -= 1
        arr[bound], arr[s] = arr[s], arr[bound]
        self.quick_sort_helper(arr, s, bound - 1)
        self.quick_sort_helper(arr, bound + 1, e)

    def selection_sort(self, arr):
        for i in range(0, len(arr), 1):
            min_element = i
            for j in range(i, len(arr), 1):
                if arr[min_element] > arr[j]:
                    min_element = j

            arr[i], arr[min_element] = arr[min_element], arr[i]
