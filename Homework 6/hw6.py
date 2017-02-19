from web import LinkCollector
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import URLError

class ImageCollector(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr, value in attrs:
                if attr == 'src':
                    if value[:4] == 'http':
                        self.links.add(value)
                    else:
                        url = urljoin(self.url, value)
                        self.links.add(url)
    def getImages(self):
        return self.links
    

from web import Crawler

class ImageCrawler(Crawler):

    # both methods extend the Crawler's method

    def __init__(self):
        Crawler.__init__(self)
        self.images = set()

    def crawl(self, url, depth = 0, relativeOnly = True):
        ic = ImageCollector(url)
        ic.feed(urlopen(url).read().decode())
        self.images.add(url)

        Crawler.crawl(self,url,depth=0,relativeOnly=True)

    def getImages(self):
        return self.images
         

        


def scrapeImages(url, filename, depth = 0, relativeOnly = True):
    ic = ImageCollector(url)
    ic.feed(urlopen(url).read().decode())

    file = open(filename,'w')
    file.write( '<html><body>')
    for link in ic.getImages():
        file.write('<img src={}></a><br>\n'.format(link))
    file.write( '</body></html>')
    file.close()



if __name__=='__main__':
    import doctest
    print(doctest.testfile( 'hw6TEST.py'))
