import fileinput
from pymystem3 import Mystem
'''
Turns text into one-lemma-per-line and filters out non-analysable
strings like numbers and names (capitalised mid-sentence)
Those elements are written in the output as "*element"
'''


def analyse_string(stri):
    res = m.lemmatize(stri)[0]
    return res


m = Mystem()
for line in fileinput.input():
    line = line.split()
    prev = ''
    for el in line:
        if el.strip(',.!»«()') and el.strip(',.!»«()').isalpha() and not (prev and prev[-1] not in '.!?' and el[0].isupper()):
            print(analyse_string(el))
        else:
            print('*', el.strip(',.!»«()'), sep='')
        prev = el
