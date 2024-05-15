from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def main ():

    # Navigate to Yahoo Finance
    # Locate the search bar
    # Search for the user specified stock symbol - We will need to determine if the symbol is valid somehow
    # Load the stock specfic page
    # Scrape the stock price at the current time 
    # Scrape the first 3 videos that appear in the all section
    driver = webdriver.Chrome()

    driver.get("https://ca.finance.yahoo.com/")

    title = driver.title

    driver.implicitly_wait(0.10)

    # Search Bar
    search_bar = driver.find_element(By.ID ,"yfin-usr-qry")
    # Search for user inputed stock symbol/tick and direct automation to page
    search_bar.send_keys("GME", Keys.ENTER)
    time.sleep(5)

    # text_box = driver.find_element(by=By.NAME, value="my-text")
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # text_box.send_keys("Selenium")
    # submit_button.click()

    # message = driver.find_element(by=By.ID, value="message")
    # text = message.text

    driver.quit()
    print(title)

main()