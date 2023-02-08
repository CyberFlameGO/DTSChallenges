package net.cyberflame.dtschallenges;

import java.nio.charset.StandardCharsets;
import java.text.MessageFormat;
import java.util.Locale;
import java.util.Scanner;

public enum Main {
    ;

    /**
     * @param args
     * @throws RuntimeException
     */
    public static void main(final String[] args) {
        final Scanner scanner = new Scanner(System.in, StandardCharsets.UTF_8);
        final int gsm;
        final String paperTypeQuestion = "Poster paper, or office paper? ";
        System.out.print(paperTypeQuestion);
        gsm = switch (scanner.nextLine().toLowerCase(Locale.ROOT).strip()) {
            case "poster" -> 130;
            case "office" -> 90;
            default ->
                    throw new IllegalStateException("Unexpected value, try 'poster' or 'office'.");
        };
        final String pagesAmountQuestion = "How many pages is your booklet: ";
        System.out.print(pagesAmountQuestion);
        try {
            final int number = scanner.nextInt();
            final Integer calculatedWeight = Integer.valueOf(number * gsm);
            final String rawBookletStr = "The booklet weight is: {0}gsm";
            final String bookletWeightFString = MessageFormat.format(rawBookletStr, calculatedWeight);
            System.out.println(bookletWeightFString);
        } catch (final RuntimeException e) {
            final String invalidPagesError = "Invalid number of pages!";
            System.out.println(invalidPagesError);
        } finally {
            scanner.close();
        }
    }
}
