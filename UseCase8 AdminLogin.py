import csv
class Category:
    def __init__(self,category, code):
        self.category= category
        self.code = code
    def GetCategory (self):
        return self.category
    def GetCode(self):
        return self.code
#The TopUp class
class TopUp:
    def __init__(self, title, price, code, description, entType, entUnit, entValue, entQuantity, passengerName, passengerQuantity):
        self.title = title# topup name
        self.price = price #price in pence 
        self.code = code #number
        self.description = description  # topup description
        self.entType = entType    # fixed date or flexible
        self.entUnit = entUnit   # minutes/days/annual
        self.entValue = entValue   # how many of that unit
        self.entQuantity = entQuantity  # number of entitlements
        self.passengerName = passengerName  # Student, Adult
        self.passengerQuantity = passengerQuantity  # how many people covered
    def GetTitle(self):
        return self.title
    def GetPrice(self):
        return self.price
    def GetCode(self):
        return self.code
    def GetDescription(self):
        return self.description
    def GetEntType(self):
        return self.entType
    def GetEntUnit(self):
        return self.entUnit
    def GetEntValue(self):
        return self.entValue
    def GetEntQuantity(self):
        return self.entQuantity
    def GetPassengerName(self):
        return self.passengerName
    def GetPassengerQuantity(self):
        return self.passengerQuantity
#Class to describe one purchase a customer makes
class Purchase:
    def __init__(self, topupTitle, price):
        self.topupTitle = topupTitle   # what they bought
        self.price = price             # what it cost in pence
    def GetTopUpTitle(self):
        return self.topupTitle
    def GetPrice(self):
        return self.price


#Part of UseCase8 Admin Login
#Base class for anyone who uses the system
class User:
    def __init__(self, username):
        self.username = username
    def GetUsername(self):
        return self.username

#A Customer is a User who buys tickets
class Customer(User):
    def __init__(self, username):
        #call the User __init__ so username still gets set
        super().__init__(username)

# An Admin is a User who can change prices
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username)   # reuse User's setup
        self.password = password
    def CheckPassword(self, attempt):
        # returns True only if the entered password matches
        return attempt == self.password


listOfPurchases =[] #store's purchase
listOfCatClasses =[]
listOfCategories = []
listOfCodes =[]

