
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load MMGBSA data
df = pd.read_csv("MMGBSAvsTime.csv")

# Extract ligand columns (excluding duplicates like '.1', '.2')
ligand_columns = [col for col in df.columns if '.' not in col and col != "Time (ns)"]
mmgbsa_data = df[ligand_columns]
time_values = df["Time (ns)"]

# Prepare data for heatmap
heatmap_data = mmgbsa_data.T
heatmap_data.columns = time_values

# Plot the heatmap
plt.figure(figsize=(16, 6))
sns.heatmap(
    heatmap_data,
    cmap="gist_rainbow",
    vmin=-95, vmax=-65,
    cbar_kws={'label': 'MMGBSA Energy (kcal/mol)'}
)
plt.xlabel("Simulation Time (ns)", fontsize=12)
plt.ylabel("Ligand", fontsize=12)
plt.title("MMGBSA Binding Energy Heatmap (-95 to -65 kcal/mol, Rainbow)", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("mmgbsa_rainbow_heatmap.png", dpi=300)
plt.show()
