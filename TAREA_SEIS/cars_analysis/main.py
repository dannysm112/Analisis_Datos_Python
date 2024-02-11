import pandas as pd

# Cargar el archivo .csv
df = pd.read_csv('data_cars.csv')

# Visualizar las primeras 5 filas del archivo
print(df.head())

# Verificar la cantidad de valores faltantes
print(df.isnull().sum())

# Eliminar datos duplicados
df.drop_duplicates(inplace=True)

# Convertir columnas a tipos de datos adecuados
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['selling_price'] = pd.to_numeric(df['selling_price'], errors='coerce')
df['km_driven'] = pd.to_numeric(df['km_driven'], errors='coerce')

# Verificar los tipos de datos
print(df.dtypes)

# Guardar los datos limpios en un nuevo archivo .csv
df.to_csv('data_cars_limpio.csv', index=False)
