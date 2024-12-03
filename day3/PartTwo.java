package aoc2024.day3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class PartTwo {
    public static void main(String[] args) {
        // Get list of all mul(X,Y) from file
        int totalScore = 0;
        List<Integer> scores = new ArrayList<Integer>();
        Pattern pattern = Pattern.compile("[0-9]+");

        List<String> lists = getFileData();
        for (int i = 0; i < lists.size(); i++) {
            // Now we can actually get the numbers
            int score = 1;
            Matcher matcher = pattern.matcher(lists.get(i));
            while (matcher.find()) {
                int multiplier = Integer.parseInt(matcher.group());
                score *= multiplier;
            }
            scores.add(score);
        }

        for (int i = 0; i < scores.size(); i++) {
            totalScore += scores.get(i);
        }

        System.out.println("this is the total score: " + totalScore);
    }

    public static List<String> getFileData() {
        List<String> lists = new ArrayList<String>();
        // Remove all the strings in the text between don't() and do()
        String pattern = "(don't\\(\\).*?do\\(\\))|(don't\\(\\).*$)";
        Pattern multiplyPattern = Pattern.compile("mul\\([0-9]+,[0-9]+\\)");

        try {
            File input = new File("aoc2024/day3/inputs/input.txt");
            Scanner reader = new Scanner(input);

            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                String cleanedData = data.replaceAll(pattern, "");
                Matcher matcher = multiplyPattern.matcher(cleanedData);
                while (matcher.find()) {
                    lists.add(matcher.group());
                }
            }

            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("something went wrong!");
            e.printStackTrace();
        }

        return lists;
    }

    public static List<Integer> getRange(int n1, int n2) {
        System.out.println("getting the range with these numbers: " + n1 + " & " + n2);
        Boolean reverse = false;
        int currentNumber = 0;

        // Case n1 < n2
        if (n1 < n2) {
            currentNumber = n1;
        }

        // Case n1 > n2
        if (n1 > n2) {
            currentNumber = n2;
        }

        List<Integer> range = new ArrayList<Integer>();

        System.out.println("starting with current number: " + currentNumber);
        System.out.println("Reverse: " + reverse);
        if (reverse) {
            while (currentNumber < n1) {
                range.add(currentNumber);
                currentNumber++;
            }
        } else {
            while (currentNumber < n2) {
                range.add(currentNumber);
                currentNumber++;
            }
        }

        return range;
    }
};