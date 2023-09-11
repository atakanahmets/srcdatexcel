import pandas as pd

excel_file = 'updated_data.xlsx'
df = pd.read_excel(excel_file, names=["city", "name", "phone"])

new_city = input("Yeni şehir adını girin: ")
new_name = input("Yeni ismi girin: ")
new_phone = input("Yeni telefon numarasını girin: ")

new_data = {
    "city": [new_city],
    "name": [new_name],
    "phone": [new_phone]
}

new_df = pd.DataFrame(new_data)

df = pd.concat([df, new_df], ignore_index=True)

output_file = 'updated_data.xlsx'
df.to_excel(output_file, index=False)

print("Veri başarıyla eklendi dosya 'updated_data.xlsx' olarak kayıt edildi")
updated_df = pd.read_excel(output_file)
print("\nGüncel Veriler:")
print(updated_df)