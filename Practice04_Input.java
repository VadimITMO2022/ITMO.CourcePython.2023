

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class Practice04_Input {
    public static void main(String[] args) {

        int i, j;

// transa=0 матрица А не транспонирована; transa=1 матрица А транспонирована
// transb=0 матрица B не транспонирована; transb=1 матрица B транспонирована

        int transa = 1;
        int transb = 0;

// Размерность матрицы op(A)= m x k
// Размерность матрицы op(B)= k x n
// Размерность матрицы C= m x n

        int m = 10;
        int k = 8;
        int n = 6;

// матрицы op(A), op(B) и C
        int[][] Array_op_A = new int[m][k];
        int[][] Array_op_B = new int[k][n];
        int[][] Array_C = new int[m][n];

// Размерность матрицы A= s1 x s2
// Размерность матрицы B= t1 x t2
        int s1, s2; // размерность матрицы A
        int t1, t2; // размерность матрицы B

        // размерность матрицы A:  s1 x s2

        if (transa == 0) {
            // op(A)=A
            s1 = m;
            s2 = k;
        } else {
            // op(A)=A^Т
            s1 = k;
            s2 = m;
        }

        // размерность матрицы B:  t1 x t2

        if (transb == 0) {
            // op(B)=B
            t1 = k;
            t2 = n;
        } else {
            // op(B)=B^Т
            t1 = n;
            t2 = k;
        }

        System.out.print("размерность матрицы op(A): " + m + "x" + k + "\n");
        System.out.print("размерность матрицы op(B): " + k + "x" + n + "\n");
        System.out.print("размерность матрицы C: " + m + "x" + n + "\n");
        System.out.print("\n");
        System.out.print("размерность матрицы A: " + s1 + "x" + s2 + "\n");
        System.out.print("размерность матрицы B: " + t1 + "x" + t2 + "\n");
        System.out.print("\n");

// матрицы A и B
        int[][] Array_A = new int[s1][s2];
        int[][] Array_B = new int[t1][t2];

        Random rnd = new Random();

        // величины alpha и beta
        int alpha = rnd.nextInt(100);
        int beta = rnd.nextInt(100);
        System.out.print("параметер alpha: " + alpha+"\n");
        System.out.print("параметер beta: " + beta+"\n");
        System.out.println();

        //-----------------------------------------------------------

        // задание и печать элементов матрицы A

        System.out.print("Array A" + "\n");
        for (i = 0; i < s1; i++) {
            String str_A = " ";
            for (j = 0; j < s2; j++) {
                Array_A[i][j] = rnd.nextInt(100);
                str_A = str_A + "(" + i + j + ") " + Array_A[i][j] + "    ";
            }
            System.out.print(str_A + "\n");
        }
        System.out.print("\n");

        //----------------------------------------------------------------------

        // задание и печать элементов матрицы B
        System.out.print("Array B" + "\n");
        for (i = 0; i < t1; i++) {
            String str_B = " ";
            for (j = 0; j < t2; j++) {
                Array_B[i][j] = rnd.nextInt(100);
                str_B = str_B + "(" + i + j + ") " + Array_B[i][j] + "    ";
            }
            System.out.print(str_B + "\n");
        }
        System.out.print("\n");

        //----------------------------------------------------------------------

        // задание и печать элементов матрицы С
        System.out.print("Array С" + "\n");
        for (i = 0; i < m; i++) {
            String str_C = " ";
            for (j = 0; j < n; j++) {
                Array_C[i][j] = rnd.nextInt(100);
                str_C = str_C + "(" + i + j + ") " + Array_C[i][j] + "    ";
            }
            System.out.print(str_C + "\n");
        }
        System.out.print("\n");
//-----------------------------------------------------------
// матрица op(A)
        System.out.print("Array op(A)" + "\n");
        for (i = 0; i < m; i++) {
            String str_op_A = " ";
            for (j = 0; j < k; j++) {
                if (transa == 0)
                    Array_op_A[i][j] = Array_A[i][j];
                else
                    Array_op_A[i][j] = Array_A[j][i];
                str_op_A = str_op_A + "(" + i + j + ") " + Array_op_A[i][j] + "    ";
            }
            System.out.print(str_op_A + "\n");
        }
        System.out.print("\n");


        //-----------------------------------------------------------
// матрица op(B)
        System.out.print("Array op(B)" + "\n");
        for (i = 0; i < k; i++) {
            String str_op_B = " ";
            for (j = 0; j < n; j++) {
                if (transb == 0)
                    Array_op_B[i][j] = Array_B[i][j];
                else
                    Array_op_B[i][j] = Array_B[j][i];
                str_op_B = str_op_B + "(" + i + j + ") " + Array_op_B[i][j] + "    ";
            }
            System.out.print(str_op_B + "\n");
        }
        System.out.print("\n");

// ----------------------------------------------------------------------------------------------

        // записываем параметры alpha,beta
        // размерности массивов m,n,k
        // и сами массивы op(A),op(B) и C
        // в файл "input.txt"

        try {
            FileWriter writer = new FileWriter("input.txt");

            String str1 = Integer.toString(alpha) + "\n";
            String str2 = Integer.toString(beta) + "\n";
            writer.write(str1);
            writer.write(str2);

            String str3 = Integer.toString(m) + "\n";
            String str4 = Integer.toString(k) + "\n";
            String str5 = Integer.toString(n) + "\n";
            writer.write(str3);
            writer.write(str4);
            writer.write(str5);

            for (i = 0; i < m; i++)
                for (j = 0; j < k; j++) {
                    String str6 = Integer.toString(Array_op_A[i][j]) + "\n";
                    writer.write(str6);
                }

            for (i = 0; i < k; i++)
                for (j = 0; j < n; j++) {
                    String str7 = Integer.toString(Array_op_B[i][j]) + "\n";
                    writer.write(str7);
                }

            for (i = 0; i < m; i++)
                for (j = 0; j < n; j++) {
                    String str8 = Integer.toString(Array_C[i][j]) + "\n";
                    writer.write(str8);
                }

            writer.close();
        } catch (IOException ex) {
        }

//-----------------------------------------------------------

    }

}



