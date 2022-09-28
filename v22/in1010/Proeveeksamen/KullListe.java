import java.util.Iterator;
class KullListe extends Kull {
    Hund start;
    Hund peker;
    KullListe(Hund mor, Hund far) {
        super(mor, far);
    }

    public void settInn(Hund h) {
        if (start == null) {
            start = h;
            peker = h;
        } else {
            if (peker.compareTo(h) <= 0) {
                peker.neste = h;
                peker = peker.neste;
            } else {
                Hund tmp = start;
                while (tmp.compareTo(h) == -1) {
                    tmp = tmp.neste;
                }
                h.neste = tmp.neste;
                tmp.neste = h;
            }
            
        }
        
    }
    public Iterator<Hund> iterator() {
        return new Iterator<Hund>();
    }
}
