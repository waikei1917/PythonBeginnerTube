import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "lxml")

    ul_items = soup.find('ul', {'class': 'rows'})
    for li_items in ul_items.find_all('li', {'class':'result-row'}):
        title_content = li_items.find('a',{'class':'result-title hdrlnk'})
        content = title_content.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}:<>?><,./~`=-\""
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

start('https://sfbay.craigslist.org/search/sby/cto?s=')