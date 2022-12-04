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
  if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
      with open(__file__.replace('.py','_test.txt'), "r") as f:
        testinput = f.read()
      print('Test 1: ', part1(testinput))
      print('Test 2: ', part2(testinput))
    elif sys.argv[1] == 'submit':
      if sys.argv[2] == 'a':
        submit(part1(data))
      if sys.argv[2] =='b':
        submit(part2(data))   
  else:
    print('Part 1: ',part1(data))
    print('Part 2: ',part2(data))