"""
Fibonacci sequence

0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

def fib_recursion(n):
    if n <= 1:
        return n

    return fib_recursion(n-1) + fib_recursion(n-2)

def fib_non_recursion(n):

    if n <= 1:
        return n

    a = 1
    b = 1
    for _ in range(2, n):
        a, b = a + b, a

    return a

def my_memory(f):
    memory = {}

    def helper(num):
        if num in memory:
            return memory[num]
        memory[num] = f(num)

        return memory[num]

    return helper

@my_memory
def fib_memorize(n):
    if n <= 1:
        return n

    return fib_recursion(n-1) + fib_recursion(n-2)


if __name__ == '__main__':
    # for n in range(10):
    #     print(fib_memorize(n))
    print(fib_memorize(30))
    print(fib_memorize(30))


