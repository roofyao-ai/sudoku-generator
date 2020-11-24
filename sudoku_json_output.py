# !/usr/bin/python
import sys
from Sudoku.Generator import *

# setting difficulties and their cutoffs for each solve method
difficulties = {
    'easy': (35, 0), 
    'medium': (81, 5), 
    'hard': (81, 10), 
    'extreme': (81, 15)
}

# getting desired difficulty from command line
difficulty = difficulties[sys.argv[1]]

# constructing generator object from puzzle file (space delimited columns, line delimited rows)
gen = Generator("base.txt")

# applying 100 random transformations to puzzle
gen.randomize(100)

# getting a copy before slots are removed
initial = gen.board.copy()

# applying logical reduction with corresponding difficulty cutoff
gen.reduce_via_logical(difficulty[0])

# catching zero case
if difficulty[1] != 0:
    # applying random reduction with corresponding difficulty cutoff
    gen.reduce_via_random(difficulty[1])


# getting copy after reductions are completed
final = gen.board.copy()

answer = ""
for col in xrange(0, 9):
    for row in xrange(0, 9):
        answer += str(initial.rows[col][row].value)
    answer += ","
answer = answer[:-1]

question = ""
for col in xrange(0, 9):
    for row in xrange(0, 9):
        question += str(final.rows[col][row].value)
    question += ","
question = question[:-1]
print(question)