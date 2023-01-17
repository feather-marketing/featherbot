import re
import requests
from bs4 import BeautifulSoup

class Content:

    def scrape(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        
        resp = requests.get(url, headers=headers)
        
        # Html
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def slug_score(self, url):
        idx = url.rfind("/")
        slug = url[idx:]
        slug_words = slug.split("-")

        slug_score = 0

        if "_" not in slug:
            slug_score += 1
        if len(slug_words)<5:
            slug_score += 1
        if len(slug)<15:
            slug_score += 1

        # smth like if it contains "action" verbs / nouns or lots of "the", "and", "is"
        return slug_score

    def lang(self, url):
        #https://developers.google.com/search/docs/specialty/international/localized-versions
        soup = self.scrape(url)
        return soup.html.attrs["lang"]

    def byline(self, url):
        # https://developers.google.com/search/docs/appearance/publication-dates
        soup = self.scrape(url)

        # Method 1: check json_ld
        json_ld = soup.find("script", {"type":"application/ld+json"})
        if json_ld:
            # Adding length to start at beginning of actual date
            json_ld = json_ld.text
            idx = json_ld.find("datePublished")+len("datePublished")+3
            date = json_ld[idx:idx+10]
        else:
            date = None


        # Method 2: check "user-visible"
        # Posted [date]
        # Published [date]
        # Last updated: [date]
        # Updated [date]

        return date

    def title(self, url):
        # https://developers.google.com/search/docs/appearance/title-link#page-titles
        soup = self.scrape(url)
        title = soup.title.text
        return title

    def description(self, url):
        soup = self.scrape(url)
        desc = soup.find("meta", {"name":"description"})
        if desc:
            desc = desc["content"]
        else:
            desc = None
        return desc

    def images(self, url):
        # https://developers.google.com/search/docs/appearance/google-images
        soup = self.scrape(url)
        imgs = soup.find_all("img")

        data = []
        for img in imgs:
            src = img["src"]

            # image alt
            try:
                alt = img["alt"]
            except:
                alt = None
            
            # If image has a class, if it contains lazyload
            # If it doesnt have either then set to False
            try:
                lazy_load = img["class"]
                if "lazyload" in lazy_load:
                    lazy_load = True
                else:
                    lazy_load = False
            except:
                lazy_load = False

            row = [src, alt, lazy_load]

            data.append(row)
    
        return data

    def videos(self, url):
        # https://developers.google.com/search/docs/appearance/video
        return None