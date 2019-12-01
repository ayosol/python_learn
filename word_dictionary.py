import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
import sys
import win32com.client as wincl


speak = wincl.Dispatch("SAPI.SpVoice")

url = "https://www.dictionary.com/browse/"

# read the word from the command line arguments and append to the url
shouldSpeak = False


try:
    word = sys.argv[1]
    url += word
except:
    print("Specify a word!")
    exit(-1)

try:
    shouldSpeak = True if sys.argv[2] == '--speak' else False
except IndexError:
    pass

# load the website's source code
try:
    r = requests.get(url)
    soup = bs(r.content, 'lxml')
except:
    print("You're probably not connected to the internet!")
    exit(-1)

dictionary = {}

# parse the source to obtain all necessary info
# try:
sections = soup.select('section.css-pnw38j.e1hk9ate0')
# print(sections)
for section in sections:
    # print(section.text)
    name = section.find("span", {"class": "luna-pos"})
    if name is not None:
        name = name.text
        div = section.find('div', {'class': 'default-content'})
        if div is not None:
        # print(div)
        # print(type(div))

    # answer_list = soup.findAll("ol")[0]
    # meanings = div.findChildren('span', recursive=False)
            meanings = div.find_all('span', {'class': 'css-1p89gle'})
            dictionary[name] = meanings
# except:
#     print("Word not found!")
#     exit(-1)


# display the results
# print()
# print(word + ": " + header)

# for (i, meaning) in enumerate(meanings):
#     print()
#     print(str(i + 1) + ".", meaning.text)
# pprint(dictionary)
for part_of_speech, meanings in dictionary.items():
    print()
    print(part_of_speech)
    if part_of_speech.lower() == 'idiom':
        continue
    for index, meaning in enumerate(meanings):
        print(str(index + 1) + ".", meaning.text)
        if shouldSpeak:
            speak.Speak(meaning.text)
