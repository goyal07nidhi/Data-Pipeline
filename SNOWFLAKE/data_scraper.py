from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests

load_dotenv(verbose=True)

class DataScraper:
    _instance = None

    def __init__(self):
        raise RuntimeError("Use DataScraper.instance()")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)

        return cls._instance

    def scrape(self, url, download_path):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = soup.findAll('a')
        scrape_link = []
        files = []
        file_count = 0

        for link in links:
            scrape_link.append(link.get_text())

        for sl in scrape_link:
            if sl.endswith(".csv.gz"):
                response = requests.get(url + sl)
                with open(download_path + sl, 'wb') as f:
                    f.write(response.content)
                file_count += 1
                if file_count >= 2:
                    break

        print('Scraping complete!')
        return files
