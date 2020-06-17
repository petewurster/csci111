/*
JavaArraysWithFilesUsingMethods.java;
last edit: 2020-06-17, by pWurster;
gets 5 test scores from a source file and then calculates the high, low, and average
and outputs these results to a new file using class methods
*/

package pw.javaArraysWithFilesUsingMethods;
import java.util.Scanner;

public class JavaArraysWithFilesUsingMethods {
    //declare class constants
    public static int LENGTH = 5;   //array lengths for this class needs to be <= # of lines in source file
    public static String INFILE = "scores.txt";             //data source filepath
    public static String OUTFILE = "results_summary.txt";   //output filepath


    /*
    main function to control program flow
     */
    public static void main(String[] args) throws Exception {
        //define scores via data read from file
        double[] scores = readScoresFromFile(new double[LENGTH]);

        //define results via returned values from calculation functions
        double[] results = {findHighScore(scores), findLowScore(scores), calculateAverage(scores)};

        //write results to file
        writeResultsToFile(results);
    }



    /*
    takes an empty array and returns that array after populating it with data
    read from the filepath at INFILE
    */
    public static double[] readScoresFromFile(double scores[]) throws Exception {
        java.io.File inFile = new java.io.File(INFILE); //instantiate file handle
        Scanner dataFromFile = new Scanner(inFile);     //instantiate Scanner

        //inform user of task
        System.out.printf("reading data from '%s'", INFILE);

        //loop to collect data from user
        for (int x = 0; x < scores.length; x++) {
            //cast input to doubles and store in array by index
            scores[x] = Double.parseDouble(dataFromFile.nextLine());

            System.out.print(".");  //update task progress
        }

        System.out.println();
        dataFromFile.close();   //done with Scanner
        return scores;
    }



    /*
    loops thru array to find the high score and returns it
    */
    public static double findHighScore(double scores[]) {
        double highScore = scores[0];
        for (double score: scores) {
            if (score > highScore) highScore = score;
        }
        return highScore;
    }



    /*
    loops thru array to find the low score and returns it
     */
    public static double findLowScore(double scores[]) {
        double lowScore = scores[0];
        for (double score: scores) {
            if (score < lowScore) lowScore = score;
        }
        return lowScore;
    }



    /*
    reads an array, calculates and returns the average of its values
    */
    public static double calculateAverage(double scores[]) {
        double acc = 0.0;
        for (double score: scores) {
            acc += score;
        }
        return acc / scores.length;
    }



    /*
    expects an array of doubles that represent the high/low/average scores
    */
    public static void writeResultsToFile(double results[]) throws Exception {
        java.io.File outFile = new java.io.File(OUTFILE);   //instantiate file handle
        java.io.PrintWriter outputStream = new java.io.PrintWriter(outFile);    //instantiate PrintWriter

        //output results to file
        outputStream.printf("The highest score is %.2f.%nThe lowest score is %.2f.%n", results[0], results[1]);
        outputStream.printf("The average of these scores is %.2f.", results[2]);
        outputStream.println();

        //done with PrintWriter
        outputStream.close();

        //inform user of results
        System.out.printf("results written to '%s'", OUTFILE);
        System.out.println();
    }



}//end of class