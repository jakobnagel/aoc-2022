#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const char ROCK = 'A';
const char PAPER = 'B';
const char SCISSORS = 'C';
const char LOSE = 'X';
const char DRAW = 'Y';
const char WIN = 'Z';

int linescore(string line)
{
  int score = 0;
  char theirMove = line[0];
  char myMove;
  char outcome = line[2];

  if (outcome == DRAW)
    myMove = theirMove;
  else if (outcome == WIN)
  {
    if (theirMove == ROCK)
      myMove = PAPER;
    else if (theirMove == PAPER)
      myMove = SCISSORS;
    else
      myMove = ROCK;
  }
  else
  {
    if (theirMove == ROCK)
      myMove = SCISSORS;
    else if (theirMove == PAPER)
      myMove = ROCK;
    else
      myMove = PAPER;
  }

  if (myMove == ROCK)
    score += 1;
  else if (myMove == PAPER)
    score += 2;
  else
    score += 3;

  if (outcome == WIN)
    score += 6;
  else if (outcome == DRAW)
    score += 3;

  return score;
}

int main()
{
  int score = 0;
  string line;
  ifstream Guide("input.txt");

  while (getline(Guide, line))
  {
    score += linescore(line);
  }
  Guide.close();

  cout << "Score: " << score;
  return 0;
}