using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Input_int
{
    internal class Program
    {
        static void Main(string[] args)
        {
           

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
                int[,] Array_op_A = new int[m, k];
                int[,] Array_op_B = new int[k, n];
                int[,] Array_C = new int[m, n];

                // Размерность матрицы A= s1 x s2
                // Размерность матрицы B= t1 x t2
                int s1, s2; // размерность матрицы A
                int t1, t2; // размерность матрицы B

                // размерность матрицы A:  s1 x s2

                if (transa == 0)
                {
                    // op(A)=A
                    s1 = m;
                    s2 = k;
                }
                else
                {
                    // op(A)=A^Т
                    s1 = k;
                    s2 = m;
                }

                // размерность матрицы B:  t1 x t2

                if (transb == 0)
                {
                    // op(B)=B
                    t1 = k;
                    t2 = n;
                }
                else
                {
                    // op(B)=B^Т
                    t1 = n;
                    t2 = k;
                }

                Console.WriteLine("размерность матрицы op(A): " + m + "x" + k);
                Console.WriteLine("размерность матрицы op(B): " + k + "x" + n);
                Console.WriteLine("размерность матрицы C: " + m + "x" + n);
                Console.WriteLine("\n");
                Console.WriteLine("размерность матрицы A: " + s1 + "x" + s2);
                Console.WriteLine("размерность матрицы B: " + t1 + "x" + t2);
                Console.WriteLine("\n");

                // матрицы A и B
                int[,] Array_A = new int[s1, s2];
                int[,] Array_B = new int[t1, t2];

                Random rnd = new Random();

                // величины alpha и beta
                int alpha = rnd.Next(0, 100);
                int beta = rnd.Next(0, 100);
                Console.WriteLine("параметер alpha: " + alpha);
                Console.WriteLine("параметер beta: " + beta);
                Console.WriteLine();

                //-----------------------------------------------------------

                // задание и печать элементов матрицы A

                Console.WriteLine("Array A");
                for (i = 0; i < s1; i++)
                {
                    String str_A = " ";
                    for (j = 0; j < s2; j++)
                    {
                        Array_A[i, j] = rnd.Next(0, 100);
                        str_A = str_A + "(" + i + j + ") " + Array_A[i, j] + "    ";
                    }
                    Console.WriteLine(str_A);
                }
                Console.WriteLine();

                //----------------------------------------------------------------------

                // задание и печать элементов матрицы B
                Console.WriteLine("Array B");
                for (i = 0; i < t1; i++)
                {
                    String str_B = " ";
                    for (j = 0; j < t2; j++)
                    {
                        Array_B[i, j] = rnd.Next(0, 100);
                        str_B = str_B + "(" + i + j + ") " + Array_B[i, j] + "    ";
                    }
                    Console.WriteLine(str_B);
                }
                Console.WriteLine();

                //----------------------------------------------------------------------

                // задание и печать элементов матрицы С
                Console.WriteLine("Array С");
                for (i = 0; i < m; i++)
                {
                    String str_C = " ";
                    for (j = 0; j < n; j++)
                    {
                        Array_C[i, j] = rnd.Next(0, 100);
                        str_C = str_C + "(" + i + j + ") " + Array_C[i, j] + "    ";
                    }
                    Console.WriteLine(str_C);
                }
                Console.WriteLine();
                //-----------------------------------------------------------
                // матрица op(A)
                Console.WriteLine("Array op(A)");
                for (i = 0; i < m; i++)
                {
                    String str_op_A = " ";
                    for (j = 0; j < k; j++)
                    {
                        if (transa == 0)
                            Array_op_A[i, j] = Array_A[i, j];
                        else
                            Array_op_A[i, j] = Array_A[j, i];
                        str_op_A = str_op_A + "(" + i + j + ") " + Array_op_A[i, j] + "    ";
                    }
                    Console.WriteLine(str_op_A);
                }
                Console.WriteLine();


                //-----------------------------------------------------------
                // матрица op(B)
                Console.WriteLine("Array op(B)");
                for (i = 0; i < k; i++)
                {
                    String str_op_B = " ";
                    for (j = 0; j < n; j++)
                    {
                        if (transb == 0)
                            Array_op_B[i, j] = Array_B[i, j];
                        else
                            Array_op_B[i, j] = Array_B[j, i];
                        str_op_B = str_op_B + "(" + i + j + ") " + Array_op_B[i, j] + "    ";
                    }
                    Console.WriteLine(str_op_B);
                }
                Console.WriteLine();

                // ----------------------------------------------------------------------------------------------

                // записываем параметры alpha,beta
                // размерности массивов m,n,k
                // и сами массивы op(A),op(B) и C
                // в файл "input.txt"

                try
                {
                    //  FileWriter writer = new FileWriter("input.txt");

                    StreamWriter sw = new StreamWriter("input.txt");

                    String str1 = alpha.ToString();
                    String str2 = beta.ToString();
                    sw.WriteLine(str1);
                    sw.WriteLine(str2);

                    String str3 = m.ToString();
                    String str4 = k.ToString();
                    String str5 = n.ToString();
                    sw.WriteLine(str3);
                    sw.WriteLine(str4);
                    sw.WriteLine(str5);

                    for (i = 0; i < m; i++)
                        for (j = 0; j < k; j++)
                        {
                            String str6 = Array_op_A[i, j].ToString();
                            sw.WriteLine(str6);
                        }

                    for (i = 0; i < k; i++)
                        for (j = 0; j < n; j++)
                        {
                            String str7 = Array_op_B[i, j].ToString();
                            sw.WriteLine(str7);
                        }

                    for (i = 0; i < m; i++)
                        for (j = 0; j < n; j++)
                        {
                            String str8 = Array_C[i, j].ToString();
                            sw.WriteLine(str8);
                        }

                    sw.Close();
                }
                catch (IOException ex)
                {
                }

                //-----------------------------------------------------------

                Console.ReadLine();

            }

        }


    }


