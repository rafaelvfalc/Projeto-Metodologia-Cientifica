import pytest

from sort.bubblesort import bubble_sort
from sort.shellsort import shell_sort
from sort.mergesort import merge_sort
from sort.quicksort import quick_sort

LIST1 = [5,4,3,2,1]
LIST2 = [1,2,3,4,5,0,9,8,7,6]
LIST3 = [13,87,34,9,12,99,17,65]
LIST4 = [7,8,9,10,11,12]
LIST5 = [9,9,4,3,1,17,14,21]

def test_bubblesort():

    assert bubble_sort(LIST1) == [1,2,3,4,5]
    assert bubble_sort(LIST2) == [0,1,2,3,4,5,6,7,8,9]
    assert bubble_sort(LIST3) == [9,12,13,17,34,65,87,99]
    assert bubble_sort(LIST4) == [7,8,9,10,11,12]
    assert bubble_sort(LIST5) == [1,3,4,9,9,14,17,21]

def test_shellsort():

    assert shell_sort(LIST1) == [1,2,3,4,5]
    assert shell_sort(LIST2) == [0,1,2,3,4,5,6,7,8,9]
    assert shell_sort(LIST3) == [9,12,13,17,34,65,87,99]
    assert shell_sort(LIST4) == [7,8,9,10,11,12]
    assert shell_sort(LIST5) == [1,3,4,9,9,14,17,21]

def test_mergesort():

    assert merge_sort(LIST1) == [1,2,3,4,5]
    assert merge_sort(LIST2) == [0,1,2,3,4,5,6,7,8,9]
    assert merge_sort(LIST3) == [9,12,13,17,34,65,87,99]
    assert merge_sort(LIST4) == [7,8,9,10,11,12]
    assert merge_sort(LIST5) == [1,3,4,9,9,14,17,21]

def test_quicksort():

    assert quick_sort(LIST1) == [1,2,3,4,5]
    assert quick_sort(LIST2) == [0,1,2,3,4,5,6,7,8,9]
    assert quick_sort(LIST3) == [9,12,13,17,34,65,87,99]
    assert quick_sort(LIST4) == [7,8,9,10,11,12]
    assert quick_sort(LIST5) == [1,3,4,9,9,14,17,21]