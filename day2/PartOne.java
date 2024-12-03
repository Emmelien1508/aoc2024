package aoc2024.day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

class PartOne {
    public static void main(String[] args) {
        // Get file data in lists of integers
        List<String[]> lists = getFileData();

        // Per list, check if all increasing / decreasing
        // AND if increasing / decreasing with 1, 2 or 3
        int totalSafe = 0;
        for (int i = 0; i < lists.size(); i++) {
            String[] list = lists.get(i);

            Boolean safe = true;
            Boolean[] increasing = new Boolean[list.length - 1];

            for (int j = 0; j < list.length - 1; j++) {
                int n1 = Integer.parseInt(list[j]);
                int n2 = Integer.parseInt(list[j + 1]);

                // Check for difference
                int difference = getDifference(n1, n2);
                if (difference < 1 || difference > 3) {
                    safe = false;
                }

                // Check for all increasing or all decreasing
                if (n1 > n2) {
                    increasing[j] = true;
                } else {
                    increasing[j] = false;
                }
            }

            Boolean same = isAllEqual(increasing);
            if (!same) {
                safe = false;
            }

            if (safe) {
                totalSafe++;
            }
        }

        System.out.println("This is the total nr of safe items: " + totalSafe);
    }

    public static int getDifference(int n1, int n2) {
        if (n1 < n2) {
            return n2 - n1;
        }
        return n1 - n2;
    }

    public static Boolean isAllEqual(Boolean[] array) {
        return Arrays.stream(array).allMatch(element -> Objects.equals(array[0], element));
    }

    public static List<String[]> getFileData() {
        List<String[]> files = new ArrayList<>();

        try {
            File input = new File("inputs/input.txt");
            Scanner reader = new Scanner(input);

            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                String[] dataArray = data.split(" ");

                // Append dataArray to some list and return this
                files.add(dataArray);
            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println(("something went wrong!"));
            e.printStackTrace();
        }

        return files;
    }
};