********************************
Frequently Asked Questions (FAQ)
********************************

Why un-normalized counts?
=========================
DESeq2 requires count data from RNA-Seq (or another high-throughput sequencing
experiment) as a matrix of raw values. Non-integer values are converted to
integers so DESeq2 can run. The values must be **un-normalized**, since the
DESeq2 model corrects for library size internally — do not use counts scaled by
library size. For already-normalized counts, use edgeR or limma instead.

Why am I getting an error while uploading files?
================================================
* DEBrowser supports tab-, comma-, or semicolon-separated files. Spaces or
  non-numeric characters inside numeric columns cause upload errors — remove
  them first.
* Using the **same gene name more than once** also fails. This often happens
  after opening a file in Excel, which auto-converts some gene names to dates
  (e.g. ``SEP9`` → ``SEP.09.2018``). Disable that conversion before opening such
  files.
* Files that mix tabs and spaces as delimiters need to be cleaned before
  loading.

Why did some columns not show up after upload?
==============================================
If a numeric column contains a non-numeric character or a space, that column is
dropped (or the upload errors). Clean these values before uploading.

Why can't I see all the background data in Main Plots?
======================================================
To keep plotting fast, only 10% of non-significant (NS) genes are drawn by
default. For publication figures, open **Main Options** on the left and set
**Background Data (%)** to 100%.

Why do I get an error when I click **DE Genes** in the Enrichment tab?
=============================================================================
Enrichment needs the correct **organism** selected first. Choose it, set your
other parameters, and click **Submit**. The enriched **categories** then appear
on the **Tables** tab; select a category and click **DE Genes** to see the genes
behind it.

How do I download selected data from Main Plots / QC Plots / Heatmaps?
=============================================================================
Set **Choose dataset** to **selected** under **Data Options** on the left. A new
field, **The plot used in selection**, appears — pick Main plot, Main Heatmap, or
QC Heatmap. Then click **Download Data**, or open the **Tables** tab to view the
selection.

How do I switch between light and dark mode?
============================================
Click the moon/sun button in the top-right of the navbar, or press ``T``. The
choice persists across the session. You can also jump between the six top-level
tabs with the number keys ``1``–``6`` (shortcuts are ignored while you are typing
in a field).

Can I save or share an analysis?
================================
Yes. Click **Bookmark** (top-right) to capture the full analysis state behind a
stable URL you can revisit or share. For a portable record, use the **Export**
menu to download the session as an R script, R Markdown / HTML, a Jupyter
notebook, or a ready-to-paste methods paragraph.

Is the AI assistant safe to use with sensitive data?
====================================================
AI features are **off by default** and make no network calls until you enable
them and choose a provider. For maximum privacy, use the local **Ollama**
provider — the model runs entirely on your machine and no data leaves it. Even
with a cloud provider, per-call privacy modes let you send only gene symbols, and
API keys are stored in your OS keychain via ``keyring``, never in plaintext.
