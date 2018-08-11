*****************
DEBrowser Modules
*****************

Debrowser is created with moduler structure which allows user to run each module separately. In this guide, you can find explanation about structure of  modules and how to run each module.  

Demo Data
=========

To start with, you need to create following variables: ``demodata`` and ``metadatatable`` by using your data and save as ``demodata.Rda``. The structure of these variables showed at below::

    > head (demodata)
                   exper_rep1 exper_rep2 exper_rep3 control_rep1 control_rep2 control_rep3
    AK212155       0.00       0.00          0          0.0            0            0
    Sp2           52.00      47.00         36         99.0           53           66
    AK051368       4.39       1.11          0          1.1            0            0
    Ubiad1       121.00     125.00         65        134.0           95          111
    Src           21.00      35.00         20         43.0           22           32
    Racgap1        9.00      20.00         11         14.0           10            7
    
    > head (metadatatable)
      samples          treatment batch
    1   exper_rep1     cond1     1
    2   exper_rep2     cond1     2
    3   exper_rep3     cond1     1
    4 control_rep1     cond2     2
    5 control_rep2     cond2     1
    6 control_rep3     cond2     2


One way to import tsv files is showed at below::
    
    demodata  <- read.table("~/Downloads/shKRAS.tsv", header=T, row.names=1, sep="\t")
    
Now we can run each modules separately through R studio by clicking **Run App** button.

Example Modules
===============

You can reach `demo data`_ and latest versions of modules through our `github page.`_ 

.. _github page.: https://github.com/UMMS-Biocore/debrowser_bioconductor_release/tree/develop/inst/examples
.. _demo data: https://github.com/UMMS-Biocore/debrowser_bioconductor_release/tree/develop/inst/extdata/demo

Barmain plot::

    library(debrowser)
    options(warn =-1)
    header <- dashboardHeader( title = "DEBrowser Bar Plots" )
    
    sidebar <- dashboardSidebar(
        sidebarMenu(
            id="DEAnlysis",
            menuItem("BarMain", tabName = "BarMain"),
            textInput("genename", "Gene/Region Name", value = "Foxa3"),
            plotSizeMarginsUI("barmain", h=400)
        )
    )

    body <- dashboardBody(
        tabItems(
            tabItem(
                tabName="BarMain", 
                fluidRow(column(12,getBarMainPlotUI("barmain")))
            )
        )
    )

    ui <- dashboardPage(header, sidebar, body, skin = "blue")

    server <- function(input, output, session) {
        load(system.file("extdata", "demo", "demodata.Rda", package = "debrowser"))
            observe({
                if (!is.null(input$genename))
                    callModule(debrowserbarmainplot, "barmain", demodata, metadatatable$sample, metadatatable$treatment, input$genename) 
                })
    }
            
    shinyApp(ui, server)
    

The example module is created with UI and Server with ``shinyApp(ui, server)`` command. Similarly UI structure is defined with the ``ui <- dashboardPage(header, sidebar, body, skin = "blue")`` command. You can simply follow the structure of UI which is created by four variables: ``header``, ``sidebar``, ``body`` and ``skin``. In the server function, ``demodata``, ``metadatatable`` variables are loaded from ``demodata.Rda``, and debrowserbarmainplot module is called with ``callModule`` function.
    
