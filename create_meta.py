import sys

# define inital x coord value

x = 1.48
xinc = 0.1

# define initial y coord value

y = 3.90
yinc = -0.15

# define write line
def main():
    with open('meta.dat', 'w+') as f:
        for i in range(17):
            for j in range(17):
                write_line(f, j, i)

def write_line(inp_file, i, j):
    xval = x + xinc * i
    yval = y + yinc * j
    inp_file.write('diag_%d.%d.dat %0.2f %0.2f 400 400 310\n' %(j, i, xval, yval))

main()
