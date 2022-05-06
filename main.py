import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers import scrap_job_page_by_url, export_to_json
from selenium.common.exceptions import NoSuchElementException   
from dotenv import load_dotenv

load_dotenv()

jobs_scraped = []
url = os.getenv('EMPLEO_BAHIA_URL')
chromedriver = os.getenv('SELENIUM_DRIVER_PATH')

driver = webdriver.Chrome(chromedriver)
driver.get(url)

jobs_list = driver.find_elements(By.XPATH, './/div[@class="flex-none md:flex md:flex-1 md:flex-col pb-4 md:pb-0 md:mx-2 shadow-md bg-gray-200 mt-3"]');

for job in jobs_list:
    job_url = job.find_element(By.XPATH, './/form[@class="text-center pb-2"]').get_attribute('action');
    job_details = scrap_job_page_by_url(job_url)
    jobs_scraped.append(job_details)

driver.quit()

export_to_json(jobs_scraped)
print('Empleo Bahía jobs scraped :D')