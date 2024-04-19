class Product:
    def _init_(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self): 
            print("Name:", self.name) 
            print("Price:", self.price) 
            print("Quantity:", self.quantity)

    def calculate_cost(self):
        return self.price* self.quantity

class Electronics (Product): 
    def _init_(self, name, price, quantity, brand): 
        super()._init_(name, price, quantity)
        self.brand = brand
    def display_product_info(self):
        super().display_product_info()

        print("Brand:", self.brand)

class Clothing(Product):

    def _init_(self, name, price, quantity, size):
        super()._init_(name, price, quantity)
        self.size = size

    def display_product_info(self):
        super().display_product_info()
        print("Size:", self.size)

class Book(Product):

    def _init_(self, name, price, quantity, author): 
        super()._init_(name, price, quantity)
        self.author = author

    def display_product_info(self):
        super().display_product_info() 
        print("Author:", self.author)

electronics1 = Electronics("PC", 2000, 2, "Dell")
clothing1 = Clothing("Shirt", 1500, 5, "Medium")

clothing1.display_product_info()
electronics1.display_product_info()

44
45

book1 = Book("Head First Java", "1000", "8", "Kathy Sierra and Bert Bates")

46

print("electronics1") (4/4 3:39 PM) Harpreet Singh
class Library:
    bookcollection = []
 
    # construction
    def _init_(self, listofbooks):
        self.bookcollection = listofbooks
 
    # method to show all the books
    def displayAvailableBook(self):
        if len(self.bookcollection) == 0:
            print("No Books")
       
        else:
            print("The books we have in the library are:")
            for Book in self.bookcollection:
                print(Book)
 
    def borrowbook(self, user,book):
        if book in self.bookcollection:
            self.bookcollection.remove(book)
            print("Confirm checkout:", + book) 
            print("Welcome to our Calculator")
 
X = float(input("Enter the first number: "))
Y = float(input("Enter the second number: "))
Sign = input("Select - or +: ")
 
if Sign == "+":
    Sum = X + Y
else:
    Sum = X - Y
 
print("Result:", Sum) [3/7 2:52 PM] ~ Ankit
import random
 
    #initiate a secret number
secret_number=random.randint(1,100)
print(secret_number)
    #user input - to guess what is the number from user
userguessing= int(input("Enter Number:"))
 
    #check the answer is correct
if userguessing == secret_number:
    print("Bingo!")
    #give hint, is the guess number is too high
elif userguessing > secret_number:
        print("too low")
else:
    print("you loss")