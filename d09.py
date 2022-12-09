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
test2 = 1


from collections import defaultdict
from collections import deque

def part1(mydata):
    visited = defaultdict(int)
    moves = deque([])
    rope = [[0, 0], [0,0]]
    head = len(rope) - 1
    tail = 0
    x = 0
    y = 1
    visited[tuple(rope[tail])] = 1
    for l in mydata.splitlines():
        for c in range(int(l[2:])):
            moves.append(l[0])
    while len(moves) > 0:
        if moves[0] == "R":
            rope[head][x] += 1
        elif moves[0] == "L":
            rope[head][x] -= 1
        elif moves[0] == "U":
            rope[head][y] += 1
        elif moves[0] == "D":
            rope[head][y] -= 1
        else:
            return None
        for i in range(len(rope)-1,0,-1):
            if abs(rope[i-1][x] - rope[i][x]) > 1 or abs(rope[i-1][y] - rope[i][y]) > 1:
                if rope[i][x] > rope[i-1][x]:
                    rope[i-1][x] += 1
                elif rope[i][x] < rope[i-1][x]:
                    rope[i-1][x] -= 1
                if rope[i][y] > rope[i-1][y]:
                    rope[i-1][y] += 1
                elif rope[i][y] < rope[i-1][y]:
                    rope[i-1][y] -= 1
        visited[tuple(rope[tail])] = 1
        moves.popleft()
    return len(visited.keys())

def part2(mydata):
    visited = defaultdict(int)
    moves = deque([])
    x = 0
    y = 1
    rope = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]
    head = len(rope) - 1
    tail = 0
    visited[tuple(rope[tail])] = 1
    for l in mydata.splitlines():
        for c in range(int(l[2:])):
            moves.append(l[0])
    while len(moves) > 0:
        if moves[0] == "R":
            rope[head][x] += 1
        elif moves[0] == "L":
            rope[head][x] -= 1
        elif moves[0] == "U":
            rope[head][y] += 1
        elif moves[0] == "D":
            rope[head][y] -= 1
        else:
            return None
        for i in range(len(rope)-1,0,-1):
            if abs(rope[i-1][x] - rope[i][x]) > 1 or abs(rope[i-1][y] - rope[i][y]) > 1:
                if rope[i][x] > rope[i-1][x]:
                    rope[i-1][x] += 1
                elif rope[i][x] < rope[i-1][x]:
                    rope[i-1][x] -= 1
                if rope[i][y] > rope[i-1][y]:
                    rope[i-1][y] += 1
                elif rope[i][y] < rope[i-1][y]:
                    rope[i-1][y] -= 1
        visited[tuple(rope[tail])] = 1
        moves.popleft()
    return len(visited.keys())


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
