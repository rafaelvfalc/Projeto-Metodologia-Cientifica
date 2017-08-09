"""
This is a pure python implementation of the shell sort algorithm

"""
import os

import statistics
import pandas
import time

from memory_profiler import memory_usage

global data

def shell_sort(file_path, output_path):
    """Pure implementation of shell sort algorithm in Python
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending

    """
    global data

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

    data = [end_time - start_time , "shellsort", file_size]

if __name__ == "__main__":
    import sys

    dir_path = os.getcwd()

    input_file = sys.argv[2]
    output_file = sys.argv[3]

    sort_function = (shell_sort,(dir_path + "/" + input_file, dir_path + "/results/" + output_file))
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