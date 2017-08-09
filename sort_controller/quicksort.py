"""
This is a pure python implementation of the quick sort algorithm

"""

import os

import statistics
import pandas
import time

from memory_profiler import memory_usage

global data

def quick_sort_wrapper(file_path, output_path):

    global data

    file_size = os.path.getsize(os.getcwd() + "/" + input_file)

    numbers_unsorted = open(file_path, "r")
    collection = map(int, [line.strip().split(' ') for line in numbers_unsorted.readlines()][0])

    start_time = time.clock()
    numbers_sorted = quick_sort(collection)
    end_time = time.clock()

    data = [end_time - start_time , "quicksort", file_size]


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

    dir_path = os.getcwd()

    input_file = sys.argv[2]
    output_file = sys.argv[3]

    sort_function = (quick_sort_wrapper,(dir_path + "/" + input_file, dir_path + "/results/" + output_file))
    mem_usage = memory_usage(sort_function, .001)

    data.append(statistics.mean(mem_usage))

    if os.path.exists(dir_path + "/results/" + output_file):
        tmp_dataframe_1 = pandas.read_csv(dir_path + "/results/" + output_file)
        tmp_dataframe_2 = pandas.DataFrame([data], columns=['total time', 'algorithm', 'file size', "memory usage"])
        dataframe = pandas.concat([tmp_dataframe_1, tmp_dataframe_2])
        dataframe.to_csv(dir_path + "/results/" + output_file, index=False)
    else:
        dataframe = pandas.DataFrame([data], columns=['total time', 'algorithm', 'file size', "memory usage"])
        dataframe.to_csv(dir_path + "/results/" + output_file, index=False)