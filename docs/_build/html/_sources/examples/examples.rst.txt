********
Examples
********

This guide is walkthrough for the preparation of figures which is used in DEBrowser paper. PCA, Heatmap, All2All will be plotted as an example for QC plots. Next, differential expression analysis will be conducted and their results will be visualized with Main plots such as **Scatter**, **Volcano** and **MA**. More detailed analysis will be covered by using simultaneously created Heatmap and KEGG pathway on the selected portion of the data.

QC plots without Batch Effect Correction
========================================

    1) **Upload Data:** To begin the analysis, you need to load Demo Data by clicking **Load Demo (Donnard et al)!** button. Then click on **Filter** button to start **Low Count Filtering**. 
    2) **Low Count Filtering:** Filtering method is selected as **Max** with cutoff 10 (which filter genes where maximum count for each gene across all samples are less than 10) and activated by clicking **Filter** button which is located at the center of the page. After filtration you can see the distribution of the data as shown at below. Now, you can proceed by clicking **Batch Effect Correction** button.
    
    .. image:: ../debrowser_pics2/example_filtering.png
	:align: center
	:width: 99%
    
    3) **Batch Effect Correction and Normalization:**  Following options were selected to normalize the data: 
        
        * **Normalization method:** MRN
        * **Correction Method:** None
        
    In order to adjust the appearance, use PCA controls which is located between two PCA plots.
    
        * **Text On/Off:** On
        * **Select legend:** color
        * **Color field:** batch
        * **Shape field:** batch
        
    .. image:: ../debrowser_pics2/example_pca_before_batch.png
	:align: center
	:width: 60%
	
    4) **All2All:**  After batch effect correction, you can click 'Go to QC plots!' to view quality control metrics on your data. The page opens with a Principal Component Analysis (PCA) plot. You can select **All2All** option from **Plot type** on the left sidebar menu. In order to get the figure as shown at below, you need to adjust other parameters of **plot options**    on the left sidebar menu.
    
    .. image:: ../debrowser_pics2/example_all2all_before.png
	   :align: center
	   :width: 55%    
    
    * **All2All - Plot Options:** Following options are selected and their screenshots are shown at below.

        * **Plot Type:** All2All
        * **Data Options:** Choose a dataset: all-detected
        * **QC options - all2all - Size & Margins:** Check the box of the **Plot Size** and adjust width and height as 800 and 800, respectively.
        * **QC options - all2all - Options:**  corr font size: 1.8 (adjust the font size of the text inside the box)

        
    .. image:: ../debrowser_pics2/example_all2all_menu.png
	   :align: center
	   :width: 40% 
    
    5) **Heatmap:**  To visualize heatmap as shown at below, please select **Heatmap** option from **Plot type** on the left sidebar menu and adjust plot options. 

    .. image:: ../debrowser_pics2/example_heatmap_before.png
	   :align: center
	   :width: 40%

    * **Heatmap - Plot Options:** Similar to All2All plot, we need to adjust plotting options on the left sidebar menu.

        * **Plot Type:** Heatmap
        * **Heatmap Colors:** Check the box of custom colors.
        * **Data Options:** Choose a dataset: most varied, top-n:1000, total min count:100 (to show the top 1000 most varied genes (based on coefficient of variance) whose total counts are higher than 100)
        * **QC options - kmeans:** Check the box of kmeans clustering. Select 7 as # of clusters. You might need to change the order of the clusters and click **change order** button to get gradual changes on heatmap as in the figure.
        * **QC options - heatmap - Size & Margins:** Check the box of the **Plot Size** and adjust width and height to 690 and 1200, respectively.
        
    .. image:: ../debrowser_pics2/example_heatmap_menu.png
	   :align: center

QC plots after Batch Effect Correction
======================================

