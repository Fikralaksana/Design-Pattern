class LibraryAction:
    def borrow(self):
        action = self.create_action()
        action.borrow()

    def return_book(self):
        action = self.create_action()
        action.return_book()

    def buy(self):
        action = self.create_action()
        action.buy()

    def create_action(self) -> "Action": ...


class BookActionFactory(LibraryAction):
    def create_action(self) -> "Action":
        return BookAction()


class Action:
    def borrow(self): ...

    def return_book(self): ...

    def buy(self): ...


class BookAction(Action):
    def borrow(self):
        print("Borrowed process is started")

    def return_book(self):
        print("Returned process is started")

    def buy(self):
        print("Bought process is started")


def borrow_endpoint_handler(factory: LibraryAction):
    factory.borrow()


# client code
if __name__ == "__main__":
    borrow_endpoint_handler(BookActionFactory())
