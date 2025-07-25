# MD_Insight
These Python scripts generate publication‑ready visualisations for common post‑processing metrics in protein–ligand molecular‑dynamics (MD) simulations and MM/GBSA binding‑free‑energy calculations.


A collection of lightweight Python scripts that turn raw **RMSD / MM‑GBSA / RMSF** CSV outputs into publication‑ready figures for protein–ligand molecular‑dynamics (MD) projects.

---

## 📂 Repository Contents

| Script | Plot Produced | Required CSV | Output PNG |
| ------ | ------------- | ------------ | ---------- |
| `rmsd_vs_time_all_ligands.py` | RMSD vs time line plot (with 0‑50 ns & 50‑100 ns means) | `RMSD_Ca.csv` | `rmsd_vs_time_all_ligands.png` |
| `rmsd_violin_plot.py` | Violin plot of RMSD distributions (first vs second half) | `RMSD_Ca.csv` | `rmsd_violin_plot_exclude_frame0.png` |
| `mmgbsa_violin_plot.py` | Violin plot of MM/GBSA energies (ligands sorted by mean) | `MMGBSAvsTime.csv` | `mmgbsa_violin_plot.png` |
| `mmgbsa_cdf_plot.py` | CDF plot of MM/GBSA energies per ligand | `MMGBSAvsTime.csv` | `mmgbsa_cdf_plot.png` |
| `mmgbsa_heatmap.py` | Rainbow heat‑map of MM/GBSA energies (‑95 → ‑65 kcal mol⁻¹) | `MMGBSAvsTime.csv` | `mmgbsa_rainbow_heatmap.png` |
| `LigFitLig_violin_plot.py` | LigFit‑Lig RMSD violin plot (0‑50 ns vs 50‑100 ns) | `Lfl.csv` | `lfl_violin_plot_exclude_frame0.png` |
| `LigFitProt_violin_plot.py` | LigFit‑Prot RMSD violin plot (0‑50 ns vs 50‑100 ns) | `Lfp.csv` | `lfp_violin_plot_exclude_frame0.png` |
| `shannon_entropy_plot_v2.py` | Shannon‑entropy trace for per‑residue RMSF (top & bottom‑5 highlighted) | `RMSF_Ca.csv` | `shannon_entropy_plot_fixed.png` |

> **Tip:** Keep your CSV and PNG filenames as above, or edit the variables at the top of each script.

---

## 🔧 Installation

```bash
# 1. Clone the repository
git clone https://github.com/DurdagiLab/MD_Insight.git
cd md‑analysis‑plots

# 2. (Recommended) create a clean environment
conda create -n mdplots python=3.9
conda activate mdplots

# 3. Install Python dependencies
pip install -r requirements.txt


