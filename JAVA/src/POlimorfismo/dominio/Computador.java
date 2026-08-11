package POlimorfismo.dominio;

public class Computador extends Produto {
    public static final double Imposto_Por_Cento = 0.21;
    public Computador(String nome, double valor){
        super(nome, valor);
    }

    @Override
    public double calcularImposto() {
        System.out.println("Calculando o Imposto do Computador");
        return this.valor * Imposto_Por_Cento;
    }

}
