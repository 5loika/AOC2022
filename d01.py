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

10000'''
test1 = 24000
test2 = 45000

def part1(rawdata):
  calories = []
  total = 0
  line = rawdata.splitlines()
  for i in line:
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
  line = rawdata.splitlines()
  for i in line:
    if i == '': 
      calories.append(total)
      total = 0
    else:
      total += int(i)
  calories.sort(reverse=True)
  return(calories[0]+calories[1]+calories[2])
if __name__ == "__main__":
  expect1 = None
  expect2 = None
  if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
      if test1 == part1(testdata):
        print('Test 1 - passsed:', test1)
      else:
        print('Test 1 - failed:',part1(testdata))
      test2 = part2(testdata)
      if test2 == part2(testdata):
        print('Test 2 - passed:', test2)
      else:
        print('Test 2 - failed:', part2(testdata))
    elif sys.argv[1] == 'submit':
      if sys.argv[2] == 'a':
        submit(part1(data))
      if sys.argv[2] =='b':
        submit(part2(data))   
  else:
    print('Part 1: ',part1(data))
    print('Part 2: ',part2(data))