package net.cyberflame.dtschallenges.challenges;

public interface IChallenge {

    void main(String[] args);
    default void run() {
        System.out.println("Running challenge " + this.getClass().getSimpleName());
        main(new String[] {});
    }
}
