package net.cyberflame.dtschallenges.challenges;

import net.cyberflame.dtschallenges.Main;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.concurrent.TimeUnit;


public class PythonChallenges extends BaseChallenge {

    @Override
    public void main(String[] args) {
        System.out.println("This is challenge " + Main.getChallenge());
        Process proc = null;
        try {
            String pyScriptLoc = Main.class.getProtectionDomain().getCodeSource().getLocation()
                    .toURI().getPath();
            proc = new ProcessBuilder("python", pyScriptLoc, Integer.toString(Main.getChallenge()))
                    .inheritIO()
                    .start();
            assert null != proc;
            if (!proc.waitFor(10L, TimeUnit.SECONDS)) {
                proc.destroyForcibly();
            }
        } catch (IOException | URISyntaxException e) {
            e.printStackTrace();
        }

        catch (InterruptedException e) {
            proc.destroyForcibly();
            e.printStackTrace();
        }

        if (proc.exitValue() != 0) {
            System.out.println("Process exited with non-zero status code. Code: " + proc.exitValue());
            // Handle error
        }
    }
}
