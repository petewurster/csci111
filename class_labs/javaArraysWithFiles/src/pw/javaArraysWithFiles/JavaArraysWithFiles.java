/*
JavaArraysWithFiles.java;
last edit: 2020-06-16, by pWurster;
gets 5 test scores from the a source file and then calculates the high, low, and average
and outputs these results to a new file
*/

package pw.javaArraysWithFiles;
import java.util.Scanner;

public class JavaArraysWithFiles {
    //declare class constants
    public static int LENGTH = 5;   //array lengths for this class needs to be <= # of lines in source file
    public static String INFILE = "scores.txt";             //data source file location
    public static String OUTFILE = "results_summary.txt";   //output file location

    public static void main(String[] args) throws Exception {
        //init vars
        double[] scores = new double[LENGTH]; //array to hold scores
        double average;     //calculated later
        double highScore;   //will be set after data is collected
        double lowScore;    //will be set after data is collected

        //instantiate file handles
        java.io.File inFile = new java.io.File(INFILE);
        java.io.File outFile = new java.io.File(OUTFILE);

        //instantiate a Scanner
        Scanner dataFromFile = new Scanner(inFile);

        //instantiate a PrintWriter
        java.io.PrintWriter outputStream = new java.io.PrintWriter(outFile);

        //loop to collect data from user
        System.out.print("reading file data");
        for (int x = 0; x < scores.length; x++) {
            //cast input to doubles and store in array by index
            scores[x] = Double.parseDouble(dataFromFile.nextLine());
            System.out.print(".");
        }

        //kill the scanner
        dataFromFile.close();

        //use first value of the array to define high/low scores
        highScore = scores[0];
        lowScore = scores[0];

        double total = 0.0; //temp var
        for (double score: scores) {
            //set high and/or low scores as appropriate
            if (score > highScore ) highScore = score;
            if (score < lowScore ) lowScore = score;

            //update total
            total += score;
        }

        //calculate average
        average = total / scores.length;

        //output results to file
        outputStream.printf("The highest score is %.2f.%nThe lowest score is %.2f.%n", highScore, lowScore);
        outputStream.printf("The average of these scores is %.2f.", average);
        outputStream.println();

        //kill the PrintWriter
        outputStream.close();

        //inform user of results
        System.out.printf("%nresults written to '%s'", OUTFILE);
        System.out.println();





    }
}