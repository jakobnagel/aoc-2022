import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class App {
  public static void main(String[] args) throws Exception {
    ArrayList<String> lines = getItems();
    String[][] rucksacks = sortRucksacks(lines);
    /*
     * char[] commonItems = commonItems(rucksacks);
     * int[] priorities = new int[commonItems.length];
     * 
     * for (int i = 0; i < priorities.length; i++) {
     * priorities[i] = itemToPriority(commonItems[i]);
     * }
     * 
     * int sum = 0;
     * for (int i = 0; i < priorities.length; i++) {
     * sum += priorities[i];
     * }
     * 
     * System.out.println(sum);
     */

    String[][] groups = new String[rucksacks.length / 3][3];
    for (int i = 0; i < rucksacks.length; i++) {
      int group = Math.floorDiv(i, 3);
      int memberNumber = i % 3;
      groups[group][memberNumber] = rucksacks[i][0] + rucksacks[i][1];
    }

    char[] priorityItems = new char[groups.length];
    for (int i = 0; i < groups.length; i++) {
      priorityItems[i] = duplicate2(groups[i]);
    }

    int sum = 0;
    for (int i = 0; i < priorityItems.length; i++) {
      sum += itemToPriority(priorityItems[i]);
    }

    System.out.println(sum);
  }

  static ArrayList<String> getItems() {
    ArrayList<String> lines = new ArrayList<String>();
    try {
      File inputFile = new File("input.txt");
      Scanner myReader = new Scanner(inputFile);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        lines.add(data);
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }

    return lines;
  }

  static String[][] sortRucksacks(ArrayList<String> rucksackList) {
    int amountRucksacks = rucksackList.size();
    String[][] rucksacks = new String[amountRucksacks][2];

    for (int i = 0; i < amountRucksacks; i++) {
      String rucksack = rucksackList.get(i);
      int mid = Math.round(rucksack.length() / 2);
      rucksacks[i][0] = rucksack.substring(0, mid);
      rucksacks[i][1] = rucksack.substring(mid);
    }

    return rucksacks;
  }

  static char[] commonItems(String[][] rucksacks) {
    int amountRucksacks = rucksacks.length;

    char[] commonItems = new char[amountRucksacks];

    for (int i = 0; i < amountRucksacks; i++) {
      String com1 = rucksacks[i][0];
      String com2 = rucksacks[i][1];
      commonItems[i] = duplicate(com1, com2);
    }

    return commonItems;
  }

  static char duplicate(String pack1, String pack2) {
    for (int i = 0; i < pack1.length(); i++) {
      char item = pack1.charAt(i);
      if (pack2.contains("" + item)) {
        return item;
      }
    }
    return '\0';
  }

  static char duplicate2(String[] packs) {
    for (int i = 0; i < packs[0].length(); i++) {
      char item = packs[0].charAt(i);
      boolean duplicate = true;
      for (int j = 1; j < packs.length; j++) {
        if (!packs[j].contains("" + item)) {
          duplicate = false;
          break;
        }
      }

      if (duplicate) {
        return item;
      }
    }
    return '\0';
  }

  static int itemToPriority(char item) {
    String lowercase = "abcdefghijklmnopqrstuvwxyz";
    int priority;

    if (lowercase.contains("" + item)) {
      priority = item - 'a' + 1;
    } else {
      priority = item - 'A' + 27;
    }

    return priority;
  }
}
