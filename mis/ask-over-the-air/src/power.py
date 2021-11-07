import math

fp = open("./ask-over-the-air.csv", "r")

data = []
vals = fp.readline()
while True:
    vals = fp.readline()
    if vals == "":
        break

    vals = vals.split(",")
    val_i = float(vals[1])
    val_q = float(vals[2])
    #    data.append(math.sqrt(val_i * val_i + val_q * val_q))
    print("%e" % math.sqrt(val_i * val_i + val_q * val_q))
