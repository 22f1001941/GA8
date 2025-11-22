#!/usr/bin/env python3
"""
generate_correlation.py

Reads 'q-excel-correlation-heatmap.xlsx', computes the correlation matrix for the five
supply-chain variables, writes correlation.csv, and saves a heatmap image heatmap.png
with a Red -> White -> Green color scale sized 512x512 pixels.

Usage:
    python generate_correlation.py --input q-excel-correlation-heatmap.xlsx --outdir submission

Dependencies:
    pip install pandas matplotlib openpyxl numpy
"""

import argparse
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def red_white_green_cmap():
    # Custom Red -> White -> Green colormap
    cdict = {
        'red':   ((0.0, 1.0, 1.0),
                  (0.5, 1.0, 1.0),
                  (1.0, 0.0, 0.0)),
        'green': ((0.0, 0.0, 0.0),
                  (0.5, 1.0, 1.0),
                  (1.0, 1.0, 1.0)),
        'blue':  ((0.0, 0.0, 0.0),
                  (0.5, 1.0, 1.0),
                  (1.0, 0.0, 0.0))
    }
    return LinearSegmentedColormap('RedWhiteGreen', cdict)

def compute_and_save(input_path, outdir):
    # Read the Excel file (first sheet or sheet named)
    df = pd.read_excel(input_path, engine='openpyxl')

    # Check for required columns
    required_cols = ['Supplier_Lead_Time', 'Inventory_Levels',
                     'Order_Frequency', 'Delivery_Performance', 'Cost_Per_Unit']
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Input is missing required columns: {missing}")

    # Subset the columns (ensures order)
    data = df[required_cols].copy()

    # Compute correlation matrix (Pearson)
    corr = data.corr(method='pearson')

    # Ensure outdir exists
    os.makedirs(outdir, exist_ok=True)

    # Save correlation CSV
    csv_path = os.path.join(outdir, 'correlation.csv')
    corr.to_csv(csv_path, index=True)

    # Create heatmap figure with Red -> White -> Green
    cmap = red_white_green_cmap()

    # Matplotlib figure size: determine dpi so that final image is 512x512 px
    # We'll set figure size in inches and dpi to get 512 px output.
    width_px = 512
    height_px = 512
    dpi = 100  # choose dpi; then figsize = pixels/dpi
    figsize = (width_px / dpi, height_px / dpi)

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    # Plot heatmap
    im = ax.imshow(corr.values, cmap=cmap, vmin=-1, vmax=1, aspect='equal')

    # Show labels for ticks (column names)
    labels = corr.columns.tolist()
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
    ax.set_yticklabels(labels, fontsize=8)

    # Annotate each cell with correlation value (2 decimal places)
    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            val = corr.iat[i, j]
            ax.text(j, i, f"{val:.2f}", ha='center', va='center', fontsize=8, color='black')

    # Remove spines and add a grid-ish look
    ax.set_xticks(np.arange(-.5, len(labels), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(labels), 1), minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=1)
    ax.tick_params(which='minor', bottom=False, left=False)

    # Add colorbar (optional)
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=8)

    # Tight layout and save at exact pixel size
    plt.tight_layout()

    img_path = os.path.join(outdir, 'heatmap.png')
    fig.savefig(img_path, dpi=dpi, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)

    print(f"Wrote correlation CSV -> {csv_path}")
    print(f"Wrote heatmap image -> {img_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute correlation matrix and generate heatmap.')
    parser.add_argument('--input', '-i', default='q-excel-correlation-heatmap.xlsx', help='Input Excel file path')
    parser.add_argument('--outdir', '-o', default='submission', help='Output directory (default: submission)')
    args = parser.parse_args()

    compute_and_save(args.input, args.outdir)
