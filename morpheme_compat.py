import fileinput
import json

roots = {}


def get_closest(razz):
    razz2 = []
    for raz in razz:
        # for every analysis, 1. find the root(s)
        # 2. find the adjacent affixes (or roots)
        raz2 = []  # to be analysed here
        raz = raz.split('-')
        for i in range(len(raz)):
            if '.root' in raz[i]:
                rt = {'root': raz[i]}
                if i > 0:
                    if i > 1 and raz[i - 1] == 'о' and 'root' in raz[i - 2]:
                        rt['pref'] = raz[i - 2]
                    else:
                        rt['pref'] = raz[i - 1]
                if i < len(raz) - 1:
                    if i < len(raz) - 2 and 'root' in raz[i + 2] and raz[i + 1] == 'о':
                        rt['suf'] = raz[i + 2]
                    else:
                        rt['suf'] = raz[i + 1]
                raz2.append(rt)
        razz2.append(raz2)
    return razz2


for line in fileinput.input():
    line = line.strip()
    # parse line into parts
    razz = line.split('/')[1:]
    razz2 = get_closest(razz)
    for raz2 in razz2:
        for raz in raz2:
            if raz['root'] in roots:
                if 'pref' in raz and raz['pref'] in roots[raz['root']]['prefs']:
                    roots[raz['root']]['prefs'][raz['pref']] += 1
                if 'suf' in raz and raz['suf'] in roots[raz['root']]['sufs']:
                    roots[raz['root']]['sufs'][raz['suf']] += 1
            else:
                roots[raz['root']] = {'prefs': {}, 'sufs': {}}
                if 'pref' in raz:
                    roots[raz['root']]['prefs'][raz['pref']] = 1
                if 'suf' in raz:
                    roots[raz['root']]['sufs'][raz['suf']] = 1

with open('roots.json', 'w') as f:
    json.dump(roots, f)
