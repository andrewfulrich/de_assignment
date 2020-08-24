#!/usr/bin/python3
import sys
from itertools import permutations 

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    digits = [int(d) for d in str(num)]
    # return if it's just a single digit
    if len(digits) == 1:
        return -1

    # return if it's already the biggest
    sorted_reversed=digits[::-1]
    sorted_reversed.sort(reverse=True)
    if sorted_reversed == digits:
        return -1

    #simplicity or performance? for this case, I'll take simplicity
    #get all permutations
    perms=[''.join(p) for p in permutations(str(num))]
    #filter for the ones that are greater than num
    numbers=list(filter(lambda perm: perm>num, [int(perm) for perm in perms]))
    #return the least one from that filtered set
    numbers.sort()
    return numbers[0]

if __name__ == "__main__":
    main()



