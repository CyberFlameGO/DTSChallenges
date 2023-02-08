package net.cyberflame.dtschallenges;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.nio.charset.StandardCharsets;
import java.text.MessageFormat;
import java.util.Enumeration;
import java.util.Locale;
import java.util.Scanner;
import java.util.ResourceBundle;

public enum Main {
    ;

    /**
     * @param args
     * @throws RuntimeException
     */
    public static void main(final String[] args) {
        final Scanner scanner = new Scanner(System.in, StandardCharsets.UTF_8);
        final int gsm;
        final ResourceBundle resourceBundle = new ResourceBundle() {
            @Override
            protected @Nullable Object handleGetObject(@NotNull String key) {
                return null;
            }

            @Override
            public @Nullable Enumeration<String> getKeys() {
                return null;
            }
        };
        final String paperTypeQuestion = resourceBundle.getString("paper.type");
        System.out.print(paperTypeQuestion);
        gsm = switch (scanner.nextLine().toLowerCase(Locale.ROOT).strip()) {
            case "poster" -> 130;
            case "office" -> 90;
            case default -> throw new RuntimeException("Invalid paper type");
        };
        final String pagesAmountQuestion = resourceBundle.getString("pages.amount");
        System.out.print(pagesAmountQuestion);
        try {
            final int number = scanner.nextInt();
            final Integer calculatedWeight = Integer.valueOf(number * gsm);
            final String rawBookletStr = resourceBundle.getString("booklet.weight");
            final String bookletWeightFString = MessageFormat.format(rawBookletStr, calculatedWeight);
            System.out.println(bookletWeightFString);
        } catch (final RuntimeException e) {
            final String invalidPagesError = resourceBundle.getString("invalid.pages");
            System.out.println(invalidPagesError);
        } finally {
            scanner.close();
        }
    }
}
