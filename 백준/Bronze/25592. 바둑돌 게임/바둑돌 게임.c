#include <stdio.h>

int factorial(int turn);

int main(void) {
  int n;
  int hop = 1;
  int turn = 1;
  scanf("%d", &n);

  while (1) {
    if ((hop >= n && (turn % 2 != 0))) {
      printf("%d\n", hop - n);
      break;
    } else if ((hop > n) && (turn % 2 == 0)) {
      printf("0\n");
      break;
    } else {
      turn++;
      hop = factorial(turn);
    }
  }
  return 0;
}

int factorial(int turn) {
  int result = 0;
  for (int i = 0; i <= turn; i++) {
    result += i;
  }
  return result;
}