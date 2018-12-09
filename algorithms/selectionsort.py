"""
Selection sort - A naive sorting algorithm

Iterate from left to right [, , , -->, , , ]
Find the lowest number in array and more it to the beginning of the array.
Start again but starting from n+1 in the index as you've already sorted this part.

Time Complexity: O(n)^2 as for each pass you iterate over every element.
Space Complexity: O(1) as you change vales in place you don't create any new memory.

Good uses: ??
Bad uses: Almost everything as its O(n)^2.
"""
# TODO: Add a condition to break out of the sort when minimum_index  == 0 (nothing to swap).

from utils.timer import Timer
from utils.arrays import swap


def selectionSort(numbers, debug=False):
    minimum_index = 0
    for pointer in range(len(numbers)):
        minimum = 99*99                                         # just some huge number to be less than
        for i, num in enumerate(numbers[pointer:]):             # everything from pointer+ is already sorted
            if num < minimum:                                   # find the min of the sub array
                if debug: print('%s is less than %s' % (num, minimum))
                minimum = num                                   # store min and its index to use for swapping
                minimum_index = i

        if debug: print('Minimum this round is %s' % minimum)
        numbers = swap(numbers, minimum_index + pointer, pointer)   # as min_index is enumerating from sub array add pointer
        if debug: print('Pass %s: %s' % (pointer, numbers))

    return numbers


if __name__ == '__main__':
    import random

    with Timer():
        selectionSort([5, 9, 3, 1, 2, 8, 4, 7, 6], debug=True)
    with Timer():
        selectionSort([random.randint(1, 10) for _ in range(100)])
    with Timer():
        selectionSort([random.randint(1, 10) for _ in range(10000)])
