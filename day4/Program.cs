// See https://aka.ms/new-console-template for more information
using System.IO;

string[] lines = File.ReadAllLines("input.txt");

int containedCount = 0;
foreach (string line in lines)
{
  if (IsContained(line))
  {
    containedCount++;
  }
}

Console.WriteLine(containedCount);


bool IsContained(string line)
{
  string[] elves = split(line, ',');
  string[] elf1 = elves[0].Split('-');
  string[] elf2 = elves[1].Split('-');

  int min1 = Convert.ToInt32(elf1[0]);
  int max1 = Convert.ToInt32(elf1[1]);
  int min2 = Convert.ToInt32(elf2[0]);
  int max2 = Convert.ToInt32(elf2[1]);

  return min1 >= min2 && max1 <= max2 || min2 >= min1 && max2 <= max1;
}

string[] split(string line, char sChar)
{
  int idx = line.IndexOf(sChar);
  string[] splitLine = new string[2];
  splitLine[0] = line.Substring(0, idx);
  splitLine[1] = line.Substring(idx + 1);
  return splitLine;
}