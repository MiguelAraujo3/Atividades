package POlimorfismo.servico;

import POlimorfismo.repositorio.Repositorio;

public class RepositorioArquivo implements Repositorio {
    @Override
    public void salvar() {
        System.out.println("Salvando em Arquivo");
    }
}
