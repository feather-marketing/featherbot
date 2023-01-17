import requests
from bs4 import BeautifulSoup

class Technical:

    def scrape(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        
        # Html
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def robots(self, url):
        soup = self.scrape(url)
        robots = soup.find("meta", {"name":"robots"})
        if robots:
            robots = robots["content"]
        else:
            robots = None
        return robots

    def json_ld(self,url):
        soup = self.scrape(url)
        json_ld = soup.find("script", {"type":"application/ld+json"})
        if json_ld:
            json_ld = json_ld.text
        else:
            json_ld = None
        return json_ld

    def open_graph(self, url):
        soup = self.scrape(url)

        tags = [
            "og:locale",
            "og:type",
            "og:title",
            "og:description",
            "og:url",
            "og:site_name",
            "og:updated_time"
        ]

        og_data = {}
        for tag in tags:
            data = soup.find("meta", {"property":tag})
            if data:
                og_data[tag]=data["content"]
            else:
                og_data[tag]=None
        return og_data

    def canonical(self, url):
        soup = self.scrape(url)
        canonical = soup.find("link", {"rel":"canonical"})
        if canonical:
            canonical = canonical["href"]
        else:
            canonical = None
        return canonical

    def social_tags(self, url):
        soup = self.scrape(url)

        tags = [
            "twitter:title",
            "twitter:description"
        ]

        data = {}
        for tag in tags:
            result = soup.find("meta", {"name":tag})
            if result:
                data[tag] = True
            else:
                data[tag] = False
        return data