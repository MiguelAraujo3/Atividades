package projetoEstudante.dominio;

public class Aluno {
    public double media(double soma, int quant) {
        soma /= quant;
        return soma;
    }

    public void alunosMaiorNota(String[] aluno) {
        System.out.print("Aluno(s) com a(s) maior(es) nota(s): ");
        for (String name : aluno) {
            if (name == null) {
                System.out.print("");
            } else {
                System.out.print(name + "; ");
            }
        }
        System.out.print("");
    }

    public String situacao(double nota, double notaCorte) {
        if (nota >= notaCorte) {
            return "Aprovado";
        } else {
            return "Reprovado";
        }
    }

    public String situacaoNota(double nota, double maiorNota, double menorNota) {
        if (nota == maiorNota) {
            return " | Maior nota da turma";
        } else if (nota == menorNota) {
            return " | Menor nota da turma";
        } else {
            return "";
        }
    }

    public double frequencia(double aulas, double faltas) {
        double result = (aulas-faltas)/aulas *100;
        if (aulas >= faltas) {
            return result;
        } else {
            System.out.println("ERRO, A QUANTIDADE DE FALTAS É MAIOR QUE AS AULAS");
            return 0;
        }
    }
}
