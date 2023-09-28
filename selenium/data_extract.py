from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome()
options.add_argument("--verbose")
driver.get('https://www.wikipedia.org/')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="searchInput"]'))).click()
driver.find_element(By.XPATH, '//input[@id="searchInput"]').send_keys("India")
driver.find_element(By.XPATH, '//button[@class="pure-button pure-button-primary-progressive"]').click()
driver.implicitly_wait(10)
# driver.find_element(By.XPATH, '(//td[@class="infobox-data"])[22]').select()
# driver.find_element(By.XPATH, '(//h3[@class="title-and-badge style-scope ytd-video-renderer"]//a//yt-formatted-string)[1]').click()
infobox = driver.find_element(By.XPATH, 'td[@class="infobox-data"]')

driver.infobox.find_element(By.XPATH,)
time.sleep(5)
# --------------------------------------------------------
# Database 
# 5 types of Relationhips
# https://blog.devart.com/types-of-relationships-in-sql-server-database.html#:~:text=There%20are%20five%20types%20of,working%20example%20of%20their%20usage.
# https://fmhelp.filemaker.com/help/18/fmp/en/index.html#page/FMP_Help/many-to-many-relationships.html