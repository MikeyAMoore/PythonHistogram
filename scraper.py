import requests
from bs4 import BeautifulSoup

def daily_smarty_links(links):
    titles = []

    for link in links:
        print(link['href'])
    
    return titles


     

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, "html.parser")
links = soup.find_all("a")

daily_smarty_links(links)