Since we finalized out plots without applying batch effect correction, we can return back to batch effect correction step and change the **Correction Method** as **Combat** and continue to create new graphs with the same parameters as we used before. To make it more user friendly, we are going to start explain these steps from the beginning. If you choose to continue from batch effect correction, please skip first two steps and continue reading from 3rd step: **Batch Effect Correction and Normalization**. 

    1) **Upload Data:** To begin the analysis, load Demo Data by clicking **Load Demo (Donnard et al)!** button. Then click on **Filter** button to start **Low Count Filtering**. 
    2) **Low Count Filtering:** Select **Max** method with cutoff 10 (which filter genes where maximum count for each gene across all samples are less than 10), then click **Filter** button which is located at the center of the page. After filtration, proceed to next step by clicking **Batch Effect Correction** button.
    
    3) **Batch Effect Correction and Normalization:**  Following options were selected to apply both normalization and batch effect correction: 
        
        * **Normalization method:** MRN
        * **Correction Method:** Combat
        * **Treatment:** treatment
        * **Batch:** batch
        
    Please adjust PCA controls (which is located between two PCA plots) as listed below.
    
        * **Text On/Off:** On
        * **Select legend:** color
        * **Color field:** batch
        * **Shape field:** batch
        
    .. image:: ../debrowser_pics2/example_pca_after_batch.png
	:align: center
	:width: 60%
	
    4) **All2All:**  After batch effect correction, click 'Go to QC plots!' and select **All2All** option from **Plot type** on the left sidebar menu. Please adjust All2All - Plot Options as listed below.
    
    .. image:: ../debrowser_pics2/example_all2all_after.png
	   :align: center
	   :width: 55%    
    
    * **All2All - Plot Options:**

        * **Plot Type:** All2All
        * **Data Options:** Choose a dataset: all-detected
        * **QC options - all2all - Size & Margins:** Check the box of the **Plot Size** and adjust width and height to 800 and 800, respectively.
        * **QC options - all2all - Options:**  corr font size: 1.8 
        
    .. image:: ../debrowser_pics2/example_all2all_menu.png
	   :align: center
	   :width: 40%
    
    5) **Heatmap:**  Please select **Heatmap** option from **Plot type** on the left sidebar menu and adjust plot options according to the list below.

    .. image:: ../debrowser_pics2/example_heatmap_after.png
	   :align: center
	   :width: 40%

    * **Heatmap - Plot Options:** 

        * **Plot Type:** Heatmap
        * **Heatmap Colors:** Check the box of custom colors.
        * **Data Options:** Choose a dataset: most varied, top-n:1000, total min count:100 (to show the top 1000 most varied genes (based on coefficient of variance) whose total counts are higher than 100)
        * **QC options - kmeans:** Check the box of kmeans clustering. Select 7 as # of clusters. You might need to change the order of the clusters and click **change order** button to get gradual changes on heatmap as in the figure.
        * **QC options - heatmap - Size & Margins:** Check the box of the **Plot Size** and adjust width and height to 690 and 1200, respectively.
        
    .. image:: ../debrowser_pics2/example_heatmap_menu.png
	   :align: center



