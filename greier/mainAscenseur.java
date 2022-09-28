import java.util.Scanner;
class mainAscenseur {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Bouton de 1 à 4");
        int bouton = sc.nextInt();
        System.out.println("Etage de 1 à 3");
        int etage = sc.nextInt();
        Ascenseur asc = new Ascenseur(1, bouton, etage);
        asc.start();
        
    }
}