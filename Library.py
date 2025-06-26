class book:
    def _init_(self, title, author,isd):
        self.title=title
        self.author=author 
        self.isd=isd
    def info(self):
        print(self.title,self.
        author,self.isd)
b1=book("Physics","HC verma","10000021")
b2=book("maths","S Dey","2000948575")
b2.author
class library:
    def _init_(self,name):
        self.name=name
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f'Author{book.author}is added to your library')
    def remove_book(self,isd1):
        for book in self.books:
            if (book.isd==isd1):
                self.books.remove(book)
        print(f"no book is found with isd {isd}") 
    def display (self):
        print(f'books in {self.name} is')
        if not self.books:
            print("no books found")
        for book in self.books:
            book.info()
            
 
l1=library ("digital_library")
l1.add_book(b1)
l1.add_book(b2)

l1.books

l1.display()