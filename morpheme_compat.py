import fileinput
import json

roots = {}

for line in fileinput.input():
    line = line.strip()
    # parse line into parts
    razz = line.split('/')[1:]
    razz2 = []
    for raz in razz:
        # then root and stuff
        raz2 = {}
        pref = ''
        suf = ''
        for mor in raz.split('-'):
            if '.root' in mor:
                raz2['root'] = mor
                if pref:
                    raz2['pref'] = pref
            else:
                if 'root' not in raz2:
                    pref = mor
                elif not suf:
                    suf = mor
        if suf:
            raz2['suf'] = suf
        if 'root' not in raz2:
            continue
        razz2.append(raz2)
    for raz in razz2:
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
