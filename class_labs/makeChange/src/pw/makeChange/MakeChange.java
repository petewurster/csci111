/*
MakeChange.java;
last edit: 2020-06-05, by pWurster;
takes integer value from user (in cents) and converts to quantities of
coin representations attempting to use the same design from my Python version
*/

package pw.makeChange; //namespace
import java.util.Scanner;

public class MakeChange {

    public static void main(String[] args) {
        //init variables
        short total; //number of cents, set by user input
        //(using parallel arrays because I don't remember how to use a k:v structure in Java)
        short[] coins = {0, 0, 0, 0}; //holds the count of each coin
        String[] denominations = {"Quarters", "Dimes", "Nickels", "Pennies"}; //names of each coin

        //cast user input to short
        System.out.print("Enter a number of cents: ");
        Scanner rawInput = new Scanner(System.in);
        total = rawInput.nextShort();
        rawInput.close();

        //process data
        coins[0] = (short) (total / 25);
        coins[1] = (short) (total % 25 / 10);
        coins[2] = (short) (total % 25 % 10 / 5);
        coins[3] = (short) (total % 25 % 10 % 5);

        //display results
        System.out.printf("\n%d cents converts to:\n", total);
        for(short coin = 0; coin < coins.length; coin++) {
            System.out.printf("\t%s: %d%n", denominations[coin], coins[coin]);
        }
    }
}
