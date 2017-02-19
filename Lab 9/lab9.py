from html.parser import HTMLParser
from urllib.request import urlopen

class HeadingParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []
        self.indicator = False
        self.headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    def handle_starttag(self, tag, attrs):
        if tag in self.headers:
            self.indicator = True
    def handle_endtag(self, tag):
        if tag in self.headers:
            self.indicator = False 
    def handle_data(self, data):
        if self.indicator == True:
            data = data.strip()
            if data != '':
                self.data.append(data.strip())
    def getheadings(self):
        return self.data
        

def testHP(url):
    hp = HeadingParser()
    hp.feed(urlopen(url).read().decode())
    return hp.getheadings()






if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab9TEST.py' ))
