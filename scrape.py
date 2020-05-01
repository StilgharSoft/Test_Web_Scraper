from requests import get
from bs4 import BeautifulSoup
from datetime import datetime

def scrape(page_url, output):
    result=[]
    page = get(page_url)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    for item in soup.find_all('div', class_='caption'):
        for child in item.findChildren():
            
            try:
                if child.name == 'h4' and 'price' in child.attrs['class']:
                    price = child.text
            except:
                pass

            try:
                if child.name == 'a':
                    name = child.attrs['title']
            except:
                pass

        result.append([price[1:], name])

    now = datetime.now()

    with open(str(now.year) + str(now.month) + str(now.day) + \
              str(now.hour) + str(now.minute) + str(now.second) + \
              ' ' + output, 'w') as lista_txt:

        for item in result:
            lista_txt.write(','.join(item)+'\n')
    return 0
