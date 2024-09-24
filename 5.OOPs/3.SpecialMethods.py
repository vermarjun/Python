class Books():
    def __init__(self,author,pages,bookname):
        self.bookname = bookname
        self.author = author
        self.pages = pages
    def __str__(self) -> str:
        return f'{self.bookname} by {self.author}, {self.pages} long'
    def __len__(self):
        return self.pages

my_book = Books('Arjun Verma',200,'Reasons why you should sucide and Easiest ways to die in 2024') 
print(my_book) #Since i have defined in my function of what to return in case of string or else this would have given memory location instead 
length = len(my_book)
print(length) #This would be giving type error if i had not defined what to do with len operator in my object!)