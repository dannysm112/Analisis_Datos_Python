import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Cargar los datos limpios
df = pd.read_csv('data_cars_limpio.csv')


# Dividir los datos en características (años) y objetivo (precios)
X_year = df['year'].values.reshape(-1, 1)
y_price = df['selling_price'].values

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_year, y_price, test_size=0.2, random_state=42)

# Modelo de regresión lineal
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
y_pred_lr = model_lr.predict(X_test)

# Modelo de regresión no lineal (polinomial de grado 2)
model_poly = make_pipeline(PolynomialFeatures(2), LinearRegression())
model_poly.fit(X_train, y_train)
y_pred_poly = model_poly.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse_lr = mean_squared_error(y_test, y_pred_lr)
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_lr = r2_score(y_test, y_pred_lr)
r2_poly = r2_score(y_test, y_pred_poly)
mae_lr = mean_absolute_error(y_test, y_pred_lr)
mae_poly = mean_absolute_error(y_test, y_pred_poly)

print("MSE Regresión Lineal:", mse_lr)
print("MSE Regresión No Lineal (Polinomial):", mse_poly)
print("R² Regresión Lineal:", r2_lr)
print("R² Regresión No Lineal (Polinomial):", r2_poly)
print("MAE Regresión Lineal:", mae_lr)
print("MAE Regresión No Lineal (Polinomial):", mae_poly)

# Graficar resultados
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred_lr, color='red', label='Regresión Lineal')
plt.plot(X_test, y_pred_poly, color='green', label='Regresión No Lineal (Polinomial)')
plt.xlabel('Año')
plt.ylabel('Precio de venta')
plt.title('Predicción de precios de vehículos a lo largo de los años')
plt.legend()
plt.show()




# Dividir los datos en características (kilómetros) y objetivo (precios)
X_km = df['km_driven'].values.reshape(-1, 1)
y_price = df['selling_price'].values

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_km, y_price, test_size=0.2, random_state=42)

# Modelo de regresión lineal
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
y_pred_lr = model_lr.predict(X_test)

# Modelo de regresión no lineal (polinomial de grado 2)
model_poly = make_pipeline(PolynomialFeatures(2), LinearRegression())
model_poly.fit(X_train, y_train)
y_pred_poly = model_poly.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse_lr = mean_squared_error(y_test, y_pred_lr)
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_lr = r2_score(y_test, y_pred_lr)
r2_poly = r2_score(y_test, y_pred_poly)
mae_lr = mean_absolute_error(y_test, y_pred_lr)
mae_poly = mean_absolute_error(y_test, y_pred_poly)

print("MSE Regresión Lineal:", mse_lr)
print("MSE Regresión No Lineal (Polinomial):", mse_poly)
print("R² Regresión Lineal:", r2_lr)
print("R² Regresión No Lineal (Polinomial):", r2_poly)
print("MAE Regresión Lineal:", mae_lr)
print("MAE Regresión No Lineal (Polinomial):", mae_poly)

# Graficar resultados
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred_lr, color='red', label='Regresión Lineal')
plt.plot(X_test, y_pred_poly, color='green', label='Regresión No Lineal (Polinomial)')
plt.xlabel('Kilómetros recorridos')
plt.ylabel('Precio de venta')
plt.title('Relación entre kilómetros recorridos y precio de venta de vehículos')
plt.legend()
plt.show()
