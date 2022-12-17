from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
fields = ['Product', 'Price']

def writeInCsv(filename, data):
    # writing to csv file 
    with open(filename, 'w') as csvfile:
    # creating a csv writer object 
        csvwriter = csv.writer(csvfile)
    # writing the fields 
        csvwriter.writerow(fields)
    # writing the data rows 
        csvwriter.writerows(data)

def scrapFromWebsite():
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'lxml')
    divs = html.find_all('div', {'class': 'thumbnail'})
    data = []
    for d in divs:
        value = d.find('h4', {'class': 'price'}).string
        title = d.find('a', {'class':'title'}).string
        data.append([title, value])
    writeInCsv('products.csv', data)

def main():
    scrapFromWebsite()

if __name__=="__main__":
    main()