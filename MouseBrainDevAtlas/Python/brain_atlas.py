import scanpy as s
  
adata = sc.read('dev_all.loom')

#AnnData object with n_obs × n_vars = 292495 × 31053 
#    obs: 'Age', 'CellCycle', 'Cell_Conc', 'Chemistry', 'ChipID', 'Class', 'ClusterName', 'Clusters', 'Date_Captured', 'DonorID', 'DoubletFinderPCA', 'HPF_LogPP', 'IsCycling', 'Label', 'Location_E9_E11', 'NCellsCluster', 'NGenes', 'Num_Pooled_Animals', 'PCR_Cycles', 'Plug_Date', 'Project', 'PseudoAge', 'PseudoTissue', 'Region', 'SampleID', 'SampleName', 'Sample_Index', 'Sex', 'Species', 'Split', 'Strain', 'Subclass', 'Target_Num_Cells', 'Tissue', 'TotalUMI', 'Transcriptome', 'cDNA_Lib_Ok', 'ngperul_cDNA'
#    var: 'Accession', 'Chromosome', 'End', 'Gamma', 'Selected', 'Start', 'Strand', 'Valid'
#    obsm: 'BTSNE', 'HPF', 'HPF_theta', 'PCA', 'TSNE', 'UMAP', 'UMAP3D'
#    varm: 'HPF', 'HPF_beta', 'MultilevelMarkers'
#    layers: 'matrix', 'expected', 'pooled', 'spliced', 'unspliced'
