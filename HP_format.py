import pandas as pd
from PubChem import *


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

    out.append(name)
    out.append('')
    out.append('Hazard Statements')
    out.append('')

    for h, i in zip(hazards, range(len(hazards))):

        if '+' in h:
            hazards[i] = h.split('+')

            for j in range(len(hazards[i])-1):
                hazards[i][j+1] = '+ ' + hazards[i][j+1]

    hazards = flatten(hazards)

    for h in hazards:
        out.append((h + ':').ljust(10) + hazards_dict['phrase'].loc[h.replace('+', '')])

    out.append('')
    out.append('Precautionary Statements')
    out.append('')

    for p, i in zip(precautions, range(len(precautions))):

        if '+' in p:
            precautions[i] = p.split('+')

            for j in range(len(precautions[i]) - 1):
                precautions[i][j+1] = '+ ' + precautions[i][j+1]

    precautions = flatten(precautions)

    for p in precautions:
        out.append((p + ':').ljust(10) + precautions_dict['phrase'].loc[p.replace('+ ', '')])

    out.append('')
    out.append('Disposal: DISPOSAL')
    out.append('')

    return out


def format_for_latex(cid, name, sort_alphabetically):

    hazards_dict = pd.read_excel('hazards_dict.xlsx', index_col=0)
    precautions_dict = pd.read_excel('precautions_dict.xlsx', index_col=0)

    out = []
    pictograms = []
    hazards, precautions = get_H_and_P(cid)

    if sort_alphabetically:
        hazards.sort()
        precautions.sort()

    out.append(r'\subsubsection*{' + name + '}')
    out.append('')
    out.append(r'\textbf{Hazard Statements}')
    out.append('')
    out.append(r'\bigskip')
    out.append('')

    for h, i in zip(hazards, range(len(hazards))):

        if '+' in h:
            hazards[i] = h.split('+')

            for j in range(len(hazards[i]) - 1):
                hazards[i][j + 1] = '+ ' + hazards[i][j + 1]

    hazards = flatten(hazards)

    for h in hazards:
        if not hazards_dict['pictogram'].loc[h.replace('+ ', '')] in pictograms:
            out.append(r'\ghspic{' + hazards_dict['pictogram'].loc[h.replace('+ ', '')] + r'}')
            pictograms.append(hazards_dict['pictogram'].loc[h.replace('+ ', '')])

    out.append('')
    out.append(r'\begin{description}')
    out.append('')
    out.append(r'\itemsep -1.5mm')

    for h in hazards:
        out.append(r'\item{\textbf{' + (h + ':') + r'}}  ' + hazards_dict['phrase'].loc[h.replace('+ ', '')])

    out.append('')
    out.append(r'\end{description}')
    out.append('')
    out.append(r'\textbf{Precautionary Statements}')
    out.append('')
    out.append(r'\begin{description}')
    out.append('')
    out.append(r'\itemsep -1.5mm')
    out.append('')

    for p, i in zip(precautions, range(len(precautions))):

        if '+' in p:
            precautions[i] = p.split('+')

            for j in range(len(precautions[i]) - 1):
                precautions[i][j + 1] = '+ ' + precautions[i][j + 1]

    precautions = flatten(precautions)

    for p in precautions:
        out.append(r'\item{\textbf{' + (p + ':') + r'}}  ' + precautions_dict['phrase'].loc[p.replace('+ ', '')])

    out.append('')
    out.append(r'\end{description}')
    out.append('')
    out.append(r'\bigskip')
    out.append('')
    out.append(r'\textbf{Disposal:} DISPOSAL')
    out.append('')

    return out

