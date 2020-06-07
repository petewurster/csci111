/*
pw_lab03_quadrant_distance.py;
last edit: 2020-06-07, by pWurster;
Gets x,y coords from the user, displays Cartesian Quadrant and distance
from the origin in unspecified units to 3 points of precision
*/
package pw.quadrantDistance;
import java.util.Scanner;

public class QuadrantDistance {
    public static void main(String[] args) {
        int PRECISION = 3;//arbitrarily set to 3 for cleaner output
        double distance = 0.0; //units away from origin
        double[] point = {0.0, 0.0}; //point at (x, y)
        String quadrant = "I"; //Cartesian quadrant I-IV (default is I)

        //instantiate a Scanner
        Scanner rawInput = new Scanner(System.in);

        //prompt user for coords
        System.out.print("Enter point values for (x, y)\nseparated by a COMMA: ");

        //parse input string into point as an array
        String[] line = rawInput.nextLine().split(",", 2);
        rawInput.close();//kill the Scanner
        point[0] = Double.parseDouble(line[0]);
        point[1] = Double.parseDouble(line[1]);

        //calculate hypotenuse to determine distance
        distance = Math.hypot(Math.abs(point[0]), Math.abs(point[1]));

        //determine quadrant
        if (point[0] >= 0 && point[1] >= 0) {
            //pass
        } else if (point[0] < 0 && point[1] >= 0) {
            quadrant = "II";
        } else if (point[0] < 0 && point[1] < 0) {
            quadrant = "III";
        } else {
            quadrant = "IV";
        }

        //display results
        System.out.printf("\nPoint (" + point[0] + ", " + point[1] + ") lies in Quadrant %s of the Cartesian\n", quadrant);
        System.out.printf("plane and is %." + PRECISION + "f units away from the Origin (0, 0).", distance);
        System.out.println();
    }
}
