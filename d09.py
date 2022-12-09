#!/bin/python3

import sys
from aocd import data
from aocd import submit
from collections import defaultdict
from collections import deque

testdata = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
test1 = 13
test2 = None


def part1(mydata):
    visited = defaultdict(int)
    moves = deque([])
    head = ([0,0])
    tail = ([0,0])
    visited[tuple(tail)] = 1
    for l in mydata.splitlines():
        for c in range(int(l[2:])):
            moves.append(l[0])
    while len(moves) > 0:
        dir = ([0,0])
        if moves[0] == 'R':
            head[0] += 1
        elif moves[0] == 'L':
            head[0] -= 1
        elif moves[0] == 'U':
            head[1] += 1
        elif moves[0] == 'D':
            head[1] -= 1
        else:
            return(None)
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            if head[0] > tail[0]:
                tail[0] += 1    
            elif head[0] < tail[0]:
                tail[0] -= 1
            if head[1] > tail[1]:
                tail[1] += 1
            elif head[1] < tail[1]:
                tail[1] -= 1
        visited[tuple(tail)] = 1
        moves.popleft()
    return(len(visited.keys()))


def part2(mydata):
    return None


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