Main Plots::

    library(plotly)
    library(debrowser)
    header <- dashboardHeader(title = "DEBrowser Main Plots")
    sidebar <- dashboardSidebar(  sidebarMenu(id="DEAnalysis",
        menuItem("Main", tabName = "Main"),
        mainPlotControlsUI("main"),
        plotSizeMarginsUI("main")))
        
    body <- dashboardBody(
        tabItems(
            tabItem(tabName="Main", getMainPlotUI("main"),
                column(4,
                       verbatimTextOutput("main_hover"),
                       verbatimTextOutput("main_selected")
                )
            )
        )
    )

    ui <- dashboardPage(header, sidebar, body, skin = "blue")

    server <- function(input, output, session) {
        #Example usage with demodata
        load(system.file("extdata", "demo", "demodata.Rda",
                     package = "debrowser"))
        dat <-c()
        dat$columns <- c("exper_rep1", "exper_rep2", "exper_rep3",
                        "control_rep1", "control_rep2", "control_rep3")
        dat$conds <- factor( c("Control", "Control", "Control",
                        "Treat", "Treat", "Treat") )
        dat$data <- data.frame(demodata[, dat$columns])
    
        # You can also use your dataset by reading your data from a file like below;
        # The data in this commented out example is not supplied but these lines 
        # can give you an idea about how to read the data from a file;
        #
        # data  <- read.table("~/Downloads/shKRAS.tsv", header=T, row.names=1, sep="\t")
        # dat$columns <- c("CNT.2", "CNT.3", "CNT.4", 
        #               "shKRAS_T1", "shKRAS_T2", "shKRAS_T3")
        # dat$conds <- factor( c("Control", "Control", "Control",
        #                        "shKRAS", "shKRAS", "shKRAS") )
        # dat$data <- data.frame(data[, dat$columns])
        #
        xdata <- generateTestData(dat)
        selected <- callModule(debrowsermainplot, "main", xdata)
    
        output$main_hover <- renderPrint({
            selected$shgClicked()
        })
        output$main_selected <- renderPrint({
            selected$selGenes()
        })
    }
    shinyApp(ui, server)

PCA plot::
    
    library(debrowser)
    header <- dashboardHeader(title = "DEBrowser PCA Plots")
    
    sidebar <- dashboardSidebar(  
        sidebarMenu(id="DataAssessment",
        menuItem("PCA", tabName = "PCA"),
        menuItem("PCA Options",
        pcaPlotControlsUI("pca")),
        plotSizeMarginsUI("pca", w=600, h=400, t=50, b=50, l=60, r=0)
    ))

    body <- dashboardBody(
                tabItems(
                    tabItem(tabName="PCA", getPCAPlotUI("pca"),
                        column(4,
                            verbatimTextOutput("pca_hover"),
                            verbatimTextOutput("pca_selected")
                        )
                    )
                )   
            )

    ui <- shinydashboard::dashboardPage(header, sidebar, body, skin = "blue")

    server <- function(input, output, session) {
        load(system.file("extdata", "demo", "demodata.Rda", package = "debrowser"))
        selected <- callModule(debrowserpcaplot, "pca", demodata)
    }

    shinyApp(ui, server)
    
All2All Plot::

    library(debrowser)
    options(warn =-1)
    header <- dashboardHeader( title = "DEBrowser All2All Plots")
    sidebar <- dashboardSidebar(  sidebarMenu(id="DEAnlysis",
        menuItem("All2All", tabName = "All2All"),
        plotSizeMarginsUI("all2all", h=800, w=800),
        all2allControlsUI("all2all")
        )
    )

    body <- dashboardBody(
            tabItems(
                tabItem(tabName="All2All", 
                    fluidRow(column(12,getAll2AllPlotUI("all2all")))
                )
            )
        )

    ui <- dashboardPage(header, sidebar, body, skin = "blue")

    server <- function(input, output, session) {
        load(system.file("extdata", "demo", "demodata.Rda",package = "debrowser"))
        observe({
            callModule(debrowserall2all, "all2all", demodata, input$cex)
        })
        }

    shinyApp(ui, server)
    
Batch Effect Module:: 

    library(debrowser)
    options(warn =-1)
    header <- dashboardHeader(title = "DEBrowser Batch Effect")
    sidebar <- dashboardSidebar(sidebarMenu(id="DataPrep", 
        menuItem("BatchEffect", tabName = "BatchEffect")
        )
    )
    body <- dashboardBody(
        tabItems(
            tabItem(tabName="BatchEffect", batchEffectUI("batcheffect"),
                column(4,
                       verbatimTextOutput("batcheffecttable")
                )
            )
        )   
    )

    ui <- dashboardPage(header, sidebar, body, skin = "blue")

    server <- function(input, output, session) {
        load(system.file("extdata", "demo", "demodata.Rda", package = "debrowser"))
        ldata <- reactiveValues(count=NULL, meta=NULL)
        ldata$count <- demodata
        ldata$meta <- metadatatable
        data <- callModule(debrowserbatcheffect, "batcheffect", ldata)
        observe({
            output$batcheffecttable <- renderPrint({
                head( data$BatchEffect()$count )
            })
        })
    }

    shinyApp(ui, server)

