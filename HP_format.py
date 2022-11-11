import pandas as pd
from PubChem import *
import pubchempy as pcp


def format_for_word(compound_cid_list, compound_name_dict):

    hazards_dict = pd.read_excel('hazards_dict')
    precautions_dict = pd.read_excel('precautions_dict')

    out_printable_list = []

    for cid in compound_cid_list:
        hazards, precautions = get_H_and_P(cid)
        hazards.sort()
        precautions.sort()

        out_printable_list.append(compound_name_dict[cid])
        out_printable_list.append([])
        out_printable_list.append('Hazard Statements')
        out_printable_list.append([])

        for h in hazards:
            h.split('+')
            out_printable_list.append((h[0] + ':').ljust(10) + hazards_dict[h[0]])

            for i in range(len(h)-1):
                out_printable_list.append(('+ ' + h[i+1] + ':').ljust(10) + hazards_dict[h[i+1]])

        out_printable_list.append([])
        out_printable_list.append('Precationary Statements')
        out_printable_list.append([])

        for p in precautions:
            p.split('+')
            out_printable_list.append((p[0] + ':').ljust(10) + precautions_dict[p[0]])

            for i in range(len(p) - 1):
                out_printable_list.append(('+ ' + p[0] + ':').ljust(10) + precautions_dict[p[0]])

    return out_printable_list
