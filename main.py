import numpy as np
import pandas as pd

excel_file = 'updated_data.xlsx'  #Arama yapmak istediğimiz dosya adını yazıyoruz
df = pd.read_excel(excel_file, names=["city", "name", "phone"])

search_input = input("Arama yapmak istediğiniz şehir adını, ismi veya numarayı girin: ")

result = df[df['city'].str.contains(search_input, case=False) | df['name'].str.contains(search_input, case=False) | df['phone'].astype(str).str.contains(search_input)]

if not result.empty:
    print("Eşleşen Sonuçlar:")
    print(result)
else:
    print("Eşleşen sonuç bulunamadı.")
