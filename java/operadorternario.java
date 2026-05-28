import java.util.Scanner;

public class operadorternario {
    public static void main (String[]args){
        Scanner input = new Scanner(System.in);
        System.out.print("Digite sua idade: ");
        int idade = input.nextInt();
        if (idade >= 18){
        System.out.println("Maior de idade");
        }
        else {
            System.out.println("Menor de idade");
        }
    }
}