/*
JavaArrays.java;
last edit: 2020-06-16, by pWurster;
gets 5 test scores from the user and then calculates the high, low, and average
to demonstrate array usage
*/

package pw.javaArrays;
import java.util.Scanner;

public class JavaArrays {
    //declare class constant
    public static int LENGTH = 5;   //set array lengths for this class

    public static void main(String[] args) {
        //init vars
        double[] scores = new double[JavaArrays.LENGTH]; //array to hold scores
        double average;     //calculated later
        double highScore;   //will be set after data is collected
        double lowScore;    //will be set after data is collected

        //instantiate a Scanner
        Scanner rawInput = new Scanner(System.in);

        //loop to collect data from user
        for (int x = 0; x < scores.length; x++) {
            System.out.printf("Enter a score: ");
            //cast input to doubles and store in array by index
            scores[x] = Double.parseDouble(rawInput.nextLine());
        }

        //kill the scanner
        rawInput.close();

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

        //display results
        System.out.printf("The highest score is %.2f.%nThe lowest score is %.2f.%n", highScore, lowScore);
        System.out.printf("The average of these scores is %.2f.", average);
        System.out.println();






    }
}
