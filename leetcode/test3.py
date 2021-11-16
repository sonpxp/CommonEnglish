import csv
import json
import os.path
import time

import requests
from bs4 import BeautifulSoup


class ElementsScraper:
    base_url = 'https://scrapingkungfu.herokuapp.com/chamber_3?page='

    @staticmethod
    def fetch(url):
        print('HTTP GET request to URL: %s' % url, end='')
        response = requests.get(url)
        print(' | Status code: %s' % response.status_code)

        return response

    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')

        titles = [title.text for title in content.findAll('strong', {'class': 'movie-title'})]
        print(len(titles))
        genres = [genres.text for genres in content.findAll('span', {'class': 'movie-genre'})]
        countries = [countries.text for countries in content.findAll('span', {'class': 'movie-country'})]
        years = [years.text for years in content.findAll('span', {'class': 'movie-year'})]
        directors = [directors.text for directors in content.findAll('span', {'class': 'movie-director'})]
        starrings = [starrings.text for starrings in content.findAll('span', {'class': 'movie-starring'})]
        posters = [posters['src'] for posters in content.findAll('img', {'class': 'movie-poster'})]

        for index in range(0, len(titles)):
            item = {
                'title': titles[index],
                'genre': genres[index],
                'country': countries[index],
                'year': years[index],
                'director': directors[index],
                'starring': starrings[index],
                'poster': posters[index]
            }

            self.to_csv(item)
            # self.to_json(item)
            print(item)

    @staticmethod
    def to_json(item):
        with open('test3_dict.json', 'w', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False, indent=4)

    @staticmethod
    def to_csv(item):
        movie_exists = os.path.isfile('movies.csv')

        with open('movies.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=item.keys())

            if not movie_exists:
                writer.writeheader()

            writer.writerow(item)

    def run(self):
        for page in range(1, 5):
            next_page = self.base_url + str(page)
            response = self.fetch(next_page)

            if response.status_code == 200:
                self.parse(response.text)
            else:
                print('Something has gone wrong, skiping to next page')
                continue

            time.sleep(2)


if __name__ == '__main__':
    scraper = ElementsScraper()
    scraper.run()
