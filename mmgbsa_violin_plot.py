
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load MMGBSA data
df = pd.read_csv("MMGBSAvsTime.csv")

# Filter ligand columns (exclude .1, .2 duplicates)
ligand_columns = [col for col in df.columns if '.' not in col and col != "Time (ns)"]
mmgbsa_data = df[ligand_columns]
time_values = df["Time (ns)"]

# Prepare data for violin plot
heatmap_data = mmgbsa_data.T
heatmap_data.columns = time_values

# Melt for seaborn plotting
violin_df = heatmap_data.T.melt(var_name='Ligand', value_name='MMGBSA Energy')

# Sort ligands by average energy (ascending: strong binders on left)
ligand_means = heatmap_data.mean(axis=1).sort_values()
sorted_ligands = ligand_means.index.tolist()
violin_df["Ligand"] = pd.Categorical(violin_df["Ligand"], categories=sorted_ligands, ordered=True)

# Plot violin chart
plt.figure(figsize=(12, 6))
sns.violinplot(data=violin_df, x='Ligand', y='MMGBSA Energy', palette='rainbow')
plt.title("Distribution of MMGBSA Energies per Ligand (Sorted by Mean Energy)", fontsize=14, fontweight='bold')
plt.xlabel("Ligand (Sorted by Binding Strength)", fontsize=12)
plt.ylabel("MMGBSA Energy (kcal/mol)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("mmgbsa_violin_plot.png", dpi=300)
plt.show()