Main Box plot::

    library(debrowser)
    library(plotly)
    options(warn =-1)

    header <- dashboardHeader(title = "DEBrowser Box Plots")
    sidebar <- dashboardSidebar(  sidebarMenu(id="DEAnlysis",
        menuItem("BoxMain", tabName = "BoxMain"),
        textInput("genename", "Gene/Region Name", value = "Foxa3" ),
        plotSizeMarginsUI("boxmain", h=400, t = 30)
        )
    )

    body <- dashboardBody(
        tabItems(
            tabItem(tabName="BoxMain", 
                fluidRow(column(12,getBoxMainPlotUI("boxmain")))
            )
        )
    )
    ui <- dashboardPage(header, sidebar, body, skin = "blue")

    server <- function(input, output, session) {
        load(system.file("extdata", "demo", "demodata.Rda", package = "debrowser"))
    observe({
        if (!is.null(input$genename))
            callModule(debrowserboxmainplot, "boxmain", demodata, metadatatable$sample, metadatatable$treatment, input$genename)
        })
    }

    shinyApp(ui, server)

Density Plot::

    library(debrowser)
    options(warn =-1)
    header <- dashboardHeader(title = "DEBrowser Density Plots" )
    sidebar <- dashboardSidebar(  sidebarMenu(id="DataAssessment",
        menuItem("Density", tabName = "Density"),
        textInput("maxCutoff", "Max Cutoff", value = "10" ),
        plotSizeMarginsUI("density", h=400),
        plotSizeMarginsUI("afterFiltering", h=400)  
        )      
    )

    body <- dashboardBody(
        tabItems(
            tabItem(tabName="Density", 
                fluidRow(column(12,getDensityPlotUI("density"))),
                fluidRow(column(12,getDensityPlotUI("afterFiltering")))
            )
        )
    )

    ui <- dashboardPage(header, sidebar, body, skin = "blue")

    server <- function(input, output, session) {
        load(system.file("extdata", "demo", "demodata.Rda", package = "debrowser"))
        filtd <- reactive({
        # Filter out the rows that has maximum 100 reads in a sample
        subset(demodata, apply(demodata, 1, max, na.rm = TRUE)  >=  as.numeric(input$maxCutoff))
        })
        observe({
            if(!is.null(filtd())){
                callModule(debrowserdensityplot, "density", demodata)
                callModule(debrowserdensityplot, "afterFiltering", filtd())
            }
        })
    }
    shinyApp(ui, server)


Heatmap Module::

    library(debrowser)
    library(DESeq2)
    library(heatmaply)
    library(RColorBrewer)
    library(gplots)
    options(warn=-1)
    header <- dashboardHeader(title = "DEBrowser Heatmap")
    sidebar <- dashboardSidebar( getJSLine(), sidebarMenu(id="DataAssessment",
        menuItem("Heatmap", tabName = "Heatmap"),
        plotSizeMarginsUI("heatmap"),
        heatmapControlsUI("heatmap"))
    )

    body <- dashboardBody(
        tabItems(
            tabItem(tabName="Heatmap",  getHeatmapUI("heatmap"),
                column(4,
                       verbatimTextOutput("heatmap_hover"),
                       verbatimTextOutput("heatmap_selected")
                )
            )
        )
    )

    ui <- dashboardPage(header, sidebar, body, skin = "blue")

    server <- function(input, output, session) {
        load(system.file("extdata", "demo", "demodata.Rda", package = "debrowser"))
        insulinSignalingGenes <- reactive({
            genes <-  c("Prkar2a", "Tsc1", "Mapk8", "Sos1", "Pik3r1", "Srebf1",
                        "Insr", "Fasn", "Ppp1r3b", "Pik3r3", "Ptprf", "Pklr",
                        "Irs2", "Socs4", "Eif4ebp1", "Ppp1r3c", "Pygl", "Socs2",
                        "Cbl","Acaca", "Crkl")
            normDat <- getNormalizedMatrix(demodata, method = "MRN")
            normDat[genes, ]
        })
        selected <- reactiveVal()
        observe({
            withProgress(message = 'Creating plot', style = "notification", value = 0.1, 
            { selected(callModule(debrowserheatmap, "heatmap", insulinSignalingGenes())) }
            )
        })
        output$heatmap_hover <- renderPrint({
            if (!is.null(selected()) && !is.null(selected()$shgClicked()) && 
                selected()$shgClicked() != "")
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



