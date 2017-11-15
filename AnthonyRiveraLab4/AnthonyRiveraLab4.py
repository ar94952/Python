#Anthony Rivera
#Python CIS 117 OL
#Lab4
#09/18/2017

def main():  

   fp = open("Lab4.txt"); #I had a long day and I tried really hard to get it to print.
   inventory = [];
  

   for rec in fp:
       inventory.append(((rec.split(','))[0],((rec.split(','))[1]).strip('\n')));
  

   print("\n Welcome to Shopping Cart! \n Today you can buy: \n\n");
  

   for i in range(0,len(inventory)):
       print(" %8d %-15s $%4.2f" % (i, inventory[i][0], float(inventory[i][1])));
  
   selectedItems = [];
   choice = "y";
  

   while choice == 'y':
       sno = int(input("\n\n Enter the serial number of the item to place in your cart: "));
       qty = int(input("\n Enter the quantity for the this item: "));
       
       selectedItems.append((sno,qty));
       choice = input("\n Do you want to select another item (y/n)? ");
  
   print("\n\n Here is the receipt for your shopping cart: \n\n ----------------------------------- \n ");
  
   
   total = 0;
   for item in selectedItems:
       
       print(" %-15s $%-5.2f %d $%-10.2f " % (inventory[item[0]][0], float(inventory[item[0]][1]), item[1], float(inventory[item[0]][1]) * item[1]));
       total = total + float(inventory[item[0]][1]) * item[1];
   print("\n ---------------------------------- \n ");
   print(" \t Total: \t $" + str(total));
   print("\n ---------------------------------- \n\n\n ");
      
main();