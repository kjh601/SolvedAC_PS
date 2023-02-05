#include <stdio.h>
#include <string.h>

int main()
{
  unsigned int bit = 0;
  char cmd[7];
  int cmd_n, num;
  scanf("%d", &cmd_n);
  while (cmd_n--)
  {
    scanf("%s", cmd);
    if (cmd[1] == 'd')
    {
      scanf("%d", &num);
      bit |= (1 << num);
    }
    else if (cmd[1] == 'e')
    {
      scanf("%d", &num);
      bit &= ~(1 << num);
    }
    else if (cmd[1] == 'h')
    {
      scanf("%d", &num);
      if (bit & (1 << num))
        printf("1\n");
      else
        printf("0\n");
    }
    else if (cmd[1] == 'o')
    {
      scanf("%d", &num);
      bit ^= (1 << num);
    }
    else if (cmd[1] == 'l')
      bit = (1 << 21) - 1;
    else if (cmd[1] == 'm')
      bit = 0;
  }
  return 0;
}