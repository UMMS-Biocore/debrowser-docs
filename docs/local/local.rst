******************
Installation Guide
******************

Before you start, install R and (optionally) RStudio. You can install DEBrowser
from Bioconductor or from source. See *Operating System Dependencies* below if
your OS is missing system libraries.

**A.1 Bioconductor (recommended)**::

    if (!requireNamespace("BiocManager", quietly = TRUE))
        install.packages("BiocManager")
    BiocManager::install("debrowser")

**A.2 Bioconductor — development version**::

    if (!requireNamespace("BiocManager", quietly = TRUE))
        install.packages("BiocManager")
    BiocManager::install("debrowser", version = "devel")

**B. From source**::

    install.packages("devtools")   # if not already installed
    library("devtools")
    install_github("UMMS-Biocore/debrowser", build_vignettes = TRUE)

Alternatively, download the source from
`GitHub <https://github.com/UMMS-Biocore/debrowser>`_, decompress it, and
install::

    R CMD INSTALL debrowser-develop   # where the folder is debrowser-develop

-----

After installation, load and start DEBrowser::

    library(debrowser)
    startDEBrowser()

``startDEBrowser()`` launches the app in your browser on port ``3838`` (which
keeps bookmark URLs stable across restarts). Continue with the
:doc:`Quick-start Guide <../quickstart/quickstart>`.

.. note::

    The optional **AI interpretation** features depend on three additional
    packages. Install them once if you plan to use AI::

        install.packages(c("ellmer", "whisker", "keyring"))

    DEBrowser works fully without them; AI simply stays unavailable.

Operating System Dependencies
=============================

On Fedora / Red Hat / CentOS::

    openssl-devel libxml2-devel libcurl-devel libpng-devel

On Ubuntu / Debian::

    sudo apt-get install libcurl4-openssl-dev libssl-dev \
        libxml2-dev libudunits2-dev
