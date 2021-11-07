fp = open("./digital_ask_solve.csv", "r")

data = []
# vals = fp.readline()
while True:
    vals = fp.readline()
    if vals == "":
        break

    vals = vals.split(",")
    data.append(int(vals[1]))

new_data = []
count = 0
current_value = 1
for i in range(len(data)):
    if current_value == data[i]:
        count += 1
    else:
        count = 1

    if count >= 16:
        new_data.append(current_value)
        count = 1

    current_value = data[i]


c = 0
for i in range(len(new_data)):
    c = (c << 1) | new_data[i]
    if i % 8 == 7:
        print(chr(c), end="")
        c = 0

print("")
