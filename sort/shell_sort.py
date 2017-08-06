"""
This is a pure python implementation of the shell sort algorithm

"""
import os

import statistics
import pandas
import time

from memory_profiler import memory_usage

def shell_sort(file_path, output_path):
    """Pure implementation of shell sort algorithm in Python
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending

    """
    # Marcin Ciura's gap sequence
    file_size = os.path.getsize(os.getcwd() + "/" + input_file)
    start_time = time.clock()
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    numbers_unsorted = open(file_path, "r")
    collection = map(int, [line.strip().split(' ') for line in numbers_unsorted.readlines()][0])

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1

    end_time = time.clock()

    data = {'total time': end_time - start_time ,'algorithm': "shellsort", 'file size': file_size}
    dataframe = pandas.DataFrame([data], columns=['total time', 'algorithm', 'file size'])
    dataframe.to_csv(output_path)
    
    return collection

if __name__ == "__main__":
    import sys

    dir_path = os.getcwd()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    tuple_function = (shell_sort,(dir_path + "/" + input_file, dir_path + "/results/" + output_file))

    mem_usage = memory_usage(tuple_function, .001)

    dataframe = pandas.read_csv(dir_path + "/results/" + output_file, index_col=0)
    dataframe["memory usage"] = statistics.mean(mem_usage)
    
    dataframe.to_csv(dir_path + "/results/" + output_file)
