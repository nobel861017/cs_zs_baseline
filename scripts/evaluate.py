from pathlib import Path
import os
import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='The input file of pseudo-probability')
args = parser.parse_args()


table = dict()

with open(args.input, 'r') as f:
    for line in f.readlines():
        line = line.strip().split(' ')
        #print(line)
        filename, prob = line[0], float(line[1])
        filename = Path(filename)

        idx = str(os.path.splitext(os.path.basename(filename))[0])
        sets = os.path.basename(os.path.dirname(os.path.dirname(filename)))
        sets_dir = os.path.dirname(os.path.dirname(filename))
        lang = os.path.basename(os.path.dirname(sets_dir))
        correct_or_wrong = os.path.basename(os.path.dirname(filename))
        # print(correct_or_wrong)
        if lang not in table.keys():
            table[lang] = dict()
        if sets not in table[lang].keys():
            table[lang][sets] = dict()
        
        if idx not in table[lang][sets].keys():
            table[lang][sets][idx] = dict()

        table[lang][sets][idx][correct_or_wrong] = prob

for lang in table.keys():
    for sets in table[lang].keys():
        correct_counter= 0
        total = 0
        
        for idx in table[lang][sets].keys():
            if ("correct" in table[lang][sets][idx].keys() and "wrong" in table[lang][sets][idx].keys()):
                if table[lang][sets][idx]["correct"] > table[lang][sets][idx]["wrong"]:
                    correct_counter += 1
                total += 1
        
        print(f'Accuracy of {lang} {sets}: {correct_counter / total}')
        print(f'Total pair: {total}')

print('Finished evaluation.')
