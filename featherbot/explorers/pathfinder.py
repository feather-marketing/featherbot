import requests
from bs4 import BeautifulSoup


class Pathfinder:
    """
    FeaterBot scrapes and collects all resources inside a domain.

    This includes images, files, and URI's but does *not* parse any on-page, or technical 
    information.

    Separating these functions allows asynchronus processing of the pages. Bare in mind each
    system will make an independent request (unless they can be combined) so do not overload
    client resources.
    """

    def __init__(self, url):
        self.visited = []
        self.to_visit = []
        self.url = url
        self.current = None
        self.debug = False

    def scrape(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        
        resp = requests.get(url, headers=headers)
        
        # Html
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def add_url(self, url):

        # Conditions for url to be added to visit queue
        conditions = (
            url not in self.visited
            and url not in self.to_visit
            and url != self.current
            and url.startswith(self.url)
            and "?" not in url
            and "#" not in url
        )

        if conditions:
            if self.debug == True:
                print("New URL: ",url)
            self.to_visit.append(url)

    def crawl(self, url):

        # Finds and adds all links
        html = self.scrape(url)
        for link in html.find_all("a"):
            url = link.get("href")

            # If there's a url, fwd to add function
            if url:
                self.add_url(url)
            # If this page has no links, pass over it
            else:
                pass

    def explore(self):
        
        # Starting point
        self.to_visit.append(self.url)
        while self.to_visit:
            
            # Set current to first entry of to_visit queue
            self.current = self.to_visit.pop(0)

            # Debugging prints current, past, and coming links
            if self.debug == True:
                print("Visited: {}".format(len(self.visited)))
                print("Currently at: ",self.current)
                print("Queued: {}".format(len(self.to_visit)))
                print("\n")

            # Try crawling and adding links
            try:
                self.crawl(self.current)
            except Exception as e:
                print(e)
                continue
            
            # Once crawl complete add current url to visited
            finally:
                self.visited.append(self.current)
        
        return self.visited