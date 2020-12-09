# !/usr/bin/python
import sys
from Sudoku.Generator import *
import json

def generate_soduku(difficulty_str):
    difficulties = {
        'easy': (35, 0), 
        'medium': (81, 5), 
        'hard': (81, 10), 
        'extreme': (81, 15)
    }
    base = "base.txt"
    difficulty = difficulties[difficulty_str]
    gen = Generator(base)
    gen.randomize(100)
    initial = gen.board.copy()
    gen.reduce_via_logical(difficulty[0])
    # catching zero case
    if difficulty[1] != 0:
        # applying random reduction with corresponding difficulty cutoff
        gen.reduce_via_random(difficulty[1])
    final = gen.board.copy()
    return (initial, final)

def generate_soduku_map(difficulty_str):
    initial, final = generate_soduku(difficulty_str)
    data = {}

    answer = ""
    for col in range(0, 9):
        for row in range(0, 9):
            answer += str(initial.rows[col][row].value)
        answer += ","
    answer = answer[:-1]
    data['a'] = answer

    question = ""
    for col in range(0, 9):
        for row in range(0, 9):
            question += str(final.rows[col][row].value)
        question += ","
    question = question[:-1]
    data['q'] = question
    return data

if __name__ == '__main__':
    initial, final = generate_soduku(sys.argv[1])
    # printing out complete board (solution)
    print("The initial board before removals was: \r\n{0}".format(initial))
    # printing out board after reduction
    print("\r\nThe generated board after removals was: \r\n{0}".format(final))
    
    print("\n\nJson format:")
    json_str = json.dumps(generate_soduku_map(sys.argv[1]))
    print(json_str)
    print("")
