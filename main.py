import streamlit as st
import pandas as pd
from data_loader import cargar_dfs, crear_df_ventas_completo

st.set_page_config(page_title="Dashboard Ventas - Sprint 1 Guayerd", layout="wide")

# =======================
# Carga de datos
# =======================
df1, df2, df3, df4 = cargar_dfs()
df_ventas = crear_df_ventas_completo(df1, df2, df3, df4)

# =======================
# Cabecera HTML
# =======================
st.markdown("""
<div style='background-color:#1E90FF;padding:10px;border-radius:5px'>
    <h1 style='color:white;text-align:center;'>Dashboard Ventas - Sprint 1 Guayerd</h1>
</div>
""", unsafe_allow_html=True)

# =======================
# Filtros interactivos
# =======================
st.sidebar.header("Filtros")
ciudad_sel = st.sidebar.multiselect("Ciudad", options=df_ventas['ciudad'].unique(), default=df_ventas['ciudad'].unique())
producto_sel = st.sidebar.multiselect("Producto", options=df_ventas['nombre_producto_venta'].unique(), default=df_ventas['nombre_producto_venta'].unique())
cliente_sel = st.sidebar.multiselect("Cliente", options=df_ventas['nombre_cliente_venta'].unique(), default=df_ventas['nombre_cliente_venta'].unique())
fecha_rango = st.sidebar.date_input("Rango de fechas", [df_ventas['fecha'].min(), df_ventas['fecha'].max()])

# Aplicar filtros
df_filtrado = df_ventas[
    (df_ventas['ciudad'].isin(ciudad_sel)) &
    (df_ventas['nombre_producto_venta'].isin(producto_sel)) &
    (df_ventas['nombre_cliente_venta'].isin(cliente_sel)) &
    (df_ventas['fecha'].between(pd.to_datetime(fecha_rango[0]), pd.to_datetime(fecha_rango[1])))
]

# =======================
# Métricas principales
# =======================
total_ventas = df_filtrado['importe'].sum()
num_clientes = df_filtrado['id_cliente'].nunique()
num_productos = df_filtrado['id_producto'].nunique()
num_ventas = df_filtrado['id_venta'].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Ventas", f"${total_ventas:,}")
col2.metric("👤 Clientes Únicos", num_clientes)
col3.metric("🛒 Productos Vendidos", num_productos)
col4.metric("📄 Total Ventas Registradas", num_ventas)

# =======================
# Gráficos
# =======================
st.subheader("🏆 Top 10 Productos por Ventas")
top_productos = df_filtrado.groupby('nombre_producto_venta')['importe'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_productos)

st.subheader("🌆 Ventas por Ciudad")
ventas_ciudad = df_filtrado.groupby('ciudad')['importe'].sum().sort_values(ascending=False)
st.bar_chart(ventas_ciudad)

st.subheader("👥 Top 10 Clientes por Compras")
top_clientes = df_filtrado.groupby('nombre_cliente_venta')['importe'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_clientes)

st.subheader("🔍 Detalle de ventas filtrado")
st.dataframe(df_filtrado)
