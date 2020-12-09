# coding=utf-8
import os
import sys
from time import strptime
from Sudoku.Generator import *
from sudoku_generator import *
import json
from  datetime import *

input_dir = os.getcwd()

forward_years = 10
begin = datetime.now()
begin = datetime(begin.year, begin.month, 15, begin.hour, begin.minute, begin.second, begin.microsecond)
last = datetime(begin.year+forward_years, begin.month, begin.day, begin.hour, begin.minute, begin.second, begin.microsecond)

def same_day(tm1, tm2):
    return tm1.year == tm2.year and tm1.month == tm2.month and tm1.day == tm2.day

key_set = set()

# 生成easy数据
log_file_path = os.path.join(input_dir, "log.txt")
log_file = open(log_file_path, "a")

difficulties = ["easy", "medium", "hard"]
for difficulty in difficulties:
    print(difficulty)
    data = {}
    file_path = os.path.join(input_dir, difficulty+".json")
    output_file = open(file_path, 'w')
    loop_date = begin
    while True:
        question = generate_soduku_map(difficulty)
        key = question['q']
        if key in key_set:
            continue
        loop_date += timedelta(days=1)
        date_key = loop_date.strftime("%Y%m%d")
        data[date_key] = question
        log_file.write("%s %s\n" % (difficulty, date_key))
        log_file.flush()
        if same_day(loop_date, last):
            break
    output_file.write(json.dumps(data))
    output_file.close()
log_file.close()


