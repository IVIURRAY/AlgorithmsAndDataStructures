"""
Bubble Sort - A naive sorting algorithm

Iterate from left to right [, , , -->, , , ]
If L is smaller than R then swap them. Moving largest value to the

Time Complexity: O(n)^2 as for each pass you iterate over every element.
Space Complexity: O(1) as you change vales in place you don't create any new memory.

Good uses: Inserting one item into an already sorted list then only one iteration needed to sort the array.
Bad uses: Almost everything as its O(n)^2.
"""
# TODO - Add condition to break out when complete iteration without a swap

from utils.timer import Timer
from utils.arrays import swap


def bubbleSort(numbers, debug=False):
    for x in range(len(numbers)):
        for i in range(len(numbers[:-x])):
            if i+1 < len(numbers):
                if numbers[i] > numbers[i+1]:
                    numbers = swap(numbers, i, i+1)

                if debug:
                    print('Pass: %s Iteration %s' % (x, i), numbers)


if __name__ == '__main__':
    import random
    with Timer():
        bubbleSort([5, 9, 3, 1, 2, 8, 4, 7, 6], debug=True)
    with Timer():
        bubbleSort([random.randint(1, 10) for _ in range(100)])
    with Timer():
        bubbleSort([random.randint(1, 10) for _ in range(10000)])

print('done')
