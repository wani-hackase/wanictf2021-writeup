#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char flag[0x34];

void setup() {
  FILE *f = NULL;

  alarm(60);
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);

  if ((f = fopen("flag.txt", "rt")) == NULL) {
    printf("NotFound::flag.txt\n");
    exit(0);
  }
  fscanf(f, "%s", flag);
  fclose(f);
}

int main() {
  char password[0x34] = "";
  int ok = 0;

  setup();

  printf("ふっかつのじゅもんを　いれてください\n");
  gets(password);

  if (strcmp(password, flag) == 0)
    ok = 1;

  if (ok) {
    printf("よくぞもどられた！\n");
    printf("%s\n", flag);
  } else {
    printf("じゅもんが　ちがいます\n");
  }
}
