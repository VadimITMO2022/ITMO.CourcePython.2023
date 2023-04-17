
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;


public class Practice04_Dgemm {

    public static void main(String[] args) throws IOException {

        int l_max = 50;
        int alpha;
        int beta;

        long[] time = new long[l_max];

        int m, k, n;

        int i, j;
        long t0, t1, delta;


        try {
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));

            alpha = Integer.parseInt(reader.readLine());
            beta = Integer.parseInt(reader.readLine());
            m = Integer.parseInt(reader.readLine());
            k = Integer.parseInt(reader.readLine());
            n = Integer.parseInt(reader.readLine());

            int[][] Array_op_A = new int[m][k];
            int[][] Array_op_B = new int[k][n];
            int[][] Array_C = new int[m][n];
            int[][] Array_D = new int[m][n];

            for (i = 0; i < m; i++)
                for (j = 0; j < k; j++) {
                    Array_op_A[i][j] = Integer.parseInt(reader.readLine());
                }

            for (i = 0; i < k; i++)
                for (j = 0; j < n; j++) {
                    Array_op_B[i][j] = Integer.parseInt(reader.readLine());
                }

            for (i = 0; i < m; i++)
                for (j = 0; j < n; j++) {
                    Array_C[i][j] = Integer.parseInt(reader.readLine());
                }

            reader.close();

            for (int l = 0; l < l_max; l++) {
                 t0 = System.nanoTime();
             //   t0 = System.currentTimeMillis();

                // computation matrix D
                for (i = 0; i < m; i++)
                    for (j = 0; j < n; j++) {
                        Array_D[i][j] = 0;
                        for (int i1 = 0; i1 < k; i1++)
                            Array_D[i][j] = Array_D[i][j] + Array_op_A[i][i1] * Array_op_B[i1][j];
                        Array_D[i][j] = alpha * Array_D[i][j] + beta * Array_C[i][j];
                    }
               t1 = System.nanoTime();
               // t1 = System.currentTimeMillis();
              time[l] = t1 - t0;


                /**
                 // print array D
                 System.out.print("l=" + l + "  time=" + time[l] + "\n");
                for (i = 0; i < m; i++) {
                    for (j = 0; j < n; j++) {
                        System.out.print(" " + "(" + i + j + ") " + Array_D[i][j] + " ");
                    }
                    System.out.println();
                }
                 */
            }

        } catch (IOException ex) {
        }



// sort array 'time'
        Arrays.sort(time);

        try {
            // write array 'time' to file 'time.txt'
            FileWriter writer_time = new FileWriter("time.txt");
            writer_time.write(String.valueOf(l_max)+ "\n");
            int ll = 0;
            while (ll < l_max) {
                String str = String.valueOf(ll) + "\n" + String.valueOf(time[ll]) + "\n";
                writer_time.write(str);
                ll = ll + 1;
            }
            writer_time.close();
        } catch (IOException ex) {
        }

        System.out.println();
        // computation average value
        float av = 0;
        for (int l = 0; l < l_max; l++) {
            av = av + (float) time[l];
            System.out.println("l=" + l + "    " + "t=" + time[l] + " nanosec");
        }
        av=av/(float)l_max;
// computation mean dispersion
        float s = 0;
        for (int l = 0; l < l_max; l++) {
            s = (float) (s + Math.pow(av - (float) time[l], 2));
        }
        float Dev = (float)Math.sqrt(s / l_max);

        // computation median value
        float med;
        if (l_max % 2 != 0) {
            int l1 = (l_max - 1) / 2 ;
            med = time[l1];
          //  System.out.println("l1=" + l1);
        } else {
            int l2 = l_max / 2-1;
            int l3 = l_max / 2;
            med = (float) ((time[l2] + time[l3]) / 2.);
          //  System.out.println("l2=" + l2+"    l3=" + l3 );
        }

        System.out.println("shortest time= " + time[0] + "\n" + "longest time= " + time[l_max - 1]);
        System.out.println("average value= " + av);
        System.out.println("median value= " + med);
        System.out.println("mean deviation= " + Dev);

    }

}

