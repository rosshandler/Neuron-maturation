wot optimal_transport --matrix data/PCA.txt --cell_days data/cell_days.txt \
  --local_pca 0 --growth_iters 3 --out tmaps/pca --verbose

wot trajectory --tmap tmaps/pca --cell_set data/neurons_cell_set.gmt --day 18 

wot trajectory_trends --trajectory data/wot_trajectory.txt --cell_days data/cell_days.txt --matrix data/brain_atlas.h5ad


table(d[grep('Neuron', d$Class),]$Age)

 e10.0  e11.0  e12.0  e12.5  e13.0  e13.5  e14.0  e14.5  e15.0  e15.5  e16.0 
   263   4039  10950   1535   6109   7642   4479   7977   8832   5589   8965 
e16.25  e16.5  e17.0  e17.5  e18.0   e7.0   e8.0   e8.5   e9.0 
  2886   8150  12743   5064  15831      0      0      0      9 
