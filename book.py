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
print("Confirm checkout:", + "book")