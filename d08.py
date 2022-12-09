#!/bin/python3

import sys
from aocd import data
from aocd import submit
import numpy as np

testdata = """30373
25512
65332
33549
35390"""
test1 = 21
test2 = 8


def part1(mydata):
    txtTrees = []
    for l in mydata.splitlines():
        txtTrees.append(list([int(x) for x in l]))
    trees = np.array(txtTrees)
    rows, cols = trees.shape
    count = 2 * (rows - 1) + 2 * (cols - 1)  # Count all edge trees
    for row in range(1, rows - 1):  # Check all interior trees
        for col in range(1, cols - 1):
            t = trees[row, col]
            left = max(trees[row, :col])
            right = max(trees[row, col + 1 :])
            top = max(trees[:row, col])
            bottom = max(trees[row + 1 :, col])
            if t > left or t > right or t > top or t > bottom:
                count += 1
    return count


def part2(mydata):
    txtTrees = []
    scores = []
    for l in mydata.splitlines():
        txtTrees.append(list([int(x) for x in l]))
    trees = np.array(txtTrees)
    rows, cols = trees.shape
    for row in range(1, rows - 1):  # Check all interior trees
        for col in range(1, cols - 1):
            t = trees[row, col]
            left = trees[row, :col]
            right = trees[row, col + 1 :]
            up = trees[:row, col]
            down = trees[row + 1 :, col]
            l = r = u = d = 0
            for n in left[::-1]:
                l += 1
                if n >= t:
                    break
            for n in up[::-1]:
                u += 1
                if n >= t:
                    break
            for n in right:
                r += 1
                if n >= t:
                    break
            for n in down:
                d += 1
                if n >= t:
                    break
            scores.append(l * u * r * d)
    return max(scores)


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
