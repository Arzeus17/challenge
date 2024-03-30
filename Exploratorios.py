import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Cargo el archivo CSV
df = pd.read_csv("testMeLi.csv")

#Análisis de Precios
df = df.dropna(subset=['Price'])
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Calculo el precio promedio por marca
precios_promedio_por_marca = df.groupby('Search Term')['Price'].mean()

# Calculo la distribución de precios por marca
distribucion_precios_por_marca = df.groupby('Search Term')['Price'].describe()

print("Precios promedio por marca:")
print(precios_promedio_por_marca)

print("\nDistribución de precios por marca:")
print(distribucion_precios_por_marca)


# Grafico los precios promedio por marca
precios_promedio_por_marca.plot(kind='bar', color='skyblue')
plt.title('Precios promedio por marca de teléfonos')
plt.xlabel('Marca')
plt.ylabel('Precio promedio (ARS)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafico la distribución de precios por marca
for marca, datos in distribucion_precios_por_marca.iterrows():
    plt.hist(df[df['Search Term'] == marca]['Price'], bins=20, alpha=0.5, label=marca)

plt.title('Distribución de precios por marca de teléfonos')
plt.xlabel('Precio (ARS)')
plt.ylabel('Frecuencia')
plt.legend()
plt.tight_layout()
plt.show()


# Grafico un diagrama de caja y bigotes (boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Search Term', y='Price', data=df)
plt.title('Distribución de Precios por Marca de Dispositivos de Streaming')
plt.xlabel('Marca')
plt.ylabel('Precio')
plt.xticks(rotation=45)  
plt.grid(True)
plt.show()


# Análisis del Estado del Producto

df = df.dropna(subset=['Condition'])
marcas_top_5 = df['Search Term'].value_counts().index[:5]

df_marcas = pd.DataFrame(index=marcas_top_5)

# Filtro el DataFrame original para incluir solo las marcas con celulares usados
df_usados = df[df['Search Term'].isin(marcas_top_5)]

# Calculo el conteo de teléfonos nuevos y usados por marca
conteo_por_marca = df_usados.groupby(['Search Term', 'Condition']).size().unstack()
conteo_por_marca.fillna(0, inplace=True)

# Relleno las filas con marcas que no tienen celulares usados con ceros
conteo_por_marca = conteo_por_marca.reindex(index=marcas_top_5, fill_value=0)

# Normalizo los valores de cada fila para que sumen 1
conteo_por_marca_norm = conteo_por_marca.div(conteo_por_marca.sum(axis=1), axis=0)

# Creo un gráfico de barras apiladas 2D
conteo_por_marca_norm.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Proporción de teléfonos nuevos y usados por marca')
plt.xlabel('Marca')
plt.ylabel('Proporción')
plt.xticks(rotation=45)
plt.legend(title='Estado del Producto')
plt.tight_layout()
plt.show()


# Análisis de las Ventas del Producto
df = df[['Search Term', 'Sold Quantity']]

df = df.dropna()
cantidad_vendida_por_marca = df.groupby('Search Term')['Sold Quantity'].sum()

cantidad_vendida_por_marca = cantidad_vendida_por_marca.sort_values(ascending=False)

# Verifico si hay datos para graficar
if not cantidad_vendida_por_marca.empty:
    plt.figure(figsize=(8, 6))
    plt.pie(cantidad_vendida_por_marca, labels=cantidad_vendida_por_marca.index, autopct='%1.1f%%', startangle=140)
    plt.title('Proporción de unidades vendidas por marca de teléfonos')
    plt.axis('equal')  
    plt.show()
else:
    print("No hay suficientes datos para graficar.")


