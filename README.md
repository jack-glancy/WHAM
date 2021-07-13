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
#### Two Dimensional WHAM
1. Run create_2D_meta.py to generate meta.dat file.
2. Use the line below to WHAM the data:
```
$ wham-2d Px=0 xmin xmax nbinx Py=0 ymin ymax nbiny conver 310 0 meta.dat results.dat 0
```
where xmin, xmax, ymin and ymax = minimum and maximum reaction coordinate values for your dataset, nbinx and nbiny are the numbers of bins to divide the x and y data into,  conver is the convergence limit (usually fine to leave at 0.01) and temp is the temperature of your MD.  
An example line is below:
```
$ wham-2d Px=0 1.4 3.2 15 Py=0 1.4 4.0 15 0.01 310 0 meta.dat results.dat 1
```
> Notes: More detail can be found at the Grossfield website - http://membrane.urmc.rochester.edu/?page_id=126
