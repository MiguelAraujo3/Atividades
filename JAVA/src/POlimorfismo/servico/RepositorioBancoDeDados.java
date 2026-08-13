package POlimorfismo.servico;

import POlimorfismo.repositorio.Repositorio;

public class RepositorioBancoDeDados implements Repositorio {
    @Override
    public void salvar() {
        System.out.println("Salvando em Banco de Dados");
    }
}
