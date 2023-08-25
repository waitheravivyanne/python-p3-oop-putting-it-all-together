#!/usr/bin/env python3

class Book:
     def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
     @property
     def page_count(self):
        return self._page_count
    
     @page_count.setter
     def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

     def turn_page(self):
          print("Flipping the page...wow, you read fast!")

if __name__ == "__main__":
                book = Book("Sample Book", 100)
                print(book.page_count)
                book.page_count = "not an integer"
                print(book.page_count)