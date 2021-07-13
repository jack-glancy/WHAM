import sys

# define inital x coord value

x = 1.48
xinc = 0.1

# define initial y coord value

y = 3.90
yinc = -0.15

# define number of windows in x coord

nwinx = 17

# define number of windows in y coord

nwiny = 17

# define write line
def main():
    with open('meta.dat', 'w+') as f:
        for i in range(nwinx):
            for j in range(nwiny):
                write_line(f, i, j)

def write_line(inp_file, i, j):
    xval = x + xinc * i
    yval = y + yinc * j
    inp_file.write('diag_%d.%d.dat %0.2f %0.2f 400 400 310\n' %(i, j, xval, yval))

main()
