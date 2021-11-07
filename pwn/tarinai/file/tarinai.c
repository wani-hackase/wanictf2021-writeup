#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void init() {
  alarm(60);
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

int vuln() {
  char Name[256];
  printf("Name @>%p\n", &Name);
  printf("Name>");
  read(0, Name, 258);
  printf("Hello %s", Name);
  return 0;
}

int main() {
  int a = 1;
  init();
  vuln();
  return 0;
}
