import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

class PartOne {
    public static void main(String []args) {
        // Get the file data in two columns
        List<List<Integer>> columns = getFileData();
        List<Integer> leftCol = columns.get(0);
        List<Integer> rightCol = columns.get(1);

        // Sort arrays from smallest to largest
        leftCol.sort(null);
        rightCol.sort(null);

        int totalDistance = 0;
        for (int i = 0; i < leftCol.size(); i++) {
            totalDistance += getAbsoluteNumber(leftCol.get(i), rightCol.get(i));
        }

        System.out.println("this is the total distance: " + totalDistance);
    }

    public static int getAbsoluteNumber(int a, int b) {
        if (a < b) {
            return b - a;
        }
        return a - b;
    }

    public static List<List<Integer>> getFileData() {
        // Initalize the columns
        List<Integer> leftCol = new ArrayList<>();
        List<Integer> rightCol = new ArrayList<>();

        try {
            File input = new File("inputs/input.txt");
            Scanner reader = new Scanner(input);

            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                String[] dataArray = data.split(" ");

                // First and last are for left and right col
                String firstElement = dataArray[0];
                String lastElement = dataArray[dataArray.length - 1];

                int firstElementInt = Integer.parseInt(firstElement);
                int lastElementInt = Integer.parseInt(lastElement);

                leftCol.add(firstElementInt);
                rightCol.add(lastElementInt);
            }
            reader.close();
        } catch (FileNotFoundException e){
            System.out.println("Something went wrong!");
            e.printStackTrace();
        }

        return Arrays.asList(leftCol, rightCol);
    }
};