#UseCase7 load any previously saved purchases at startup
try:
    # open the saved file in read mode ('r')
    with open('purchases.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            # each row is a list like (Adult Single,300)
            if len(row) == 2:                     #skip any blank/broken lines
                oldPurchase = Purchase(row[0], row[1])   # rebuild the Purchase object
                listOfPurchases.append(oldPurchase)
    print("Loaded", len(listOfPurchases), "previous purchase(s).")
except FileNotFoundError:
    # no file yet that's fine (it just means no purchases have been saved before)
    print("No previous purchases found. Starting fresh.")

#USE CASE 8: choose customer or admin, with admin login
admin = Admin("start", "open")
isAdmin = False
userType = input("Are you a customer or admin? (customer/admin): ")
if userType == "admin":
    # keep asking for the password until it's correct
    while isAdmin == False:
        attempt = input("Enter admin password: ")
        if admin.CheckPassword(attempt):
            isAdmin = True
            print("Admin login successful.")
        else:
            print("Wrong password. Try again.")


#Reads csv file
with open('mobile_products.csv', mode = 'r') as file:
    csvFile = csv.DictReader(file)
    code = 0
    for lines in csvFile:
        category= lines ['category_title']
        if category not in listOfCategories:
            listOfCategories.append(category)
            listOfCodes.append(code)
            cat1 = Category (category,code) 
            listOfCatClasses.append(cat1)
            code += 1

shopping = True
while shopping == True:
    print("Please choose a category of tickets")
    for cat in listOfCatClasses:
        print("For",cat.GetCategory(),"enter",cat.GetCode())
    # Keep asking until the user gives a valid choice
    validChoice = False
    while validChoice == False:
        try:
            choice = int(input("Enter your choice: "))   # fails here if it's not a number
            if choice < 0:
                raise IndexError  # treat negatives as invalid too
            chosen = listOfCatClasses[choice]   # fails here if the number is off the menu
            validChoice = True 
        except ValueError:
            print("Please enter a number, not text.")
        except IndexError:
            print("That number is not on the menu. Try again.")

    print("You chose", listOfCatClasses[choice].GetCategory())

    chosenCategory = listOfCatClasses[choice].GetCategory()   # name of the category picked

    listOfTopUpClasses = []   # will hold TopUp objects for the chosen category
    listOfTopUpTitles = []    # tracks titles already added, to skip duplicates

    with open('mobile_products.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        topUpCode = 0
        for lines in csvFile:
            # only rows belonging to the category the user chose
            if lines['category_title'] == chosenCategory:
                title = lines['topup_title']
                # some top-ups repeat across rows, so skip duplicates
                if title not in listOfTopUpTitles:
                    listOfTopUpTitles.append(title)
                    price = lines['topup_price_in_pence'] 
                    topup1 = TopUp(title, price, topUpCode,
                        lines['topup_description'],
                        lines['topup_entitlement_type'],
                        lines['topup_entitlement_unit'],
                        lines['topup_entitlement_value'],
                        lines['topup_entitlement_quantity'],
                        lines['topup_passenger_class_name'],
                        lines['topup_passenger_class_quantity'])# make the object
                    listOfTopUpClasses.append(topup1)
                    topUpCode += 1

    print() #adds space (for easier usability for the customer)
    print("Top-up types in", chosenCategory)
    for topup in listOfTopUpClasses:
        pounds = int(topup.GetPrice()) / 100  # price is in pence, /100 for pounds
        print("For", topup.GetTitle(), "(£" + str(pounds) + ") enter", topup.GetCode())

    # USE CASE 3: show full details of a chosen top-up
    validTopUp = False
    while validTopUp == False:
        try:
            topupChoice = int(input("Enter the number of a top-up to see details: "))
            if topupChoice < 0: # to stop input errors
                raise IndexError
            chosenTopUp = listOfTopUpClasses[topupChoice]
            validTopUp = True
        except ValueError:
            print("Please enter a number, not text.")
        except IndexError:
            print("That number is not on the menu. Try again.")

    print()# space
    print("Details for", chosenTopUp.GetTitle())
    print("Description:", chosenTopUp.GetDescription())
    print("Price: £" + str(int(chosenTopUp.GetPrice()) / 100))
    print("Entitlement type:", chosenTopUp.GetEntType())

    if chosenTopUp.GetEntUnit() != "":
        print("Duration:", chosenTopUp.GetEntValue(), chosenTopUp.GetEntUnit())
    else:
        print("Duration: fixed date ticket")

    if chosenTopUp.GetEntQuantity() != "":
        print("Number of entitlements:", chosenTopUp.GetEntQuantity())

    print("Passenger type:", chosenTopUp.GetPassengerName())
    print("Number of people covered:", chosenTopUp.GetPassengerQuantity())

    #USE CASE 4: purchase the chosen topup
    confirm = input("Do you want to buy this topup? (yes/no): ")
    if confirm == "yes":
        # make a Purchase object from the top-up chosen in Use Case 3
        newPurchase = Purchase(chosenTopUp.GetTitle(), chosenTopUp.GetPrice())
        listOfPurchases.append(newPurchase)
        print("Purchase added:", newPurchase.GetTopUpTitle())
    else:
        print("No purchase made.")

    # show what's in the basket so far
    print()
    print("Your purchases so far:")
    for p in listOfPurchases:
        print("-", p.GetTopUpTitle(), "£" + str(int(p.GetPrice()) / 100))

    again = input("Would you like to buy another ticket? (yes/no): ")
    if again != "yes":
        shopping = False

# once the loop ends, show everything bought this session
print()
print("Your purchases this session:")
for p in listOfPurchases:
    print("-", p.GetTopUpTitle(), "£" + str(int(p.GetPrice()) / 100))

    
# USE CASE 6 save purchases to a file when the program closes
try:
    # open the file in write mode ('w')  creates it if it doesn't exist
    # newline='' stops blank rows appearing between lines 
    with open('purchases.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # write one row per purchase: the title and the price
        for p in listOfPurchases:
            writer.writerow([p.GetTopUpTitle(), p.GetPrice()])
    print()
    print("Your purchases have been saved.")
except:
    print("Sorry, there was a problem saving your purchases.")
