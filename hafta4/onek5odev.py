import pandas as pd
import numpy as np

np.random.seed(42)
veri = np.random.normal(50, 10, 100)
veri = np.append(veri, [150, -50, 200])
df_aykiri = pd.DataFrame({'Olcu': veri})

Q1 = df_aykiri['Olcu'].quantile(0.25)
Q3 = df_aykiri['Olcu'].quantile(0.75)
IQR = Q3 - Q1

alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR

df_temizlenmis = df_aykiri[(df_aykiri['Olcu'] >= alt_sinir) & (df_aykiri['Olcu'] <= ust_sinir)]
aykiri_deger_sayisi = len(df_aykiri) - len(df_temizlenmis)

print(f"Orijinal Veri Boyutu: {len(df_aykiri)}")
print(f"Temizlenmiş Veri Boyutu: {len(df_temizlenmis)}")
print(f"Tespit Edilen ve Silinen Aykırı Değer Sayısı: {aykiri_deger_sayisi}")
