/*
Main.java;
last edit: 2020-06-21, by pWurster;
used with Item.java to demonstrate OOP basics
*/

package pw.itemDemo;

public class Main {
    //declare tax rate constant
    final public static double TAXRATE = .08;

    /*
    main control function
     */
    public static void main(String[] args) {

        //create an array filled with Item objects
        Item[] cart = {
                //create default instance
                new Item(),
                //insert a non-tax exempt item
                new Item("shovel", "22p31", 14.99, false),
                //demonstrates polymorphism by using default member value if taxExempt status is not provided
                new Item("cordless drill", "a1a1a", 140.49),
                //insert some tax exempt items
                new Item("frozen dinner", "f7910", 4.50, true),
                //demonstrates polymorphism by using default member value if taxExempt status is not provided
                new Item("hawaiian shirt", "st555", 20.00)
        };

        //display info to user
        provideSummary(cart);


        //set properties for default Item instance
        cart[0].setItemName("apple");
        cart[0].setProductId("12345");
        cart[0].setPrice(1.25);
        cart[0].toggleTaxes();


        //alter some other items in the array (ie apply coupons)
        cart[1].setPrice(7.0);  //modify shovel
        cart[4].setPrice(10.0); //modify shirt
        cart[4].toggleTaxes();  //apply tax exemption for clothes

        System.out.printf("%nCOUPONS APPLIED!%n %s: %s%n %s: %s%n",
                cart[1].getProductId(), cart[1].getItemName(), cart[4].getProductId(), cart[4].getItemName());


        //re-display info to user to show that changes were made
        provideSummary(cart);

    }





    /*
    summarizes the contents of the array cart
    */
    public static void provideSummary(Item[] cart) {
         //set accumulators
        double total = 0.0;
        double noTax = 0.0;

        System.out.printf("%nThere are %d items in your cart:%n", cart.length);

        //loop over array to sum taxable/nontaxable costs
        for (Item obj : cart) {
            //demonstrates usage of the toString method
            System.out.println(obj.toString());
            if (obj.isTaxExempt() == true) {
                noTax += obj.getPrice();
            }else{
                total += obj.getPrice();
            }
        }



        //display cart tallies to user
        showOutput(total, noTax);
    }




    /*
    outputs calculated cart info
     */
    public static void showOutput(double total, double noTax) {
        System.out.println();
        System.out.printf("%17s %10.2f%n","Taxable subtotal:", total);
        System.out.printf("%17s %10.2f%n", (TAXRATE * 100) + "% sales tax:", total * TAXRATE);
        System.out.printf("%17s %10.2f%n","Untaxed subtotal:", noTax);
        System.out.printf("%17s %10.2f", "Total:", total + (total * TAXRATE) + noTax);
        System.out.println();
    }

}   //end of class
