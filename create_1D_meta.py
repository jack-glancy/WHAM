import sys

# define inital x coord value
x = 1.48
xinc = 0.1
nwin = 17

# define write line
def main():
    with open('meta.dat', 'w+') as f:
        for i in range(nwin):
                write_line(f, i)

def write_line(inp_file, i):
    xval = x + xinc * i
    inp_file.write('diag_%d.dat %0.2f 400 310\n' %(i, xval))

main()
