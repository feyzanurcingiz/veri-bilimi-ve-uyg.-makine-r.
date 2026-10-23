import pandas as pd

ham_veri = pd.DataFrame({
    'Gozlem_ID': [101, 102, 102, 103, 104, 104],
    'Cinsiyet': ['Erkek', 'Kadın', 'Kadln', 'Erkek', 'Bilinmiyor', 'Bilinmiyor'],
    'Yas': [25, 30, 30, 22, -5, -5]
})

temiz_veri = ham_veri.drop_duplicates(subset=['Gozlem_ID'], keep='first').copy()
temiz_veri['Cinsiyet'] = temiz_veri['Cinsiyet'].replace({'Kadln': 'Kadın'})
temiz_veri = temiz_veri[temiz_veri['Yas'] > 0]

print(temiz_veri)
