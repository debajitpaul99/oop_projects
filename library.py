class Library:
    def __init__(self):
        self.book_list = []
    def entry_book(self,book):
        self.book_list.append(book)

class Book:
    def __init__(self,book_id,title,author,availability = True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
    def borrow_book(self,given_id):
        if self.book_id == given_id:
            if self.availability:
                self.availability = False
                print(f'Successfully borrowed.Book ID:{self.book_id}')
            else:
                print(f'Book ID {self.book_id} is already borrowed')
    def return_book(self):
        if self.availability is False:
            self.availability = True
            print('Thanks for returning the book')
    def view_book_info(self):
        print(f'Book_id:{self.__book_id}\nTitle:{self.__title}\nAuthor:{self.__author}')

library = Library()
ansi = Book(114,'Programming','Balaguruswami')
circuit = Book(115,'Electrical Circuit','Sadiku')
library.entry_book(ansi)
library.entry_book(circuit)

while True:
    print('Press 1 to view all books in the library')
    print('Press 2 to borrow book')
    print('Press 3 to return book')
    print('Press 4 to exit from the system')
    op = int(input('Enter option: '))

    if op == 1:
        print('Here all the books')
        for book in library.book_list:
            book.view_book_info()
    elif op == 2:
        flag = False
        id = int(input('Enter book id: '))
        for book in library.book_list:
            if book.book_id == id:
                flag = True
                book.borrow_book(id)
        if flag is False:
            print('Book ID is invalid')    
    elif op == 3:
        id = int(input('Enter book id: '))
        for book in library.book_list:
            if book.book_id == id:
                book.return_book()
    elif op == 4:
        print('Exit')
        break
    else:
        print('Invalid option, press correct key')