#include <stdio.h>

int main(void) {
  int r, c, w;
  int j;
  int dp[31][31] = {0};
  int sum = 0;
  int endpoint = 0;

  scanf("%d %d %d", &r, &c, &w);
  endpoint = c;

  dp[1][1] = 1;
  dp[2][1] = 1;
  dp[2][2] = 1;

  for (int i = 3; i < r + w; i++) {
    for (int j = 1; j < r + w; j++) {
      dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
    }
  }

  sum += dp[r][c]; // 꼭짓점
  endpoint++;

  for (int i = r + 1; i < r + w; i++) {
    for (int j = c; j <= endpoint; j++) {
      sum += dp[i][j];
    }
    endpoint++;
  }

  printf("%d\n", sum);
  return 0;
}