The Differential Expression Plots
=================================

    1) **Upload Data:** To begin the analysis, load Count Data by clicking **Load Demo (Vernia et. al)!** button. Then click on **Filter** button to start **Low Count Filtering**. 
    2) **Low Count Filtering:** Select **Max** method with cutoff 10 (which filter genes where maximum count for each gene across all samples are less than 10), then click **Filter** button which is located at the center of the page. Proceed to next step by clicking **Batch Effect Correction** button.
    3) **Batch Effect Correction and Normalization:**  We are going to skip both normalization and batch effect correction by selecting following options: 
        
        * **Normalization method:** None
        * **Correction Method:** None
        
    4) **DE Analysis:**  After batch effect correction, click 'Go to DE Analysis'. In this page, we will add groups for comparison. Click on **Add New Comparison** button and select **Select Meta** as **treatment**. It will automatically separate experiment and control data into two groups. You can leave other parameters as default as listed below and click "Submit" button.
    
        * **DE method:** DESeq2
        * **Fit Type:** parametric
        * **betaPrior:** FALSE
        * **Test Type:** Wald
    
    .. image:: ../debrowser_pics2/example_DE_form.png
	   :align: center
	   :width: 90%

    5) **Main Plots Analysis:** Upon finishing the DESeq analysis, you will see DE Results in table format. Please click on **Go to Main Plots!** button which will open **Scatter Plot**. You can switch to **Volcano Plot** and **MA Plot** by using **Plot Type** section at the left side of the menu. Since these plots are interactive, you can click to **zoom** button on the top of the graph and select the area you would like to zoom in by drawing a rectangle. Please see the plots at below:

    .. image:: ../debrowser_pics2/example_main_plots.png
       :align: center
       :width: 99%
    
    Please keep in mind that to increace the performance of the generating graph, by default 10% of non-significant(NS) genes are used to generate plots. We used all of the NS genes in our plots that showed above, therefore please click **Main Options** button and change Background Data(%) to 100% on the left sidebar.
    
    .. image:: ../debrowser_pics2/example_background_data.png
       :align: center
       :width: 30%
    
    6) **Read count plots:** Lets return back to **Scatter Plot** by using **Plot Type** section. You can hover on each point on the graph to see their read counts as a bar graph as shown at below. In this example FABP3 is selected to show the high variance of this gene across samples.

    .. image:: ../debrowser_pics2/example_scatter_hover.png
       :align: center
       :width: 99%
       
    If you want to mark FABP3 gene on the plot, click on Data Options and enter **FABP3** in to the **search field** as showed below. You will see green mark on the plot that shows FABP3.
    
    .. image:: ../debrowser_pics2/example_scatter_search.png
       :align: center
       :width: 30%

    7) **Lasso selection:** DEBrowser can draw heatmaps of any selected region of any main plot. Selection can be made in a rectangular form or as a free-form using plotly’s lasso select. To do so, first click **NS** label at the upper right side of the figure, and hide non-significant genes. Then click on lasso select button at the top of the plot and select the genes you're interested as shown at below. Heatmap will appear just next to scatter plot. Additionally, you can activate interactive mapping option for heatmap by clicking **Interactive** button under **Heatmap Options** on the left sidebar menu. Now, you can hover on the each block of heatmap to see gene name and its value.
    
    .. tip::
    
        **Interactive Feature:** In order to increase the performance of the generating heatmaps, **interactive** option is disabled by default. After deciding plotting/clustering parameters of the heatmap, you might activate this feature to investigate each block in detail.
    
    .. image:: ../debrowser_pics2/example_scatter_lasso.png
       :align: center
       :width: 60%
       
    .. image:: ../debrowser_pics2/example_scatter_lasso_heatmap.png
       :align: center
       :width: 99%
    
    8) **Scatter plot of the genes enriched in insulin signalling pathway:** In this example, we will highlight genes enriched in insulin signalling pathway. If you already hid NS genes, you can show them by clicking on the **NS** label at the upper right side of the figure. Click on the **Data Options** and enter following genes in to the **search field**:: 
    
        Cbl
        Sos1
        Irs2
        Insr
        Ptprf
        Tsc1
        Crkl
        Prkar2a
        Acaca
        Fasn
        Mapk8
        Ppp1r3b
        Ppp1r3c
        Srebf1
        Pklr
        Pik3r1
        Pygl
        Pik3r3
        Socs4
        Socs2
        Eif4ebp1
        
    .. tip::
    
        If you enter more than three lines of genes, search tool will automatically match the beginning and end of the search phrases. Otherwise it will find matched substrings in the gene list.
        
        
    Now, you will see green marks on the **searched genes** as shown below:
    
    .. image:: ../debrowser_pics2/example_scatter_insulin_A.png
       :align: center
       :width: 60%
    
    Lets, hide all the genes other then **searched genes** by clicking **NS**, **Up** and **Down** labels at the upper right side of the figure. Since only the selected genes are left on the graph, we can select these genes by clicking on **Select Box** icon and drawing a rectangle which covers all of these genes.  

    .. image:: ../debrowser_pics2/example_scatter_insulin_select.png
       :align: center
       :width: 60%
    
    Here as shown below, heatmap will be simultaneously created just next to scatter plot. You might need to change plot margins as following: 
    
    * **Heatmap options -> heatmap - Size & Margins:** Please check the box of the **Plot Size** and adjust width and height to 580 and 500, respectively. 
    
     .. image:: ../debrowser_pics2/example_scatter_insulin_before_norm.png
       :align: center
       :width: 60%    
    
    Since the data is not normalized, data of exper_rep3 looks like it belongs to control group. We strongly recommend normalization before plotting subset of genes. To normalize, please change the parameters as described below and see the updated figure at below:
    
    * **Data options -> Normalization Methods:** Please select **MRN** from the dropdown box.
    
    .. image:: ../debrowser_pics2/example_scatter_insulin_B.png
       :align: center
       :width: 60%  
    
    
    

