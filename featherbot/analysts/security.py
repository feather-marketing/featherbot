class Security:
    def __init__(self):
        pass

    # https://developers.google.com/search/docs/essentials/spam-policies

    def scrape(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        
        resp = requests.get(url, headers=headers)
        
        # Html
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def cloacking():
        pass
    def doorways():
        pass
    def hacked_content():
        pass
    def hidden_data():
        pass
    def fake_traffic():
        pass
    def malware():
        pass
    def false_functionality():
        pass
    def sneaky_redirects():
        pass
    def scraped_content():
        pass
    def keyword_stuffing():
        pass
    def link_spam():
        pass
    def spam_content():
        pass
    def thin():
        pass
    def user_generated_spam():
        pass
    def fraud():
        pass