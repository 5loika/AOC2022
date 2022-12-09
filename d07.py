#!/bin/python3

import sys
from aocd import data
from aocd import submit

testdata = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
test1 = 95437
test2 = 24933642


def part1(mydata):
    dirtree = {}
    dirsize = {}
    worksize = 0
    workpath = ""
    maxdepth = 0
    depth = 0
    listing = False
    lines = mydata.splitlines()
    lines.append("$ cd /")
    for l in lines:
        words = l.split(" ")
        if words[0] == "$":
            if listing:
                listing = False
                dirsize[workpath] = worksize
                worksize = 0
            if words[1] == "cd":
                if words[2] == "/":
                    workpath = "/"
                elif words[2] == "..":
                    elements = workpath.split("/")
                    elements = elements[1:-1]
                    workpath = ""
                    for w in elements:
                        workpath = workpath + "/" + w
                    depth -= 1
                else:
                    if workpath == "/":
                        workpath = workpath + words[2]
                    else:
                        workpath = workpath + "/" + words[2]
                    depth += 1
                    if depth > maxdepth:
                        maxdepth = depth
            elif words[1] == "ls":
                listing = True
            else:
                print("Error:", words)
        else:
            if words[0] == "dir":
                NotImplemented
            else:
                worksize += int(words[0])
    for n in range(maxdepth - 1, 0, -1):
        for k in dirsize.keys():
            if k.count("/") == n:
                for l in dirsize.keys():
                    if l != k:
                        if l.find(k) == 0:
                            dirsize[k] = dirsize[k] + dirsize[l]
    result = 0
    for d in dirsize.values():
        if d <= 100000:
            result += d
    return result


def part2(mydata):
    dirtree = {}
    dirsize = {}
    worksize = 0
    workpath = ""
    maxdepth = 0
    depth = 0
    listing = False
    lines = mydata.splitlines()
    lines.append("$ cd /")
    for l in lines:
        words = l.split(" ")
        if words[0] == "$":
            if listing:
                listing = False
                dirsize[workpath] = worksize
                worksize = 0
            if words[1] == "cd":
                if words[2] == "/":
                    workpath = "/"
                elif words[2] == "..":
                    elements = workpath.split("/")
                    elements = elements[1:-1]
                    workpath = ""
                    for w in elements:
                        workpath = workpath + "/" + w
                    depth -= 1
                else:
                    if workpath == "/":
                        workpath = workpath + words[2]
                    else:
                        workpath = workpath + "/" + words[2]
                    depth += 1
                    if depth > maxdepth:
                        maxdepth = depth
            elif words[1] == "ls":
                listing = True
            else:
                print("Error:", words)
        else:
            if words[0] == "dir":
                NotImplemented
            else:
                worksize += int(words[0])
    for n in range(maxdepth - 1):
        for k in dirsize.keys():
            if k.count("/") == n:
                for l in dirsize.keys():
                    if l != k:
                        if l.find(k) == 0:
                            dirsize[k] = dirsize[k] + dirsize[l]
    maxspace = 70000000
    freespace = maxspace - dirsize["/"]
    needspace = 30000000 - freespace
    candidates = []
    for i in dirsize.keys():
        if dirsize[i] > needspace:
            candidates.append(dirsize[i])
    return min(candidates)


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
