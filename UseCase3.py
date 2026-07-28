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
class TopUp:
    def __init__(self, title, price, code, description, entType, entUnit, entValue, entQuantity, passengerName, passengerQuantity):
        self.title = title# topup name
        self.price = price #price in pence 
        self.code = code #number
        self.description = description  # topup description
        self.entType = entType    # fixed date or flexible
        self.entUnit = entUnit   # minutes / days / annual
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

listOfCatClasses =[]
listOfCategories = []
listOfCodes =[]
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
