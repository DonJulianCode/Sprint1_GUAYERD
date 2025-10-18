import streamlit as st
import pandas as pd
from data_loader import cargar_dfs, crear_df_ventas_completo

st.set_page_config(page_title="Dashboard Ventas - Proyecto Fénix", layout="wide")

df1, df2, df3, df4 = cargar_dfs()
df_ventas = crear_df_ventas_completo(df1, df2, df3, df4)

st.title("📊 Dashboard de Ventas - Proyecto Fénix")

# Métricas principales
total_ventas = df_ventas['importe'].sum()
num_clientes = df_ventas['id_cliente'].nunique()
num_productos = df_ventas['id_producto'].nunique()
num_ventas = df_ventas['id_venta'].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Ventas", f"${total_ventas:,}")
col2.metric("👤 Clientes Únicos", num_clientes)
col3.metric("🛒 Productos Vendidos", num_productos)
col4.metric("📄 Total Ventas Registradas", num_ventas)

# Top 10 productos por ventas
st.subheader("🏆 Top 10 Productos por Ventas")
top_productos = df_ventas.groupby('nombre_producto_venta')['importe'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_productos)

# Ventas por ciudad
st.subheader("🌆 Ventas por Ciudad")
ventas_ciudad = df_ventas.groupby('ciudad')['importe'].sum().sort_values(ascending=False)
st.bar_chart(ventas_ciudad)

# Ventas por cliente
st.subheader("👥 Top 10 Clientes por Compras")
top_clientes = df_ventas.groupby('nombre_cliente_venta')['importe'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_clientes)

st.write("🔍 Detalle de ventas completo")
st.dataframe(df_ventas)
