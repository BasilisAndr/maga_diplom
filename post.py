import fileinput
from pprint import pprint

res_all = []
res = {}
current = ''
for line in fileinput.input():
    line = line.replace('.verb', '').replace('.adv', '')
    line = line.strip()
    if line:
        pieces = line.split('\t')
        current = pieces[-3]
        if float(pieces[-1]) in res:
            res[float(pieces[-1])].append(pieces[-2])
        else:
            res[float(pieces[-1])] = [pieces[-2]]
    else:
        res_all.append([current, res])
        res = {}


for word, item in res_all:
    if len(item) == 1 and item[list(item.keys())[0]][0].endswith('?'):
        print(f'{word}\t*{word}')
    else:
        maxx = max(item.keys())
        raz = '\t'.join(list(set(item[maxx])))
        print(f'{word}\t{raz}')
