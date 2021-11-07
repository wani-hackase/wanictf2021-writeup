---
title: docker_dive
level: 2
flag: FLAG{y0u_Kn0W_H0w_to_Get_1nto_7he_DockeR}
writer: EBeb
---

# Docker Dive
## 問題文

Dockerの中に入ってsolverを実行してください。

+ Install Docker !
+ 与えられたDockerfileでDockerをbuildしてください 
+ dockerのなかに/bin/shを実行して入ってください 
+ /bin/bashでエラーがでる場合は/bin/shです。
+ solverを実行してください


Dockerは個人の環境に関係なく同じ環境を構築するために使われます。  
一部のpwn問題は問題サーバー構築に使ったDockerfileを一緒に提供しています。  
ローカルで動いてリモートで動かない場合はDockerを使って確認しましょう！


## 解法

docker build . 
docker run -it [image Name] /bin/sh  
./solver  

