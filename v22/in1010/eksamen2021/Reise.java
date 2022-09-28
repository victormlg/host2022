class Reise {
    String navn;
    int pris;
    int antallLedigePlasser;

    Reise(String navn, int pris, int antallLedigePlasser) {
        this.navn=navn;
        this.pris = pris;
        this.antallLedigePlasser = antallLedigePlasser;
    }
    int pris() {
        return (int) (pris*1.25);
    }
}