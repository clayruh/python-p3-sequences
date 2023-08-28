#!/usr/bin/env python3
def print_fibonacci(length):
    sequence = []
    for i in range(length):
        if i > 1:
            num = sequence[-2] + sequence[-1]
        else:
            num = i
        sequence.append(num)
    print(sequence)

# print_fibonacci(4)
# print(sequence)