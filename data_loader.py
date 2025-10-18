import pandas as pd

URLS = {
    "clientes": "https://github.com/DonJulianCode/Sprint1_GUAYERD/raw/refs/heads/main/clientes.xlsx",
    "detalle_ventas": "https://github.com/DonJulianCode/Sprint1_GUAYERD/raw/refs/heads/main/detalle_ventas.xlsx",
    "productos": "https://github.com/DonJulianCode/Sprint1_GUAYERD/raw/refs/heads/main/productos.xlsx",
    "ventas": "https://github.com/DonJulianCode/Sprint1_GUAYERD/raw/refs/heads/main/ventas.xlsx"
}

def cargar_dfs():
    df1 = pd.read_excel(URLS["clientes"])
    df2 = pd.read_excel(URLS["detalle_ventas"])
    df3 = pd.read_excel(URLS["productos"])
    df4 = pd.read_excel(URLS["ventas"])
    return df1, df2, df3, df4

def crear_df_ventas_completo(df1, df2, df3, df4):
    detalle_completo = df2.merge(df3, on='id_producto', suffixes=('_detalle','_producto'))
    ventas_detalle = detalle_completo.merge(df4, on='id_venta')
    df_ventas_completo = ventas_detalle.merge(df1, on='id_cliente', suffixes=('_venta','_cliente'))
    return df_ventas_completo
