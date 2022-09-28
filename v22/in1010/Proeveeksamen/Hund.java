import java.util.Iterator;
class Hund implements Comparable<Hund> {
    String navn;
    Kull mittKull;
    Tidspunkt minFodselstid;
    Hund neste = null;

    Hund(Kull k, String navn, Tidspunkt fodt) {
        this.navn = navn;
        mittKull = k;
        minFodselstid = fodt;
    }
    @Override
    public int compareTo(Hund h) {
        if (minFodselstid.compareTo(h.minFodselstid) == 1) {
            return 1;
        } else if (minFodselstid.compareTo(h.minFodselstid) == 0) {
            return 0;
        } else {
            return -1;
        }
    }
    public Hund mor() {
        return mittKull.mor;
    }
    public Hund far () {
        return mittKull.far;
    }
    public boolean erHelsosken(Hund h) {
        return (far().equals(h.far()) && mor().equals(h.mor()));
    }
    public boolean erHalvsosken(Hund h) {
        return (far().equals(h.far()) ^ mor().equals(h.mor()));
    }
    public Hund finnEldsteKjenteOpphav() {
        if (this.far() == null && this.mor() == null) {
            return this;
        }
        if (this.far() != null) {
            return this.far().finnEldsteKjenteOpphav();
        }
        return this.mor().finnEldsteKjenteOpphav();
    }
}
abstract class Kull implements Iterable<Hund> {
    Hund mor, far;
    Kull (Hund mor, Hund far) {
        this.mor = mor;
        this.far = far;
    }
    public abstract void settInn(Hund h);
    
    public abstract Iterator<Hund> iterator();
}
