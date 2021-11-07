echo "Yes, we love VBA!"

$input = Read-Host "Password"

if ($input -eq "FLAG{w0w_7h3_3mb3dd3d_vb4_1n_w0rd_4u70m471c4lly_3x3cu73d_7h3_p0w3r5h3ll_5cr1p7}") {
  Write-Output "Correct!"
} else {
  Write-Output "Incorrect"
}

