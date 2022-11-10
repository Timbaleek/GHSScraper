import pandas as pd
import numpy as np
import pubchempy as pcp


class Gestis:
    def __init__(self):
        self.data = pd.read_csv('gestis_data.csv')

    def name_get_url(self, query):
        return self.data.loc[self.data['NAME'] == query]


cid = pcp.get_substances('water', 'name')[0].standardized_cid
compounds = pcp.get_compounds('water', 'name')
print(compounds[0].synonyms)
