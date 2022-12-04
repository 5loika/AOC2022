#!/bin/python3

import sys
from aocd import data
from aocd import submit
from itertools import zip_longest

testdata = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
test1 = 157
test2 = 70

# found with google search...
def grouper(iterable_obj, count, fillvalue=None):
    args = [iter(iterable_obj)] * count
    return zip_longest(*args, fillvalue=fillvalue)
 
def part1(mydata):
  total = 0
  lines = mydata.splitlines()
  for line in lines:
    l = list(set(line[:len(line)//2]) & set(line[-len(line)//2:]))
    v = ord(l[0])
    if v > 96:
      total += v - 96
    else:
      total += v - 38
  return(total)

def part2(mydata):
  total = 0
  lines = mydata.splitlines()
  for line in grouper(lines, 3, ""):
    l = list(set(line[0]) & set(line[1]) & set(line[2]))
    v = ord(l[0])
    if v > 96:
      total += v - 96
    else:
      total += v - 38
  return(total)

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