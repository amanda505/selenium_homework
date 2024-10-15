from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


keyword = "transformer toys"
service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
# Navigate to Google
driver.get("https://www.google.com")

# Find the search box and enter the keyword
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "search")))

# Find all search result links with an updated selector
search_results = driver.find_elements(By.CSS_SELECTOR, "div#search a")
print(f"Found {len(search_results)} search results")
    
# Extract and print the first 10 URLs, excluding google.com
urls = []
for result in search_results:
    url = result.get_attribute("href")
    if url and "http" in url and "google.com" not in url:
        urls.append(url)
        if len(urls) == 10:
            break

# Print the filtered URLs
for url in urls:
    print(url)

# Print the total number of URLs found
print(f"\nTotal URLs found: {len(urls)}")