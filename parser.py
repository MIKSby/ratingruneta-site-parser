from firefox_driver import FirefoxDriver
from bs4 import BeautifulSoup
import requests
from time import sleep
import re
from tqdm import tqdm
from random import uniform


class RatingRunetaParser(FirefoxDriver):
    def __init__(self):
        super().__init__()

    def perform_parsing(self, url):
        driver = self.run_browser()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        tds = [td for td in soup.find_all('td')]
        links = [i for i in tds if i.find('a')]
        ready_sites, not_ready_sites = [], []
        for i in links:
            link = i.a['href']
            if link[:4] == 'http':
                ready_sites.append(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', link)[0])
            else:
                not_ready_sites.append(link)
        for i in tqdm(not_ready_sites):
            r = requests.get(f'http://www.ratingruneta.ru{i}contacts/').text
            num_pos = r.find('Показать телефон')
            for_regular = r[num_pos:num_pos + 300]
            ready = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', for_regular)
            if ready:
                ready_sites.append(ready[0])
            sleep(uniform(0.3, 0.6))
        return ready_sites

    @staticmethod
    def save_result_to_file(results):
        with open('results.txt', 'a') as f:
            for result in results:
                f.write(f'{result}\n')
