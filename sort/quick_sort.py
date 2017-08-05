"""
This is a pure python implementation of the quick sort algorithm

"""

import os

import pandas
import time

def quick_sort_wrapper(file_path, output_path):

    file_size = os.path.getsize(os.getcwd() + "/" + input_file)

    numbers_unsorted = open(file_path, "r")
    collection = map(int, [line.strip().split(' ') for line in numbers_unsorted.readlines()][0])

    start_time = time.clock()
    numbers_sorted = quick_sort(collection)
    end_time = time.clock()

    data = {'total time': end_time - start_time ,'algorithm': "mergesort", 'file size': file_size}
    dataframe = pandas.DataFrame([data], columns=['total time', 'algorithm', 'file size'])

    dataframe.to_csv(output_path)

    return numbers_sorted


def quick_sort(ARRAY):
    """Pure implementation of quick sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    """

    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)

if __name__ == "__main__":
    import sys
    import os

    dir_path = os.getcwd()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    quick_sort_wrapper(dir_path + "/" + input_file,  dir_path + "/results/" + output_file)
    