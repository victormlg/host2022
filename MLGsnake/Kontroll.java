public class Kontroll {
    Modell modell;
    
    public Kontroll() {
        View gui = new View(this);
        modell = new Modell(gui);
        modell.startSpill();
    }
    public void lukkVindu() {
        System.exit(9);
    }
    public void nyRetning(char r) {
        modell.nyRetning(r);
    }
}
