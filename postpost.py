import fileinput


wds = "ов-ник нн-ость и-тель тель-ниц ич-еск тель-ск ов-ик ян-ск и-ян \
тель-ств ов-ств ов-изн ова-ниj ир-ова-нн ич-еск ств-енн ир-ова ист-ич-еск н-ость \
т-ость".split()


to_replace = {}
for wd in wds:
    to_replace[wd.replace('-', '')] = wd


for line in fileinput.input():
    addendum = []
    line = line.strip()
    if '*' in line:
        print(line)
    else:
        razz = line.split('/')[1:]
        for raz in razz:
            for cmb in to_replace:
                if cmb in raz:
                    addendum.append(raz.replace(cmb, to_replace[cmb]))
        if addendum:
            addendum = list(set(addendum))
            line += "\t{}".format('\t'.join(addendum))
        print(line)
