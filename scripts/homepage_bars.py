"""Full-width three-panel closed-loop results for the paper page.

(a) component additions, (b) RoboMME suite means, (c) Piper task TSR.
Numbers are from the English manuscript tables in root.tex.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "assets" / "plots"

INK = "#141413"
MUTED = "#6b6257"
LINE = "#d9d0c3"
OURS = "#d97757"
FRAMESAMP = "#9dd4c7"
NATIVE = "#a8c5e6"
BASE = "#e8e6e3"
PAPER = "#fffcf7"

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 12,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "legend.frameon": False,
})


def style_ax(ax):
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=LINE, linewidth=0.6)
    ax.tick_params(length=0)
    for label in ax.get_xticklabels():
        label.set_fontsize(11)


def panel_components(ax):
    labels = ["Counting\nGDN", "Permanence\nretrieval", "Reference\nfusion"]
    deltas = [6.94, 4.22, 4.50]
    x = np.arange(len(labels))
    ax.bar(x, deltas, color=OURS, edgecolor=INK, linewidth=0.6, width=0.62, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Δ TSR (pp)")
    ax.set_ylim(0, 9)
    ax.set_title("(a) Component additions", loc="left", fontsize=13, pad=8)
    style_ax(ax)


def panel_suites(ax):
    labels = ["Counting", "Permanence", "Reference", "Imitation"]
    framesamp = np.array([65.22, 25.11, 36.33, 51.39])
    ours = np.array([70.83, 27.75, 45.31, 53.00])
    x = np.arange(len(labels))
    w = 0.36
    ax.bar(x - w / 2, framesamp, width=w, color=FRAMESAMP, edgecolor=INK,
           linewidth=0.6, label="FrameSamp+Modul", zorder=3)
    ax.bar(x + w / 2, ours, width=w, color=OURS, edgecolor=INK,
           linewidth=0.6, label="Ours", zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=18, ha="right")
    ax.set_ylabel("TSR (%)")
    ax.set_ylim(0, 92)
    ax.set_title("(b) RoboMME suites", loc="left", fontsize=13, pad=8)
    ax.legend(loc="upper left", fontsize=10, ncol=1)
    style_ax(ax)


def panel_piper(ax):
    labels = ["Pick×3", "Swing×2", "RePick", "Shell"]
    series = [
        (r"$\pi_{0.5}$", [20.0, 6.7, 3.3, 30.0], BASE),
        ("NativeMEM", [20.0, 30.0, 40.0, 36.7], NATIVE),
        ("FrameSamp", [26.7, 36.7, 33.3, 53.3], FRAMESAMP),
        ("Ours", [80.0, 93.3, 36.7, 40.0], OURS),
    ]
    x = np.arange(len(labels))
    n = len(series)
    width = 0.2
    offsets = (np.arange(n) - (n - 1) / 2) * width
    for off, (name, values, color) in zip(offsets, series):
        ax.bar(x + off, values, width=width * 0.92, color=color, edgecolor=INK,
               linewidth=0.5, label=name, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("TSR (%)")
    ax.set_ylim(0, 115)
    ax.set_title("(c) Piper tasks", loc="left", fontsize=13, pad=8)
    ax.legend(loc="upper right", fontsize=9, ncol=2)
    style_ax(ax)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.15), layout="constrained")
    panel_components(axes[0])
    panel_suites(axes[1])
    panel_piper(axes[2])
    stem = OUT / "results_trio"
    fig.savefig(stem.with_suffix(".svg"), bbox_inches="tight")
    fig.savefig(stem.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(stem.with_suffix(".png"), dpi=180, bbox_inches="tight")
    plt.close(fig)
    print("wrote", stem)


if __name__ == "__main__":
    main()
