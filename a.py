import requests, json, pyprind, sys, shutil
from bs4 import BeautifulSoup
json_arr = []

def dump(fileName):
	with open(fileName, 'w', encoding='UTF-8') as f:
		json.dump(json_arr, f)

def parsePage(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text)

	for i in soup.select('div.table-list div.row div.table-icon.col-md-2'):
		#try:
		product = i.select('strong span')[0].text
		product = product.replace('\n','').strip()
		restaurant = i.select('small')[0].text	
		restaurant = restaurant.replace('— Rating','')

		#except Exception as e:
			#pass
		# imghref = i.select('img')[0]['src']

		tmp={}
		# dict這個型態的值是可以改變的 
		#所以python不會自動幫你建一個新的物件而是用指標（reference）的方式連結到同一個變數
		tmp['product'] = product
		tmp['restaurant'] = restaurant
		json_arr.append(tmp)

	dump('demo.json')

parsePage('http://masteroverwatch.com/leaderboards/pc/global/mode/ranked/category/skillrating')