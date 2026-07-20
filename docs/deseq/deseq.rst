***********
DE Analysis
***********

This page describes the differential-expression engines DEBrowser uses and the
parameters it exposes for each.

Introduction
============

Differential gene expression analysis finds genes, transcripts, or regions whose
difference in expression between two or more sets of samples — accounting for the
variance within a condition — is higher than expected by chance. DEBrowser wraps
three established Bioconductor engines,
`DESeq2 <https://bioconductor.org/packages/DESeq2>`_ (Love et al., 2014),
`edgeR <https://bioconductor.org/packages/edgeR>`_ (Robinson et al., 2010), and
`limma <https://bioconductor.org/packages/limma>`_ (Ritchie et al., 2015),
coupled with `Shiny <https://shiny.posit.co>`_ to produce real-time changes in
your plot queries and interactive browsing of your DE results. You select the
engine and its parameters on the **Comparison** step of the Data Prep wizard,
under **Advanced model settings**.

DESeq2
======

See the `DESeq2 user guide <https://bioconductor.org/packages/DESeq2>`_.

DESeq2 groups samples into conditions and computes, for every gene, the
probability of differential expression using a negative binomial model,
reporting both a nominal and a multiple-testing-corrected (``padj``) p-value.

**Un-normalized counts.** DESeq2 requires raw, un-normalized counts (the model
corrects for library size internally). Non-integer values are converted to
integers as needed. Do not feed it pre-scaled or normalized values — use edgeR or
limma for those.

**Parameters**

* **fitType** — ``parametric``, ``local``, or ``mean``: how dispersions are fit
  to the mean intensity (see ``estimateDispersions``).
* **betaPrior** — whether to place a zero-mean normal prior on the non-intercept
  coefficients (see ``nbinomWaldTest``).
* **testType** — ``Wald`` (``nbinomWaldTest``) or ``LRT`` (likelihood-ratio test
  on the difference in deviance between a full and reduced model, ``nbinomLRT``).
* **rowsum.filter** — regions/genes/isoforms with total count (across all
  samples) below this value are filtered out.

edgeR
=====

See the `edgeR user guide <https://bioconductor.org/packages/edgeR>`_.

**Parameters**

* **Normalization** — scaling factors for raw library sizes: ``TMM``, ``RLE``,
  ``upperquartile``, or ``none``.
* **Dispersion** — a numeric dispersion, or a string telling edgeR to estimate
  it from the data.
* **testType** — ``exactTest`` (per-gene exact test between two groups) or
  ``glmLRT`` (negative-binomial GLM with genewise likelihood-ratio tests).
* **rowsum.filter** — low-total-count features are removed.

limma
=====

See the `limma user guide <https://bioconductor.org/packages/limma>`_. limma is
ideal when data are already normalized (e.g. spike-in or another scaling), in
which case prefer it over DESeq2 or edgeR.

**Parameters**

* **Normalization** — ``TMM``, ``RLE``, ``upperquartile``, or ``none``.
* **Fit Type** — ``ls`` (least squares) or ``robust`` (robust regression).
* **Norm. Bet. Arrays** — normalize between arrays so intensities/log-ratios
  share similar distributions across samples.
* **rowsum.filter** — low-total-count features are removed.

Batch-effect correction
========================

On the **Batch effect** step DEBrowser can correct known technical batch effects
before DE, using
`ComBat <https://bioconductor.org/packages/sva>`_ or **ComBat-Seq** (from the SVA
package) or `Harman <https://bioconductor.org/packages/Harman>`_. ComBat is
applied with SVA's defaults; ComBat-Seq operates directly on counts. Choose a
normalization method (MRN, TMM, RLE, upperquartile) alongside the correction
method, and confirm the effect with the inline PCA / IQR / Density plots.

References
==========

1. Anders S. et al. (2014) HTSeq — a Python framework to work with
   high-throughput sequencing data.
2. Chang W. et al. (2016) shiny: Web Application Framework for R.
3. Johnson W.E. et al. (2007) Adjusting batch effects in microarray expression
   data using empirical Bayes methods. *Biostatistics* 8, 118–127.
4. Love M.I. et al. (2014) Moderated estimation of fold change and dispersion for
   RNA-seq data with DESeq2. *Genome Biol.* 15, 550.
5. Murtagh F. and Legendre P. (2014) Ward's hierarchical agglomerative clustering
   method. *J. Classification* 31.
6. Ritchie M.E. et al. (2015) limma powers differential expression analyses for
   RNA-sequencing and microarray studies. *Nucleic Acids Res.* 43, e47.
7. Robinson M.D. et al. (2010) edgeR: a Bioconductor package for differential
   expression analysis of digital gene expression data. *Bioinformatics* 26,
   139–140.
8. Vernia S. et al. (2014) The PPARα-FGF21 hormone axis contributes to metabolic
   regulation by the hepatic JNK signaling pathway. *Cell Metab.* 20, 512–525.
