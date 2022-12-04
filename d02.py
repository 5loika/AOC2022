import sys
from aocd import data
from aocd import submit

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