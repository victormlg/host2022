class Tidspunkt implements Comparable<Tidspunkt> {
    public int aar, mnd, dag, time, min, sek;
    Tidspunkt(int aar, int mnd, int dag, int time, int min, int sek) {
        this.aar = aar;
        this.mnd = mnd;
        this.dag = dag;
        this.time = time;
        this.min = min;
        this.sek = sek;
    }
    @Override
    public int compareTo(Tidspunkt tidspunkt) {
        if (aar > tidspunkt.aar && mnd > tidspunkt.mnd && dag > tidspunkt.dag && time > tidspunkt.time && min > tidspunkt.min && sek > tidspunkt.sek) {
            return 1;
        } else if (aar == tidspunkt.aar && mnd == tidspunkt.mnd && dag == tidspunkt.dag && time == tidspunkt.time && min == tidspunkt.min && sek == tidspunkt.sek) {
            return 0;
        } else {
            return -1;
        }
    }
}