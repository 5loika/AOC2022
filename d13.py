#!/bin/python3

import sys
from aocd import data
from aocd import submit
import itertools as it

testdata = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
test1 = 13
test2 = 140

def comp(l,r):
    if type(l) is list and type(r) is list:
        z = it.zip_longest(l,r)
        for i in z:
            if i[0] == None:
                return(True)
            if i[1] == None:
                return(False)
            res = comp(i[0],i[1])
            if res is not None:
                return(res)
        return(None)
    elif type(l) is int and type(r) is int:
        if l < r:
            return(True)
        elif l > r:
            return(False)
        else:
            return(None)
    elif type(l) is int and type(r) is list:
        l = [l]
        return comp(l,r)
    elif type(l) is list and type(r) is int:
        r = [r]
        return comp(l,r)

def part1(mydata):
    index = 0
    count = 0
    pairs = mydata.split("\n\n")
    for p in pairs:
        index += 1
        l, r = p.splitlines()
        l = eval(l)
        r = eval(r)
        if comp(l,r):
            count += index
    return(count)


def part2(mydata):
    lines = []
    for l in mydata.splitlines():
        if not l == '':
            lines.append(eval(l))
    lines.append([[2]])
    lines.append([[6]])
    for i in range(1, len(lines)): # Insertion Sort
        key_item = lines[i]
        j = i - 1
        while j >= 0 and not comp(lines[j],key_item):
            lines[j + 1] = lines[j]
            j -= 1
        lines[j + 1] = key_item
    res = 1
    for i in range(len(lines)-1):
        if lines[i] == [[2]] or lines[i] == [[6]]:
            res *= (i+1)
    return res


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "submit":
            if sys.argv[2] == "a":
                submit(part1(data), part="a")
            elif sys.argv[2] == "b":
                submit(part2(data), part="b")
            else:
                print("Specify a or b")
        elif sys.argv[1] == "run":
            if sys.argv[2] == "a":
                print("Part 1: ", part1(data))
            elif sys.argv[2] == "b":
                print("Part 2: ", part2(data))
            else:
                print("Part 1: ", part1(data))
                print("Part 2: ", part2(data))
        elif sys.argv[1] == "test":
            result1 = part1(testdata)
            if test1 == result1:
                print("Test 1 - Pass:", result1)
            else:
                print("Test 1 - Fail:", result1)
            result2 = part2(testdata)
            if test2 == result2:
                print("Test 2 - Pass:", result2)
            else:
                print("Test 2 - Fail:", result2)
    else:
        print("Part 1: ", part1(data))
        print("Part 2: ", part2(data))
