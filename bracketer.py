import fileinput
import json

with open('roots.json') as f:
    roots = json.load(f)


def get_closest(razz):
    razz2 = []
    for raz in razz:
        # for every analysis, 1. find the root(s)
        # 2. find the adjacent affixes (or roots)
        raz2 = []  # to be analysed here
        raz = raz.split('-')
        for i in range(len(raz)):
            if '.root' in raz[i]:
                rt = {'root': i}
                if i > 0:
                    if raz[i - 1] == 'о' and 'root' in raz[i - 2]:
                        rt['pref'] == i - 2
                    else:
                        rt['pref'] == i - 1
                if i < len(raz):
                    if raz[i + 1] == 'о' and 'root' in raz[i + 2]:
                        rt['suf'] == i + 2
                    else:
                        rt['suf'] == i + 1
                raz2.append(rt)
        razz2.append(raz2)
    return razz2


def get_brackets(razz, razz2):
    res = []
    for raz, raz2 in razz, razz2:
        # 3. look up the root
        # 4. look up the adjacent affixes
        # 5. compare the compat number of pref and suf
        # 6. put brackets
        left_br = []
        right_br = []
        raz = raz.split('-')
        for rt in raz2:
            pref_num = 0
            suf_num = 0
            root = raz[rt['root']]
            if pref in rt:
                pref = raz[rt['pref']]
            if suf in rt:
                suf = raz[rt['suf']]
            if root in roots:
                if pref and pref in roots[root]['prefs']:
                    pref_num = roots[root]['prefs'][pref]
                if suf and suf in roots[root]['sufs']:
                    suf_num = roots[root]['sufs'][pref]
            winner = False
            if pref_num > suf_num:
                winner = True
            if winner:
                left_br.append(rt['pref']) # bracket before that
                right_br.append(rt['root']) # bracket after that
            else:
                left_br.append(rt['root'])
                if suf:
                    right_br.append(rt['suf'])
                else:
                    right_br.append(rt['root'])
        stri = []
        for i in range(len(raz)):
            if i in left_br:
                stri.append('[{}'.format(raz[i]))
            elif i in right_br:
                stri.append('{}]'.format(raz[i]))
            else:
                stri.append(raz[i])
        res.append('-'.join(stri))
    return res


for line in fileinput.input():
    line = line.strip()
    # parse line into parts
    razz = line.split('\t')[1:]
    razz2 = get_closest(razz)
    analyses_with_brackets = get_brackets(razz, razz2)
    print(line[0], '\t', '\t'.join(analyses_with_brackets), sep='')
