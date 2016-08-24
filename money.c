#include <stdio.h>
int main(void){
  char player[4][16];
  int money[4] = {0};
  int loss[4] = {0};
  int win[4] = {0};
  int i, tmp;
  int lastWinner = -1;
  int maxComboWinner = -1;
  int tmpCombo = 0;
  int maxCombo = -1;
  int gameCount = 0;
  int lastLoser = -1;
  int maxBadComboLoser = -1;
  int tmpBadCombo = 0;
  int maxBadCombo = -1;
  for(i = 0; i < 4; i++)
    scanf("%s", player[i]);
  i = 0;
  while(scanf("%d", &tmp) != EOF){
    if(i == 0)
      gameCount++;
    money[i] += tmp;
    if(tmp < 0){
      loss[i]++;
      if(i == lastLoser){
        tmpBadCombo++;
        if(tmpBadCombo > maxBadCombo){
          maxBadCombo = tmpBadCombo;
          maxBadComboLoser = lastLoser;
        }
      }
      else{
        lastLoser = i;
        tmpBadCombo = 1;
      }
    }
    else if(tmp > 0){
      win[i]++;
      if(i == lastWinner){
        tmpCombo++;
        if(tmpCombo > maxCombo){
          maxCombo = tmpCombo;
          maxComboWinner = lastWinner;
        }
      }
      else{
        lastWinner = i;
        tmpCombo = 1;
      }
    }
    i++;
    i %= 4;
  }
  printf("        Total: %d games\n", gameCount);
  for(i = 0; i < 4; i++)
    printf("%7s ", player[i]);
  printf("\n");

  for(i = 0; i < 4; i++)
    printf("%7d ", money[i]);
  printf("\n");
  printf("        Losses\n");
  for(i = 0; i < 4; i++)
    printf("%7d ", loss[i]);
  printf("\n");
  printf("        Wins\n");
  for(i = 0; i < 4; i++)
    printf("%7d ", win[i]);
  printf("\n");
  printf("        Combo\n");
  printf("     %d-winning, made by %s\n", maxCombo, player[maxComboWinner]);
  printf("     %d-losing, made by %s\n", maxBadCombo, player[maxBadComboLoser]);
}
