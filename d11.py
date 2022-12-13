#!/bin/python3

import sys
from aocd import data
from aocd import submit
from collections import deque
import re

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
test2 = 2713310158

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
    inspected = []
    monkeylist = mydata.split("\n\n")
    for m in monkeylist:
        testdiv = 0
        iftrue = 0
        iffalse = 0
        for n in m.split("\n"):
            if n.find("Starting items:") > 0:
                monkeys.append(deque(([int(x) for x in re.findall("\d+", n)])))
            elif n.find("Operation:") > 0:
                if n.find("*") > 0:
                    if n.find("old * old") > 0:
                        operations.append(["square",1])
                    else:
                        l = re.findall("\d+",n)
                        operations.append(["mult",int(l[0])])
                elif n.find("+") > 0:
                    l = re.findall("\d+",n)
                    operations.append(["plus",int(l[0])])
            elif n.find("Test:") > 0:
                l = re.findall("\d+",n)
                testdiv = int(l[0])
            elif n.find("true:") > 0:
                l = re.findall("\d+",n)
                iftrue = int(l[0])
            elif n.find("false:") > 0:
                l = re.findall("\d+",n)
                iffalse = int(l[0])
                throw.append([testdiv,iftrue,iffalse])
        inspected.append(0)        

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
    inspected = []
    monkeylist = mydata.split("\n\n")
    for m in monkeylist:
        testdiv = 0
        iftrue = 0
        iffalse = 0
        for n in m.split("\n"):
            if n.find("Starting items:") > 0:
                monkeys.append(deque(([int(x) for x in re.findall("\d+", n)])))
            elif n.find("Operation:") > 0:
                if n.find("*") > 0:
                    if n.find("old * old") > 0:
                        operations.append(["square",1])
                    else:
                        l = re.findall("\d+",n)
                        operations.append(["mult",int(l[0])])
                elif n.find("+") > 0:
                    l = re.findall("\d+",n)
                    operations.append(["plus",int(l[0])])
            elif n.find("Test:") > 0:
                l = re.findall("\d+",n)
                testdiv = int(l[0])
            elif n.find("true:") > 0:
                l = re.findall("\d+",n)
                iftrue = int(l[0])
            elif n.find("false:") > 0:
                l = re.findall("\d+",n)
                iffalse = int(l[0])
                throw.append([testdiv,iftrue,iffalse])
        inspected.append(0)         


    throwlcm = 1 # Calculate LCM of test divisors to reduce worry
    for n in range(len(throw)):
        throwlcm *= throw[n][0]

    for i in range(10000):
        for j in range(len(monkeys)):
            while monkeys[j]:
                item = monkeys[j].popleft()
                inspected[j] += 1
                item = updateitem(item,operations[j][0],operations[j][1])
                item = item % throwlcm
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
