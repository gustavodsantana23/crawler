import requests
from bs4 import BeautifulSoup
import getopt
import sys

class Crawler:

	def __init__(self, url):
		self.url = url
		self.page = requests.get('https://fleeber.com/artists')
		self.soup = BeautifulSoup(self.page.text, 'html.parser')

	def get_artists(self):
		artist_name_list = self.soup.find(class_='musiciansList')
		artist_list_anchors = artist_name_list.find_all('a')
		for a in artist_list_anchors:
			img = a.img['src']

			name = a.find(class_='musicianName')
			name = name.string

			styles = a.find(class_='extra')
			styles = styles.string

			print("Name: {}, a: {}, img: {} , styles: {}".format(
				name, a['href'], img, styles))

def main():
	# try:
	# 	opts, remainder = getopt.getopt(sys.argv[1:], 'u:v', ['url=', 'verbose'])
	# 	print(opts['-u'])
	# except Exception as e:
	# 	raise e

	c =  Crawler('fleeber.com/artists')
	c.get_artists()

	# # Collect and parse first page
	# page = requests.get('https://fleeber.com/artists')

	# # Pull all text from the BodyText div
	# 

	# # Pull text from all instances of <a> tag within BodyText div

	# for a in artist_name_list_items:
	# 	print(a)

if __name__ == '__main__':
	main()