# TVET Bangladesh Teacher Survey — Analysis

Exploratory data analysis of survey responses from **1,301 TVET teachers** and
**1,212 students** across polytechnic institutes in Bangladesh (Oct–Dec 2024).

**Research areas covered:**
- Educational qualification profiles
- Training and certification participation rates and types
- Adoption of Bloom's Taxonomy and blended learning
- Departmental composition and cross-variable patterns
- Temporal response patterns and institutional benchmarking
- Student challenges (standalone analysis)

---

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Register the kernel with Jupyter (optional but recommended)

```bash
python -m ipykernel install --user --name tvet-bd --display-name "TVET BD"
```

### 4. Launch the notebook

```bash
jupyter notebook analysis.ipynb
```

> Run cells **top-to-bottom** in order. All figures are saved automatically
> to `figures/` as both 300 DPI PNG and PDF.

---

## Repository Structure

```
TVET_BD/
├── data/
│   ├── TVET_Teachers.xlsx                              # Primary cleaned dataset (1,301 teachers)
│   ├── State of Technical and Vocational Education...  # Full survey with Timestamp (1,301 rows)
│   └── Challenges Faced by Students...                 # Student survey (1,212 students)
├── figures/                                            # Auto-generated journal-quality figures
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # load_data(), load_data_with_timestamp(), load_student_data()
│   └── visualizations.py   # plot_pie(), plot_bar_pie(), plot_bar_annotated(), plot_heatmap()
├── analysis.ipynb           # Full analysis notebook (run top-to-bottom)
├── requirements.txt
└── README.md
```

---

## Datasets

| File | Respondents | Type |
|------|-------------|------|
| `TVET_Teachers.xlsx` | 1,301 | TVET teachers (cleaned, 7 variables) |
| `State of TVET...xlsx` | 1,301 | Same teachers + Timestamp (10 columns) |
| `Challenges Faced by Students...xlsx` | 1,212 | Polytechnic students (19 variables) |

> The two teacher files share the same rows in the same order.
> `load_data_with_timestamp()` merges the Timestamp automatically.
> The student dataset covers only 1 of 45 institutions — it is analysed standalone.

---

## Output Figures

All figures are saved to `figures/` as **300 DPI PNG** using `fig.savefig(..., dpi=300, bbox_inches='tight')`.

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `pandas` | Data loading and manipulation |
| `matplotlib` | Figure generation |
| `seaborn` | Statistical visualisations and colour palettes |
| `scipy` | Chi-square tests of independence |
| `openpyxl` | Reading `.xlsx` files |
| `jupyter` / `notebook` | Running the analysis notebook |

---

## License

MIT License
