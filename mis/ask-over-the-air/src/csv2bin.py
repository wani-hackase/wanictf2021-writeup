import sys
import numpy as np


if len(sys.argv) != 3:
    print("filename needed")
    exit(1)

filename_in = sys.argv[1]
filename_out = sys.argv[2]

fp = open(filename_in, "r")


data = []
while True:
    s = fp.readline()
    if s == "":
        break
    values = s.split(",")
    real = float(values[0])
    imag = float(values[1])
    data.append(complex(real, imag))

data = np.array(data, dtype=np.complex64)

file = open(filename_out, "wb")
file.write(data)
file.close()
