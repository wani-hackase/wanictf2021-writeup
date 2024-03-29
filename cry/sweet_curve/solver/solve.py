p = 0x89A4E2C7F834F5FBC6F2A314E373E3723DE7DF6283C5D97CBCA509C61E02965B7EF96EFCE1D827BFDFA7F21D22803558BB549F9EA15DFE9F47D3976648C55FEB


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        a = (self.y - other.y) * pow(self.x - other.x, -1, p) % p
        b = (self.y * other.x - other.y * self.x) * pow(self.x - other.x, -1, p) % p
        x_R = (a * a - self.x - other.x) % p
        y_R = (-a * x_R - b) % p
        return Point(x_R, y_R)


x_P = 0x1E1CBA0E07C61CF88E9F23B9859093C33C26CF83BCFB6FE24D7559CD0EA86FB2F144AE643AC5EDF6F04EF065DC7C2C18D88AE02843592D5E611029FEFC0FECE
y_P = 0x198420B30A4330F82380326895D0AC06A1859BC49D45CD4B08021B857D23D515163B9151FBAF7AE5F816D485D129D3B1C4630D1FB45C6790AF551428A5C85667
x_Q = 0x7E32EDFD7BEFD8DF93D7B738D6A1C95E1CFD56B3A6CCC4A62E4E0AE9059B4903E71FCCBE07D8D45C762B4A3ED5C9D1A2505043D033E58ADB72191259B81BC47D
y_Q = 0x46016C676585FEAF048FFF9D5CBB45DBD598C6C4C81694E0881BF110B57012F0BAC6EAF7376FEE015C8CECBA1FC92206CA346F7D72EE1D60F820091C85FA76B3


P = Point(x_P, y_P)
Q = Point(x_Q, y_Q)
R = P + Q
flag = R.x
flag = bytes.fromhex(f"{flag:x}")
print(flag)
