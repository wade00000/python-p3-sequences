#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    fib = [0,1]

    while len(fib) != length:
        next_number = fib[-1] + fib[-2]
        fib.append(next_number)

    print(fib)
    

print_fibonacci(10)