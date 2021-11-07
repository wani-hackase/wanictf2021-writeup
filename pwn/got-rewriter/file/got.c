#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void init();

void win() {
  printf("congratulation!\n");
  system("/bin/sh");
  exit(0);
}

unsigned long int get_val() {
  char str_val[0x20];
  int ret;
  unsigned long int val;
  ret = read(0, str_val, 0x20 - 1);
  str_val[ret] = 0;
  val = strtol(str_val, NULL, 16);
  return val;
}

void vuln() {
  char str_val[0x20];
  unsigned long int val;
  unsigned long int *p;
  int ret;

  printf("Please input target address (0x600000-0x700000): ");
  val = get_val();
  printf("Your input address is 0x%lx.\n", val);
  if (val < 0x600000 || val > 0x700000) {
    printf("you can't rewrite 0x%lx!\n", val);
    return;
  }
  p = (unsigned long int *)val;

  printf("Please input rewrite value: ");
  val = get_val();
  printf("Your input rewrite value is 0x%lx.\n\n", val);

  printf("*0x%lx <- 0x%lx.\n\n\n", (unsigned long int)p, val);
  *p = val;
}

int main() {
  init();
  printf("Welcome to GOT rewriter!!!\n");
  printf("win = 0x%lx\n", (unsigned long int)win);
  while (1) {
    vuln();
  }
}

void init() {
  alarm(0x100);
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}
