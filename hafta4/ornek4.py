import pandas as pd
import numpy as np

veri_seti = pd.DataFrame({
    'Maas': [5000, 6000, np.nan, 8000, 7500, 200000],
    'Deneyim': [2, np.nan, 5, 8, 4, 10],
    'Departman': ['IT', 'IK', 'IT', np.nan, 'Satis', 'IT']
})

veri_seti['Maas'] = veri_seti['Maas'].fillna(veri_seti['Maas'].median())
veri_seti['Deneyim'] = veri_seti['Deneyim'].fillna(veri_seti['Deneyim'].mean())
veri_seti['Departman'] = veri_seti['Departman'].fillna(veri_seti['Departman'].mode()[0])

print(veri_seti)
