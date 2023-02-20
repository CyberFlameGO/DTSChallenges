package net.cyberflame.dtschallenges.challenges;

import net.cyberflame.dtschallenges.Main;

import java.io.IOException;
import java.net.URISyntaxException;
import java.lang.IllegalThreadStateException;
import java.util.concurrent.TimeUnit;


public class PythonChallenges extends BaseChallenge {

    @Override
    public void main(String[] args) {
        System.out.println("This is challenge " + Main.getChallenge());
        Process proc = null;
        try {
            String pyScriptLoc = Main.class.getProtectionDomain().getCodeSource().getLocation()
                    .toURI().getPath();
            proc = new ProcessBuilder("python", pyScriptLoc,
            Long.toString(ProcessHandle.current().pid()),
            Integer.toString(Main.getChallenge()))
                    .inheritIO()
                    .start();
            if (!proc.waitFor(600L, TimeUnit.SECONDS)) {
                 proc.destroyForcibly();
            }
        } catch (IOException | URISyntaxException e) {
            e.printStackTrace();
        }

        catch (InterruptedException | IllegalThreadStateException e) {
//             proc.destroyForcibly();
                e.printStackTrace();
        }

        assert proc != null;
        if (proc.exitValue() != 0) {
            System.out.println("Process exited with non-zero status code. Code: " + proc.exitValue());
            // Handle error
        }
    }
}
