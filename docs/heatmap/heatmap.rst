********
Heatmaps
********

The heatmap is a compact way to compare gene expression across samples in one
plot. You can change the clustering method, the distance method, the size, and
the ``padj`` / fold-change cutoffs, and switch to an interactive version for
selection. Heatmaps appear both on the **QC Plots** tab (Plot Type → Heatmap) and
next to the **Main Plots** when you select a region.

.. image:: ../debrowser_pics2/qc-heatmap.png
    :align: center
    :width: 99%

Clustering & linkage methods
============================

* **complete** — closest cluster pairs are merged up to a distance threshold;
  the distance between clusters is the maximum pairwise member distance.
* **ward.D2** — minimizes within-cluster squared deviations for compact,
  spherical clusters (Murtagh & Legendre 2014); dissimilarities are squared
  before updating, which makes it sensitive to outliers.
* **single** — the minimum of the pairwise member distances.
* **average** — the average of the pairwise member distances.
* **mcquitty** — a new cluster's distance to another cluster is the average of
  the merged clusters' distances to it.
* **median** — averaging with the median to reduce outlier influence.
* **centroid** — Euclidean distance between cluster centroids/means.

Distance methods
================

* **cor** — ``1 - cor(x)``; less sensitive to outliers and scaling.
* **euclidean** — root sum of squared differences; sensitive to outliers and
  scaling.
* **maximum** — the maximum distance across corresponding genes.
* **manhattan** — the sum of absolute differences.
* **canberra** — a scaled Minkowski variant dividing absolute differences by the
  sum of absolute counts.
* **minkowski** — a generalized Euclidean distance.

.. note::

    For distances other than ``cor``, the dissimilarity is defined as
    ``1 - (correlation between samples)``.

Interactive heatmap
===================

Tick the **Interactive** checkbox on the left panel (under the height/width
options) to switch to a zoomable, two-color heatmap. As in the Main Plots, click
and drag to select genes — highlight the middle of a gene's box to fully select
it. The selection can then be sent to the **Enrichment** tab for GO/KEGG/GSEA
queries.

.. tip::

    Interactive rendering is heavier, so it is off by default. Settle your
    clustering/plotting parameters first, then enable it to inspect blocks in
    detail.

Heatmap of a Main-Plot selection
================================

Select a region of a Main Plot (Scatter, Volcano, or MA) with the **box-select**
or **lasso-select** tool and a heatmap of just those genes appears next to the
plot. Click a group label (Up / Down / NS) in the legend to hide it, so you can
lasso only up- or down-regulated genes; the heatmap updates as you select.

.. tip::

    Normalize before plotting heatmaps: **Data options → Normalization
    Methods**.

Scale options
=============

The **Scale Option** panel on the left controls how values are transformed
before plotting:

1. **Center** — subtract each column's mean (default: on).
2. **Scale** — divide the (centered) columns by their standard deviation, or by
   the root-mean-square if centering is off (default: on).
3. **Log** — apply ``log2`` to the matrix (default: on).
4. **Pseudo-Count** — a small value added before ``log2`` to avoid ``log(0)``
   (default: 0.1).
