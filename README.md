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
Prices are stored in pence in the CSV, so they are divided by 100 to display in pounds.

Use Case 3 View full details of a top-up
After choosing a top-up, the program displays its full details: description,
price, entitlement type, duration, number of
entitlements, passenger type and number of people covered.
The TopUp class was extended to store all detail fields.

Use Case 4  Purchase a topup
After viewing a topup's details, the user can choose to buy it. A confirmed
purchase is recorded so it can later be saved to a file.
A Purchase class stores the title and price of a bought topup.
Confirmed purchases are added to a list of Purchase objects.
The list is the structure that Use Cases 6 and 7 will save to, and load from, a file.

#Use Case 5 Buy multiple tickets in one session
The purchasing steps are wrapped in a while loop so the customer can buy
several tickets in a single run, and is asked after each purchase whether
they want to continue.
The list of purchases is created once, before the loop, so it keeps every ticket bought instead of being reset each time.
After each purchase the user is asked "buy another?" anything other than "yes" ends the loop.
When the loop ends, all purchases made in the session are listed.

#Use Case 6 Save purchases to a file
When the program closes, all purchases from the session are written to
purchases.csv so they are not lost.
The file is opened in write mode using csv.writer.
Each Purchase is written as one line: title,price.
The whole write is wrapped in try/except so a file error does notcrash the program.

#Use Case 7 Load previous purchases at startup
When the program starts, it reads purchases.csv and rebuilds any previously
saved purchases so they are not lost between runs.
The file is read with csv.reader 
Each row is a title and price, used to rebuild a Purchase object.
A missing file is caught with except FileNotFoundError, so the first ever run does not crash it just starts with no history.
Works as a pair with UseCase6 load on start, save the whole list onexit, so purchases build up across sessions.

#Use Case 8 Admin login
The user chooses to continue as a customer or log in as an admin, with admin
access protected by a password.

A User base class holds a username. Customer and Admin both inherit from it (inheritance), and Admin adds a password and a CheckPassword method.
The usertype prompt loops until "customer" or "admin" is entered, somisspellings are rejected.
The admin password loops with no attempt limit; typing "exit" continuesas a customer so a non-admin is never trapped.
Choosing customer creates a Customer object and greets the user.
An isAdmin flag records admin access, which will unlock price changes inUse Case 9.


#Use Case 9 Admin changes a top-up price
A logged-in admin can change the price of a top up for the current session.
The block only runs if isAdmin is True, so customers skip it entirely.
This is where the login flag from Use Case 8 is used.
The admin picks a category, then a top-up, then enters a new price in pence. All three inputs are validated with try/except loops.
The new price is set directly on the TopUp object (topUpToChange.price).







