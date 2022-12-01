#include <stdio.h>

#define MAXLINE 10

char line[MAXLINE];

int readline(void);
int linetoint(void);

/* sums all the lines between empty spaces, returns longest */
int main(void)
{
  int longest = 0, current = 0;
  extern char line[];

  while (readline() != EOF)
  {
    int amount = linetoint();
    current += amount;
    // Empty Line
    if (amount == 0)
    {
      if (current > longest)
      {
        longest = current;
      }
      current = 0;
    }
  }

  printf("\nMost Calories: %d\n", longest);
  return 0;
}

/* getline: reads a line into line, returns the length of the line */
int readline(void)
{
  int c, i;
  extern char line[];

  for (i = 0; i < MAXLINE - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
    line[i] = c;

  if (c == EOF)
    return EOF;
  if (c == '\n')
  {
    line[i] = c;
    ++i;
  }
  line[i] = '\0';
  return i;
}

/* linttoint: converts array of characters (line) to int */
int linetoint(void)
{
  int num = 0, digit = 0, i = 0, c = 0;
  extern char line[];

  while (i < MAXLINE - 1 && (c = line[i]) != '\n' && c != '\0')
  {
    if (c >= '0' && c <= '9')
    {
      digit = c - '0';
      num *= 10;
      num += digit;
    }
    ++i;
  }

  return num;
}