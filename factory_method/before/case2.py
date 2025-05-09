class Book:
    def borrow(self):
        print("Borrowed book process is started")

    def return_book(self):
        print("Returned book process is started")

    def buy(self):
        print("Buy book process is started")


class Magazine:  # This class being added in the package code
    def borrow(self):
        print("Borrowed magazine process is started")

    def return_book(self):
        print("Returned magazine process is started")

    def buy(self):
        print("Buy magazine process is started")


def borrow_endpoint_handler(types: str):  # This handler changes in the package code
    if types == "book":
        book = Book()
        book.borrow()
    elif types == "magazine":
        magazine = Magazine()
        magazine.borrow()


# client code
if __name__ == "__main__":
    borrow_endpoint_handler("magazine")  # client also need to change the code
