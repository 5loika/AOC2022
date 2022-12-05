#!/bin/python3

import sys
from aocd import data
from aocd import submit
import re

testdata = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
test1 = 'CMZ'
test2 = 'MCD'

def part1(mydata):
  #stacks = [['Z','N'],['M','C','D'],['P']]
  stacks = [['N','C','R','T','M','Z','P'],['D','N','T','S','B','Z'],['M','H','Q','R','F','C','T','G'],['G','R','Z'],['Z','N','R','H'],['F','H','S','W','P','Z','L','D'],['W','D','Z','R','C','G','M'],['S','J','F','L','H','W','Z','Q'],['S','Q','P','W','N']]
  indata = mydata.split('\n\n')
  lines = indata[1].splitlines()
  for line in lines:
    count,src,dst = [int(x) for x in re.findall(r'\d+', line)]
    for i in range(count):
      stacks[dst-1].append(stacks[src-1].pop())
  tops = ''
  for i in range(9):
    tops += stacks[i][-1]
  return(tops)

def part2(mydata):
  #stacks = [['Z','N'],['M','C','D'],['P']]
  stacks = [['N','C','R','T','M','Z','P'],['D','N','T','S','B','Z'],['M','H','Q','R','F','C','T','G'],['G','R','Z'],['Z','N','R','H'],['F','H','S','W','P','Z','L','D'],['W','D','Z','R','C','G','M'],['S','J','F','L','H','W','Z','Q'],['S','Q','P','W','N']]
  tmp = []
  indata = mydata.split('\n\n')
  lines = indata[1].splitlines()
  for line in lines:
    count,src,dst = [int(x) for x in re.findall(r'\d+', line)]
    for i in range(count):
      tmp.append(stacks[src-1].pop())
    for j in range(count):
      stacks[dst-1].append(tmp.pop())
  tops = ''
  for i in range(9):
    tops += stacks[i][-1]
  return(tops)
    
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