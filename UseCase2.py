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
    def __init__(self, title, price, code):
        self.title = title # top-up name,from topuptitle
        self.price = price # price in pence,from topup price in pence
        self.code = code # number the user types to choose it
    def GetTitle(self):
        return self.title
    def GetPrice(self):
        return self.price
    def GetCode(self):
        return self.code


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
            #print("For",cat1.GetCategory(),"enter",cat1.GetCode())
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

#print(lines['category_title'], "contains", lines['category_description'])