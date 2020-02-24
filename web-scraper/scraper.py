from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

browser = webdriver.Chrome()

title = []
reviews = []
ratings = []
names = []

for j in range(1, 1200):
	url = "https://www.flipkart.com/boat-rockerz-255f-bluetooth-headset/product-reviews/itm4b5bc4473563b?pid=ACCF6SZ8EFWFEPZ6&lid=LSTACCF6SZ8EFWFEPZ6WFAW4Y&marketplace=FLIPKART&page={}".format(j)
	browser.get(url)
	
	if "_1EPkIx" in browser.page_source:
		rm = browser.find_element_by_class_name("_1EPkIx")
		rm.click()

	content = browser.page_source
	soup = BeautifulSoup(content, "html.parser")

	t = soup.select("._2xg6Ul")

	r = soup.select(".qwjRop")

	rt = soup.select(".hGSR34.E_uFuv")

	n = soup.select("._3LYOAd._3sxSiS")

	
	for i in range(len(t)):
		title.append(t[i].getText())
		reviews.append(r[i].getText().replace("READ MORE", ""))
		ratings.append(rt[i].getText())
		names.append(n[i].getText())
browser.quit()
df = pd.DataFrame({'Name':names, 'Ratings':ratings, 'Title':title, 'Reviews':reviews}) 
df.to_csv('BOAT_Rockerz_Bluetooth_Headset.csv', index=False, encoding='utf-8')


