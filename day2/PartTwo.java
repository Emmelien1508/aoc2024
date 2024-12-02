import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

class PartTwo {
    public static void main(String[] args) {
        List<List<String>> lists = getFileData();

        // For each array in lists, check by removing one item if it becomes safe.
        // Set totalSafe int
        // Loop over list in lists
        // Set safeList variable []
        // Remove item j of list and test for safety
        // Save result in safeList variable
        // If any value of safeList is true, then add 1 to totalSafe
        int totalSafe = 0;
        for (int i = 0; i < lists.size(); i++) {
            List<String> list = lists.get(i);
            Boolean[] safeList = new Boolean[list.size()];

            for (int j = 0; j < list.size(); j++) {
                List<String> newList = removeItemFromList(j, list);
                Boolean safe = testForSafety(newList);
                safeList[j] = safe;
            }

            Boolean anyTrue = testIfAnyTrue(safeList);
            if (anyTrue) {
                totalSafe++;
            }
        }

        System.out.println("So many are safe: " + totalSafe);
    }

    public static List<String> removeItemFromList(int index, List<String> array) {
        if (array == null || index < 0 || index >= array.size()) {
            return array;
        }

        List<String> newArray = new ArrayList<String>(array.size());
        for (int i = 0; i < array.size(); i++) {
            if (i == index) {
                continue;
            }
            newArray.add(array.get(i));
        }

        return newArray;
    }

    public static Boolean testIfAnyTrue(Boolean[] array) {
        Boolean anyTrue = false;

        for (int i = 0; i < array.length; i++) {
            if (array[i]) {
                anyTrue = true;
            }
        }

        return anyTrue;
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

    public static List<List<String>> getFileData() {
        List<List<String>> files = new ArrayList<>();

        try {
            File input = new File("inputs/input.txt");
            Scanner reader = new Scanner(input);

            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                List<String> dataArray = Arrays.asList(data.split(" "));

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

    public static Boolean testForSafety(List<String> array) {
        Boolean safe = true;
        Boolean[] increasing = new Boolean[array.size() - 1];

        for (int j = 0; j < array.size() - 1; j++) {
            int n1 = Integer.parseInt(array.get(j));
            int n2 = Integer.parseInt(array.get(j + 1));

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

        return safe;
    }
}