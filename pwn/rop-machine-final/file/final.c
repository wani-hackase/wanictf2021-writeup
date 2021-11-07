#include <fcntl.h>
#include <malloc.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

// for compatibility
extern char *gets(char *s);

char *name_gadgets[16];
u_int64_t addr_gadgets[16];
char buf[128];

void rop_pop_rdi();
void rop_pop_rsi();
void rop_pop_rdx();

void init() {
  alarm(300);
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void create_gadgets_table() {
  name_gadgets[0] = "execute";
  name_gadgets[1] = "push value";
  name_gadgets[2] = "pop rdi; ret";
  name_gadgets[3] = "pop rsi; ret";
  name_gadgets[4] = "pop rdx; ret";
  name_gadgets[5] = "gets";
  name_gadgets[6] = "open";
  name_gadgets[7] = "read";
  name_gadgets[8] = "write";

  addr_gadgets[0] = 0;
  addr_gadgets[1] = 0;
  addr_gadgets[2] = ((u_int64_t)rop_pop_rdi) + 8;
  addr_gadgets[3] = ((u_int64_t)rop_pop_rsi) + 8;
  addr_gadgets[4] = ((u_int64_t)rop_pop_rdx) + 8;
  addr_gadgets[5] = ((u_int64_t)gets);
  addr_gadgets[6] = ((u_int64_t)open);
  addr_gadgets[7] = ((u_int64_t)read);
  addr_gadgets[8] = ((u_int64_t)write);
}

void rop_pop_rdi() {
  __asm__("pop %rdi\n\t"
          "ret\n\t");
}

void rop_pop_rsi() {
  __asm__("pop %rsi\n\t"
          "ret\n\t");
}

void rop_pop_rdx() {
  __asm__("pop %rdx\n\t"
          "ret\n\t");
}

char *get_rop_name(u_int64_t addr) {
  int i;
  for (i = 0; i < 10; i++) {
    if (addr_gadgets[i] == 0) {
      continue;
    }

    if (addr_gadgets[i] == addr) {
      return name_gadgets[i];
    }
  }

  return NULL;
}

void print_menu() {
  printf("\n\"buf\" address is %p\n", buf);
  printf("\n[menu]\n"
         "0x01. append hex value\n"
         "0x02. append \"pop rdi; ret\" addr\n"
         "0x03. append \"pop rsi; ret\" addr\n"
         "0x04. append \"pop rdx; ret\" addr\n"
         "0x05. append \"gets\" addr\n"
         "0x06. append \"open\" addr\n"
         "0x07. append \"read\" addr\n"
         "0x08. append \"write\" addr\n"
         "0x0a. show menu (this one)\n"
         "0x0b. show rop_arena\n"
         "0x00. execute rop\n");
}

u_int64_t get_uint64() {
  char buf[64];
  u_int64_t ret;
  ret = read(0, buf, 63);
  buf[ret] = 0;
  ret = strtoul(buf, NULL, 16);
  return ret;
}

u_int64_t menu() {
  u_int64_t ret;

  printf("> ");
  ret = get_uint64();
  return ret;
}

void show_arena(u_int64_t *rop_arena, int index) {
  int i;
  puts("             rop_arena");
  puts("+-----------------------------------+");
  for (i = 0; i < index; i++) {
    char *name = get_rop_name(rop_arena[i]);
    if (name != NULL) {
      printf("| 0x%016lx (%-12s) |", rop_arena[i], name);
    } else {
      printf("| 0x%031lx |", rop_arena[i]);
    }

    if (i == 0) {
      printf("<- rop start");
    }

    printf("\n");
    puts("+-----------------------------------+");
  }
}

void rop_machine() {
  u_int64_t rop_arena[128];
  u_int64_t *top = rop_arena;
  int index = 0;
  u_int64_t ret;

  print_menu();

  while (1) {
    int cmd = menu();
    printf("cmd = 0x%x\n", cmd);
    switch (cmd) {
    case 1:
      printf("hex value?: ");
      ret = get_uint64();
      rop_arena[index] = ret;
      index++;
      printf("0x%016lx is appended\n", ret);
      break;
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
      rop_arena[index] = addr_gadgets[cmd];
      printf("\"%s\" addr is appended\n", name_gadgets[cmd]);
      index++;
      break;
    case 10:
      print_menu();
      break;
    case 11:
      show_arena(rop_arena, index);
      break;
    case 0:
      show_arena(rop_arena, index);
      {
        register u_int64_t rsp asm("rsp");
        rsp = (u_int64_t)rop_arena;
        __asm__("ret");
        exit(0);
      }
    default:
      puts("bye beginner!!\n");
      exit(1);
      break;
    }
  }
}

int main() {
  init();
  create_gadgets_table();
  rop_machine();
}
