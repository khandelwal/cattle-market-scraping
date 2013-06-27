#vim: set fileencoding=utf-8
from bs4 import BeautifulSoup
import requests

import scraping

URL = "http://www.weeklylivestock.com/salereport.html"

page_html = scraping.read_url(URL)
page = BeautifulSoup(page_html)

market_markups = page.findAll('h2')

for m in market_markups:
	print m.text.strip()

	location_container = m.find_next_sibling('h4')
	if location_container:
			date_location_string = location_container.text.split('\n')[0]
			bullet_delimiter = u'\xe2\x80\xa2'

			market_date, location = date_location_string.split(bullet_delimiter)
			market_city, market_state = location.strip().rsplit(',', 1)

	destination_container = m.find_next_sibling('p')
	if destination_container:
		print destination_container


