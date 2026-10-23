import pandas as pd
import numpy as np

df_notlar = pd.DataFrame({
    'Hafta': [1, 2, 3, 4, 5, 6, 7],
    'Performans_Skoru': [45, 50, np.nan, 65, np.nan, 82, 90]
})

df_notlar['Dogrusal_Enterpolasyon'] = df_notlar['Performans_Skoru'].interpolate(method='linear')
df_notlar['Kuadratik_Enterpolasyon'] = df_notlar['Performans_Skoru'].interpolate(method='quadratic')

print(df_notlar)
