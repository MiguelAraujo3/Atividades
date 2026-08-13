package POlimorfismo.dominio;

public class Televisao extends Produto {
    public static final double Imposto_Por_Cento = 0.21;
    public Televisao(String nome, double valor) {
        super(nome, valor);
    }

    @Override
    public double calcularImposto() {
        System.out.println("Calculando imposto da Televisão");
          return this.valor * Imposto_Por_Cento;
      }
}
