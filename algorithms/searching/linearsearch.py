"""

Linear Search - A simple search algorithm.

Iterate through an unsorted array until we find our match.

Time complexity:
Space complexity:

Good cases:
Bas cases:

"""
from utils.timer import Timer


def linear_search(array, target):
    # return any([i == target for i in array])
    for i in array:
        if i == target:
            return True

    return False


if __name__ == '__main__':
    with Timer():
        print(linear_search([i for i in range(10)], 5))
    with Timer():
        print(linear_search([i for i in range(1000)], 250))
    with Timer():
        print(linear_search([i for i in range(1000000)], 999999))
