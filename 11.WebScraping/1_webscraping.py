import requests
import bs4

# GRABBING A TITLE OF PAGE:
result = requests.get("https://en.wikipedia.org/wiki/Arjuna") # LINK OF WEBSITE TO BE SCRAPPED
# print(type(result))   
## THIS WILL PRINT THE WHOLE HTML DOCUMENT OF LINK PROVIDED !!AS A STRING!!
# print(result.text)
## We need to use beautiful soup to make it to parse through this html documnet as right now this is just scrambeled html code as string!
soup = bs4.BeautifulSoup(result.text,"lxml") 
## bs4 take 2 input parameters: 1) html text that is to be beautified, 2) what engine to be used to parse through this code, ex: html
# print(soup)
## Now we can grab elements from this 
print(soup.select('title'))
## This would print a list of all elements found with the tag name 'title'. Ex: [<title>Arjuna - Wikipedia</title>] 
## To grab text out of this list we have to specify which element of list to be grabbed and the .getText() method will give text from the selected element
print(soup.select('title')[0].getText()) ## This will print out just title of the website
## This will grab all the paragraphs from the website
site_paragraphs = soup.select("p")
# print(site_paragraphs)
print(site_paragraphs[0]) ##This will give the very first para of the website
print(site_paragraphs[0].getText()) ##This will give the very first para's text 

## GRABBING BY A CLASS: using these ways you can grab all elements which share same class/id/name etc!
## soup.select('div') => All elements with the <div> tag
## soup.select('#some_id') => The HTML element containing the id attribute of some_id
## soup.select('.notice') => All the HTML elements with the CSS class named notice
## soup.select('div span') => Any elements named <span> that are within an element named <div>
## soup.select('div > span') => Any elements named <span> that are directly within an element named <div>, with no other element in between

## GRABBING IMAGE ON A WEBSITE: using these ways you can grab all elements which share same class/id/name etc!
# soup.select('img') ## This Will return list of all elements which have image tag associated with them!
#pulling out src attribute from img html element!
image = soup.select('img')[6]
# now NOtE that image here is not a string, instead it is a special element defined by library
print(image) 
print(type(image))
# So plus point here is that we can simply use this as dictionary and grab what ever tag we want to
print(image['src']) #Grabbing src attribute from html img element!
image_src_link = image['src']
# DOWNLOADING THE IMAGE I WANT!
image_link = requests.get(f'https:{image_src_link}')
## This command will print the binary code of image file in which it is stored!!
#print(image_link.content)
binary_code_of_extracted_image = image_link.content 

##Storing the image file on to computer
import os
file_path = f'{os.getcwd()}\\extractedImagefromWebsite.jpg'
with open(file_path, 'wb') as image_file: #Note hee 'wb' is used which means binary because image is written in binary code!
    image_file.write(binary_code_of_extracted_image)
    image_file.close()