Activating **Interactive** feature changes the heatmap into an interactive version with two colors, allowing you to select specific genes to be compared
within the GO term plots.  

GO Term Plots
=============

The next tab, 'GO Term', takes you to the ontology comparison portion of DEBrowser.  From here you can select the standard dataset options such as p-adjust value, fold change cut off value, which comparison set to use, and which dataset to use on the left menu.  In addition to these parameters, you also can choose from the 4 different ontology plot options: 'enrichGO','enrichKEGG', 'Disease', and 'compareCluster'.  Selecting one of these plot options queries their specific databases with your current DESeq results.

.. image:: ../debrowser_pics/go_plots_opts.png
	:align: center

Your GO plots include:

* enrichGO - use enriched GO terms
* enrichKEGG - use enriched KEGG terms
* Disease - enriched for diseases
* compareClusters - comparison of your clustered data

The types of plots you will be able to generate include:

Summary plot:

.. image:: ../debrowser_pics/go_summary.png
	:align: center

GOdotplot:

.. image:: ../debrowser_pics/go_dot_plot.png
	:align: center

Changing the type of ontology to use will also produce custom parameters for that specific ontology at the bottom of the
left option panel.

Once you have adjusted all of your parameters, you may hit the submit button in the top right and then wait
for the results to show on screen!


