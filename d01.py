#!/bin/python3

import sys
from aocd import data
from aocd import submit

testdata = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

'''
test1 = 24000
test2 = 45000

def part1(rawdata):
  calories = []
  total = 0
  lines = rawdata.splitlines()
  for i in lines:
    if i == '': 
      calories.append(total)
      total = 0
    else:
      total += int(i)
  calories.sort(reverse=True)
  return(calories[0])
def part2(rawdata):
  total = 0
  calories = []
  lines = rawdata.splitlines()
  for i in lines:
    if i == '': 
      calories.append(total)
      total = 0
    else:
      total += int(i)
  return(sum(calories[-3:]))
if __name__ == "__main__":
  expect1 = None
  expect2 = None
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
  else:
    print('Part 1: ',part1(data))
    print('Part 2: ',part2(data))