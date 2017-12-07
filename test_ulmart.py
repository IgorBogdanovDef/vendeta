import os
os.environ['http_proxy'] = '10.0.4.12:3128'
os.environ['HTTPS_PROXY'] = '10.0.4.12:3128'

import urllib.request
with urllib.request.urlopen('https://www.ulmart.ru/catalog/apple_ipad_1') as response:
   html = response.read()

from html.parser import HTMLParser

price = False
name = False
iphones = []
print (iphones)
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global price, name        
        if tag=='span':
            attrs = dict(attrs)
            if 'class' in attrs and attrs['class']=="b-price__num js-price":
                price = True
        if tag=='a':
            attrs = dict(attrs)
            if 'class' in attrs and attrs['class']=="must_be_href js-gtm-product-click":
                name = True

    def handle_data(self, data):
        global price, name, s
        if price:
            price = False
            s=data
        if name:
            name = False
            iphones.append((data.strip(), int(s.strip().replace('\xa0', ''))))


parser = MyHTMLParser()
parser.feed(html.decode())
print (iphones)
