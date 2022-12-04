import sys
from aocd import data
from aocd import submit

def part1(mydata):
  count = 0
  lines = mydata.splitlines()
  for line in lines:
    a,b = line.split(',')
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    if int(a1) <= int(b1) and int(a2) >= int(b2):
      # b is contained in a
      count += 1
    elif int(b1) <= int(a1) and int(b2) >= int(a2):
      # a is contained in b
      count += 1
  return(count)

def part2(mydata):
  count = 0
  lines = mydata.splitlines()
  for line in lines:
    a,b = line.split(',')
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    if int(a1) <= int(b1) and int(b1) <= int(a2):
      # b starts in a
      count += 1
    elif int(b1) <= int(a1) and int(a1) <= int(b2):
      # a starts in b
      count += 1
    elif int(a2) >= int(b1) and int(a2) <= int(b2):
      # a ends in b
      count += 1
    elif int(b2) >= int(a1) and int(b2) <= int(a2):
      # b ends in a
      count+= 1
  return(count)
  
if __name__ == "__main__":
  expect1 = None
  expect2 = None
  if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
      with open(__file__.replace('.py','_test.txt'), "r") as f:
        test = f.read()
      if len(sys.argv) > 2:
        expect1 = sys.argv[2]
      if len(sys.argv) > 3:
        expect2 = sys.argv[3]
      test1 = part1(test)
      print('Test 1 - Expected: ',expect1,'\tReturned: ', test1)
      test2 = part2(test)
      print('Test 2 - Expected: ',expect2,'\tReturned: ', test2)
    elif sys.argv[1] == 'submit':
      if sys.argv[2] == 'a':
        submit(part1(data))
      if sys.argv[2] =='b':
        submit(part2(data))   
  else:
    print('Part 1: ',part1(data))
    print('Part 2: ',part2(data))