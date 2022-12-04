import sys
from aocd import data
from aocd import submit

def part1(mydata):
  lines = mydata.splitlines()
  for line in lines:
    NotImplemented  
  return(None)

def part2(mydata):
  lines = mydata.splitlines()
  for line in lines:
    NotImplemented  
  return(None)
    
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