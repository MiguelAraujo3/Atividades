package projetoEstudante.dominio;

public class
Aluno {
    private String situacaoAluno;
    private double notaCorte;
    private double quantAulas;
    {
        situacaoAluno = "Não Avaliado";
    }
    public Aluno(double notaCorte, double quantAulas) {
        this.notaCorte = notaCorte;
        this.quantAulas = quantAulas;
    }
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

    public String situacao(double nota) {
        if (nota >= notaCorte) {
            situacaoAluno = "Aprovado";
            return situacaoAluno;
        } else {
            situacaoAluno = "Reprovado";
            return situacaoAluno;
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

    public double frequencia(double faltas) {
        double result = (quantAulas-faltas)/quantAulas *100;
        if (quantAulas >= faltas) {
            return result;
        } else {
            System.out.println("ERRO, A QUANTIDADE DE FALTAS É MAIOR QUE AS AULAS");
            return 0;
        }
    }
}
