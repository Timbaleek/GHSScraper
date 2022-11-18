import pandas as pd
from PubChem import *
from collections import Iterable


def flatten(codes):
    rt = []
    for i in codes:
        if isinstance(i, list):
            rt.extend(flatten(i))
        else:
            rt.append(i)
    return rt


def format_for_word(cid, name, sort_alphabetically):

    hazards_dict = pd.read_excel('hazards_dict.xlsx', index_col=0)
    precautions_dict = pd.read_excel('precautions_dict.xlsx', index_col=0)

    out = []
    hazards, precautions = get_H_and_P(cid)

    if sort_alphabetically:
        hazards.sort()
        precautions.sort()

    out.append('Hazard Statements')
    out.append([])

    for h in hazards:

        if '+' in h:
            h.split('+')

            for i in range(len(h)-1):
                h[i+1] = '+' + h[i+1]

    hazards = flatten(hazards)

    for h in hazards:

        if '+' in h:
            h.replace('+', '')
            out.append((h + ':').ljust(10) + hazards_dict[h])
            h = '+ ' + h
        else:
            out.append((h + ':').ljust(10) + hazards_dict[h])

    out.append([])
    out.append('Precationary Statements')
    out.append([])

    for p in precautions:

        if '+' in p:
            p.split('+')

            for i in range(len(p) - 1):
                p[i + 1] = '+' + p[i + 1]

    precautions = flatten(precautions)

    for p in precautions:

        if '+' in p:
            p.replace('+', '')
            out.append((p + ':').ljust(10) + hazards_dict[p])
            p = '+ ' + p
        else:
            out.append((p + ':').ljust(10) + hazards_dict[p])

    return out
