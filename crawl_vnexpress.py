from bs4 import BeautifulSoup
import urllib.request
import re
import csv


def not_relative_uri(href):
    return re.compile('^https://').search(href) is not None


url = 'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# new_feed = soup.find('h3', class_='title-news').find('a')
# title = new_feed.get('title')
# link = new_feed.get('href')
# print('Title: {}, Link: {}'.format(title, link))

# new_feeds = soup.find(
#     'section', class_='section section_stream_home section_container').find_all('a', class_='', href=not_relative_uri)

new_feeds = soup.find(
    'section', class_='section section_topstory').find_all('a', class_='', href=not_relative_uri)

# print(new_feeds)
for feed in new_feeds:
    title = feed.get('title')
    link = feed.get('href')
    print('Title: {} - Link: {}'.format(title, link))

# with open('data.csv', 'w', encoding="utf-8") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['Title', 'Link'])
#     for feed in new_feeds:
#         writer.writerow([feed.get('title'), feed.get('href')])
