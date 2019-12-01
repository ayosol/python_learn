from PyDictionary import  PyDictionary

SearchWord = input("Enter word to search: ")
try:
    myDict = PyDictionary(SearchWord)
    print(myDict.meaning(SearchWord), 'lxml')
except:
    print("Word not Found")

 #parse the source to obtain all necessary info
try:
    header = soup.findAll("span", {"class": "luna-pos"})[0].text
    answer_list = soup.findAll("ol")[0]
    meanings = answer_list.findChildren("li", recursive=False)
except:
    print("Word not found!")
    exit(-1)