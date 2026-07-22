# Bus-Ticket
Creating a bus ticket
Use Case 1 Set up a category class
i ran into some problems usuing github i think ive resolved it

validating usecase1:
The category menu lets the user pick a ticket category by typing a number.
To stop the program crashing on bad input
Typing letters instead of a number is caught and re-asks.
A number that is not on the menu is caught and re-asks.
Negative numbers are rejected too, so they cannot select the wrong
category by counting from the end of the list.

Use Case 2 – List top-up types in a category
Once the user has chosen a category, the program shows every top-up type
available in that category, with its price.
A TopUp class stores each top-up's title, price and menu code.
Prices are stored in pence in the CSV, so they are divided by 100
to display in pounds.