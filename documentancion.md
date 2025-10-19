# 📊 Proyecto de Análisis de Ventas - Sprint 1

## 🎯 Tema, problema y solución
**Tema:** Análisis exploratorio de datos de ventas.  
**Problema:** Se requiere identificar patrones clave en las ventas históricas —productos más vendidos, clientes principales, medios de pago frecuentes y comportamiento mensual— para apoyar la toma de decisiones comerciales.  
**Solución:** Desarrollar un programa en Python que combine múltiples archivos de ventas, realice cálculos automáticos y muestre los resultados en tablas legibles.

---

## 🧠 Dataset de referencia
- **Origen:** Archivos CSV de ventas proporcionados por la empresa o simulados desde fuentes reales.  
- **Estructura esperada:**  
  - `fecha_venta` → Fecha de la transacción.  
  - `cliente` → Nombre o código del cliente.  
  - `producto` → Producto vendido.  
  - `cantidad` → Unidades vendidas.  
  - `monto` → Total de la venta.  
  - `medio_pago` → Efectivo, tarjeta, transferencia, etc.  

**Tipos de datos:**
- `fecha_venta`: tipo fecha (`datetime64`)
- `cantidad`: entero (`int64`)
- `monto`: numérico (`float64`)
- `medio_pago`, `cliente`, `producto`: texto (`string`)

**Escala:**  
Datos transaccionales (nivel micro), que pueden agregarse por mes, cliente o producto.

---

## ⚙️ Información técnica

### 🧩 Requerimientos
- Python 3.10+
- Librerías: `pandas`, `tabulate`

Instalación:
```bash
pip install pandas tabulate

leer rutas de archivos
unir todos en dataframe maestro
mientras True:
    mostrar menú
    si opción == 1:
        agrupar por mes y sumar montos
    si opción == 2:
        agrupar por cliente y sumar montos
    si opción == 3:
        agrupar por producto y sumar montos
    si opción == 4:
        agrupar por producto y sumar cantidades
    si opción == 5:
        contar operaciones por medio de pago
    si opción == 6:
        mostrar resumen general
    si opción == 7:
        salir del programa

