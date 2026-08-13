package POlimorfismo.servico;

import POlimorfismo.repositorio.Repositorio;

public class RepositorioMemoria  implements Repositorio {
    @Override
    public void salvar() {
        System.out.println("Salvando em Memoria");
    }
}
