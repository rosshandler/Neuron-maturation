# Install biomart bioconductor packages
library(biomaRt)
ensembl <- useEnsembl(biomart = "genes", dataset = "hsapiens_gene_ensembl")
setwd('/Users/hannaszafranska/programming')

# Save excel gene list (Feline's) file as csv (make sure only rows and columns are saved in the file).

# Read csv file into R
data <- read.csv('Selected_genes0.csv')

# load biomart, get gene ids and extract ensembl and chromosomes for each gene symbol

# write a function that takes any gene list of symbols and returns the corresponding ensembl ids and chromosomes (a character vector)
gene_tab <- getBM(attributes = c('hgnc_symbol', 'ensembl_gene_id', 'chromosome_name'),
      filters = 'hgnc_symbol',
      values = data$Gene, 
      mart = ensembl)

print(gene_tab) 

setdiff(data$Gene,gene_tab$hgnc_symbol)
