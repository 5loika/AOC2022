#!/bin/python3

import sys
from aocd import data
from aocd import submit
from collections import deque

testdata = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
test1 = 10605
test2 = None

def updateitem(item,oper,n):
    if oper == "plus":
        return item + n
    elif oper == "mult":
        return item * n
    elif oper == "square":
        return item * item   

def part1(mydata):
    monkeys = []
    operations = []
    throw = []

    # TEST INPUT
    # monkeys.append(deque([79, 98]))
    # operations.append(["mult",19])
    # throw.append([23,2,3])
    # monkeys.append(deque([54, 65, 75, 74]))
    # operations.append(["plus",6])
    # throw.append([19,2,0])
    # monkeys.append(deque([79, 60, 97]))
    # operations.append(["square",1])
    # throw.append([13,1,3])
    # monkeys.append(deque([74]))
    # operations.append(["plus",3])
    # throw.append([17,0,1])
    # inspected = [0,0,0,0]
    # END TEST INPUT

    # PUZZLE INPUT
    monkeys.append(deque([97, 81, 57, 57, 91, 61]))
    operations.append(["mult",7])
    throw.append([11,5,6])
    monkeys.append(deque([88, 62, 68, 90]))
    operations.append(["mult",17])
    throw.append([19,4,2])
    monkeys.append(deque([74, 87]))
    operations.append(["plus",2])
    throw.append([5,7,4])
    monkeys.append(deque([53, 81, 60, 87, 90, 99, 75]))
    operations.append(["plus",1])
    throw.append([2,2,1])
    monkeys.append(deque([57]))
    operations.append(["plus",6])
    throw.append([13,7,0])
    monkeys.append(deque([54, 84, 91, 55, 59, 72, 75, 70]))
    operations.append(["square",1])
    throw.append([7,6,3])
    monkeys.append(deque([95, 79, 79, 68, 78]))
    operations.append(["plus",3])
    throw.append([3,1,3])
    monkeys.append(deque([61, 97, 67]))
    operations.append(["plus",4])
    throw.append([17,0,5])
    inspected = [0, 0, 0, 0, 0, 0, 0, 0]
    # END PUZZLE INPUT

    for i in range(20):
        for j in range(len(monkeys)):
            while monkeys[j]:
                item = monkeys[j].popleft()
                inspected[j] += 1
                item = updateitem(item,operations[j][0],operations[j][1])
                item //= 3
                if (item % throw[j][0]) == 0:
                    monkeys[throw[j][1]].append(item)
                else:
                    monkeys[throw[j][2]].append(item)
    inspected.sort()
    return inspected[-1]*inspected[-2]


def part2(mydata):
    monkeys = []
    operations = []
    throw = []

    # TEST INPUT
    # monkeys.append(deque([79, 98]))
    # operations.append(["mult",19])
    # throw.append([23,2,3])
    # monkeys.append(deque([54, 65, 75, 74]))
    # operations.append(["plus",6])
    # throw.append([19,2,0])
    # monkeys.append(deque([79, 60, 97]))
    # operations.append(["square",1])
    # throw.append([13,1,3])
    # monkeys.append(deque([74]))
    # operations.append(["plus",3])
    # throw.append([17,0,1])
    # inspected = [0,0,0,0]

    # PUZZLE INPUT
    monkeys.append(deque([97, 81, 57, 57, 91, 61]))
    operations.append(["mult",7])
    throw.append([11,5,6])
    monkeys.append(deque([88, 62, 68, 90]))
    operations.append(["mult",17])
    throw.append([19,4,2])
    monkeys.append(deque([74, 87]))
    operations.append(["plus",2])
    throw.append([5,7,4])
    monkeys.append(deque([53, 81, 60, 87, 90, 99, 75]))
    operations.append(["plus",1])
    throw.append([2,2,1])
    monkeys.append(deque([57]))
    operations.append(["plus",6])
    throw.append([13,7,0])
    monkeys.append(deque([54, 84, 91, 55, 59, 72, 75, 70]))
    operations.append(["square",1])
    throw.append([7,6,3])
    monkeys.append(deque([95, 79, 79, 68, 78]))
    operations.append(["plus",3])
    throw.append([3,1,3])
    monkeys.append(deque([61, 97, 67]))
    operations.append(["plus",4])
    throw.append([17,0,5])
    inspected = [0, 0, 0, 0, 0, 0, 0, 0]

    throwlcm = 1
    for n in range(len(throw)):
        throwlcm *= throw[n][0]

    for i in range(10000):
        for j in range(len(monkeys)):
            while monkeys[j]:
                item = monkeys[j].popleft()
                inspected[j] += 1
                item = updateitem(item,operations[j][0],operations[j][1])
                if item > throwlcm: item = item % throwlcm
                if (item % throw[j][0]) == 0:
                    monkeys[throw[j][1]].append(item)
                else:
                    monkeys[throw[j][2]].append(item)
    inspected.sort()
    return inspected[-1]*inspected[-2]


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
