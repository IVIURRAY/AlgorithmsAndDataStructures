"""
Insertion Sort - A sorting algorithm

Consider the left most array index sorted.
Take the next item in the array and compare it to the sorted array.

Time complexity: O(n)^2 as each item is compared against each other. Wost case in array is in reverse order.
Space complexity: O(n) as can be done in place.

Good uses: Slightly more optimal than selection and bubble.
Bad uses: In siutaions when the array is in decending order.
"""
from utils.arrays import swap
from utils.timer import Timer


def insertionSort(numbers, debug=False):

    for i in range(1, len(numbers)):

        # element to be compared
        current = numbers[i]

        # comparing the current element with the sorted portion and swapping
        while i > 0 and numbers[i - 1] > current:
            if debug: print('%s is less than %s - swapping %s' % (current, numbers[i - 1], numbers))
            numbers = swap(numbers, i, i-1)
            i-=1

        if debug:
            print('Current array: %s' % (numbers))

    return numbers

if __name__ == '__main__':
    import random
    with Timer():
        insertionSort([5, 9, 3, 1, 2, 8, 4, 7, 6], debug=True)
    with Timer():
        insertionSort([random.randint(1, 10) for _ in range(100)])
    with Timer():
        insertionSort([random.randint(1, 10) for _ in range(10000)])
