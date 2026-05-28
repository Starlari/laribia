import java.util.Scanner;

public class area {
    public static void main (String[]args){
        Scanner input = new Scanner(System.in);
        System.out.print("Digite a medida da base do seu retângulo: ");
        float base = input.nextFloat();
        System.out.print("Digite a medida da altura do seu retângulo: ");
        float altura = input.nextFloat();
        float area = (altura * base);
        System.out.println("A área do seu retângulo foi de: " + area);
        String tamanho = area >= 800 ? "Retangulo grande." : "Retangulo pequeno";
        System.out.println(tamanho);
        }
    }