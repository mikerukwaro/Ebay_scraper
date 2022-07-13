import requests
from bs4 import BeautifulSoup

class ebay():
    def __init__(self):
        pass

    def setup(self):
        for pages in range(5):
            url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw=sony+playstation+3+&_sacat=0&LH_TitleDesc=0&_pgn={pages}"
            response = requests.get(url).text
            soup = BeautifulSoup(response, "html.parser")
            self.finding_content(soup)

    def finding_content(self, soup):
        all_cont = soup.find_all("li", class_="s-item s-item__pl-on-bottom s-item--watch-at-corner")
        for all in all_cont:
            price = all.find("span", class_="s-item__price").text
            product_name = all.find("h3", class_="s-item__title").text
            print(price)
            print(product_name)
        print("************************************************")
        print()

    def run(self):
        self.setup()

if __name__ == "__main__":
    scrape = ebay()
    scrape.run()