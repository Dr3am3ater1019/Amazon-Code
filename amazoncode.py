import gspread

from oauth2client.service_account import ServiceAccountCredentials

import gspread

# Set up google sheets api
# "client_email": "tech-products@tech-sheet-392020.iam.gserviceaccount.com"

from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = r"C:\Users\cabam\Desktop\Python\Amazonwebscraping\tech-sheet-392020-66a0553d311b.json"
credentials = service_account.Credentials.from_service_account_file(filename=SERVICE_ACCOUNT_FILE)
client = gspread.authorize(credentials)

# scrape amazon website
import os
import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By

# set up Selenium

chrome_driver_path = r"C:\Users\cabam\Desktop\Python\Amazonwebscraping\chromedriver_win32\chromedriver.exe"
os.environ["PATH"] += os.pathsep + chrome_driver_path

# Define the function to scrape product details 

def scrape_product_details(url):
	driver = webdriver.Chrome()
	driver.get(url)

	# code to extract product details from the current product page using selenium
	# your code here
	
	driver.quit()

#Scrape Amazon website

url = "https://www.amazon.com"
search_term = "tech products"

# Generate the search result URLs

search_url = f"{url}/s?k={search_term}"
driver = webdriver.Chrome()
driver.get(search_url)

# code to extract the search result URLs using Selenium

search_result_urls = []

 # CSS selector to target the search result elements

search_result_elements = driver.find_elements(By.CSS_SELECTOR, '.s-result-time') 

# CSS selector to target the anchor element containing the URL

for element in search_result_elements:
	url = element.find_element_by_css_selector('a').get_attribute('href')
	search_result_urls.append(url)


driver.quit()

# Define the number of concurrent threads for parallel processing

num_threads = 5

# create a ThreadPoolExevutor with the desired number of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
	# Submit the scraping tasks to the executor
	futures = [executor.submit(scrape_product_details, url) for url in search_result_urls]

	# Wait for all to complete

	concurrent.futures.wait(futures)

# Code to handle the scraped product details, write them to a Google Sheet

sheet = client.open('Tech Products').sheet1

for product in products:
	row = [
		product['name'],
		product['category'],
		product['url'],
		product['price'],
		product['total_ratings'],
		product['average_rating']
	]

	sheet.append_row(row)

print("Data has been written to the Google Sheet.")