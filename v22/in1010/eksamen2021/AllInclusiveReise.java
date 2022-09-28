class AllInclusiveReise extends Reise{
    int kvalitetsvurdering; //mellom 1 og 6

    AllInclusiveReise(String navn, int pris, int antallLedigePlasser, int kvalitetsvurdering) {
        super(navn, pris, antallLedigePlasser);
        this.kvalitetsvurdering = kvalitetsvurdering;
    }
    
}