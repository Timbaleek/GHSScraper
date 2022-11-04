import pandas as pd
import numpy as np

gestis_data = pd.read_excel('gestis_data.xlsx')
print(gestis_data)
print(gestis_data.loc[gestis_data['FORMULA'] == 'H2O'])


