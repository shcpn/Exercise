import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
import csv

url = input ("Get URL: ")
csv_PATH = input ("enter your csv file path: ")

response = requests.get(url)
html_source = bs(response.text, 'html.parser')

with open(csv_PATH, "a", encoding='UTF8', newline='') as new:
	writer = csv.writer(new)
	writer.writerow(html_source)
	new.close

print (html_source)
