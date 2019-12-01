# from PyDictionary import  PyDictionary
import requests
from bs4 import BeautifulSoup as bs

# url = "http://pydictionary-geekpradd.rhcloud.com/api/meaning/[word]""
# SearchWord = input("Enter word to search: ")
# try:
#     myDict = PyDictionary(SearchWord)
#     print(myDict.getMeanings, 'lxml')
# except:
#     print("Word not Found")


url = "http://pydictionary-geekpradd.rhcloud.com/api/meaning/"

# read the word from the command line arguments and append to the url
try:
    SearchWord = input("Enter word to search: ")
    url += SearchWord
except:
    print("Specify a word!")
    exit(-1)

# load the website's source code
#try:
r = requests.get(url)
soup = bs(r.content, 'lxml')
# except:
#     print("You're probably not connected to the internet!")
#     exit(-1)

# parse the source to obtain all necessary info
try:
    header = soup.findAll("span", {"class": "luna-pos"})[0].text
    answer_list = soup.findAll("ol")[0]
    meanings = answer_list.findChildren("li", recursive=False)
except:
    print("Word not found!")
    exit(-1)


# display the results
print()
print(SearchWord + ": " + header)

for (i, meaning) in enumerate(meanings):
    print()
    print(str(i + 1) + ".", meaning.text)