package POlimorfismo.test;

import POlimorfismo.dominio.Computador;
import POlimorfismo.dominio.Produto;
import POlimorfismo.dominio.Televisao;
import POlimorfismo.dominio.Tomate;
import POlimorfismo.servico.CalculadoraImposto;

public class ProdutoTest01 {
    static void main(String[] args ) {
        Produto computador = new Computador("Miguel", 11000);
        Produto tomate = new Tomate("Tomate cabeçã", 10);
        Produto tv = new Televisao("Philco", 3000);
        CalculadoraImposto.calcularImposto(computador);
        System.out.println("--------------------------");
        CalculadoraImposto.calcularImposto(tomate);
        System.out.println("--------------------------");
        CalculadoraImposto.calcularImposto(tv);
    }
}
