
import pandas as pd
import matplotlib.pyplot as plt

# Load RMSD data
df = pd.read_csv("RMSD_Ca.csv")

# Time vector and midpoint
time = df["Time (ns)"]
midpoint = 50

# Create figure
plt.figure(figsize=(12, 6))

# Plot each ligand
for ligand in df.columns:
    if ligand != "Time (ns)":
        rmsd = df[ligand]
        first_half = rmsd[time <= midpoint]
        second_half = rmsd[time > midpoint]
        mean_first = first_half.mean()
        mean_second = second_half.mean()
        plt.plot(time, rmsd, label=f"{ligand} (0–50 ns: {mean_first:.2f}, 50–100 ns: {mean_second:.2f})")

# Vertical line at 50 ns
plt.axvline(x=50, color='gray', linestyle='--', linewidth=1.5)

# Axis limits and labels
plt.ylim(0, 4)
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("RMSD (Å)", fontsize=12)
plt.title("RMSD vs Time for All Ligands\n(Mean RMSD in First and Second Half in Legend)", fontsize=14, fontweight='bold')

# Remove grid and set white background
ax = plt.gca()
ax.set_facecolor("white")
ax.grid(False)

# Legend
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=9)
plt.tight_layout()
plt.savefig("rmsd_vs_time_all_ligands.png", dpi=300)
plt.show()
