import pandas as pd
import numpy as np
import pubchempy as pcp
import PubChem


class Gestis:
    def __init__(self):
        self.data = pd.read_csv('gestis_data.csv')

    def name_get_url(self, query):
        return self.data.loc[self.data['NAME'] == query]


cid = PubChem.get_cid_from_name('Ethanol')
print(cid)
print(PubChem.get_H_and_P_from_name(cid))

#cid = pcp.get_substances('water', 'name')[0].standardized_cid
#compounds = pcp.get_compounds('water', 'name')
# print(compounds[0].synonyms)
