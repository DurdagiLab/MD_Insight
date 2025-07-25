
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load LFL data
df = pd.read_csv("Lfl.csv")

# Prepare data: exclude frame 0, split into 0–50 ns and 50–100 ns halves
violin_data = []
time = df["Time (ns)"]

for ligand in df.columns:
    if ligand != "Time (ns)":
        values = df[ligand]

        mask_first = (time > 0) & (time <= 50)
        mask_second = time > 50

        for v in values[mask_first]:
            violin_data.append({"Ligand": ligand, "LFL": v, "Half": "0–50 ns"})
        for v in values[mask_second]:
            violin_data.append({"Ligand": ligand, "LFL": v, "Half": "50–100 ns"})

# Convert to DataFrame
violin_df = pd.DataFrame(violin_data)

# Plot
plt.figure(figsize=(14, 6))
sns.violinplot(data=violin_df, x="Ligand", y="LFL", hue="Half", split=True, palette="Set2")

plt.title("LFL Distribution Excluding Frame 0 (Violin Plot)", fontsize=14, fontweight="bold")
plt.xlabel("Ligand", fontsize=12)
plt.ylabel("LFL", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("lfl_violin_plot_exclude_frame0.png", dpi=300)
plt.show()
