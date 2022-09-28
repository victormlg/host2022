import java.util.Scanner;

class Ascenseur extends Thread {
    int shift;
    int x;
    int y;
    public Ascenseur(int shift, int bouton, int etage) {
        this.shift = shift;
        x =  bouton;
        y = etage; 
    }
    @Override
    public void run() {
        Scanner sc = new Scanner(System.in);
        String svar = sc.next();
        System.out.println("Continuer?");
        while(svar.equals("yes")) {
            remiseANiveau(x, y);
            System.out.println("waiting...");
            sleep(5000);
            if


            System.out.println("Continuer?");
        }
    }
    public int shift() {
        return shift;
    }
    public void setShift(int gearShift) {
        shift = gearShift;
    }
    public void setY(int igrec) {
        y = igrec;
    }
    public void stopp() {
        System.out.println("Stop à l'étage");
    }
    public void move(int millisecond) throws InterruptedException {
        System.out.println("L'ascenseur vient");
        sleep(millisecond);
    }
    public void unstop() {
        System.out.println("Redémarre");
    }
    int remiseANiveau(int a, int b) {
        //a=x, b=y
        if (a == b) {
            return 1; //fin remise à niveau. Base case
        }
        if (a%2 != shift()) {
            if (shift() == 1) {
                setShift(2); //S'il doit monter et que c'est mode descend, change de mode
            } else {
                setShift(1);
            }
        } 
        unstop();
        move(2000);
        stopp();
        if (shift() ==1) {
            setY(b+1);
            return remiseANiveau(a, b+1);
        }
        setY(b-1);
        return remiseANiveau(a, b-1);
    }
}