"""

Binary Search - A search algorithm.

Firstly we need a sorted array.
Once we've this we can find the midpoint.
If mid < target then do the same to the left array
If mid > target then do the same to the right array
[1, 2, 3, 4, 5, 6, 7, 8] --> target 5
          ^              mid --> len(arr) / 2 = 4
                         mid < target: search the right array
[#, #, #, #, 5, 6, 7, 8] repeat

Time complexity: O(log(n)) as the array is halved each time.
Space complexity: O(log(n)) as we make a new array and the recursion of the function makes a new entry into the heap.

Good cases: Does not scale exponentially, but array needs to be sorted first.
Bas cases: When array is unsorted and the three is left/right skewed.
"""
from utils.timer import Timer


def binary_search(array, target):
    i = len(array) // 2
    mid = array[i]
    print(len(array))
    if i == 1 and mid != target:
        print('Did not find %s in array.' % target)
        return False

    if mid == target:
        return True

    if mid < target:
        return binary_search(array[i:], target)
    if mid > target:
        return binary_search(array[:i], target)

    return False


if __name__ == '__main__':
    with Timer():
        print(binary_search([i for i in range(10)], 5))
    with Timer():
        print(binary_search([i for i in range(1000)], 250))
    with Timer():
        print(binary_search([i for i in range(1000000)], 500))
