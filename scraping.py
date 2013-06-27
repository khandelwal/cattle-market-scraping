import requests 


def read_url(url):
	r = requests.get(url)
	return r.text
