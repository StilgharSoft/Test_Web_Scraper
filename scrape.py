from requests import get
from bs4 import BeautifulSoup
from datetime import datetime

def scrape(page_url, output):
    scrape_result=[]

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

        scrape_result.append([price[1:], name])

    now = datetime.now()

    timestamp = str(now.year)[2:] + str(now.month).zfill(2) + str(now.day).zfill(2) + '_' + \
                str(now.hour).zfill(2) + str(now.minute).zfill(2) + str(now.second).zfill(2)

    with open(timestamp + '_' + output, 'w') as output_file:
        for item in scrape_result:
            output_file.write(','.join(item)+'\n')

    return 0
