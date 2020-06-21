/*
Item.java;
last edit: 2020-06-21, by pWurster;
defines an Item class intended for use inside a Cart
(Cart class not included as per assignment instructions, but some Cart behaviors are implemented as static methods of Main)
*/

package pw.itemDemo;

public class Item {
    //init member properties
    private String itemName;
    private String productId;
    private double price = 0.0;
    private boolean taxExempt = false; //default provided for shorthand instantiation


    Item() {}     //default instantiation


    //standard verbose instantiation
    Item (String itemName, String productId, double price, boolean taxExempt) {
        this.itemName = itemName;
        this.productId = productId;
        this.taxExempt = taxExempt;
        setPrice(price);    //uses internal method to enforce data integrity

    }


    //shorthand instantiation: uses default value for taxExempt
    Item(String itemName, String productId, double price) {
        this.itemName = itemName;
        this.productId = productId;
        setPrice(price);  //uses internal method to enforce data integrity
    }



    /*
    over-ride default toString()
    */
    public String toString() {
        return "itemName: " + this.getItemName() +
                ", productId: " + this.getProductId() +
                ", price: " + this.getPrice() +
                (this.isTaxExempt() == true ? " (taxExempt)" : "");
    }



    /*//////////////////////////////////////////
    necessary getters due to all member properties being private;
    method names serve as their own descriptions
    */
    public String getItemName() {
        return this.itemName;
    }

    public String getProductId() {
        return this.productId;
    }

    public double getPrice() {
        return this.price;
    }

    public boolean isTaxExempt() {
        return this.taxExempt;
    }




    /*///////////////////////////////////////////////////
    setters provided for all member properties for use in cases of default instantiation;
    method names serve as their own descriptions (mostly)
    */
    public void setItemName(String itemName) {
    	this.itemName = itemName;
    }

    public void setProductId(String productId) {
    	this.productId = productId;
    }

    public void toggleTaxes() {
        this.taxExempt = !this.taxExempt;
    }

    public void setPrice(double newPrice) {
        /*
        poorly created objects may result in an Item being free, but this will protect from said
        Items lowering the total cost of Items inside the cart
        */
        if (newPrice < 0.0) {
            this.price = 0.0;
        }else{
            this.price = newPrice;
        }
    }


}//end Class
