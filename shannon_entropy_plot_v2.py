
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Shannon entropy hesaplayan fonksiyon (manuel)
def shannon_entropy_manual(prob_dist):
    prob_dist = np.array(prob_dist)
    prob_dist = prob_dist[prob_dist > 0]  # log(0) sorununu önlemek için
    return -np.sum(prob_dist * np.log2(prob_dist))

# CSV dosyasını yükle
df = pd.read_csv("RMSF_Ca.csv")

# Ligand sütunları
ligand_cols = ['Alnespirone', 'Carafiban', 'Etofylline_clofibrate', 'Morclofone', 'Xantifibrate', 'Compound 46']

# Compound 46'daki eksik verileri çıkar
valid_mask = df["Compound 46"].notna()
rmsf_valid = df.loc[valid_mask, ligand_cols].values
residues = df.loc[valid_mask, "Residue #"].values

# Entropi hesapla (manuel)
shannon_entropy = []
for row in rmsf_valid:
    probs = row / np.sum(row)
    ent = shannon_entropy_manual(probs)
    shannon_entropy.append(ent)

shannon_entropy = np.array(shannon_entropy)

# Renk haritası için normalize et
norm = mcolors.Normalize(vmin=min(shannon_entropy), vmax=max(shannon_entropy))
colors = cm.coolwarm(norm(shannon_entropy))

# En yüksek ve en düşük 5 entropili residue'ları bul
top5_idx = np.argsort(shannon_entropy)[-5:]
bottom5_idx = np.argsort(shannon_entropy)[:5]

# Çizim
fig, ax = plt.subplots(figsize=(14, 6))
for i in range(len(residues) - 1):
    ax.plot(residues[i:i+2], shannon_entropy[i:i+2], color=colors[i], linewidth=2.5)

ax.set_yscale("log")
ax.plot(residues[top5_idx], shannon_entropy[top5_idx], 'o', color='black', markersize=8, label="Top 5")
ax.plot(residues[bottom5_idx], shannon_entropy[bottom5_idx], 'o', color='blue', markersize=8, label="Bottom 5")

ax.set_xlabel("Residue Number", fontsize=14)
ax.set_ylabel("Shannon Entropy (bits, log scale)", fontsize=14)
ax.set_title("Shannon Entropy per Residue (Top & Bottom 5 Marked)", fontsize=16, fontweight='bold')

# Renk skalası doğru şekilde eksenle ilişkilendirilmiş halde
sm = cm.ScalarMappable(norm=norm, cmap='coolwarm')
sm.set_array([])
fig.colorbar(sm, ax=ax, label='Entropy Magnitude')

plt.tight_layout()
plt.savefig("shannon_entropy_plot_fixed.png", dpi=300)
plt.show()
