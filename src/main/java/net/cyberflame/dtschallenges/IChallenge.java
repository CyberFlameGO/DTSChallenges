package net.cyberflame.dtschallenges;

import java.io.IOException;

public interface IChallenge {

    void main(String[] args) throws IOException;
    default void run() {
        System.out.println("Running challenge " + this.getClass().getSimpleName());
        main(new String[] {});
    }
}
