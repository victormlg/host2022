import java.util.Iterator;
class KullArray extends Kull {

    Hund[] arr = new Hund[60];

    KullArray(Hund mor, Hund far) {
        super(mor, far);
    }
    public void settInn(Hund h) {
        Hund tmp = null;
        if (arr[h.minFodselstid.sek] != null) {
            tmp = arr[h.minFodselstid.sek];
            arr[h.minFodselstid.sek] = h;
            h.neste = tmp;
        } else {
            arr[h.minFodselstid.sek] = h;
        }
    }
    public Iterator<Hund> iterator() {
        return null;
    }
    public void skrivUtAlle() {
        for (Hund hund : arr) {
            Hund tmp = hund;
            System.out.println(hund.navn);
            while (tmp.neste != null) {
                tmp = tmp.neste;
                System.out.println(tmp.navn);
            }
        }
    }
}