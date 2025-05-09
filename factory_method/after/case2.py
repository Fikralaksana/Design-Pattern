# notice that we import the case1 file
# which show us that, there will be no changes in the package code
# only client code will be changed
from case1 import LibraryAction, Action, borrow_endpoint_handler

# client code
if __name__ == "__main__":
    # add new item type
    class MagazineActionFactory(LibraryAction):
        def create_action(self) -> "Action":
            return MagazineAction()

    class MagazineAction(Action):
        def borrow(self):
            print("Custom magazine borrowed process is started")

        def return_book(self):
            print("Custom magazine returned process is started")

        def buy(self):
            print("Custom magazine buy process is started")

    # use the new item type
    borrow_endpoint_handler(MagazineActionFactory())
