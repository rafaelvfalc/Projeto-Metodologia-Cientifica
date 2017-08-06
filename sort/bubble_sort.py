"""
This is pure python implementation of bubble sort algorithm

"""

import os

import statistics
import pandas
import time

from memory_profiler import memory_usage

def bubble_sort(file_path, output_path):
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    """

    numbers_unsorted = open(file_path, "r")
    collection = map(int, [line.strip().split(' ') for line in numbers_unsorted.readlines()][0])
    file_size = os.path.getsize(os.getcwd() + "/" + input_file)

    start_time = time.clock()
    length = len(collection)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
    end_time = time.clock()

    data = {'total time': end_time - start_time ,'algorithm': "bubblesort", 'file size': file_size}
    dataframe = pandas.DataFrame([data], columns=['total time', 'algorithm', 'file size'])
    dataframe.to_csv(output_path)

    return collection

if __name__ == "__main__":
    import sys

    dir_path = os.getcwd()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    tuple_function = (bubble_sort,(dir_path + "/" + input_file, dir_path + "/results/" + output_file))

    mem_usage = memory_usage(tuple_function, .001)

    dataframe = pandas.read_csv(dir_path + "/results/" + output_file, index_col=0)
    dataframe["memory usage"] = statistics.mean(mem_usage)
    
    dataframe.to_csv(dir_path + "/results/" + output_file)
    