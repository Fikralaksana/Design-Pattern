class Book:
    def borrow(self):
        print("Borrowed book process is started")

    def return_book(self):
        print("Returned book process is started")

    def buy(self):
        print("Buy book process is started")


def borrow_endpoint_handler():
    book = Book()
    book.borrow()


# client code
if __name__ == "__main__":
    borrow_endpoint_handler()
