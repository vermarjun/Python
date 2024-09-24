import requests
import bs4

html_page = requests.get("https://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(html_page.text,"lxml")
div_quotes = soup.select(".quote")
print(len(div_quotes))

##LIST OF ALL THE AUTHORS ON FIRST PAGE:
authors_on_first_page = []
for quote in div_quotes:
    div_author = quote.select(".author")
    author = div_author[0].getText()
    authors_on_first_page.append(author)
print(authors_on_first_page)

##LIST OF ALL THE QUOTES ON FIRST PAGE:
quotes_on_first_page = []
for quote in div_quotes:
    div_quote = quote.select(".text")
    quote = div_quote[0].getText()
    quotes_on_first_page.append(quote)
print(quotes_on_first_page)

##TOP 10 TAGS ON FIRST PAGE:
div_tags = soup.select(".tag-item")
print(len(div_tags))
tags_on_first_page = []
for tags in div_tags:
    a_tag = tags.select(".tag")
    tag = a_tag[0].getText()
    tags_on_first_page.append(tag)
print(tags_on_first_page)

##LIST OF ALL THE UNIQUE AUTHORS ON THE WEBSITE:
# pages = range(1,11)
row_result = ''
authors_on_website = []
page = 1
while row_result != " No quotes found! ":
    # for page in pages:
    print(f'currently parsing page {page}')
    html_content = requests.get(f'https://quotes.toscrape.com/page/{page}/')
    soup = bs4.BeautifulSoup(html_content.text,"lxml")
    div_quotes = soup.select(".quote")
        # print(len(div_quotes))
    for quote in div_quotes:
        div_author = quote.select(".author")
        author = div_author[0].getText()
        authors_on_website.append(author)
        # print(authors_on_website)
    # authors_on_website.append(authors_on_first_page)
    div_col_md_8 = soup.select(".col-md-8")
    # quotes_div = div_col_md_8[1]
    page=page+1
    if "No quotes found!" in div_col_md_8[1].getText():
        row_result = " No quotes found! "
        print("No page found, Exiting the loop")
        break
    else:
        continue

print(authors_on_website)
x = set(authors_on_website)
print(x)
print(f'authors on website {len(authors_on_website)}')
print(f'authors on website set {len(x)}')