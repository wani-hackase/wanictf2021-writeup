#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int counter = 0;

char *textArea[6];
char lyrics[3][16];

void (*fp[2])(char *);

void init() {
  alarm(600);
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

char *parseVar(char *var) {
  int intTemp;
  char *str_temp;
  if (var[0] == '%') {
    intTemp = var[1] - 48;
    if (intTemp < 0 || intTemp > 2)
      printf("Out of Boundary!\n");
    else if (strlen(lyrics[intTemp]) == 0)
      printf("Cannot access memory\n");
    else
      return lyrics[intTemp];
  } else {
    return var;
  }
  return NULL;
}

void sing(char *parameter) {
  printf("🎵");
  printf(
      parseVar(parameter)); // Looks Safe since we use % as register indicator!
  printf("🎵\n");
}

void ereaseLyrics(char *parameter) {
  int i;
  if (parameter[0] != '%')
    printf("ERROR : Destination of 'erease' should be register\n");
  else {
    i = parameter[1] - 48;
    if (i < 0 || i > 2)
      printf("Out of Boundary!\n");
    else
      lyrics[i][0] = '\0';
  }
}

void writeLyrics(char *parameter1, char *parameter2) {
  int i;
  if (parameter1[0] != '%')
    printf("ERROR : Destination of 'write' should be register\n");
  else {
    i = parameter1[1] - 48;
    memcpy(lyrics[i], parseVar(parameter2), 16);
  }
}

void parser(char *command) {
  char *token;
  char *cmd[4];
  int i = 0;
  printf("command : %s\n", command);
  if (command == NULL)
    return;
  cmd[i] = strtok(command, " ");
  while (cmd[i] != NULL && i < 3) {
    i++;
    cmd[i] = strtok(NULL, " ");
  }
  if (cmd[0] != NULL) {
    if (strcmp(cmd[0], "sing") == 0) {
      fp[0](cmd[1]);
    } else if (strcmp(cmd[0], "erease") == 0) {
      fp[1](cmd[1]);
    } else if (strcmp(cmd[0], "write") == 0) {
      writeLyrics(cmd[1], cmd[2]);
    } else {
      printf("Invalid command %s\n", cmd[0]);
    }
  } else {
    printf("Nothing to process\n");
  }
  printf("----Lyrics list----\n");
  for (int j = 0; j < 5; j++) {
    if (lyrics[j] != NULL)
      printf("[%d]: %s\n", j, lyrics[j]);
    else
      printf("[%d]: NULL\n", j);
  }
  printf("-------------------\n");
}

void initializeSystem() {
  char *Checker[6];
  printf("Initializing System...\n");
  printf("Checking Available Memory...\n");
  fp[0] = sing;
  fp[1] = ereaseLyrics;
  for (int i = 0; i < 6; i++) {
    Checker[i] = (char *)malloc(32 * sizeof(char));
    if (Checker[i] == NULL) {
      printf("ERROR! Can't get the memory!\n");
      exit(-1);
    }
  }
  printf("Memory available...\n");
  for (int i = 5; i >= 0; i--) {
    free(Checker[i]);
  }
}

int main() {
  init();

  if (counter != 0)
    printf("Program came from the future\n\n");

  printf("I'm born to take flag with music\n");
  int i;
  for (i = 0; i < 101; i++) {
    switch (i) {
    case 0:
      printf("Year : %d\n", 2061 + i);
      parser(textArea[0]);
      break;
    case 15:
      printf("Year : %d\n", 2061 + i);
      parser(textArea[1]);
      break;
    case 20:
      printf("Year : %d\n", 2061 + i);
      parser(textArea[2]);
      break;
    case 60:
      printf("Year : %d\n", 2061 + i);
      parser(textArea[3]);
      break;
    case 100:
      printf("Year : %d\n", 2061 + i);
      parser(textArea[4]);
      parser(textArea[5]);
    }
  }

  printf("I wasn't able to get the flag.\n\n");
  initializeSystem();
  printf("Give me your code to send to the past\n");
  printf("counter : %d\n", counter);

  for (int i = 0; i < 6; i++) {
    textArea[i] = (char *)malloc(32 * sizeof(char));
    printf("%d>", i);

    read(0, textArea[i], 0x40);
  }

  printf("Change this FLAGless history!! Please...\n");
  counter += 1;
}
