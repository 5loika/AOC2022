#!/bin/python3

import sys
from aocd import data
from aocd import submit


testdata = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
test1 = 13140
test2 = None


def part1(mydata):
    pc = 1
    x = 1
    signals = []
    checkcycle = 20
    for l in mydata.splitlines():
        op = l[0:4]
        if op == 'noop':
            pc += 1
            if pc >= checkcycle:
                signals.append(pc*x)
                checkcycle += 40
        elif op == 'addx':
            v = int(l[4:])
            pc += 1
            if pc >= checkcycle:
                signals.append(pc*x)
                checkcycle += 40
            pc += 1
            x += v
            if pc >= checkcycle:
                signals.append(pc*x)
                checkcycle += 40
    return(sum(signals))

def part2(mydata):
    pc = 0
    x = 1
    display = ''
    for l in mydata.splitlines():
        sprite = range(x-1,x+2)
        op = l[0:4]
        if op == 'noop':
            if (pc%40) in sprite:
                display += '#'
            else:
                display += ' '
            pc += 1
        elif op == 'addx':
            v = int(l[4:])
            if (pc%40) in sprite:
                display += '#'
            else:
                display += ' '
            pc += 1
            if (pc%40) in sprite:
                display += '#'
            else:
                display += ' '
            pc += 1
            x += v
    for i in range(0,240,40):
        print(display[i:i+40])
    return(None)


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
