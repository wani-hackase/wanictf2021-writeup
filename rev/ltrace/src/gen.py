flag = "FLAG{c4n_y0u_7r4c3_dyn4m1c_l1br4ry_c4ll5?}\0"

res = []
for i in range(len(flag)):
    res.append(ord(flag[i]) ^ 0x53)
print(res, len(res))
