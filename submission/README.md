# Supply Chain Analytics — Correlation Matrix Visualization

This repository contains the outputs for the OptimalFlow Logistics correlation analysis task.

## Files in this folder (`submission/`)

- `correlation.csv` — correlation matrix exported from the provided dataset.
- `heatmap.png` — heatmap screenshot produced with Red → White → Green color scale (512×512 px).
- `q-excel-correlation-heatmap.xlsx` — (not included here) original Excel dataset used to compute correlations.
- `generate_correlation.py` — Python script used to compute the correlation matrix and generate the heatmap.

## Steps performed

1. Imported the dataset `q-excel-correlation-heatmap.xlsx` into Python (pandas).  
2. Calculated the correlation matrix for the columns:
   - `Supplier_Lead_Time`
   - `Inventory_Levels`
   - `Order_Frequency`
   - `Delivery_Performance`
   - `Cost_Per_Unit`
3. Exported the correlation matrix to `correlation.csv`.
4. Created a heatmap image `heatmap.png` sized **512×512 pixels**. The heatmap uses a **Red (low) → White → Green (high)** custom color scale to match Excel conditional formatting color semantics.

## Contact
For questions, contact: **22f1001941@ds.study.iitm.ac.in**
