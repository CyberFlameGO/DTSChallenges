package net.cyberflame.dtschallenges;

public interface IChallenge {

    void main(String[] args);
    default void run() {
        System.out.println("Running challenge " + this.getClass().getSimpleName());
        main(new String[] {});
    }
}
