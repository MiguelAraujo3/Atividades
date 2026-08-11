package POlimorfismo.test;

import POlimorfismo.dominio.Computador;
import POlimorfismo.dominio.Produto;
import POlimorfismo.dominio.Tomate;

public class PRodutTest02 {
    static void main(String[] args) {
        Produto produto = new Computador("Ryzen", 3000);
        System.out.println(produto.getNome());
        System.out.println(produto.getValor());
        System.out.println(produto.calcularImposto());
        System.out.println("-----------------");
        Produto produto2 = new Tomate("Ciciliano", 10);
        System.out.println(produto2.getNome());
        System.out.println(produto2.getValor());
        System.out.println(produto2.calcularImposto());
        System.out.println("-----------------");
    }
}
