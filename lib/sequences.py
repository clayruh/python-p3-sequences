#!/usr/bin/env python3
sequence = []

def print_fibonacci(length):
    for i in range(length):
        if i > 1:
            num = sequence[-2] + sequence[-1]
        else:
            num = i
        sequence.append(num)

# print_fibonacci(0)
# print(sequence)