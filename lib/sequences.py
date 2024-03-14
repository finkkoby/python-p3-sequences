#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        answer = []
    elif length < 3 and length > 0:
        answer = []
        for i in range(length):
            answer.append(i)
    else:
        answer = [0, 1]
        for i in range (2, length):
            answer.append(answer[i-1] + answer[i-2])
    print(answer)
