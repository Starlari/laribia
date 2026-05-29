public class continue
{
	public static void main(String[] args) {
		int contador = 0;
		while (contador < 10){
		    contador++;
		    if (contador % 2 == 0){
		     continue;   
		    }
		
		System.out.println("ímpar: " + contador);
	    }
    }
}