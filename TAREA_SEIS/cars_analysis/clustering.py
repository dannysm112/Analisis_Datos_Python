from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos limpios
df = pd.read_csv('data_cars_limpio.csv')

# Preparar los datos para el clustering
X_cluster = df[['year', 'selling_price', 'km_driven']]
scaler = StandardScaler()
X_cluster_scaled = scaler.fit_transform(X_cluster)


# Determinar el número óptimo de clusters utilizando el método del codo
inertia = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_cluster_scaled)
    inertia.append(kmeans.inertia_)

# Graficar el método del codo
plt.plot(range(2, 11), inertia, marker='o')
plt.xlabel('Número de clusters')
plt.ylabel('Inertia')
plt.title('Método del codo para determinar el número óptimo de clusters')
plt.show()

# Seleccionar el número óptimo de clusters basado en el codo del gráfico
optimal_k_codo = inertia.index(min(inertia)) + 2
print("Número óptimo de clusters basado en el método del codo:", optimal_k_codo)

# Aplicar K-Means con el número óptimo de clusters
kmeans_codo = KMeans(n_clusters=optimal_k_codo, random_state=42)
kmeans_codo.fit(X_cluster_scaled)
cluster_labels_codo = kmeans_codo.labels_

# Calcular las métricas después del clustering
mse_km = mean_squared_error(X_cluster_scaled, kmeans_codo.cluster_centers_[kmeans_codo.labels_])
r2_km = r2_score(X_cluster_scaled, kmeans_codo.cluster_centers_[kmeans_codo.labels_])
mae_km = mean_absolute_error(X_cluster_scaled, kmeans_codo.cluster_centers_[kmeans_codo.labels_])

print("MSE después de clustering:", mse_km)
print("R² después de clustering:", r2_km)
print("MAE después de clustering:", mae_km)

# Visualizar los resultados del clustering
pca = PCA(n_components=2)
X_cluster_pca = pca.fit_transform(X_cluster_scaled)
plt.scatter(X_cluster_pca[:, 0], X_cluster_pca[:, 1], c=cluster_labels_codo, cmap='viridis')
plt.xlabel('Componente principal 1')
plt.ylabel('Componente principal 2')
plt.title('Resultados del clustering con K-Means (Método del codo)')
plt.show()





# Determinar el número óptimo de clusters utilizando el método de Silhouette
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    cluster_labels = kmeans.fit_predict(X_cluster_scaled)
    silhouette_avg = silhouette_score(X_cluster_scaled, cluster_labels)
    silhouette_scores.append(silhouette_avg)

# Graficar los puntajes de Silhouette
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.xlabel('Número de clusters')
plt.ylabel('Silhouette Score')
plt.title('Método de Silhouette para determinar el número óptimo de clusters')
plt.show()

# Seleccionar el número óptimo de clusters basado en el mayor puntaje de Silhouette
optimal_k_silhouette = silhouette_scores.index(max(silhouette_scores)) + 2
print("Número óptimo de clusters basado en el método de Silhouette:", optimal_k_silhouette)

# Aplicar K-Means con el número óptimo de clusters
kmeans_silhouette = KMeans(n_clusters=optimal_k_silhouette, random_state=42)
kmeans_silhouette.fit(X_cluster_scaled)
cluster_labels_silhouette = kmeans_silhouette.labels_

# Calcular las métricas después del clustering
mse_km = mean_squared_error(X_cluster_scaled, kmeans_silhouette.cluster_centers_[kmeans_silhouette.labels_])
r2_km = r2_score(X_cluster_scaled, kmeans_silhouette.cluster_centers_[kmeans_silhouette.labels_])
mae_km = mean_absolute_error(X_cluster_scaled, kmeans_silhouette.cluster_centers_[kmeans_silhouette.labels_])

print("MSE después de clustering:", mse_km)
print("R² después de clustering:", r2_km)
print("MAE después de clustering:", mae_km)

# Visualizar los resultados del clustering
pca = PCA(n_components=2)
X_cluster_pca = pca.fit_transform(X_cluster_scaled)
plt.scatter(X_cluster_pca[:, 0], X_cluster_pca[:, 1], c=cluster_labels_silhouette, cmap='viridis')
plt.xlabel('Componente principal 1')
plt.ylabel('Componente principal 2')
plt.title('Resultados del clustering con K-Means (Método de Silhouette)')
plt.show()
