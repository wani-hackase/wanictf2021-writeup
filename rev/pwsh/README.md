---
title: "pwsh"
level: 2
flag: "FLAG{y0u_5ucc33d3d_1n_cl34r1n6_0bfu5c473d_p0w3r5h3ll}"
writer: "hi120ki"
---

# pwsh

## 問題文

Power!!!

[Installing PowerShell on Ubuntu](https://docs.microsoft.com/en-us/powershell/scripting/install/install-ubuntu?view=powershell-7.1#installation-via-package-repository)

## 解法

難読化されたPowerShellスクリプトです。最初の数値(`{39}{4}{12}{45}{21}{0}{36}...`)があとに続く文字のインデックス(`' world of PowerShe','d_p','cl', ...`)になっています。

また`replACe`命令で`cW4`をAscii 34の`"`、`8r3`をAscii 95の`_`、`fj7`をAscii 36の`$`に置き換える処理も行われています。

以上2点の処理を再現するPythonコードを書くと

```python
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
```

```powershell
echo "Welcome to the world of PowerShell!"

$input = Read-Host "Password"

if ($input -eq "FLAG{y0u_5ucc33d3d_1n_cl34r1n6_0bfu5c473d_p0w3r5h3ll}") {
  Write-Output "Correct!"
} else {
  Write-Output "Incorrect"
}
```

という、入力文字列がフラグ文字列`FLAG{y0u_5ucc33d3d_1n_cl34r1n6_0bfu5c473d_p0w3r5h3ll}`と一致するか判定するPowerShellスクリプトが出てきます。
