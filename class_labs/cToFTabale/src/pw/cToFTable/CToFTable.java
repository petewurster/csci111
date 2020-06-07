/*
pw_lab04_CtoFtable.py;
last edit: 2020-06-07, by pWurster;
Prints table of Celcius to Fahrenheit from Celcius 0 to 40;
*/

package pw.cToFTable; //namespace

public class CToFTable {
    public static void main(String[] args) {
        //no vars to declare -- only using temp vars in scope of 'for' loop

        //loop 40 times
        for (double celciusDegrees = 0.0; celciusDegrees < 41.0; celciusDegrees++) {
            //print ititial table headers and reprint every dozen lines for readability
            if (celciusDegrees % 12.0 == 0.0) {
                System.out.println("Celcius  Fahrenheit");
            }

            //calculate Fahrenheit from Celcius using the usual formula
            double fahrenheitDegrees = 9.0 / 5.0 * celciusDegrees + 32.0;

            //print each line of table, showing converted value to nearest tenth
            System.out.printf("%4.0f%12.1f%n", celciusDegrees, fahrenheitDegrees);
        }
    }
}