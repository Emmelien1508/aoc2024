package aoc2024.day3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class PartOne {
    public static void main(String[] args) {
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

        System.out.println("this is the total score: " + totalScore);
    }

    public static List<String> getFileData() {
        List<String> lists = new ArrayList<String>();
        Pattern pattern = Pattern.compile("mul\\([0-9]+,[0-9]+\\)", Pattern.CASE_INSENSITIVE);

        try {
            File input = new File("aoc2024/day3/inputs/input.txt");
            Scanner reader = new Scanner(input);

            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                Matcher matcher = pattern.matcher(data);
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
};