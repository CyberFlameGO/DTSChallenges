package net.cyberflame.dtschallenges.challenges;

import java.nio.charset.StandardCharsets;
import java.text.MessageFormat;
import java.util.Locale;
import java.util.Scanner;

public class Challenge01 extends BaseChallenge {
    @Override
    public void main(final String[] args) {
        // Creates a scanner which reads from stdin, and uses UTF-8 encoding.
        final Scanner scanner = new Scanner(System.in, StandardCharsets.UTF_8);
        // The following are the strings used in the program.
        final String paperTypeQuestion = "Poster paper, or office paper? ";
        final String rawBookletStr = "The booklet weight is: {0}gsm";
        final String invalidPagesError = "Invalid number of pages!";
        final String pagesAmountQuestion = "How many pages is your booklet: ";
        // Initialises the integer variable gsm, which is used to store the weight of the paper.
        int gsm;

        // Asks the user for the type of paper they are using, and stores the weight of the paper in gsm.
        System.out.print(paperTypeQuestion);
        gsm = switch (scanner.nextLine().toLowerCase(Locale.ROOT).strip()) {
            case "poster" -> 130;
            case "office" -> 90;
            // If the user enters an invalid value, it will throw an IllegalStateException.
            default ->
                    throw new IllegalStateException("Unexpected value, try 'poster' or 'office'.");
        };
        // Asks the user for the amount of pages in their booklet, and calculates the weight of the booklet.
        System.out.print(pagesAmountQuestion);
        // Tries to parse the input as an integer, and if it fails, it will print an error message.
        try {
            final int number = scanner.nextInt();
            final Integer calculatedWeight = Integer.valueOf(number * gsm);
            final String bookletWeightFString = MessageFormat.format(rawBookletStr, calculatedWeight);
            System.out.println(bookletWeightFString);
        } catch (final RuntimeException e) {
            System.out.println(invalidPagesError);
        } finally {
            scanner.close();
        }
    }
};
