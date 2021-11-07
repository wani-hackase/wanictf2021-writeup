echo "Welcome to the world of PowerShell!"

$input = Read-Host "Password"

if ($input -eq "FLAG{y0u_5ucc33d3d_1n_cl34r1n6_0bfu5c473d_p0w3r5h3ll}") {
  Write-Output "Correct!"
} else {
  Write-Output "Incorrect"
}
