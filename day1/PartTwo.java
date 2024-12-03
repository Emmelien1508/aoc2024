import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

class PartTwo {
    public static void main(String[] args) {
        List<List<Integer>> columns = getFileData();
        List<Integer> leftCol = columns.get(0);
        List<Integer> rightCol = columns.get(1);

        int similarityScore = 0;
        for (int i = 0; i < leftCol.size(); i++) {
            int number = leftCol.get(i);
            int duplicates = countNumberInArray(number, rightCol);
            similarityScore += number * duplicates;
        }

        System.out.println("This is the similarity score: " + similarityScore);
    }

    public static int countNumberInArray(int number, List<Integer> array) {
        int count = 0;
        for (int i = 0; i < array.size(); i++) {
            if (number == array.get(i)) {
                count++;
            }
        }

        return count;
    }

    public static List<List<Integer>> getFileData() {
        List<Integer> leftCol = new ArrayList<>();
        List<Integer> rightCol = new ArrayList<>();

        try {
            File input = new File("inputs/input.txt");
            Scanner reader = new Scanner(input);

            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                String[] dataArray = data.split(" ");

                // First and last are for left & right column
                String firstElement = dataArray[0];
                String lastElement = dataArray[dataArray.length - 1];

                int firstElementInt = Integer.parseInt(firstElement);
                int lastElementInt = Integer.parseInt(lastElement);

                leftCol.add(firstElementInt);
                rightCol.add(lastElementInt);
            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Something went wrong!");
            e.printStackTrace();
        }

        return Arrays.asList(leftCol, rightCol);
    }
}