import unittest
from src.array_sort import ArraySort

array_sort = ArraySort()

class ArraySortTest(unittest.TestCase):
    def test_bubble_sort(self):
        nums = [2, 3, 6, 1, 7, 3, 4]
        print(array_sort.bubble_sort(arr=nums))
