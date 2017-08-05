"""
This is a pure python implementation of the merge sort algorithm

"""

import os

import pandas
import time

def merge_sort_wrapper(file_path, output_path):

    file_size = os.path.getsize(os.getcwd() + "/" + input_file)

    numbers_unsorted = open(file_path, "r")
    collection = map(int, [line.strip().split(' ') for line in numbers_unsorted.readlines()][0])

    start_time = time.clock()
    numbers_sorted = merge_sort(collection)
    end_time = time.clock()

    data = {'total time': end_time - start_time ,'algorithm': "mergesort", 'file size': file_size}
    dataframe = pandas.DataFrame([data], columns=['total time', 'algorithm', 'file size'])

    dataframe.to_csv(output_path)

    return numbers_sorted

def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    """

    length = len(collection)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1

    return collection

if __name__ == "__main__":
    import sys
    import os

    dir_path = os.getcwd()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    merge_sort_wrapper(dir_path + "/" + input_file,  dir_path + "/results/" + output_file)
