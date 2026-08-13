package POlimorfismo.dominio;

public class Tomate extends Produto {
    public static final double Imposto_Por_Cento = 0.06;
    private String dataValidade;
    public Tomate (String nome, double valor){
        super(nome, valor);
    }

    public String getDataValidade() {
        return dataValidade;
    }

    public void setDataValidade(String dataValidade) {
        this.dataValidade = dataValidade;
    }

    @Override
    public double calcularImposto() {
        System.out.println("Calculando o Imposto do Tomate");
        return this.valor * Imposto_Por_Cento;
    }
}
