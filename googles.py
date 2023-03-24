# importing the BeautifulSoup Library
import bs4
import requests

# Creating the requests

res = requests.get("https://www.google.com")
print("The object type:", type(res))

# Convert the request object to the Beautiful Soup Object  
soup = bs4.BeautifulSoup(res.text)
print("The object type:", type(soup))
print(soup)

print("priting conents")
print(soup.contents)
print("printing text")
print(soup.text)
print(soup.get_attribute_list(list))