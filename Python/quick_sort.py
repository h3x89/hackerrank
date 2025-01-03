# quick sort algorithm in python

# Quick Sort is a divide-and-conquer sorting algorithm that works by:
# 1. Selecting a 'pivot' element from the array (in our case, the last element)
# 2. Partitioning the array in-place around the pivot:
#    - Moving all elements smaller than pivot to the left side
#    - Moving all elements larger than pivot to the right side
#    - Placing pivot in its final sorted position
# 3. Recursively sorting the sub-arrays on both sides of the pivot
#
# In this implementation:
# - We use the last element as pivot: arr[high]
# - We perform in-place partitioning using two pointers (i, j)
# - The partition function returns the final position of pivot
#
# Time Complexity:
# - Average case: O(n log n)
# - Worst case: O(n^2) when array is already sorted
# Space Complexity: O(log n) due to recursive call stack

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)
    return arr

# Wrapper function for easier usage
def quick_sort(arr):
    if not arr:
        return []
    return quick_sort_in_place(arr.copy(), 0, len(arr) - 1)

import unittest

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
    
    def test_quick_sort_empty(self):
        self.assertEqual(quick_sort([]), [])
    
    def test_quick_sort_single(self):
        self.assertEqual(quick_sort([1]), [1])
    
    def test_quick_sort_sorted(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]) 

if __name__ == '__main__':
    unittest.main()
