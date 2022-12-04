import sys
from aocd import data
from aocd import submit
def part1(rawdata):
  # A = Rock(1), B = Paper(2), C = Scissor(3)
  # X = Rock(1), Y = Paper(2), Z = Scissor(3)
  # Win = +6, Draw = +3, Lose = + 0 
  # WIN  AY =  8 | BZ = 9 | CX = 7  
  # DRAW AX =  4 | BY = 5 | CZ = 6 
  # LOSE AZ =  3 | BX = 1 | CY = 2
  score = 0
  lines = rawdata.splitlines()
  for line in lines:
    elf = line[0]
    me = line[2]
    if elf == 'A' and me == 'X': score += 4
    if elf == 'A' and me == 'Y': score += 8
    if elf == 'A' and me == 'Z': score += 3
    if elf == 'B' and me == 'X': score += 1
    if elf == 'B' and me == 'Y': score += 5
    if elf == 'B' and me == 'Z': score += 9
    if elf == 'C' and me == 'X': score += 7
    if elf == 'C' and me == 'Y': score += 2
    if elf == 'C' and me == 'Z': score += 6
  return(score)

def part2(rawdata):
  # A = Rock, B = Paper, C = Scissor
  # X = Win(+6), Y = Draw(+3), Z = Lose(+0)
  # Rock = 1, Paper = 2, Scissor = 3 
  # LOSE AX = 3 | BX = 1 | CX = 2  
  # DRAW AY = 4 | BY = 5 | CY = 6 
  # WIN  AZ = 8 | BZ = 9 | CZ = 7
  score = 0
  lines = rawdata.splitlines()
  for line in lines:
    elf = line[0]
    me = line[2]
    if elf == 'A' and me == 'X': score += 3
    if elf == 'A' and me == 'Y': score += 4
    if elf == 'A' and me == 'Z': score += 8
    if elf == 'B' and me == 'X': score += 1
    if elf == 'B' and me == 'Y': score += 5
    if elf == 'B' and me == 'Z': score += 9
    if elf == 'C' and me == 'X': score += 2
    if elf == 'C' and me == 'Y': score += 6
    if elf == 'C' and me == 'Z': score += 7
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