import java.util.Scanner;
import java.util.Random;

public class sayitahmin4
 {
    public static void main(String[] args) {
        Random rand = new Random();
        int rastgeleSayi = rand.nextInt(100) + 1;
        Scanner scanner = new Scanner(System.in);
        int tahmin = 0;

        System.out.println("1 ile 100 arasinda bir sayi tuttum. Bakalim tahmin edebilecek misin?");

        while (tahmin != rastgeleSayi) {
            System.out.print("Tahmininiz: ");
            tahmin = scanner.nextInt();

            if (tahmin < rastgeleSayi) {
                System.out.println("Daha buyuk bir sayi girin.");
            } else if (tahmin > rastgeleSayi) {
                System.out.println("Daha kucuk bir sayi girin.");
            } else {
                System.out.println("Tebrikler! Doğru tahmin ettiniz.");
            }
        }


        scanner.close();
    }
}