Log2 fold change comparison for PPARα pathway
=============================================
    
    1) **Upload Data:** To begin the analysis, download `full dataset (Vernia et. al)`_ and `full metadata`_ on your computer. Then click **browse** button, and select downloaded files from your computer. Please keep **Separator** as **Tab** while this processes. Finally click **upload** button to see **Upload Summary**. Now you can click on **Filter** button to start **Low Count Filtering**.

    .. _full dataset (Vernia et. al): https://bioinfo.umassmed.edu/pub/debrowser/advanced_demo.tsv
    .. _full metadata: https://bioinfo.umassmed.edu/pub/debrowser/advanced_meta.tsv
    

    2) **Low Count Filtering:** Select **Max** method with cutoff 10 (which filter genes where maximum count for each gene across all samples are less than 10), then click **Filter** button which is located at the center of the page. We are going to skip normalization and batch effect correction step by clicking 'Go to DE Analysis' button.
        
    3) **DE Analysis:**  In this page, we will add multiple groups for comparison. Click on **Add New Comparison** button and select **Select Meta** as **Cond1**. Repeat this step for **Cond2** and **Cond3** and add two more comparisons. It will automatically separate experiment and control data into two groups. You can leave other parameters as default as listed below and click "Submit" button.
    
        * **DE method:** DESeq2
        * **Fit Type:** parametric
        * **betaPrior:** FALSE
        * **Test Type:** Wald
    
    .. image:: ../debrowser_pics2/example_multi_cond.png
	   :align: center
	   :width: 70%
    
    4) **Downloading fold2Change data of selected genes**: Upon finishing the DE analysis, you will see DE Results in table format. Please click on **Go to Main Plots!** button which will open **Scatter Plot**. On the left sidebar menu, click **Data options* tab and enter following genes regarding to PPARα pathway::
    
        Cyp4a12b
        Cyp4a14
        Ehhadh
        Cyp8b1
        Cpt1b
        Cyp7b1
        Slc27a1
        Apoa5
        Pdpk1
        Apoa1
        Acadl
        Fads2
        Fabp4
        Acadm
        Apoa2
        Apoc3
        Fgf21
        Fabp5
        Fabp3
        Lpl
        Dbi
        Nr1h3
        Fabp7
        Ppara
        Ucp1
        Sdc1
        Sdc3
        Sdc2
        Fabp2
       
    Afterwards, select **comparison** option for the **Choose a dataset** field. This option will add fold change columns to to our data.
    
    Now, we need to disable filtration to get all searched genes in our dataset. To do so, enter following parameters into **Filter** field on the left sidebar menu.
       
        * **padj:** 1
        * **foldChange:** 1
       
    To confirm you can check all adjusted parameters at image below. 
    
    .. image:: ../debrowser_pics2/example_fold_selection.png
	   :align: center
	   :width: 30%
       
    It is time to download our dataset by clicking **Download Data** button on the **Data Options** field. You can open downloaded tsv file in Excel or similar programs. Once you open the file, you will see columns of count data, padj and fold2Change for all comparisons. Since we are only interested in fold2Change columns, you can delete the rest. Final data file should look like image on the left at below. 
    
    We will rename column names as follows and add new column called **chow.wt** which compares chow.wildtype with itself therefore it is filled with 1. 
    
        * **foldChange.C1.vs.C2** to chow.dbl
        * **foldChange.C3.vs.C4** to hfd.wt
        * **foldChange.C5.vs.C6** to hfd.dbl
        
    To confirm you can also download the final version of the fold2data from `this link`_.
    
    .. _this link: https://bioinfo.umassmed.edu/pub/debrowser/comparisons.tsv
    
    .. image:: ../debrowser_pics2/example_table_conversion.png
	   :align: center
	   :width: 70%
    
    5) **Creating Heatmap for fold2change data**: To create heatmap for fold change data, you have two options: A. Using startHeatmap() function or B. Use DEBrowser Heatmap module.
    
        * A. Open new R session and run following command in R or R Studio to run Heatmap module in web browser::
            
                startHeatmap()
            
        Similar to DEBrowser, you can click **browse** button, and select prepared log2change file from your computer. Please keep **Separator** as **Tab**. Finally click **upload** button to see **Upload Summary**. 
    
        * B. Open new R session and run following command in R or R Studio to load dataset as data frame (comparisons)::
    
                comparisons <- read.delim("~/Downloads/comparisons.tsv", row.names=1)
        
            You may need to change the path of the file according to your folder structure. Now, in order to open heatmap module, you need to run following script::
        
                library(debrowser)
                library(DESeq2)
                library(heatmaply)
                library(RColorBrewer)
                library(gplots)
                
                options(warn=-1)
                header <- dashboardHeader(title = "DEBrowser Heatmap")
                sidebar <- dashboardSidebar(  getJSLine(), sidebarMenu(id="DataAssessment",
                    menuItem("Heatmap", tabName = "Heatmap"),
                    plotSizeMarginsUI("heatmap"),
                    heatmapControlsUI("heatmap")))
                body <- dashboardBody(
                    tabItems(
                    tabItem(tabName="Heatmap",  getHeatmapUI("heatmap"),
                        column(4, verbatimTextOutput("heatmap_hover"), verbatimTextOutput("heatmap_selected")
                        )
                    )
                ))
            
                ui <- dashboardPage(header, sidebar, body, skin = "blue")
            
                server <- function(input, output, session) {
                selected <- reactiveVal()
                observe({
                    withProgress(message = 'Creating plot', style = "notification", value = 0.1, {
                    selected(callModule(debrowserheatmap, "heatmap", comparisons))
                    })
                })
                output$heatmap_hover <- renderPrint({
                    if (!is.null(selected()) && !is.null(selected()$shgClicked()) && selected()$shgClicked() != "")
                        return(paste0("Clicked: ",selected()$shgClicked()))
                    else
                        return(paste0("Hovered:", selected()$shg()))
                })
                output$heatmap_selected <- renderPrint({
                    if (!is.null(selected()))
                        selected()$selGenes()
                })
                }
            
                shinyApp(ui, server)
        
        
    Shiny will launch a web browser which is ready to use as a heatmap module. You need to specify following parameters to create log2fold change graph:
        
            * **Interactive:** Checked
            * **Custom Colors:** Checked
            * **Custom Colors -> Choose min colour:** #33FF00
            * **Custom Colors -> Choose median colour:** #000000
            * **Custom Colors -> Choose max colour:** #FF0000
            * **Heatmap Dendrogram -> Type:** none
            * **Scale Options -> Scale:** Checked
            * **Scale Options -> Center:** Unchecked
            * **Scale Options -> Log:** Checked
            * **Scale Options -> Pseudo Count:** 0
            
    Once you specify these parameters, your heatmap will be seen as image at below.

    .. image:: ../debrowser_pics2/example_log_heatmap.png
	   :align: center
	   :width: 70%
       
        
            
            
    
    

