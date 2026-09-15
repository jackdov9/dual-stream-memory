"""Homepage result bars from the English manuscript tables.

Core claim: dual-stream memory raises RoboMME suite means over FrameSamp+Modul,
with the largest suite gain on Reference, while Piper gains concentrate on
repeated-action counting and Shell declines.
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
    "font.size": 11,
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


def save(fig, stem):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{stem}.svg", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def grouped_bars(ax, labels, series, colors, width=0.34):
    x = np.arange(len(labels))
    n = len(series)
    offsets = (np.arange(n) - (n - 1) / 2) * width
    for off, (name, values), color in zip(offsets, series, colors):
        ax.bar(x + off, values, width=width * 0.92, color=color, edgecolor=INK,
               linewidth=0.6, label=name, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=LINE, linewidth=0.6)
    ax.tick_params(length=0)


def robomme():
    labels = ["Counting", "Permanence", "Reference", "Imitation"]
    framesamp = [65.22, 25.11, 36.33, 51.39]
    ours = [70.83, 27.75, 45.31, 53.00]
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    grouped_bars(
        ax, labels,
        [("FrameSamp+Modul", framesamp), ("Ours", ours)],
        [FRAMESAMP, OURS],
        width=0.36,
    )
    ax.set_ylabel("TSR (%)")
    ax.set_ylim(0, 85)
    ax.legend(loc="upper left", ncol=2, fontsize=10)
    fig.tight_layout()
    save(fig, "robomme_suites")


def piper():
    labels = ["Pick×3", "Swing×2", "RePick", "Shell"]
    series = [
        (r"$\pi_{0.5}$", [20.0, 6.7, 3.3, 30.0]),
        ("NativeMEM", [20.0, 30.0, 40.0, 36.7]),
        ("FrameSamp+Modul", [26.7, 36.7, 33.3, 53.3]),
        ("Ours", [80.0, 93.3, 36.7, 40.0]),
    ]
    colors = [BASE, NATIVE, FRAMESAMP, OURS]
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    grouped_bars(ax, labels, series, colors, width=0.2)
    ax.set_ylabel("TSR (%)")
    ax.set_ylim(0, 110)
    ax.legend(loc="upper right", ncol=2, fontsize=9)
    fig.tight_layout()
    save(fig, "piper_tasks")


if __name__ == "__main__":
    robomme()
    piper()
    print("wrote", OUT)
