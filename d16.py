#!/bin/python3

import sys
from aocd import data
from aocd import submit
import networkx as nx
import re
import math
from itertools import permutations
from functools import lru_cache

testdata = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


test1 = 1651
test2 = None


def part1(mydata):
    valves = []
    flowrates = {}
    G = nx.Graph()
    H = nx.DiGraph()
    H.add_node("AA", rate=0)
    lines = mydata.splitlines()
    for line in lines:
        d = line.split(" ", 9)
        srcnode = d[1]
        for destnode in d[9].split(","):
            G.add_edge(srcnode, destnode.strip())
        rate = int(re.findall(r"\d+", d[4])[0])
        if rate > 0:
            # valves.append(srcnode)
            H.add_node(srcnode,rate=rate)
            flowrates[srcnode] = rate
    valvesweight = []
    for m in H.nodes():
        for n in H.nodes():
            if m == 'AA' and n != 'AA':
                valvesweight.append([n,nx.shortest_path_length(G,m,n)])
            if m != n and n != 'AA':
                H.add_edge(m, n, weight=nx.shortest_path_length(G, m, n))
    valvesweight = sorted(valvesweight,key=lambda x:x[1])
    valves = [c[0] for c in valvesweight]
    print(valves)
    print(list(H.nodes(data=True)))
    print(list(H.edges(data=True)))
    rates = dict(H.nodes(data="rate", default=0))
    print(rates)
    maxflow = 0
    for p in permutations(valves):
        # Initialize
        currentflow = 0
        totalflow = 0
        # Move from AA to first valve
        minute = H['AA'][p[0]]["weight"]
        # Loop through valve path
        for i in range(len(p)):
            # Open current Valve:
            totalflow += currentflow
            minute += 1
            currentflow += rates[p[i]]
            if i+1 == len(p):
                break
            dist = H[p[i]][p[i+1]]["weight"]
            if (minute + dist > 30):
                break
            # Move to next Valve
            totalflow += currentflow * dist
            minute += dist
        while minute < 30: 
            totalflow += currentflow
            minute += 1           
        if totalflow > maxflow:
            maxflow = max(maxflow, totalflow)
            print(maxflow)
    return maxflow

def part2(mydata):
    valves = []
    flowrates = {}
    G = nx.Graph()
    lines = mydata.splitlines()
    for line in lines:
        d = line.split(" ", 9)
        srcnode = d[1]
        for destnode in d[9].split(","):
            G.add_edge(srcnode, destnode.strip())
        rate = int(re.findall(r"\d+", d[4])[0])
        if rate > 0:
            valves.append(srcnode)
            flowrates[srcnode] = rate
    return None

def partX(mydata):
    valves = []
    flowrates = {}
    G = nx.Graph()
    H = nx.DiGraph()
    H.add_node("AA", flow=None, rate=0)
    lines = mydata.splitlines()
    for line in lines:
        d = line.split(" ", 9)
        srcnode = d[1]
        for destnode in d[9].split(","):
            G.add_edge(srcnode, destnode.strip())
        rate = int(re.findall(r"\d+", d[4])[0])
        if rate > 0:
            valves.append(srcnode)
            H.add_node(srcnode, flow="off", rate=rate)
            flowrates[srcnode] = rate
    for m in H.nodes():
        for n in H.nodes():
            if m != n and n != 'AA':
                H.add_edge(m, n, weight=nx.shortest_path_length(G, m, n))
    print(nx.nodes(H))
    # for k in nx.edges(H):
    #     print(k,H[k[0]][k[1]]['weight'])
    maxflow = 0
    for p in permutations(valves):
        q = [i for i in p]
        thispath = nx.shortest_path(G, source="AA", target=p[0])
        for _ in range(len(p) - 1):
            for n in nx.shortest_path(G, p[_], p[_ + 1])[1:]:
                thispath.append(n)
        step = 0
        currentflow = 0
        totalflow = 0
        for node in thispath:
            if node == q[0]:
                totalflow += currentflow
                step += 1
                if step >= 30:
                    break
                totalflow += currentflow
                currentflow += flowrates[node]
                step += 1
                del q[0]
            else:
                totalflow += currentflow
                step += 1
            if step >= 30:
                break
        while step <= 30:
            step += 1
            totalflow += currentflow
        if totalflow > maxflow:
            maxflow = max(maxflow, totalflow)
            print(maxflow)
    return maxflow

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
