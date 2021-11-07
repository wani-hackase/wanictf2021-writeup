#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void init();

void win() {
  puts("welcome to WaniCTF 2021!!!");
  system("/bin/sh");
  exit(0);
}

int main() {
  init();
  win();
}

void init() {
  alarm(100);
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}
