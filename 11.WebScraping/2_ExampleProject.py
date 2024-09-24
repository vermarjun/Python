################# TOSCRAPE.COM ###############

## GOAL = GET EVERY BOOK WITH 2 STAR RATING!
import os
import requests
import bs4
pages = range(1,51)
for page in pages:
    print(f'parsing page: {page}')
    page = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html')
    soup = bs4.BeautifulSoup(page.text,"lxml")
    books_on_this_page = soup.select(".product_pod")
    for book in books_on_this_page:
        if "Two" in book.p['class']:
            print(book.h3.getText())  
    
