import java.util.Scanner;
public class Main{
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);
        int numero;
        int soma = 0;
        do {
            System.out.print("Digite um número: ");
            numero = input.nextInt();
            if (numero == 100){
                break;
            }
            if (numero < 0){
                System.out.println("Inválido");
                continue;
            }
            soma += numero;
            } while(true);
        System.out.println("Soma: " + soma);
        }
    }