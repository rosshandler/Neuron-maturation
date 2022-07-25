import pandas as pd
import scanpy as sc
  
adata = sc.read('dev_all.loom')

#AnnData object with n_obs × n_vars = 292495 × 31053 
#    obs: 'Age', 'CellCycle', 'Cell_Conc', 'Chemistry', 'ChipID', 'Class', 'ClusterName', 'Clusters', 'Date_Captured', 'DonorID', 'DoubletFinderPCA', 'HPF_LogPP', 'IsCycling', 'Label', 'Location_E9_E11', 'NCellsCluster', 'NGenes', 'Num_Pooled_Animals', 'PCR_Cycles', 'Plug_Date', 'Project', 'PseudoAge', 'PseudoTissue', 'Region', 'SampleID', 'SampleName', 'Sample_Index', 'Sex', 'Species', 'Split', 'Strain', 'Subclass', 'Target_Num_Cells', 'Tissue', 'TotalUMI', 'Transcriptome', 'cDNA_Lib_Ok', 'ngperul_cDNA'
#    var: 'Accession', 'Chromosome', 'End', 'Gamma', 'Selected', 'Start', 'Strand', 'Valid'
#    obsm: 'BTSNE', 'HPF', 'HPF_theta', 'PCA', 'TSNE', 'UMAP', 'UMAP3D'
#    varm: 'HPF', 'HPF_beta', 'MultilevelMarkers'
#    layers: 'matrix', 'expected', 'pooled', 'spliced', 'unspliced'

adata.obs['Class'].unique()
#array(['Gastrulation', 'Radial glia', 'Mesenchyme', 'Neural tube',
#       'Mesoderm', 'Neural crest', 'Bad cells', 'Endoderm', 'Ectoderm',
#       'Blood', 'Fibroblast', 'Vascular', 'Immune', 'Glioblast',
#       'Choroid plexus', 'Ependymal', 'Pineal gland',
#       'Subcommissural organ', 'Olfactory ensheathing cell',
#       'Schwann cell', 'Oligodendrocyte', 'Neuroblast', 'Undefined',
#       'Neuron'], dtype=object)


pd.DataFrame(adata.obs).to_csv('metadata.csv')
pd.DataFrame(adata.obsm['PCA']).to_csv('pca.csv')
pd.DataFrame(adata.obs_names).to_csv('cell_names.csv')
pd.DataFrame(adata.var_names).to_csv('genes_names.csv')
