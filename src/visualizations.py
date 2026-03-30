"""
Visualization utilities for the TVET Bangladesh analysis.

All figures are produced at journal-quality resolution (300 DPI).
save_figure() writes both PNG (300 DPI) and PDF (vector) to figures/.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np

FIGURES_DIR = Path(__file__).parent.parent / "figures"
DPI = 300
PALETTE = "tab10"

# Apply consistent journal-style defaults at import time
mpl.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 100,       # screen display
        "savefig.dpi": DPI,      # saved files
    }
)


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------

def save_figure(fig, filename):
    """Save *fig* to figures/ as both PNG (300 DPI) and PDF (vector).

    Parameters
    ----------
    fig : matplotlib.figure.Figure
    filename : str
        Base filename without extension (e.g. 'fig1_education').
    """
    FIGURES_DIR.mkdir(exist_ok=True)
    path = FIGURES_DIR / f"{Path(filename).stem}.png"
    fig.savefig(path, dpi=300, bbox_inches="tight")
    print(f"Saved → {path}")


# ---------------------------------------------------------------------------
# Single pie chart
# ---------------------------------------------------------------------------

def plot_pie(counts, figsize=(5, 5)):
    """Pie chart with label + percentage inside each wedge.

    Parameters
    ----------
    counts : pd.Series
        Value counts — index = category labels, values = counts.
    figsize : tuple
        Figure size in inches (width, height).

    Returns
    -------
    matplotlib.figure.Figure
    """
    colors = sns.color_palette(PALETTE, len(counts))
    fig, ax = plt.subplots(figsize=figsize)
    _, _, autotexts = ax.pie(
        counts,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
        wedgeprops={"edgecolor": "white", "linewidth": 0.8},
        textprops={"fontsize": 9, "weight": "bold"},
    )
    for i, autotext in enumerate(autotexts):
        autotext.set_text(f"{counts.index[i]}\n{autotext.get_text()}")
        autotext.set_color("white")
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Side-by-side bar + pie
# ---------------------------------------------------------------------------

def plot_bar_pie(labels, values, suptitle, bar_ylabel="", figsize=(13, 5)):
    """Side-by-side horizontal bar chart and pie chart.

    Parameters
    ----------
    labels : array-like
        Category labels.
    values : array-like
        Corresponding counts.
    suptitle : str
        Overall figure title.
    bar_ylabel : str
        Y-axis label for the bar panel.
    figsize : tuple
        Figure size in inches.

    Returns
    -------
    matplotlib.figure.Figure
    """
    labels = list(labels)
    values = list(values)
    total = sum(values)
    colors = sns.color_palette(PALETTE, len(labels))

    fig, axes = plt.subplots(1, 2, figsize=figsize)

    # --- Bar chart (horizontal, descending) ---
    axes[0].barh(labels[::-1], values[::-1], color=colors[::-1])
    axes[0].set_xlabel("Number of Respondents", fontsize=10)
    if bar_ylabel:
        axes[0].set_ylabel(bar_ylabel, fontsize=10)
    axes[0].set_title("Bar Chart", fontsize=11)
    axes[0].set_xlim(0, max(values) * 1.30)
    for idx, val in enumerate(values[::-1]):
        pct = f"{val / total * 100:.1f}%"
        axes[0].text(
            val + total * 0.01, idx,
            f"{val} ({pct})",
            color="black", ha="left", va="center", fontsize=8,
        )

    # --- Pie chart ---
    wedges, _ = axes[1].pie(
        values,
        startangle=90,
        colors=colors,
        wedgeprops={"edgecolor": "white", "linewidth": 0.8},
    )
    axes[1].set_title("Pie Chart", fontsize=11)
    axes[1].legend(
        wedges, labels,
        loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=8, frameon=False,
    )

    fig.suptitle(suptitle, fontsize=13, fontweight="bold", y=1.01)
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Horizontal bar chart with annotations
# ---------------------------------------------------------------------------

def plot_bar_annotated(counts, figsize=(8, 5)):
    """Horizontal bar chart with count + percentage annotations.

    Parameters
    ----------
    counts : pd.Series
        Value counts — index = labels, values = counts.
        Will be plotted in descending order (largest bar at top).
    figsize : tuple

    Returns
    -------
    matplotlib.figure.Figure
    """
    total = counts.sum()
    colors = sns.color_palette(PALETTE, len(counts))

    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(counts.index[::-1], counts.values[::-1], color=colors[::-1])
    ax.set_xlabel("Number of Respondents", fontsize=10)
    ax.set_xlim(0, max(counts.values) * 1.25)

    for idx, val in enumerate(counts.values[::-1]):
        pct = f"{val / total * 100:.1f}%"
        ax.text(
            val + total * 0.005, idx,
            f"{val} ({pct})",
            color="black", ha="left", va="center", fontsize=9,
        )

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Heatmap for cross-tabulations
# ---------------------------------------------------------------------------

def plot_heatmap(data, title, figsize=(8, 6), cmap="Blues", fmt=".1f",
                 cbar_label="Percentage (%)"):
    """Annotated heatmap for cross-tabulation percentage tables.

    Parameters
    ----------
    data : pd.DataFrame
        Percentage values (0–100) indexed by row and column categories.
    title : str
    figsize : tuple
    cmap : str
    fmt : str
        Number format for annotations (default '.1f').
    cbar_label : str

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        data,
        annot=True,
        fmt=fmt,
        cmap=cmap,
        ax=ax,
        linewidths=0.4,
        linecolor="white",
        cbar_kws={"label": cbar_label},
        annot_kws={"size": 9},
    )
    ax.set_title(title, fontsize=11, pad=10)
    ax.tick_params(axis="x", rotation=30)
    ax.tick_params(axis="y", rotation=0)
    fig.tight_layout()
    return fig
