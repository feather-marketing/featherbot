import re
import requests
from bs4 import BeautifulSoup

"""
    * Architect is domain wide
    * Thinking using self.url which is scraped once and can have all the operations run on it
    * otherwise every single operation requires a scrape, its likely these are going to be done together
"""

class Architect:

    def scrape(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        
        # Html
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def robots(self, url):
        url = url+"/robots.txt"
        soup = str(self.scrape(url))
        return soup

    def favicons(self, url):
        # https://developers.google.com/search/docs/appearance/favicon-in-search
        soup = self.scrape(url)

        tags = [
            "icon",
            "shortcut icon",
            "apple-touch-icon",
            "apple-touch-icon-precomposed"
        ]

        favicons = {}
        for tag in tags:
            icon = soup.find("link", rel=tag)
            if icon:
                favicons[tag]=icon["href"]
            else:
                favicons[tag]=None

        return favicons

    def discover(self, url):
        # https://developers.google.com/search/docs/appearance/google-discover
        soup = self.scrape(url)

        feeds = soup.find_all("link", {"type":"application/rss+xml"})
        return feeds

    def sitename(self, url):
        # https://developers.google.com/search/docs/appearance/site-names
        # requires either structured markup, or og
        pass

    def sitemaps(self, url):
        # It's possible sitemaps aren't in txt but in a common file_ending like "sitemap_index.xml"
        # but we should encourage usage in robots.

        robots = self.robots(url)

        sitemaps = []
        lines = str(robots).splitlines()

        for line in lines:
            if line.startswith('Sitemap:'):
                split = line.split(':', maxsplit=1)
                sitemaps.append(split[1].strip())

        return sitemaps

    def indexed(self, root):
        # Query is structured by site. Do not include https://
        # e.g. root="genex.app"
        query = "https://www.google.com/search?q=site:"+root+"&hl=en"
        response = requests.get(query, cookies={"CONSENT": "YES+1"})
        soup = BeautifulSoup(response.content, "html.parser")

        not_indexed = re.compile("did not match any documents")
        if soup(text=not_indexed):
            return False
        else:
            return True