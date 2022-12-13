#!/bin/python3

import sys
from aocd import data
from aocd import submit
import networkx as nx

testdata = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''
test1 = 31
test2 = 29

import networkx as nx

def part1(mydata):
    # letters in input: S - Start point and E - Endpoint
    letters = "SabcdefghijklmnopqrstuvwxyzE"
    heightmap = []

    # read input data to list
    for l in mydata.splitlines():
        heightmap.append([letters.index(c) for c in l])

    # save max rows/cols
    rows = len(heightmap)
    cols = len(heightmap[0])

    # find origin and destination
    for row in range(rows):
        for col in range(cols):
            if heightmap[row][col] == 0:
                origin = (row*cols)+col
                heightmap[row][col] = 1
            elif heightmap[row][col] == 27:
                dest = (row*cols)+col
                heightmap[row][col] = 26

    # create directed graph
    G = nx.DiGraph()
    for row in range(rows):
        for col in range(cols):
            node = (row*cols)+col
            nodelevel = heightmap[row][col]
            reachable = range(1,nodelevel+2)
            if col > 0: # left
                left = node - 1
                if heightmap[row][col-1] in reachable:
                    G.add_edge(node,left)
            if col < cols - 1: # right
                right = node + 1
                if heightmap[row][col+1] in reachable:
                    G.add_edge(node,right)
            if row > 0: # above
                above = node - cols
                if heightmap[row-1][col] in reachable:
                    G.add_edge(node,above)
            if row < rows -1 : # below
                below = node + cols
                if heightmap[row+1][col] in reachable:
                    G.add_edge(node,below)  


    shortpath = nx.shortest_path(G,origin,dest)
    outmap = []
    for l in mydata.splitlines():
        outmap.append([c for c in l])
    for r in range(rows):
        for c in range(cols):
            printnode = (r*cols) + c
            if printnode in shortpath:
                print("\033[92m{}\033[00m" .format(outmap[r][c]), end='')
            else:
                print(outmap[r][c],end='')
        print()
    # return shortest path
    return(nx.shortest_path_length(G,origin,dest))

def part2(mydata):
    # letters in input: S is starting point and E is end point
    letters = "SabcdefghijklmnopqrstuvwxyzE"
    heightmap = []

    # read input to list
    for l in mydata.splitlines():
        heightmap.append([letters.index(c) for c in l])

    # save max rows/cols
    rows = len(heightmap)
    cols = len(heightmap[0])
    origins = []

    # find origins and destination
    for row in range(rows):
        for col in range(cols):
            if heightmap[row][col] == 0:
                origins.append((row*cols)+col)
                heightmap[row][col] = 1
            elif heightmap[row][col] == 27:
                dest = (row*cols)+col
                heightmap[row][col] = 26
            elif heightmap[row][col] == 1:
                origins.append((row*cols)+col)

    # create directed graph of edges
    G = nx.DiGraph()
    for row in range(rows):
        for col in range(cols):
            node = (row*cols)+col
            nodelevel = heightmap[row][col]
            reachable = range(1,nodelevel+2)
            if col > 0: # Left
                left = node - 1
                if heightmap[row][col-1] in reachable:
                    G.add_edge(node,left)
            if col < cols - 1: # Right
                right = node + 1
                if heightmap[row][col+1] in reachable:
                    G.add_edge(node,right)
            if row > 0: # Above
                above = node - cols
                if heightmap[row-1][col] in reachable:
                    G.add_edge(node,above)
            if row < rows -1 : # Below
                below = node + cols
                if heightmap[row+1][col] in reachable:
                    G.add_edge(node,below)  
    
    # Find allpaths from any 'a' to 'E'    
    allpaths = []
    for a in origins:
        if nx.has_path(G,a,dest):
            l = nx.shortest_path_length(G,a,dest)
            allpaths.append(l)
            if l <= min(allpaths):
                shortstart = a
    
    shortpath = nx.shortest_path(G,shortstart,dest)
    outmap = []
    for l in mydata.splitlines():
        outmap.append([c for c in l])
    for r in range(rows):
        for c in range(cols):
            printnode = (r*cols) + c
            if printnode in shortpath:
                print("\033[92m{}\033[00m" .format(outmap[r][c]), end='')
            else:
                print(outmap[r][c],end='')
        print()
            
    # return shortest path
    return(min(allpaths))
    
if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1] == 'submit':
      if sys.argv[2] == 'a':
        submit(part1(data), part='a')
      elif sys.argv[2] =='b':
        submit(part2(data), part='b')
      else:
        print('Specify a or b') 
    elif sys.argv[1] == 'run':
      if sys.argv[2] == 'a':
        print('Part 1: ',part1(data))
      elif sys.argv[2] =='b':
        print('Part 2: ',part2(data))
      else:
        print('Part 1: ',part1(data))
        print('Part 2: ',part2(data))
    elif sys.argv[1] == 'test':
      result1 = part1(testdata)
      if test1 == result1:
        print('Test 1 - Pass:', result1)
      else:
        print('Test 1 - Fail:', result1)
      result2 = part2(testdata)
      if test2 == result2:
        print('Test 2 - Pass:', result2)
      else:
        print('Test 2 - Fail:', result2)
  else:
    print('Part 1: ',part1(data))
    print('Part 2: ',part2(data))