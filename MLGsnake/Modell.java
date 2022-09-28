import java.util.ArrayList;
import java.util.Random;

public class Modell {
    private View gui;
    private Rute[][] rutenett = new Rute[12][12];
    private char retning = 'v';
    private boolean slutt = false;
    private Rute start;
    ArrayList<Rute> slange = new ArrayList<>();
    int score;
    int antallSkatter;
    int hastighet = 750;

    public Modell(View gui) {
        this.gui = gui;
        for (int rad =0; rad < rutenett.length; rad++) { //Setter opp rutenettet
            for (int kol =0; kol < rutenett[rad].length; kol++) {
                rutenett[rad][kol] = new Rute(rad, kol);
            }
        }
        start = rutenett[6][6];
        gui.setFarge(6,6);
        slange.add(start);
        setSkatt();
    }
    public void startSpill() {
        class SekundTeller extends Thread {
            @Override
            public void run() {
                try {
                    sleep(hastighet);
                    while(!slutt) {
                        flytt(retning);
                        if (antallSkatter < 1) {
                            setSkatt();
                        }
                        sleep(hastighet);
                        sjekkKolisjon();
                    }
                    gui.tapt();
                } catch (InterruptedException e) {
                    System.out.println("s");
                }
            }
        }
        SekundTeller traad = new SekundTeller();
        traad.start();
    }
    public void flytt(char retning) {
        //slangen beveger seg i en retning
        int rad = start.hentRad();
        int kol = start.hentKol();
        
        if (retning == 'n') {
            start = rutenett[rad-1][kol];
            gui.setFarge(rad-1, kol);
            slange.add(start);
        } else if (retning == 's') {
            start = rutenett[rad+1][kol];
            gui.setFarge(rad+1, kol);
            slange.add(start);
        } else if (retning == 'o') {
            start = rutenett[rad][kol+1];
            gui.setFarge(rad, kol+1);
            slange.add(start);

        } else if (retning == 'v') {
            start = rutenett[rad][kol-1];
            gui.setFarge(rad, kol-1);
            slange.add(start);
        }
        if(!erSkatt()) {
            Rute siste = slange.remove(0);
            gui.reset(siste.hentRad(), siste.hentKol());
        } else {
            antallSkatter--;
        }
    }
    public void sjekkKolisjon() {
        //sjekker om slange treffer seg selv
        //sjekker om slangen treffer kantene
        int rad = start.hentRad();
        int kol = start.hentKol();
        
        if (retning == 'n') {
            if (rad -1 < 0) {
                slutt = true;
            } else if (gui.hentString(rad-1, kol).equals("O")) {
                slutt = true;
            }
        } else if (retning == 's') {
            if (rad +1 > rutenett.length-1) {
                slutt = true;
            } else if (gui.hentString(rad+1, kol).equals("O")) {
                slutt = true;
            }
        } else if (retning == 'o') {
            if (kol +1 > rutenett[0].length-1) {
                slutt = true;
            } else if (gui.hentString(rad, kol+1).equals("O")) {
                slutt = true;
            }

        } else if (retning == 'v') {
            if (kol -1 < 0) {
                slutt = true;       
            } else if (gui.hentString(rad, kol-1).equals("O")) {
                slutt = true;
            }
        }
    }
    public void nyRetning(char r) {
        retning = r;
    }
    public boolean erSkatt() {
        if (start instanceof Skatt) {
            gui.setScore(++score);
            rutenett[start.hentRad()][start.hentKol()] = new Rute(start.hentRad(), start.hentKol());
            if (score%3 == 0) {
                hastighet -=50;
            }
            return true;
        }
        return false;
    }
    static int trekk (int a, int b) {
        // Trekk et tilfeldig heltall i intervallet [a..b];
        return (int)(Math.random()*(b-a+1))+a;
    }
    public void setSkatt() {
        int[] tuppel = {trekk(0,11),trekk(0,11)};
        if (!gui.hentString(tuppel[0], tuppel[1]).equals("O")) { //Hvis ruten ikke er slangen, velger man en tilfeldig rute
            rutenett[tuppel[0]][tuppel[1]] = new Skatt(tuppel[0],tuppel[1]);
            gui.setFarge(tuppel[0],tuppel[1],"+");
            antallSkatter++;
        } else { //hvis ikke, så prøver man på nytt
            setSkatt();
        }
    }
}
