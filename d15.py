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

def sortDist(i):
    return i[2]


def part1(mydata):
    cave = defaultdict(None)
    lines = mydata.splitlines()
    target = 2000000
    # target = 10
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
    X = R = 0 # x-axis / column
    Y = C = 1 # y-axis / row
    MINRC = 0 # minimum r/c value
    # MAXRC = 21 # maximum r/c value (Test Data)
    MAXRC = 4000001 # maximum r/c value (Puzzle Input)
    RCRANGE = range(MINRC,MAXRC) # range 0..max for checking points
    MULT = 4000000 # frequency multiplier (from puzzle)
    sensors = [] # empty list to hold sensor info
    borders = defaultdict(None) # dict for points +1 outside sensor
    lines = mydata.splitlines() # read input data
    for line in lines: # parse input data
        Sc, Sr, Bc, Br = [int(x) for x in re.findall(r"[-]?\d+", line)]
        sensors.append([Sr,Sc,dist(Sr,Sc,Br,Bc)]) # add sensor to list
    sensors.sort(key=sortDist) # sort from large to small distance
    for s in sensors: # find border points for each sensor
        border = s[2] + 1
        Sr = s[R]
        Sc = s[C]
        for x in range (-border, border): # Maths
            dc = border - abs(x)
            r = Sr - x
            c1 = Sc + dc
            c2 = Sc - dc
            if r in RCRANGE:
                if c1 in RCRANGE and borders.get((r,c1)) == None:
                    borders[(r,c1)] = True
                if c2 in RCRANGE and borders.get((r,c2)) == None:
                    borders[(r,c2)] = True
        deletepoints = [] # will be used to cleanup points later
        for q in borders.keys(): # iterate over border cells
            if borders[q]:
                for t in sensors:
                    if dist(q[R],q[C],t[R],t[C]) <= t[2]: # seen by sensor
                        deletepoints.append(q) # mark to delete
                        break # break loop
        for u in deletepoints: # delete flagged points
            del borders[u]
        if len(borders) == 1: # if we have only 1 point it is solution
            for p in borders: # loop to show progress during long run
                print(p[R],p[C],p[Y]*MULT+p[X])
                return(p[Y]*MULT+p[X])
    for p in borders: # should have 1 point remaining
        if borders[p]:
            return(p[Y]*MULT+p[X]) # return frequency for point
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
