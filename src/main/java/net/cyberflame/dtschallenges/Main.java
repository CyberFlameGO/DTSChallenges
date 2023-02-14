package net.cyberflame.dtschallenges;

import net.cyberflame.dtschallenges.challenges.*;

import java.util.Scanner;

public class Main {

    /**
     * @throws IllegalStateException
     */
    public static void main(final String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Which challenge would you like to run? ");
        int challenge = scanner.nextInt();
        switch (challenge) {
            case 1 -> new Challenge01().run();
            default -> throw new IllegalStateException("Unexpected value: " + challenge);
        }



    }
}
