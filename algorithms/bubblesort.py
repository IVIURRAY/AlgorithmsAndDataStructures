"""
Selection sort - A naive sorting algorithm

Iterate from left to right [, , , -->, , , ]
Find the lowest number in array and more it to the beginning of the array.
Start again but starting from n+1 in the index as you've already sorted this part.

Time Complexity: O(n)^2 as for each pass you iterate over every element.
Space Complexity: O(1) as you change vales in place you don't create any new memory.

Good uses: Inserting one item into an already sorted list then only one iteration needed to sort the array.
Bad uses: Almost everything as its O(n)^2.
"""
# TODO - Add condition to break out when complete iteration without a swap

def swap(arr, i, j):
    x = arr[i]
    arr[i] = arr[j]
    arr[j] = x
    return arr


numbers = [5, 9, 3, 1, 2, 8, 4, 7, 6]

for x in range(len(numbers)):
    for i in range(len(numbers[x:])):
        if i+1 < len(numbers[x:]):
            if numbers[i] > numbers[i+1]:
                numbers = swap(numbers, i, i+1)
            print('Pass: %s Iteration %s' % (x, i), numbers)


print('done')
