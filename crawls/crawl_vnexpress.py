import re
import urllib.request

from bs4 import BeautifulSoup


def not_relative_uri(href):
    return re.compile('^https://').search(href) is not None


url = 'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

new_feeds = soup.find(
    'section', class_='section section_topstory').find_all('a', class_='', href=not_relative_uri)

for feed in new_feeds:
    title = feed.get('title')
    link = feed.get('href')
    print('Title: {} - Link: {}'.format(title, link))

# with open('data.csv', 'w', encoding="utf-8") as csv_file:
#     writer = csv.writer(../database/csv_file)
#     writer.writerow(['Title', 'Link'])
#     for feed in new_feeds:
#         writer.writerow([feed.get('title'), feed.get('href')])
