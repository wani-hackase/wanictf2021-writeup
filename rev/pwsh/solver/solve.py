s = [
    " world of PowerShe",
    "d_p",
    "cl",
    "d3",
    "ch",
    "1n_",
    "else",
    "ost cW4Passwo",
    "34r1n68r30b",
    "{\n  Writ",
    "l}",
    "_",
    "o ",
    "r",
    "W4Incor",
    "w3r5h3l",
    "W",
    "\n ",
    "t ",
    "-eq c",
    "W4FLAG{",
    "he",
    "t c",
    "(fj7inpu",
    "y0u_",
    "fj7input =",
    " ",
    "Read-H",
    "5ucc33",
    "473",
    "dc",
    "4",
    "e-Outpu",
    "cW4) ",
    "u5c",
    "0",
    "ll!cW4\n\n",
    "W4Co",
    "d",
    "e",
    "rrect!cW4\n} ",
    "rec",
    "tcW4\n}\n",
    " {",
    "tput c",
    "cW4Welcome to t",
    "f",
    " Write-Ou",
    "\n\nif ",
]

# fmt: off
key = [39,4,12,45,21,0,36,25,26,27,7,13,30,16,31,48,23,18,19,20,24,28,3,38,11,5,2,8,46,34,29,1,35,15,10,33,9,32,22,37,40,6,43,17,47,44,14,41,42]
# fmt: on

ans = ""

for i in key:
    ans += s[i]

ans = ans.replace("cW4", chr(34))
ans = ans.replace("8r3", chr(95))
ans = ans.replace("fj7", chr(36))

print(ans)
