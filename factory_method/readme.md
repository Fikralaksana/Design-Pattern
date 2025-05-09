# Factory Method

## Scenario

Let's say you have a scenarios that you need to create an python packages that manage item in the library.

1. In the business logic you record all the books history.
   Then books can be borrowed, returned, and can be bought by user.

   Using those requirements, you probably will come up with a class like this:

   ```python
   class Book:
       def borrow(self):
           print("Borrowed process is started")

       def return_book(self):
           print("Returned process is started")

       def buy(self):
           print("Buy process is started")
   ```

   And you will use those class in your system handler(we will call it client code) like this:

   ```python
   def borrow_endpoint_handler():
       book = Book()
       book.borrow()
   ```

   So, then you except the user of this package will use the handler like this (client code):

   ```python
   from package_name import borrow_endpoint_handler # import the handler

   borrow_endpoint_handler() # call the handler
   ```

2. Then after this package is released, it is working fine. Then, the user had a request to be able add other item type to the library.
   In this case the user want to add magazine to their library system with the same business logic (borrow, return, buy).

   Then you need to add more class to support the new requirements.

   ```python
   class Book:
       def borrow(self):
           print("Borrowed process is started")

       def return_book(self):
           print("Returned process is started")

       def buy(self):
           print("Buy process is started")

   class Magazine:
       def borrow(self):
           print("Borrowed process is started")

       def return_book(self):
           print("Returned process is started")

       def buy(self):
           print("Buy process is started")
   ```

Now you need to modify the `borrow_endpoint_handler` to support the new requirements.

```python
def borrow_endpoint_handler(types: str): # Now the handler require the type of item.
    if types == "book":
        book = Book()
        book.borrow()
    elif types == "magazine":
        magazine = Magazine()
        magazine.borrow()
```

Notice that changes the code inside the handler?
This will be breaking changes for your user. because other user might be already used to call the `borrow_endpoint_handler` without any parameter.
But now they need to pass the type of item to the handler.

```python
from package_name import borrow_endpoint_handler

borrow_endpoint_handler("book")
```

Also, Let's say you have other user that want to add other new type that specific to their business. You will have to modify the handler again, to add another if statement.
That require you to always modify the handler when new requirement come of your package user.
It is not good to release new version of your package only to add new item type.

## So how to avoid this?

This is where Factory Method design pattern comes in handy. Instead of modifying the handler, you can move the responsibility to create specific item to the user side.
So with this flexibility, user can create new item type without modifying the handler. which we will not break the existing handler.
Also, they can add the item that specific to their use case only easily.

Factory Method design pattern is a creational design pattern that provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.

Lets try again implement above scenario. But this time we will use Factory Method design pattern from the beginning.

1. In the business logic you need to record all the books history.
   Then books can be borrowed, returned, and can be bought by user.

   You can create a super class of the library item.
   You need to implement all the method required in the super class.
   But you can leave the `create_action` method to be implemented by the subclass.

   ```python
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

    def create_action(self) -> "Action": ... # this is for type hint, should be implemented by subclass.

    class BookActionFactory(LibraryAction):
        def create_action(self) -> "Action": # this is the implementation of the create_action method.
            return BookAction()
   ```

   Now in the handler, you can create the specific item type by using the factory method.

   ```python
   def borrow_endpoint_handler(factory: LibraryAction):
       factory.borrow()
   ```

   Then you package user can create the specific item type by using the factory method.

   ```python
   from package_name import BookActionFactory, borrow_endpoint_handler

   borrow_endpoint_handler(BookActionFactory())
   ```

2. Then after this package is released, it is working fine. Then, the user had a request to be able add other item type to the library.
   In this case the user want to add magazine to their library system with the same business logic (borrow, return, buy).

   Now there are no changes needed in your package. They can create new item type that specific to their use case.
   This is how the client code will look like:

   ```python
   from package_name import LibraryAction, Action, borrow_endpoint_handler

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

   borrow_endpoint_handler(MagazineActionFactory())
   ```

For the complete code for those 2 patterns, you can see the [before](before) and [after](after) folder.
