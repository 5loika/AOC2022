#!/bin/python3

import sys
from aocd import data
from aocd import submit

testdata = '''A Y
B X
C Z'''
test1 = 15
test2 = 12

def part1(rawdata):
  # WIN  AY =  8 | BZ = 9 | CX = 7  
  # DRAW AX =  4 | BY = 5 | CZ = 6 
  # LOSE AZ =  3 | BX = 1 | CY = 2
  # Build dictionary with all possible results
  scores = {"A X": 4, "A Y": 8, "A Z": 3, 
            "B X": 1, "B Y": 5, "B Z": 9,
            "C X": 7, "C Y": 2, "C Z": 6}
  score = 0
  lines = rawdata.splitlines()
  for line in lines:
    score += scores[line.strip()]
  return(score)

def part2(rawdata):
  # LOSE AX = 3 | BX = 1 | CX = 2  
  # DRAW AY = 4 | BY = 5 | CY = 6 
  # WIN  AZ = 8 | BZ = 9 | CZ = 7
  # Build dictionary with all possible results
  scores = {"A X": 3, "A Y": 4, "A Z": 8, 
            "B X": 1, "B Y": 5, "B Z": 9,
            "C X": 2, "C Y": 6, "C Z": 7}
  score = 0
  lines = rawdata.splitlines()
  for line in lines:
    score += scores[line.strip()]
  return(score)  

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