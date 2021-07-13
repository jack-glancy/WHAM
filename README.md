# WHAM
****
## Instructions on using the WHAM for PMF generation
#### One Dimensional WHAM
1. Run create_1D_meta.py to generate meta.dat file.
2. Use the line below to WHAM the data:
```
$ wham xmin xmax nbin conver temp 0 meta.dat result.dat
```
where xmin and xmax = minimum and maximum reaction coordinate value for your dataset, nbin is the number of bins to divide the data into, conver is the convergence limit (usually fine to leave at 0.01) and temp is the temperature of your MD. 
An example line is below:
```
$ wham 1.38 2.80 20 0.01 310 0 meta.dat result.dat
```
