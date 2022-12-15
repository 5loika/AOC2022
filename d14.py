#!/bin/python3

import sys
from aocd import data
from aocd import submit
from collections import defaultdict

testdata = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
test1 = 24
test2 = 93


def part1(mydata):
    cavemap = defaultdict(None)
    picture = []
    max_row = 0
    max_col = 0
    for l in mydata.splitlines():
        l = l.replace("-", "").replace(">", "").replace("  ", " ")
        segment = []
        for point in l.split(" "):
            c, r = [int(x) for x in point.split(",")]
            max_row = max(r, max_row)
            max_col = max(c, max_col)
            segment.append([r, c])
        picture.append(segment)
    for i in picture:
        for j in range(len(i) - 1):
            r1, c1 = i[j]
            r2, c2 = i[j+1]
            if c1 == c2:  # Same Column
                for r in range(min(r1,r2),max(r1,r2)+1):
                    cavemap[(r, c1)] = "#"
            elif r1 == r2: # Same Row
                for c in range(min(c1,c2),max(c1,c2)+1):
                    cavemap[(r1, c)] = "#"
            else:
                return "Parsing failed"
    running = True
    count = 0
    while running:
        falling = True
        snowflake = [0, 500]
        while falling:
            if snowflake[0] > max_row:
                running = False
                falling = False
            elif cavemap.get((snowflake[0]+1,snowflake[1])) == None:
                snowflake = [snowflake[0]+1,snowflake[1]]
            elif cavemap.get((snowflake[0]+1,snowflake[1]-1)) == None:
                snowflake = [snowflake[0]+1,snowflake[1]-1]
            elif cavemap.get((snowflake[0]+1,snowflake[1]+1)) == None:
                snowflake = [snowflake[0]+1,snowflake[1]+1]
            else:
                cavemap[(snowflake[0],snowflake[1])] = '*'
                count += 1
                falling = False
    return(count)


def part2(mydata):
    cavemap = defaultdict(None)
    picture = []
    max_row = 0
    max_col = 0
    for l in mydata.splitlines():
        l = l.replace("-", "").replace(">", "").replace("  ", " ")
        segment = []
        for point in l.split(" "):
            c, r = [int(x) for x in point.split(",")]
            max_row = max(r, max_row)
            max_col = max(c, max_col)
            segment.append([r, c])
        picture.append(segment)
    for i in picture:
        for j in range(len(i) - 1):
            r1, c1 = i[j]
            r2, c2 = i[j+1]
            if c1 == c2:  # Same Column
                for r in range(min(r1,r2),max(r1,r2)+1):
                    cavemap[(r, c1)] = "#"
            elif r1 == r2: # Same Row
                for c in range(min(c1,c2),max(c1,c2)+1):
                    cavemap[(r1, c)] = "#"
            else:
                return("Parsing failed")
    count = 0
    running = True
    while running:
        falling = True
        snowflake = [0, 500]
        while falling:
            if snowflake[0] > max_row:
                cavemap[(snowflake[0],snowflake[1])] = '*'
                count += 1
                falling = False
            elif cavemap.get((snowflake[0]+1,snowflake[1])) == None:
                snowflake = [snowflake[0]+1,snowflake[1]]
            elif cavemap.get((snowflake[0]+1,snowflake[1]-1)) == None:
                snowflake = [snowflake[0]+1,snowflake[1]-1]
            elif cavemap.get((snowflake[0]+1,snowflake[1]+1)) == None:
                snowflake = [snowflake[0]+1,snowflake[1]+1]
            else:
                cavemap[(snowflake[0],snowflake[1])] = '*'
                count += 1
                falling = False
                if snowflake == [0, 500]:
                    running = False
    return(count)


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
