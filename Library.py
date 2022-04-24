class Library:
    def __init__(self,booksAvailable):
        self.books = booksAvailable
    
    def display(self):
        print(f"Books available in the library are-")
        for book in self.books:
            print(book)
    
    def borrow(self,book):
        if book in self.books:
            print(f"The requested book {book} has been issued to you.")
            self.books.remove(book)
            return True
        else:
            print(f"Sorry!,The requested book {book} is not available to borrow.")
            return False
            
    def returnbook(self,book):
        self.books.append(book)
        print("Thanks for returning this book")
        
class Student:
    def request(self):
        self.book = input("Enter the name of the book you want to issue:")
        return self.book
    
    def return_book(self):
         self.book = input("Enter the name of the book you want to return: ")
         return self.book
    

centralLibrary = Library(["Maths","Science","SST"]) 
stud = Student()

    
#A menu is always made of using an Infinite loop
while (True):
    message = ''' ***** Welcome to Central Library *****
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library'''
    print(message)  
    choice = int(input("Enter your choice: Press 1 or Press 2 or Press 3 or Press 4:"))
    
    if choice == 1:
        print(centralLibrary.display())
    
    elif choice == 2:
        #print(stud.request())
        centralLibrary.borrow(stud.request())

    elif choice == 3:
        centralLibrary.returnbook(stud.return_book())

    elif choice == 4:
        print("Thanks for using this Library")
        exit()

    else:
        print("Your choice is invalid. Please check and input again")
    
   

