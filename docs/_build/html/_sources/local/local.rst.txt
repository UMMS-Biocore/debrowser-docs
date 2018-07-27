******************
Installation Guide
******************


Running these simple commands will launch the DEBrowser within your local
machine.

Before you start;
First, you will have to install R and/or RStudio.
(On Fedora/Red Hat/CentOS, these packages have to be installed;
openssl-devel, libxml2-devel, libcurl-devel, libpng-devel)

You can install DEBrowser from bioconductor or from the source code. Install the required dependencies by running the following commands in R or RStudio. 

**A. Bioconductor Installation**::

    source("https://www.bioconductor.org/biocLite.R")
    biocLite("debrowser")

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
