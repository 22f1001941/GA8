import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic monthly revenue data
np.random.seed(42)
months = pd.date_range(start="2024-01-01", periods=12, freq='M').strftime("%b")

segments = ["Premium", "Standard", "Budget"]
data = []

for seg in segments:
    base = np.random.randint(80, 150)
    seasonality = 20 * np.sin(np.linspace(0, 2 * np.pi, 12))
    noise = np.random.normal(0, 5, 12)
    revenue = base + seasonality + noise
    data.append(pd.DataFrame({
        "Month": months,
        "Revenue": revenue,
        "Segment": seg
    }))

df = pd.concat(data)

# Create 512x512 figure (8 × 8 inches × 64 dpi = 512px)
plt.figure(figsize=(8, 8))

# Lineplot
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Segment",
    palette="tab10",
    linewidth=2.5,
    marker="o"
)

plt.title("Monthly Revenue Trend by Customer Segment (Synthetic Data)")
plt.xlabel("Month")
plt.ylabel("Revenue (in thousands)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save as exactly 512x512 PNG
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
