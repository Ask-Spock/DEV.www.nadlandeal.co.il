
from bs4 import BeautifulSoup

with open('Nadlan-Deal-FR.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    print(soup.h2)
    