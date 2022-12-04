#!/bin/python3

import sys
from aocd import data
from aocd import submit
import re

testdata = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
test1 = 24000
test2 = 45000

def part1(rawdata):
  calories = []
  backpacks = rawdata.split('\n\n')
  for p in backpacks:
    calories.append(sum([int(x) for x in re.findall(r'\d+', p)]))
  return(max(calories))

def part2(rawdata):
  calories = []
  backpacks = rawdata.split('\n\n')
  for p in backpacks:
    calories.append(sum([int(x) for x in re.findall(r'\d+', p)]))
  calories.sort()
  return(sum(calories[-3:]))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
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
    elif sys.argv[1] == 'submit':
      if sys.argv[2] == 'a':
        submit(part1(data), part='a')
      elif sys.argv[2] =='b':
        submit(part2(data), part='b') 
    elif sys.argv[1] == 'run':
      if sys.argv[2] == 'a':
        print('Part 1: ',part1(data))
      elif sys.argv[2] =='b':
        print('Part 2: ',part2(data))  
  else:
    print('Part 1: ',part1(data))
    print('Part 2: ',part2(data))