import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    #while page < max_pages:
    url = 'https://sfbay.craigslist.org/search/sby/cto?s=' + str(page)
    source_code = requests.get(url)
    #print(url)

    plain_text = source_code.text
    #print(plain_text)

    soup = BeautifulSoup(plain_text, "lxml")
    #print(soup)

    for link in soup.find_all('a',{'class':'result-title hdrlnk'}):
        href = 'https://sfbay.craigslist.org' + link.get('href')
        title = link.string
        #print(href)
        #print(title)
        get_single_item_data(href)

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    #print(plain_text)
    soup = BeautifulSoup(plain_text,"lxml")
    #print(soup)

    for item_name in soup.find_all('li',{'class':'desktop'}):
        print(item_name.string)

#trade_spider(3)
#get_single_item_data('https://sfbay.craigslist.org/')


def get_some_info_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, "lxml")

    ul_items = soup.find('ul',{'class':"clfooter"})
    for li_items in ul_items.find_all('li', {'class':'desktop'}):
        for href_items in li_items.find_all('a'):
            print(href_items.get('href'))

#get_some_info_data("https://sfbay.craigslist.org/sby/cto/6051035179.html")

def get_carimage_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text,"lxml")

    ul_items = soup.find('ul', {'class':'rows'})
    for li_items in ul_items.find_all('li', {'class':'result-row'}):
        #print(li_items)
        #print('\n')
        price_items = li_items.find('span',{'class':'result-price'})
        print(price_items)

        if price_items is not None:
            print(price_items.string)

        print('\n')
        #div_item = li_items.find('div',{'class':'swipe-wrap'})
        #print(div_item)


get_carimage_data('https://sfbay.craigslist.org/search/sby/cto?s=')