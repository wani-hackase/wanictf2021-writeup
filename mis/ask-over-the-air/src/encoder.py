import math

fp = open("./FLAG", "r")

flag = fp.read()

sampling_rate = 16

samples_1_i = []
samples_1_q = []
samples_0_i = []
samples_0_q = []


def send_1_bit(b):
    if b == 1:
        for i in range(sampling_rate):
            print("%e,%e" % (samples_1_i[i], samples_1_q[i]))
    else:
        for i in range(sampling_rate):
            print("%e,%e" % (samples_0_i[i], samples_0_q[i]))


def generate_samples():
    for i in range(sampling_rate):
        samples_1_i.append(math.sin(2 * math.pi * (i / 8)))
        samples_1_q.append(math.cos(2 * math.pi * (i / 8)))
        samples_0_i.append(0.0001 * math.sin(2 * math.pi * (i / 8)))
        samples_0_q.append(0.0001 * math.cos(2 * math.pi * (i / 8)))


def send_null(sec):
    for i in range(sec * sampling_rate):
        print("0,0")


def send_preamble():
    s = "\xAA\xAA\xAA\xAA"

    for i in range(len(s)):
        val = s[i]
        for j in range(8):
            b = (ord(val) >> (7 - j)) & 0x01
            send_1_bit(b)


def send_startcode():
    s = "\xE5"
    for i in range(len(s)):
        val = s[i]
        for j in range(8):
            b = (ord(val) >> (7 - j)) & 0x01
            send_1_bit(b)


def send_flag(flag):
    for i in range(len(flag)):
        val = flag[i]
        for j in range(8):
            b = (ord(val) >> (7 - j)) & 0x01
            send_1_bit(b)


def send(flag):
    send_null(50)
    send_preamble()
    send_startcode()
    send_flag(flag)


generate_samples()
# print(samples_1_i)
# print(samples_1_q)
# print(samples_0_i)
# print(samples_0_q)


# for _ in range(10):
send(flag)
