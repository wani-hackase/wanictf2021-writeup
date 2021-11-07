#include <stdio.h>
#include <string.h>

int main(void) {
  char input[50];
  int key[43] = {21,  31, 18,  20,  40,  48, 103, 61,  12, 42,  99,
                 38,  12, 100, 33,  103, 48, 96,  12,  55, 42,  61,
                 103, 62, 98,  48,  12,  63, 98,  49,  33, 103, 33,
                 42,  12, 48,  103, 63,  63, 102, 108, 46, 83};
  char flag[43];

  for (size_t i = 0; i < 43; i++) {
    flag[i] = key[i] ^ 0x53;
  }

  printf("Input flag : ");
  scanf("%s", input);

  if (strcmp(input, flag) == 0) {
    printf("Correct! Flag is %s\n", input);
    return 0;
  } else {
    puts("Incorrect");
    return 1;
  }
}
