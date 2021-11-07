fp = open("./bits.csv", "r")

data = []
while True:
    val = fp.readline()
    if val == "":
        break

    data.append(int(val))

c = 0
for i in range(len(data)):
    c = (c << 1) | data[i]
    if i % 8 == 7:
        print(chr(c), end="")
        c = 0

print("")
