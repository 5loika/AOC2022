#!/bin/python3

import sys
from aocd import data
from aocd import submit

testdata = '''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''
test1 = 11
test2 = 26

def part1(mydata):
  uniq = 4
  for i in range(uniq,len(mydata)):
    if len(set(mydata[i-uniq:i])) == uniq:
      return(i)
  return(None)

def part2(mydata):
  uniq = 14
  for i in range(uniq,len(mydata)):
    if len(set(mydata[i-uniq:i])) == uniq:
      return(i)
  return(None)    

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