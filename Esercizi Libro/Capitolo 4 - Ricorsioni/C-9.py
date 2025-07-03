"""Write a short recursive Python function that finds the minimum and maximum
values in a sequence without using any loops."""
import random

random.seed(90)

sequence = [random.randint(0,1000) for _ in range(100)]

print(sequence)



def min_max(seq):
    if len(seq) == 1 : return seq[0], seq[0]

    if len(seq) == 2:
        a, b = seq[0], seq[1]
        if a < b:
            return a, b
        else:
            return b, a

    mid = len(seq)//2
    min1,max1 = min_max(seq[:mid])
    min2,max2 = min_max(seq[mid:])
    if min1 < min2:
        overall_min = min1
    else:
        overall_min = min2

    if max1 > max2:
        overall_max = max1
    else:
        overall_max = max2

    return overall_min, overall_max

print(min_max(sequence))
