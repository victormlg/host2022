class BareFlyReise extends Reise {

    BareFlyReise(String navn, int pris, int antallLedigePlasser) {
        super(navn, pris, antallLedigePlasser);
    }
    int pris() {
        return pris;
    }
}