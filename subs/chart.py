import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional seaborn theme
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic realistic monthly revenue data
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

np.random.seed(42)

data = pd.DataFrame({
    "Month": months,
    "Premium": np.random.normal(120000, 8000, 12).round(),
    "Regular": np.random.normal(80000, 5000, 12).round(),
    "Budget": np.random.normal(40000, 3000, 12).round()
})

data_melted = data.melt(id_vars="Month", var_name="Segment", value_name="Revenue")

# Create figure with exact 512x512 pixels
plt.figure(figsize=(5.12, 5.12), dpi=100)  # 8 inches * 64 dpi = 512 px
sns.lineplot(
    data=data_melted,
    x="Month",
    y="Revenue",
    hue="Segment",
    style="Segment",
    markers=True,
    palette="viridis"
)

# Titles and labels
plt.title("Monthly Revenue Trend by Customer Segment")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save output image
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
