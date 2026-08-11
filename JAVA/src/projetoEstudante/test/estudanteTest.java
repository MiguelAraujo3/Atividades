package projetoEstudante.test;
import java.util.Arrays;
import java.util.Scanner;
import projetoEstudante.dominio.Aluno;

public class  estudanteTest {
    public static void main(String[] args) {
        //Cabeçalho
        System.out.println();
        System.out.println("=======Critérios=======");
        System.out.println("Digite apenas o tipo pedido (ou só números ou apenas palavras)");
        System.out.println("As notas vão de 0 a 10");
        System.out.println();
        //Receber do usuário q quantidade de alunos, a nota de corte e a quantidade de aulas
        Scanner leia = new Scanner(System.in);
        System.out.print("Digite a quantidade de alunos da turma: ");
        int quant = leia.nextInt();
        System.out.print("Digite qual a nota de corte para Aprovação: ");
        double notaCorte = leia.nextDouble();
        System.out.print("Digite a quantidade de aulas que terão no período: ");
        double quantAulas = leia.nextInt();
        leia.nextLine();
        Aluno metodo = new Aluno(notaCorte, quantAulas);
        //variáveis
        int choose;
        double[] falta = new double[quant];
        double maiorNota = -1;
        double menorNota = 11;
        double[] nota = new double[quant];
        String[] nome = new String[quant];
        double soma = 0;
        int notaMaiorQuant = 0;
        String[] alunosMaiorNota = new String[quant];
        //Receber do Usuário os nomes e notas dos alunos
        for (int i = 0; i < quant; i++) {
            System.out.print("Digite o nome do aluno: ");
            nome[i] = leia.nextLine();
            System.out.printf("Digite a nota do aluno %s: ", nome[i]);
            nota[i] = leia.nextDouble();
            System.out.printf("Digite a quantidade de faltas do aluno %s: ", nome[i]);
            falta[i] = leia.nextInt();
            leia.nextLine();
            if (nota[i] < menorNota) {
                menorNota = nota[i];
            }
            if (nota[i] > maiorNota) {
                maiorNota = nota[i];
                Arrays.fill(alunosMaiorNota, null);
            }
            if (maiorNota == nota[i]) {
                alunosMaiorNota[i] = nome[i];
            }
            soma += nota[i];

        }

        //OPÇÕES
        while (true) {
            //Menu de escolhas
            System.out.println();
            System.out.println("==========OPÇÕES==========");
            System.out.println("===== 1: Visualizar a média geral da Turma ====");
            System.out.println("===== 2: Visualizar a taxa de aprovação da Turma ====");
            System.out.println("===== 3: Visualizar a maior nota da Turma ====");
            System.out.println("===== 4: Visualizar a frequência ====");
            System.out.println("===== 5: Visualizar Notas ====");
            System.out.println("===== 6: Visão Geral ====");
            System.out.println("===== 7: SAIR ====");
            System.out.print("Digite a opção: ");
            choose = leia.nextInt();
            leia.nextLine();
            System.out.println();

            if (choose == 1) {
                System.out.println("==========MÉDIA GERAL DA TURMA==========");
                System.out.printf("A média da turma é %.1f", metodo.media(soma, quant));
                System.out.println();
            } else if (choose == 2) {
                for (int i = 0; i < quant; i++) {
                    System.out.print("| Aluno: " + nome[i]);
                    System.out.printf(" | Situação: %s", metodo.situacao(nota[i]));
                    System.out.println();
                }
            } else if (choose == 3) {
                for (int i = 0; i < quant; i++) {
                    System.out.print("| Aluno: " + nome[i]);
                    System.out.print(metodo.situacaoNota(nota[i], maiorNota, menorNota));
                    System.out.println();
                }
                metodo.alunosMaiorNota(alunosMaiorNota);
                System.out.println();
            } else if (choose == 4) {
                for (int i = 0; i < quant; i++) {
                    System.out.print("| Aluno: " + nome[i]);
                    System.out.printf(" | Frequência: %.2f%%", metodo.frequencia(falta[i]));
                    System.out.println();
                }
            } else if (choose == 5){
                for (int i = 0; i < quant; i++) {
                    System.out.print("| Aluno: " + nome[i] + " | Nota: " + nota[i]);
                    System.out.println();
                }
            } else if (choose == 6){
                System.out.println("==========VISÃO GERAL==========");
                for (int i = 0; i < quant; i++) {
                    System.out.print("| Aluno: " + nome[i] + " | Nota: " + nota[i]);
                    System.out.printf(" | Situação: %s", metodo.situacao(nota[i]));
                    System.out.printf(" | Frequência: %.2f%%", metodo.frequencia(falta[i]));
                    System.out.print(metodo.situacaoNota(nota[i], maiorNota, menorNota));
                    System.out.println();
                }
                metodo.alunosMaiorNota(alunosMaiorNota);
                System.out.println();
                System.out.printf("A média da turma é %.1f", metodo.media(soma, quant));
                System.out.println();
            }
            if (choose == 7) {
                break;
            }
        }

    leia.close();
    }
}
