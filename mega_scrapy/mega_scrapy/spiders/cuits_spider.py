import scrapy
import sqlite3

# START OF HELPER FUNCTIONS
def fetchCuits():
    cuits = []
    conn = sqlite3.connect('C:\\Users\Bruno\Desktop\desarrollo\web-crawling\mega-cuits\mega_cuits.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT empr_cuit FROM main.cuits_crawled')
    rows = cur.fetchall()
    for cuit in rows:
        cuits.append(cuit)
    conn.commit()
    conn.close()
    return cuits

def completeCuitURL(cuit):
    cuitURL = 'https://www.cuitonline.com/search.php?q='
    return cuitURL + str(cuit[0])

def insertNameOnCuit(name, cuit):
    conn = sqlite3.connect('C:\\Users\Bruno\Desktop\desarrollo\web-crawling\mega-cuits\mega_cuits.sqlite')
    cur = conn.cursor()
    cur.execute("UPDATE main.cuits_crawled SET empr_name=? WHERE empr_cuit=?  ", (name, cuit))
    conn.commit()
    conn.close()
# END OF HELPER FUNCTIONS

pass


class CuitsSpider(scrapy.Spider):
    name = "cuits"
    cuits = fetchCuits()

    def start_requests(self):
        cuit_urls = []
        for cuit in self.cuits:
            cuit_urls.append(completeCuitURL(cuit))
        for url in cuit_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        parsed_response = response.css('span.denominacion::text').get()
        name = parsed_response

        for cuit in self.cuits:
            insertNameOnCuit(name, cuit[0])