package net.cyberflame.dtschallenges;

import net.cyberflame.dtschallenges.challenges.*;

import java.util.Scanner;

public class Main {

    private static int challenge;


    public static int getChallenge() {
        return challenge;
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Which challenge would you like to run? ");
        challenge = scanner.nextInt();
        switch (getChallenge()) {
            case 1 -> new Challenge01().run();
            case 2,3 -> new PythonChallenges().run();
            default -> throw new IllegalStateException("Unexpected value: " + getChallenge());
        }



    }
}
