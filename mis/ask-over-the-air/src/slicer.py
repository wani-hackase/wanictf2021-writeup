import math

fp = open("./power.csv", "r")

start = 746
interval = 16
threashold = 2.50e-03

i = 1
while True:
    if i == start:
        break

    val = fp.readline()
    if val == "":
        break
    val = float(val)
    i += 1

while True:
    val = fp.readline()
    if val == "":
        break
    val = float(val)
    if (i - start) % interval == 0:
        if val > threashold:
            print("1")
        else:
            print("0")
    i += 1
