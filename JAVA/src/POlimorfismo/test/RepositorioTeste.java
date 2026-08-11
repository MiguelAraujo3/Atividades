package POlimorfismo.test;

import POlimorfismo.repositorio.Repositorio;
import POlimorfismo.servico.RepositorioBancoDeDados;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class RepositorioTeste {
    static void main(String[] args) {
        Repositorio repositorioBancoDeDados = new RepositorioBancoDeDados();
        repositorioBancoDeDados.salvar();
        List<String> list = new ArrayList<>();
        list.add("mIGUel");
        list.add("Artiur");
        list.add("Jubileu");
        System.out.println(list);
    }
}
