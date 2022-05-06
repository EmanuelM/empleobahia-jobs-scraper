import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def scrap_job_page_by_url(url):
    chromedriver = os.getenv('SELENIUM_DRIVER_PATH')
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)

    title = driver.find_element(By.XPATH, './/h2[@class="card-title sm:text-3xl font-bold xl:hidden text-blue-cc leading-tight"]').text
    description = driver.find_element(By.XPATH, '//p[@class="text-gray-700 text-base sm:text-lg lg:text-lg 2xl:text-semibold"]').get_attribute('innerHTML')

    dates = driver.find_element(By.XPATH, './/p[@class="font-semibald text-sm md:text-lg mb-4 text-gray-700 2xl:text-semibold"]').text
    dates = dates.replace('desde ', '').replace(' hasta ', ',').split(',')
    published_at = dates[0]
    finish_at = dates[1]

    driver.quit()

    return {
        "url": url,
        "title": title,
        "published_at": published_at,
        "finish_at": finish_at,
        "description": description,
    }

def export_to_json(data):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    fileName = 'exports/' + timestamp + '_jobs.json'
    
    with open(fileName, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)