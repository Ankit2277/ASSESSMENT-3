README FOR PRINT :

It tells the computer to display the word "hello" on the screen.
Then, it tells the computer to display the word "world" on the screen.

README FOR CLASS :

This class represents a product. Products have a name, price, and quantity.
It has a method called `display_product_info()` to show the product details like name, price, and quantity.
It also has a method called `calculate_cost()` which calculates the total cost of the product by multiplying its price and quantity.
These classes are specialized types of products.
Each of these classes inherits from the Product class, which means they have all the properties and methods of the Product class.
They also have their own specific attributes like brand for Electronics, size for Clothing, and author for Book.
Each of them overrides the `display_product_info()` method from the Product class to display their specific attributes along with the general product information.
This class represents a library.
It has a list called `bookcollection` to store the books available in the library.
It has methods to display all the available books and to borrow a book.
The `borrowbook()` method removes the borrowed book from the `bookcollection` list.

README FOR BOOK :

It represents a library and contains a collection of books.
Attributes:
bookcollection: This is a list that stores the books available in the library.
Methods:
__init__(): This is a constructor method that initializes the library with a list of books provided as an argument.
displayAvailableBook(): This method displays all the books available in the library. If there are no books, it prints "No Books".
borrowbook(): This method allows a user to borrow a book from the library. If the requested book is available in the library, it removes the book from the bookcollection

README FOR SECRET NUMBER :

Generating the Secret Number:
The random.randint(1, 100) function generates a random integer between 1 and 100 and assigns it to secret_number.
This is the number the user needs to guess.
Getting User Input:
The program prompts the user to input a number with the message "Enter Number:".
The int(input()) function reads the user's input as an integer and assigns it to userguessing.
Checking the Guess:
The program compares the user's guess (userguessing) with the secret number (secret_number).
If they are equal, it prints "Bingo!" to indicate that the user guessed the correct number.
If the guess is higher than the secret number, it prints "too low" to give the user a hint to guess lower.
If the guess is lower than the secret number, it implies the user lost and prints "you loss".

README FOR CALCULATOR :

Welcome Message:
The program starts by printing "Welcome to our Calculator" to greet the user.
Input Numbers:
The user is prompted to enter two numbers: the first number and the second number.
The input() function takes user input as a string, and float() converts it to a floating-point number, which allows decimal inputs.
Input Operator:
The user is prompted to select an operator: either "+" for addition or "-" for subtraction.
The input() function reads the user's choice and assigns it to the variable Sign.
Perform Calculation:
If the operator selected is "+", the program adds the two numbers together and assigns the result to the variable Sum.
If the operator selected is "-", the program subtracts the second number from the first number and assigns the result to Sum.
Display Result:
Finally, the program prints the result of the calculation.

README FOR TURTLE(ASSESSMENT-3) :

This code uses the Turtle module in Python to draw a simple flower. 
The flower consists of six petals, each drawn using the `draw_petal()` function. 
The petals are filled with red color, creating the appearance of a flower.
After drawing all the petals, the turtle's visibility is hidden, and the window remains open to display the flower until it's manually closed. 
The background color is set to light green to provide a pleasant backdrop for the flower.

