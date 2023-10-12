import pandas as pd

# Leer el archivo xls/xlsx con pandas
ruta_xls = 'https://drive.google.com/uc?export=download&id=1wYIpM3HXXQ_vwrDMW4cvEJoIaW6U2ylP'   # Modifica esto con la ruta de tu archivo xls
ruta_csv = 'original.csv'   # Modifica esto con la ruta donde deseas guardar el csv



df = pd.read_excel(ruta_xls)

# Guardar el DataFrame en formato csv con codificación UTF-8 y separado por ";"
df.to_csv(ruta_csv, sep=';', encoding='utf-8', index=False)
