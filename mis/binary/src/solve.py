fp = open("./binary.csv", "r")

data = []
fp.readline()
while True:
    vals = fp.readline()
    if vals == "":
        break

    vals = vals.split(",")
    data.append(int(vals[1]))

c = 0
for i in range(len(data)):
    c = (c << 1) | data[i]
    if i % 8 == 7:
        print(chr(c), end="")
        c = 0

print("")
