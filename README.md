# MD_Insight
These Python scripts generate publication‑ready visualisations for common post‑processing metrics in protein–ligand molecular‑dynamics (MD) simulations and MM/GBSA binding‑free‑energy calculations.

📂 Repository Contents

Script

Plot Produced

Input CSV

Output PNG

rmsd_vs_time_all_ligands.py

RMSD vs time line plot with mean values for 0‑50 ns & 50‑100 ns

RMSD_Ca.csv

rmsd_vs_time_all_ligands.png

rmsd_violin_plot.py

Violin plot of RMSD distributions for the first and second simulation halves

RMSD_Ca.csv

rmsd_violin_plot_exclude_frame0.png

mmgbsa_violin_plot.py

Violin plot of MM/GBSA energies (ligands sorted by mean energy)

MMGBSAvsTime.csv

mmgbsa_violin_plot.png

mmgbsa_cdf_plot.py

CDF plot of MM/GBSA energies per ligand

MMGBSAvsTime.csv

mmgbsa_cdf_plot.png

mmgbsa_heatmap.py

Rainbow heat‑map of MM/GBSA energies (‑95 → ‑65 kcal mol⁻¹)

MMGBSAvsTime.csv

mmgbsa_rainbow_heatmap.png

LigFitLig_violin_plot.py

LigFit‑Lig RMSD violin plot (0‑50 ns vs 50‑100 ns)

Lfl.csv

lfl_violin_plot_exclude_frame0.png

LigFitProt_violin_plot.py

LigFit‑Prot RMSD violin plot (0‑50 ns vs 50‑100 ns)

Lfp.csv

lfp_violin_plot_exclude_frame0.png

shannon_entropy_plot_v2.py

Shannon‑entropy trace for per‑residue RMSF (log scale, top & bottom‑5 highlighted)

RMSF_Ca.csv

shannon_entropy_plot_fixed.png

🔧 Installation

# 1. Clone the repository
$ git clone https://github.com/<your‑username>/md‑analysis‑plots.git
$ cd md‑analysis‑plots

# 2. (Recommended) create a clean environment
$ conda create -n mdplots python=3.9
$ conda activate mdplots

# 3. Install Python dependencies
$ pip install -r requirements.txt

Dependenciespandas, numpy, matplotlib, seaborn (all automatically installed via the requirement file).

📑 Input Data Format

Place the CSV files listed above in the project root (or update the file paths inside the scripts if needed).

General conventions

Time column — labelled Time (ns); units are nanoseconds.

Ligand columns — one column per ligand. Duplicate trajectory slices (e.g. Ligand.1, Ligand.2) are automatically ignored by the scripts.

RMSF files — must include a Residue # column followed by ligand‑specific RMSF values.

Sample snippets for each CSV type are provided in the examples/ folder.

🚀 Usage

Run any script directly with Python:

$ python rmsd_vs_time_all_ligands.py

The corresponding PNG figure will be saved in the working directory and displayed interactively.

To regenerate all figures in one go:

for f in *.py; do python "$f"; done

📝 Citing / Acknowledging

If you use these scripts in a publication, please cite:

Sayyah et al. “DRGSCROLL: AI‑Assisted Refinement of Protein–Ligand Complexes” (2025).

🤝 Contributing

Pull requests are welcome! For substantial changes, please open an issue first to discuss what you would like to change.

Fork the repository.

Create your feature branch: git checkout -b feature/your‑feature.

Commit your changes: git commit -m 'Add some feature'.

Push to the branch: git push origin feature/your‑feature.

Open a pull request.

