#!/usr/bin/python
import sys
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse

if len(sys.argv) == 2:
	url = sys.argv[1] if sys.argv[1][0:7] == 'http://' else 'http://' + sys.argv[1]
	baseUrl = '://'.join(urlparse(url)[0:2])

	response = urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)

	for link in soup.findAll('img'):
		if link.get('src')[0] == '/':
			print baseUrl + link.get('src')
		elif link.get('src')[0:7] != 'http://':
			print baseUrl + '/' + link.get('src')
		else:
			print link.get('src')
else:
	print 'No url given'

