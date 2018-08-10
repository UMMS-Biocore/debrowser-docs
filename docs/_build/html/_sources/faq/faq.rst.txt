********************************
Frequently asked questions (FAQ)
********************************

Why un-normalized counts?
=========================
DESeq2 requires count data as input obtained from RNA-Seq or another high-thorughput sequencing experiment in the form of matrix values. Here we convert un-integer values to integer to be able to run DESeq2. The matrix values should be un-normalized, since DESeq2 model internally corrects for library size. So, transformed or normalized values such as counts scaled by library size should not be used as input. Please use edgeR or limma for normalized counts.

Why am I getting error while uploading files? 
=============================================
* DEBrowser supports tab, comma or semi-colon separated files. However spaces or characters in numeric regions not supported and causes an error while uploading files. It is crutial to remove these kind of instances from the files before uploading files.  

* Another reason of getting an error is using same gene name multiple times. This may occurs after opening files in programs such as Excel, which tends to automatically convert some gene names to dates (eg. SEP9 to SEP.09.2018). This leads numerous problems therefore you need to disable these kind of automatic conversion before opening files in these kind of programs.

* Some files contain both tab and space as an delimiter which lead to error. It is required to be cleaned from these kind of files before loading.

Why some columns not showed up after upload?
============================================
If a character in numeric area or space is exist in one of your column, either column will be eliminated or you will get an error. Therefore it is crutial to remove for these kind of instances from your files before uploading.

Why am I getting error while uploading CSV/TSV files exported from Excel?
=========================================================================
* You might getting an error, because of using same gene name multiple times. This may occurs after opening files in programs such as Excel, which tends to automatically convert some gene names to dates (eg. SEP9 to SEP.09.2018). Therefore you need to disable these kind of automatic conversion before opening files in these kind of programs.

Why can't I see all the background data in Main Plots?
======================================================
In order to increase the performance, by default 10% of non-significant(NS) genes are used to generate plots. We strongly suggest you to use all of the NS genes in your plots while publishing your results. You can easily change this parameter by clicking **Main Options** button and change Background Data(%) to 100% on the left sidebar.

Why am I getting error when I click on **DE Genes** in Go Term Analysis?
========================================================================
To start **Go Term** analysis, it is important to select correct organism from **Choose an organism** field. After selecting other desired parameters, you can click **Submit** button to run Go Term analysis. After this stage, you will able to see **categories** regarding to your selected gene list in the **Table** Tab. Once you select this category, you can click DE Genes button to see gene list regarding to selected category. 

How to download selected data from Main plots/QC Plots/Heatmaps?
================================================================
First, you need to choose **Choose dataset** field as **selected** under **Data Options** in the left sidebar. When you select this option, new field: **The plot used in selection** will appear under **Choose dataset** field. You need to specify the plot you are interested from following options: Main plot, Main Heatmap, QC Heatmap. Finally you can click **Download Data** button to download data, or if you wish to see the selected data, you can click **Tables** tab. 


