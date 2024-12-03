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

        Pattern pattern = Pattern.compile("[0-9]+", Pattern.CASE_INSENSITIVE);

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

        // System.out.println("this is the total score: " + totalScore);
    }

    public static List<String> getFileData() {
        List<String> lists = new ArrayList<String>();
        Pattern disablePattern = Pattern.compile("don't\\(\\)", Pattern.CASE_INSENSITIVE);
        Pattern enablePattern = Pattern.compile("do\\(\\)", Pattern.CASE_INSENSITIVE);
        Pattern multiplierPattern = Pattern.compile("mul\\([0-9]+,[0-9]+\\)", Pattern.CASE_INSENSITIVE);

        try {
            File input = new File("aoc2024/day3/inputs/test2.txt");
            Scanner reader = new Scanner(input);

            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                
                Matcher disableMatcher = disablePattern.matcher(data);
                Matcher enableMatcher = enablePattern.matcher(data);
                Matcher mulitiplierMatcher = multiplierPattern.matcher(data);

                // Find indices of don't()
                List<Integer> disableIndices = new ArrayList<Integer>();
                while (disableMatcher.find()) {
                    disableIndices.add(disableMatcher.end());
                }

                // Find indices of do()
                List<Integer> enableIndices = new ArrayList<Integer>();
                while (enableMatcher.find()) {
                    enableIndices.add(enableMatcher.end());
                }

                // Make a list of all indices
                // Remove the ones from start disabled until the end
                // Add again the ones from start enabled until the end
                // Do this until you've went through all one by one
                // First disabled, then abled, then disabled, then abled, etc.
                // how do we know how to do om-and-om?

                // Create list of illegalIndices
                List<Integer> illegalIndices = new ArrayList<Integer>();
                for (int i = 0; i < disableIndices.size(); i++) {
                    int disabledIndex = disableIndices.get(i);
                    for (int j = 0; j < enableIndices.size(); j++) {
                        int enabledIndex = enableIndices.get(j);
                        if (disabledIndex < enabledIndex) {
                            System.out.println("Disabled < Enabled: " + disabledIndex + " < " + enabledIndex);
                            List<Integer> disabledRange = getRange(disabledIndex, enabledIndex);
                            for (int k = 0; k < disabledRange.size(); k++) {
                                illegalIndices.add(disabledRange.get(k));
                            }
                        }
                    }
                }
                
                System.out.println("These are the illegal indices:");
                for (int i = 0; i < illegalIndices.size(); i++) {
                    System.out.println(illegalIndices.get(i));
                }

                // We can find the indices of the multipliermatcher
                while (mulitiplierMatcher.find()) {
                    lists.add(mulitiplierMatcher.group());
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
            while(currentNumber < n1) {
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