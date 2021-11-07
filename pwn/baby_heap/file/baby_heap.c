#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void init() {
  alarm(600);
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void menu() {
  printf("1. malloc\n");
  printf("2. free\n");
  printf("3. write\n");
  printf("4. exit\n>");
}

void win() { system("/bin/sh"); }

void print_fd(long long int entry, int count) {
  long long int array[5] = {
      0,
  };
  long long int *temp;
  temp = (void *)entry;
  printf("\n!! Segfault may happen when fd isn't readable address\n");
  printf("fd >>> ");
  for (int i = 0; i < count && temp > 0xFFFFFFFF && temp < 0x7FFFFFFFFFFF;
       i++) {
    array[i] = *temp;
    printf("0x%llx ", array[i]);
    temp = (void *)array[i];
  }
  if (temp < 0xFFFFFFFF || temp > 0x7FFFFFFFFFFF)
    printf("Maybe Segfault from here...");
  printf("\n           ↑ \n");
  printf("Will be allocated for the next malloc\n\n");
}

void print_info(char **list) {
  unsigned long r;

  for (int i = 0; i < 5; i++) {
    unsigned long long *p;
    unsigned long long *k;
    p = (unsigned long long *)(list[i]);
    k = (unsigned long long *)(list[i] + 8);
    printf("[%d] : ", i);
    if (list[i] == NULL)
      printf("Not Allocated\n");
    else if (*k != 0) {
      printf("Free Chunk\n");
      printf("Chunk at>%p\n", list[i]);
      printf("fd : 0x%llx\n", *p);
    } else {
      printf("Allocated Chunk\n");
      printf("Chunk at>%p\n", list[i]);
      printf("Data : %s\n", list[i]);
    }
  }
}

int main() {
  int idx;
  int choice;

  char *head;
  char *heap_list[5] = {
      NULL,
  };

  long long int entry;
  int *fd_count;

  init();
  head = (char *)malloc(0x10 * sizeof(char));
  entry = head - 0x2a0 + 0x90;
  fd_count = head - 0x2a0 + 0x10;

  while (choice != 4) {
    printf("Do arbitrary write using tcache bin.\n");
    printf("ldd (Ubuntu GLIBC 2.31-0ubuntu9.2) 2.31\n");
    printf("malloc is fixed at size 0x10\n");
    printf("\nsystem('/bin/sh') at >0x%llx\n", (long long int)win + 0x8);
    printf("Return address of main at >0x%llx\n\n", (long long int)&idx + 0x68);
    printf("Bin count >%d\n", *fd_count);
    print_fd(entry, *fd_count);
    print_info(heap_list);
    printf("---------------\n");
    menu();
    scanf("%d", &choice);
    if (choice < 1 || choice > 4) {
      printf("Out of Boundary\n");
      exit(-1);
    }
    switch (choice) {

    case 1:
      printf("Where? >");
      scanf("%d", &idx);
      if (idx < 0 || idx > 5) {
        printf("Out of Boundary\n");
        exit(-1);
      } else {
        heap_list[idx] = (char *)malloc(0x10 * sizeof(char));
        memset(heap_list[idx], 0, 0x10);
      }
      break;

    case 2:
      printf("Where? >");
      scanf("%d", &idx);
      if (idx < 0 || idx > 5) {
        printf("Out of Boundary\n");
        exit(-1);
      } else {
        free(heap_list[idx]);
      }
      break;
    case 3:
      printf("What will happen if you can write fd of free chunk?\n");
      printf("Where? >");
      scanf("%d", &idx);
      if (idx < 0 || idx > 5) {
        printf("Out of Boundary\n");
        exit(-1);
      } else {
        printf("What? ( ex: 0x123456 )>");
        scanf("%p", heap_list[idx]);
      }
    }
    printf("\n");
  }
}