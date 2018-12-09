
def swap(arr, i, j):
    """Swap in place two items in an array"""
    x = arr[i]
    arr[i] = arr[j]
    arr[j] = x
    return arr
