import sys
import numpy as np

if len(sys.argv) != 2:
    print("filename needed")
    exit(1)

filename_in = sys.argv[1]

fp = open(filename_in, "r")


data = np.fromfile(filename_in, dtype=np.complex64)
print(data)

for item in data:
    print("%e,%e" % (item.real, item.imag))
