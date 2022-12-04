import sys
from aocd import data
from aocd import submit
import re
import pandas as pd

testdata = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
test1 = 2
test2 = 4

def part1(mydata):
  count = 0
  lines = mydata.splitlines()
  for line in lines:
    # use re-findall to extract numbers from line
    a1,a2,b1,b2 = [int(x) for x in re.findall(r'\d+', line)]
    # use pandas Interval to represent each range
    a = pd.Interval(a1,a2,closed="both")
    b = pd.Interval(b1,b2,closed="both")
    # check if either Interval is fully contained by the other
    if a in b or b in a:
      count += 1
  return(count)

def part2(mydata):
  count = 0
  lines = mydata.splitlines()
  for line in lines:
    # use re-findall to extract numbers from line
    a1,a2,b1,b2 = [int(x) for x in re.findall(r'\d+', line)]
    # use pandas Interval to represent each range
    a = pd.Interval(a1,a2,closed="both")
    b = pd.Interval(b1,b2,closed="both")
    # check if the intervals overlap
    if a.overlaps(b):
      count += 1
  return(count)
  
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
        submit(part1(data))
      if sys.argv[2] =='b':
        submit(part2(data))   
  else:
    print('Part 1: ',part1(data))
    print('Part 2: ',part2(data))