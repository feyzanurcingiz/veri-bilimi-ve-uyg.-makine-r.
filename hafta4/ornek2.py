import pandas as pd
import numpy as np

tarihler = pd.date_range(start='2026-01-01', periods=6, freq='D')

sensor_verisi = pd.DataFrame({
    'Tarih': tarihler,
    'Sicaklik': [22.1, np.nan, np.nan, 23.5, np.nan, 24.0]
})

sensor_verisi['Sicaklik_FFill'] = sensor_verisi['Sicaklik'].ffill()
sensor_verisi['Sicaklik_BFill'] = sensor_verisi['Sicaklik'].bfill()

print(sensor_verisi)
