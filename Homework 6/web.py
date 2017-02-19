### using python to retrieve documents ###
'''
the import: from urllib.request import *

html documents are really text documents

If the html file is local, use open()
len(open('sample.html').read())

For remote documents, wse need urllib.request
response = urlopen('http://cnn.com')
html = response .read().decode()

retireve and save files: urlretrieve('*url*')
'''
from urllib.request import *

### HTMLparser ###
'''
breaks up an html document into usable pieces

    handle_starttag
    handle_endtag
    handle_data

these are stubs - implementation is pass
we get the behavior we want through inheriting HTMLParser
'''

from html.parser import HTMLParser

class PrintParser(HTMLParser):
    #inherits method feed

    def handle_starttag(self, tag, attrs):
        print('handle_starttag', tag, attrs)

    def handle_endtag(self, tag):
        print('handle_endtag', tag)

    def handle_data(self, data):
        print('handle_data', data)


### urljoin ###
'''
used to turn relative link to an absolute link
'''

### LinkCollector ###
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

class LinkCollector(HTMLParser):
    ''' when given a url, LinkCollector
collects all the links found at that url.  You
can retrieve either 1) relative links 2) absolute links
3) all links.   all will be returned in absolute form.
'''
    def __init__(self,url):
        # do I need this?
        HTMLParser.__init__(self)
        self.url = url
        self.absoluteLinks = set()
        self.relativeLinks = set()

    def handle_starttag(self,tag,attrs):
        if tag=='a':
            #print( tag, attrs )
            for attr,value in attrs:
                if attr=='href':
                    if value[:4]=='http': # absolute
                        self.absoluteLinks.add( value )
                    else: # relative
                        url = urljoin(self.url, value)
                        self.relativeLinks.add( url )

    def getRelatives(self):
        return self.relativeLinks
    def getAbsolutes(self):
        return self.absoluteLinks
    def getLinks(self):
        return self.relativeLinks.union(self.absoluteLinks)

def scrapeLinks( url, filename):

    ''' creates a local html file filename
containing all links found at url'''

    # collect links
    lc = LinkCollector( url )
    lc.feed( urlopen(url).read().decode())

    # write to a file
    file = open(filename,'w')
    file.write( '<html><body>')
    for link in lc.getLinks():
        file.write('<a href={}> {} </a><br>\n'.format(link,link))
    file.write( '</body></html>')
    file.close()


### Crawler ###
from urllib.error import URLError

class Crawler():

    def __init__(self):
        self.crawled = set() # pages that were read
        self.found = set()  # links found
        self.dead = set()   # pages that couldnt read

    def crawl(self,url,depth=0,relativeOnly=True):

        # create a LinkCollector and feed it html
        lc = LinkCollector(url)
        try:
            lc.feed( urlopen(url).read().decode() )
        except (UnicodeDecodeError,URLError):
            self.dead.add( url )
        self.crawled.add(url)

        if relativeOnly: # only collecting relative links
            found =  lc.getRelatives()
        else:
            found = lc.getLinks()
        self.found.update( found )

        # recursively crawl found links
        if depth>0: # crawl
            for link in found:
                if link not in self.crawled:
                    self.crawl(link,depth-1,relativeOnly)

    def getCrawled(self):
        return self.crawled
    def getFound(self):
        return self.found
    def getDead(self):
        return self.dead
