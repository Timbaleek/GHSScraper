import pandas as pd
import numpy as np

gestis_data = pd.read_excel('gestis_data.xlsx')
gestis_data.to_dict()
print(gestis_data)
