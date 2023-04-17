using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DGEMM_int
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int l_max = 50;
            int alpha;
            int beta;

            long[] time = new long[l_max];

            int m, k, n;

            int i, j;
            long t0, t1;


            try
            {

                StreamReader sr = File.OpenText("input.txt");

// reading alpha, beta, op(A), op(B), C from Input.txt

                alpha = Int32.Parse(sr.ReadLine());
                beta = Int32.Parse(sr.ReadLine());
                m = Int32.Parse(sr.ReadLine());
                k = Int32.Parse(sr.ReadLine());
                n = Int32.Parse(sr.ReadLine());

              

                int[,] Array_op_A = new int[m, k];
                int[,] Array_op_B = new int[k, n];
                int[,] Array_C = new int[m, n];
                int[,] Array_D = new int[m, n];

                for (i = 0; i < m; i++)
                    for (j = 0; j < k; j++)
                    {
                        Array_op_A[i, j] = Int32.Parse(sr.ReadLine());
                      //  Console.WriteLine(Array_op_A[i, j]);
                    }

                for (i = 0; i < k; i++)
                    for (j = 0; j < n; j++)
                    {
                        Array_op_B[i, j] = Int32.Parse(sr.ReadLine());
                      //  Console.WriteLine(Array_op_B[i, j]);
                    }

                for (i = 0; i < m; i++)
                    for (j = 0; j < n; j++)
                    {
                        Array_C[i, j] = Int32.Parse(sr.ReadLine());
                       // Console.WriteLine(Array_C[i, j]);
                    }

                sr.Close();

                for (int l = 0; l < l_max; l++)
                {                

                    DateTime date_time0 = DateTime.Now;
                    t0 = date_time0.Millisecond;

                   // t0 = GetNanoseconds();
                   // Console.WriteLine("t0="+t0);
                  

                    for (i = 0; i < m; i++)
                        for (j = 0; j < n; j++)
                        {
                            Array_D[i, j] = 0;
                            for (int i1 = 0; i1 < k; i1++)
                                Array_D[i, j] = Array_D[i, j] + Array_op_A[i, i1] * Array_op_B[i1, j];
                            Array_D[i, j] = alpha * Array_D[i, j] + beta * Array_C[i, j];
                            //   Array_C[i][j] = Array_D[i][j];
                        }
                 
                                  
                    DateTime date_time1 = DateTime.Now;
                    t1  = date_time1.Millisecond;

                    // t1 = GetNanoseconds();
                    //  Console.WriteLine("t1=" + t1);

                    time[l] = t1 - t0;
                    /**
                     // print matrix D
                     System.out.print("l=" + l + "  time=" + time[l] + "\n");
                    for (i = 0; i < m; i++) {  
                        for (j = 0; j < n; j++) {
                            System.out.print(" " + "(" + i + j + ") " + Array_D[i][j] + " "); 
                        }
                        System.out.println();
                    }
                     */
                }

            }
            catch (IOException ex)
            {
            }


         // sort array 'time'
            Array.Sort(time);


// write array 'time' to file 'time.txt'
            StreamWriter swTime = new StreamWriter("time.txt");

            String string1 = l_max.ToString();
            swTime.WriteLine(string1);
            for (int l = 0; l < l_max; l++)
            {
                String string2 = l.ToString();
                String string3 = time[l].ToString();
                swTime.WriteLine(string2 + "\n" + string3);
            }
            swTime.Close();


            Console.WriteLine();

            // calculation the average value
            double av = 0;
            for (int l = 0; l < l_max; l++)
            {
                av = av + (double)time[l];
                Console.WriteLine("l=" + l + "    " + "t=" + time[l] + " nanosec");
            }
            av = av / l_max;

// calculation the mean dispersion
            double s = 0;
            for (int l = 0; l < l_max; l++)
            {
                s = s + Math.Pow(av - (double)time[l], 2);
            }

            double Dev = Math.Sqrt(s / l_max);

// calculation the median value
            double med;
            if (l_max % 2 != 0)
            {
                int l1 = (l_max - 1) / 2;
                med = time[l1];
                //  System.out.println("l1=" + l1);
            }
            else
            {
                int l2 = l_max / 2 - 1;
                int l3 = l_max / 2;
                med = (double)(time[l2] + time[l3]) / 2d;
                //  System.out.println("l2=" + l2+"    l3=" + l3 );
            }

            Console.WriteLine("shortest time= " + time[0] + "\n" + "longest time= " + time[l_max - 1]);
            Console.WriteLine("average value= " + av);
            Console.WriteLine("median value= " + med);
            Console.WriteLine("mean deviation= " + Dev);
            Console.ReadLine();

        }

        public static long GetNanoseconds()
        {
            double timestamp = Stopwatch.GetTimestamp();
            double nanoseconds = 1_000_000_000.0 * timestamp / Stopwatch.Frequency;

            return (long)nanoseconds;
        }


    }
}






