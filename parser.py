from html.parser import HTMLParser
import urllib.request
import re
class MyHTMLParser(HTMLParser):
	cur = 15
	def handle_starttag(self, tag, attrs):
		if tag=='img':
			url = dict(attrs)["src"]

			if url.find('wp-content') != -1 and url.find('/'+'.'):
				print('1')
				print(url)
			#images = dict(attrs)["src"]
			#images.group(0)
			#print(images)
parser = MyHTMLParser(strict=False)
i = 1;
url='http://mangadoom.com/The-Breaker-New-Waves/131/15';
html = urllib.request.urlopen(url).read()
html_str = html.decode('ascii')
parser.feed(html_str)
