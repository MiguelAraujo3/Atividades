package POlimorfismo.test;

import POlimorfismo.dominio.Computador;
import POlimorfismo.dominio.Produto;
import POlimorfismo.dominio.Tomate;
import POlimorfismo.servico.CalculadoraImposto;

public class ProdutTest03 {
    static void main(String[] args) {
        Produto produto = new Computador("Ryzen", 3000);

        Tomate tomate = new  Tomate("Ciciliano", 10);
        tomate.setDataValidade("11/12/2026");

        CalculadoraImposto.calcularImposto(tomate);
        CalculadoraImposto.calcularImposto(produto);

    }
}
