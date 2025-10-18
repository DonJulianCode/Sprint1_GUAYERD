from flask import Flask, jsonify, request
from data_loader import cargar_dfs, crear_df_ventas_completo
import pandas as pd

app = Flask(__name__)

df1, df2, df3, df4 = cargar_dfs()
df_ventas = crear_df_ventas_completo(df1, df2, df3, df4)

@app.route("/ventas", methods=["GET"])
def ventas():
    fecha_inicio = request.args.get("fecha_inicio")
    fecha_fin = request.args.get("fecha_fin")
    
    df = df_ventas.copy()
    
    if fecha_inicio and fecha_fin:
        df = df[df['fecha'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]
    
    total_ventas = df['importe'].sum()
    num_clientes = df['id_cliente'].nunique()
    num_productos = df['id_producto'].nunique()
    
    return jsonify({
        "total_ventas": total_ventas,
        "num_clientes": num_clientes,
        "num_productos": num_productos,
        "detalle": df.to_dict(orient="records")
    })

@app.route("/top_productos", methods=["GET"])
def top_productos():
    top_n = int(request.args.get("top_n", 10))
    df = df_ventas.groupby('nombre_producto_venta')['importe'].sum().sort_values(ascending=False).head(top_n)
    return jsonify(df.to_dict())

@app.route("/ventas_ciudad", methods=["GET"])
def ventas_ciudad():
    df = df_ventas.groupby('ciudad')['importe'].sum().sort_values(ascending=False)
    return jsonify(df.to_dict())

@app.route("/ventas_cliente", methods=["GET"])
def ventas_cliente():
    id_cliente = request.args.get("id_cliente")
    if not id_cliente:
        return jsonify({"error": "Se requiere id_cliente"}), 400
    df = df_ventas[df_ventas['id_cliente'] == int(id_cliente)]
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
