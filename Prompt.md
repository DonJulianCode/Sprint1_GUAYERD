# 💬 Prompts utilizados con GitHub Copilot

## 🧮 Solicitud 1 – Generar pseudocódigo base del programa

> 💭 **Prompt para Copilot:**
> 
> "Crea el pseudocódigo para un programa en Python que lea múltiples archivos Excel o CSV, los combine en un único DataFrame maestro y luego muestre un menú interactivo con las siguientes opciones:
> 
> 1. Agrupar por mes y sumar montos  
> 2. Agrupar por cliente y sumar montos  
> 3. Agrupar por producto y sumar montos  
> 4. Agrupar por producto y sumar cantidades  
> 5. Contar operaciones por medio de pago  
> 6. Mostrar resumen general  
> 7. Salir del programa  
> 
> Representa la lógica general sin usar código Python, solo con estructura de pseudocódigo legible y ordenado."

---

## 🤖 Solicitud 2 – Aplicar mejoras con inteligencia artificial

> 💭 **Prompt para Copilot:**
> 
> "Optimiza el diseño del programa anterior incorporando buenas prácticas de desarrollo.  
> 
> Sugiere mejoras que incluyan:
> - Un menú más claro y modular.  
> - Resultados formateados visualmente con la librería `tabulate`.  
> - Validación y control de errores de entrada del usuario.  
> - Simplificación del proceso de lectura de múltiples archivos CSV o Excel.  
> 
> Explica brevemente cómo cada mejora aporta claridad, robustez o legibilidad al código."

---

## 📘 Solicitud 3 – Crear guía de uso en Markdown

> 💭 **Prompt para Copilot:**
> 
> "Genera un archivo de documentación en formato Markdown (`instrucciones_copilot.md`) que contenga:
> 
> - Requisitos previos e instalación de dependencias (`pandas`, `tabulate`).  
> - Instrucciones paso a paso para ejecutar el script principal `analisis_ventas.py`.  
> - Explicación del menú de opciones.  
> - Ejemplo visual de salida en formato tabular (`fancy_grid`).  
> - Notas sobre personalización, unión de archivos y posibles mejoras futuras (como exportar reportes a Excel o incluir gráficos).  
> 
> Usa una estructura clara, con secciones y emojis para hacerlo más visual y fácil de leer."

---

## 📊 Resultado esperado (resumen general del conjunto de prompts)

> 💭 **Prompt para Copilot:**
> 
> "A partir de los tres prompts anteriores, genera un script interactivo en Python que lea múltiples archivos de ventas, los consolide en un DataFrame maestro y ofrezca un menú de análisis.  
> 
> El resultado debe ser un programa funcional, limpio y visualmente agradable, que permita obtener una visión rápida del comportamiento comercial general."

---

¿Quieres que te prepare también una versión complementaria para **Copilot Chat** (formato inline en VS Code, como si estuvieras trabajando línea por línea dentro del código)?  
Puedo convertir estos mismos prompts al estilo “comentario en código” (`# Copilot, genera...`) para integrarlos directamente dentro de tu script `analisis_ventas.py`.
