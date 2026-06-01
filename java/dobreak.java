public class dobreak {
	public static void main(String[] args) {
		System.out.print("Digite um número: ");
		do{
		numero = scanner.nextInt();
		if (numero == 999){
		    break;
		}
		if (numero < 0){
		    System.out.println("Inválido!");
		    continue;
		}
		soma += numero;
		while (true);
	}
	System.out.println("Soma: " + soma );
    }
    }
}