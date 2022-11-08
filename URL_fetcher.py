import pandas as pd
import numpy as np


class Gestis:
    def __init__(self):
        self.data = pd.read_csv('gestis_data.csv')

    def name_get_url(self, query):
        return self.data.loc[self.data['NAME'] == query]
