# 🧠 Copilot Prompts Log – Excel Sales Analysis System

This document compiles the main prompts provided to GitHub Copilot during the development of the **Excel Sales Analysis System**.  
The goal of these prompts was to automate data merging, visualization, and report generation using Python.

---

## 🚀 Project Overview

The project aims to:

- Merge multiple Excel files into a unified master dataset.  
- Analyze sales performance by products, clients, and months.  
- Provide a console-based interactive menu for quick exploration.  
- Display results elegantly using the `tabulate` library.  
- Visualize data relationships between Excel files through network diagrams.  

All tasks are designed to run seamlessly in **Google Colab** or **VSCode**.

---

## 🧩 Prompts Sent to Copilot

### 1️⃣ Merge and Menu System
```text
Create a Python program that:
1. Reads several Excel files from URLs or local paths.
2. Merges them into a master dataset.
3. Displays a text-based menu with options like:
   - Show best-selling products (by quantity and by total sales).
   - Identify top customers.
   - Analyze monthly sales.
Use `tabulate` with "fancy_grid" style to display results nicely.
2️⃣ Add Option for Top Products
Add option 7 to the previous menu:
   - Show top-selling products both by quantity and total revenue.

3️⃣ Markdown Summary Report
Generate a Markdown summary report with:
   - Key metrics (sales, customers, months).
   - Highlighted top performers.
   - A short insight paragraph per section.
Output should be pure Markdown, ready to copy-paste.

4️⃣ Excel Relationship Diagram
Create a diagram that shows how the Excel files relate to each other based on shared columns.
Each file is a node; draw connecting edges where columns overlap.
Use `networkx` and `matplotlib` to visualize the relationships.

5️⃣ Schema Visualization (Mock Version)
Even without real Excel files, generate a mock relationship diagram that represents:
   - ventas_enero.xlsx
   - ventas_febrero.xlsx
   - clientes.xlsx
   - productos.xlsx
Assume shared keys like `id_producto` and `id_cliente`.
Label nodes and edges to simulate the schema visually.

6️⃣ Unified Aesthetic Output
Ensure all charts, tables, and menus are clean and formatted.
Keep everything within one Python script for easy execution in Colab or VSCode.

🧮 Tools and Libraries

pandas → Excel reading and merging
tabulate → Table formatting
networkx + matplotlib → Graph-based relationship diagrams
os → File handling
collections / itertools → Data aggregation

💡 Outcome

The resulting system provides:

An elegant, menu-driven interface for exploring sales data.
Automatically generated Markdown summaries for reporting.
Visual diagrams that clarify relationships among Excel sources.
A portable, well-documented Python script ready for real datasets.

Author: Julián Gómez Brizuela
Project: Sales Analysis Tools
Year: 2025
