
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load MMGBSA data
df = pd.read_csv("MMGBSAvsTime.csv")

# Extract original ligand columns (exclude .1, .2 duplicates)
ligand_columns = [col for col in df.columns if '.' not in col and col != "Time (ns)"]
mmgbsa_data = df[ligand_columns]
time_values = df["Time (ns)"]

# Transpose to have ligands as rows and time as columns
heatmap_data = mmgbsa_data.T
heatmap_data.columns = time_values

# Plot CDF
plt.figure(figsize=(10, 6), facecolor='white')
for ligand in heatmap_data.index:
    values = heatmap_data.loc[ligand].sort_values()
    cdf = np.arange(1, len(values) + 1) / len(values)
    plt.plot(values, cdf, label=ligand)

# Clean plot styling
ax = plt.gca()
ax.set_facecolor('white')
ax.grid(False)

# Labels and title
plt.xlabel("MMGBSA Energy (kcal/mol)", fontsize=12)
plt.ylabel("Cumulative Probability", fontsize=12)
plt.title("CDF of MMGBSA Energies per Ligand", fontsize=14, fontweight="bold")
plt.legend(fontsize=9, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("mmgbsa_cdf_plot.png", dpi=300)
plt.show()
