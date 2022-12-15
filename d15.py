#!/bin/python3

import sys
from aocd import data
from aocd import submit
import re
from collections import defaultdict

testdata = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
test1 = 26
test2 = 56000011


def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def part1(mydata):
    cave = defaultdict(None)
    lines = mydata.splitlines()
    # target = 2000000
    target = 10
    count = 0
    for line in lines:
        Sc, Sr, Bc, Br = [int(x) for x in re.findall(r"[-]?\d+", line)]
        cave[(Sr,Sc)] = 'S'
        cave[(Br,Bc)] = 'B'
        distance = dist(Sr, Sc, Br, Bc)
        if target in range(Sr-distance,Sr+distance+1):
            tr = target
            for tc in range(Sc-distance,Sc+distance+1):
                if dist(Sr, Sc, tr, tc) <= distance:
                    if cave.get((tr,tc)) == None:
                        cave[(tr, tc)] = '#'
                        count += 1
    return count

def part2(mydata):
    minr = 0
    # maxr = 21
    maxr = 4000001
    minc = 0
    # maxc = 21
    maxc = 4000001
    mult = 4000000
    sensors = []
    lines = mydata.splitlines()
    for line in lines:
        Sc, Sr, Bc, Br = [int(x) for x in re.findall(r"[-]?\d+", line)]
        distance = dist(Sr, Sc, Br, Bc)
        sensors.append([Sr, Sc, distance])
    for r in range(minr, maxr):
        if r % 1000 == 0:
            print('.',end='')
        for c in range(minc, maxc):
            for s in sensors:
                if dist(r,c,s[0],s[1]) <= s[2]:
                    break
            else:
                return(c*mult+r)


def part3(mydata):
    minr = 0
    maxr = 21
    # maxr = 4000001
    minc = 0
    maxc = 21
    # maxc = 4000001
    mult = 4000000
    cave = defaultdict(None)
    lines = mydata.splitlines()
    count = 0
    for line in lines:
        Sc, Sr, Bc, Br = [int(x) for x in re.findall(r"[-]?\d+", line)]
        cave[(Sr,Sc)] = 'S'
        cave[(Br,Bc)] = 'B'
        distance = dist(Sr, Sc, Br, Bc)
        top = max(Sr - distance,minr)
        bottom = min(Sr + distance,maxr)
        left = max(Sc - distance, minc)
        right = min(Sc + distance, maxc)
        for tr in range(top, bottom):
            for tc in range(left,right):
                if dist(Sr, Sc, tr, tc) <= distance:
                    if cave.get((tr,tc)) == None:
                        cave[(tr, tc)] = '#'
    for r in range(minr, maxr):
        for c in range(minc, maxc):
            if cave.get((r,c)) == None:
                return(c*mult+r)

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
