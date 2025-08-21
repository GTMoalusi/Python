import datetime
import os

class LMS:
    """ This class is used to keep record of books library.
    It has total four modules: "Display", "Issue books", "Return books", "Add books" and "Erase books" """

    # Constructor
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        # Load books from the file when the class is initialized
        self.load_books()

    def load_books(self):
        """Loads books from the text file into the books_dict."""
        self.books_dict = {}
        Id = 101
        try:
            with open(self.list_of_books, "r") as bk:
                content = bk.readlines()
            for line in content:
                # Add each book to the dictionary with a unique ID
                self.books_dict.update({
                    str(Id): {
                        "books_title": line.strip(), # Use strip() to remove newline characters
                        "lender_name": "",
                        "Issue_data": "",
                        "Status": "Available"
                    }
                })
                Id += 1
        except FileNotFoundError:
            print(f"Error: The file '{self.list_of_books}' was not found. Creating it...")
            # Create an empty file if it doesn't exist
            open(self.list_of_books, "a").close()

    def save_books(self):
        """Saves the current state of the books back to the file."""
        # This function is crucial for making the changes permanent
        with open(self.list_of_books, "w") as bk:
            for key, value in self.books_dict.items():
                bk.write(f"{value.get('books_title')}\n")

    def display_books(self):
        print("--------------------List of Books--------------------")
        print("Books ID", "\t", "Title")
        print("-----------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("Status"), "]")

    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y=%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] != "Available":
                print(f"This book is already issued to {self.books_dict[books_id]["lender_name"]} \
                    on {self.books_dict[books_id]["Issue_data"]}")
            else:
                your_name = input("Enter your name:")
                self.books_dict[books_id]["lender_name"] = your_name
                self.books_dict[books_id]["Issue_data"] = current_date
                self.books_dict[books_id]["Status"] = "Already Issued"
                print("Book Issued Successfully!!! \n")
        else:
            print("Book ID not found!!!")

    def add_books(self):
        new_books = input("Enter book title: ")
        if new_books == "":
            print("Book title cannot be empty.")
            return self.add_books()
        elif len(new_books) > 25:
            print("Book title length is too long! Title length should be 25 characters or less.")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.write(f"{new_books}\n")
            
            # Recalculate the next available ID and update the dictionary
            # This ensures the new book gets a correct ID
            self.load_books()
            print(f"This book '{new_books}' has been added successfully!!!")

    def return_books(self):
        books_id = input("Enter books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library. Please check your book ID.")
            else:
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_data"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully returned!!! \n")
        else:
            print("Book ID is not found")
    
    def erase_books(self):
        """Removes a book from the dictionary and the text file."""
        books_id = input("Enter books ID to remove: ")
        if books_id in self.books_dict.keys():
            # Check if the book is available before deleting
            if self.books_dict[books_id]["Status"] == "Available":
                title_to_remove = self.books_dict[books_id]["books_title"]
                del self.books_dict[books_id] # Remove the book from the dictionary
                self.save_books() # Save the updated dictionary back to the file
                print(f"The book '{title_to_remove}' has been successfully removed.")
            else:
                print("Cannot remove this book. It is currently issued.")
        else:
            print("Book ID not found. Nothing was removed.")

# The main application loop
try:
    myLMS = LMS("List_of_books.txt", "Python's Library")
    press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "E": "Erase Books", "Q": "Quit"}
    key_press = ""
    while not (key_press == "q"):
        print(f"\n-------------------- Welcome To {myLMS.library_name} Library Management System -------------------- \n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection: Issue Books\n")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\nCurrent Selection: Add Books\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection: Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection: Return Books\n")
            myLMS.return_books()
        elif key_press == "e":
            print("\nCurrent Selection: Erase Books\n")
            myLMS.erase_books()
        elif key_press == "q":
            break
        else:
            print("Invalid key pressed. Please try again.")

except Exception as e:
    # This will now catch any other unexpected errors
    print(f"An error occurred: {e}")
