******************
Installation Guide
******************

Before you start; you will have to install R and/or RStudio.
You can install DEBrowser from bioconductor or from the source code. Install the required dependencies by running the following commands in R or RStudio. 
Please check *Operating System Dependencies* section, in case your operating system requires packages to be installed.

**A.1 Bioconductor Installation** (Recommended)::

    source("https://www.bioconductor.org/biocLite.R")
    biocLite("debrowser")

**A.2 Bioconductor Installation - Developer Version**::
    
    if (!requireNamespace("BiocManager", quietly=TRUE))
    install.packages("BiocManager")
    BiocManager::install("debrowser", version = "devel")

**B. Installation instructions from source code**::

    install.packages("devtools") ## If you haven't installed devtools, you can easily install it by using this command 
    library("devtools")
    install_github("UMMS-Biocore/debrowser", build_vignettes = TRUE)
        
Alternatively, you can download the source code from `here <https://github.com/UMMS-Biocore/debrowser>`_ as a compressed format. Then you need to decompress and install with following command::
    
    R CMD INSTALL debrowser-develop  ##where folder name is debrowser-develop
    
-----

After debrowser installation, you can load and start DEBrowser by following commands::

        library(debrowser)
        startDEBrowser()

Once you run ``startDEBrowser()`` shiny will launch a web browser which is ready to use!

For more information about DEBrowser, please visit our **Quick-start Guide** section within documentation.

Operating System Dependencies
=============================

On Fedora/Red Hat/CentOS, these packages have to be installed::
    
    openssl-devel, libxml2-devel, libcurl-devel, libpng-devel

On Ubuntu 18.04 LTS, you can install required packages by following command::

    sudo apt-get install libcurl4-openssl-dev libssl-dev libv8-3.14-dev udunits-bin libudunits2-* libxml2-dev 
